from __future__ import annotations

import io
import json
from typing import Dict, List, Literal

import pandas as pd
from loguru import logger

from fast_bioservices.base import BaseModel
from fast_bioservices.biodbnet.nodes import Input, Output, Taxon
from fast_bioservices.fast_http import FastHTTP
from fast_bioservices.settings import default_workers


class BioDBNet(BaseModel, FastHTTP):
    def __init__(self, max_workers: int = default_workers, cache: bool = True):
        self._url = "https://biodbnet-abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.json"
        self._chunk_size: int = 250

        BaseModel.__init__(self, url=self._url)
        FastHTTP.__init__(self, cache=cache, workers=max_workers, max_requests_per_second=10)

    @property
    def url(self) -> str:
        return self._url

    def _are_nodes_valid(
        self,
        input_: Input | Output,
        output: Input | Output | List[Input | Output],
        direct_output: bool = False,
    ) -> bool:
        """
        The input database and output database must be different.

        Parameters
        ----------
        input_ : Input | Output
            The input database
        output : Input | Output | List[Input | Output]
            The output database
        direct_output : bool, optional
            Get direct output node(s) for a given input node (i.e., outputs reacable by a single connection), by default False

        Returns
        -------
        bool
            True if the input and output databases are different, False otherwise.
        """

        logger.debug("Validating databases")
        output_list = [output] if not isinstance(output, list) else output

        if direct_output:
            return all([o.value in self.getDirectOutputsForInput(input_) for o in output_list])
        return all([o.value in self.getOutputsForInput(input_) for o in output_list])

    def _validate_taxon_id(
        self,
        taxon: int | str | Taxon | list[int | str | Taxon],
    ) -> List[int]:
        taxon_list: list[int] = []

        if isinstance(taxon, Taxon):
            taxon_list.append(taxon.value)
        elif isinstance(taxon, int):
            taxon_list.append(taxon)
        elif isinstance(taxon, str):
            logger.warning(f"The provided taxon ID ('{taxon}') is a string, attempting to map it to a known integer value...")
            taxon_list.append(Taxon.string_to_obj(taxon).value)
        elif isinstance(taxon, list):
            for t in taxon:
                if isinstance(t, Taxon):
                    taxon_list.append(t.value)
                elif isinstance(t, int):
                    taxon_list.append(t)
                elif isinstance(t, str):
                    logger.warning(f"The provided taxon ID ('{t}') is a string, attempting to map it to a known integer value...")
                    taxon_list.append(Taxon.string_to_obj(t).value)
        else:
            raise ValueError(f"Unknown taxon type for '{taxon}': {type(taxon)}")

        for t in taxon_list:
            logger.debug(f"Validating taxon ID '{t}'")
            if t not in Taxon.member_values():  # All items in the 'Taxon' enum are valid, only need to check items not in enum
                taxon_url: str = f"https://www.ncbi.nlm.nih.gov/taxonomy/?term={t}"
                if "No items found." in str(self._get(taxon_url, temp_disable_cache=True, log_on_complete=False)[0]):
                    raise ValueError(f"Unable to find taxon '{t}'")
        logger.debug(f"Taxon IDs are valid: '{','.join([str(i) for i in taxon_list])}'")

        return taxon_list

    def getDirectOutputsForInput(self, input: Input | Output) -> List[str]:
        url = f"{self.url}?method=getdirectoutputsforinput&input={input.value.replace(' ', '').lower()}&directOutput=1"
        outputs = self._get(url, temp_disable_cache=True, log_on_complete=False)[0]
        as_json = json.loads(outputs)
        return as_json["output"]

    def getInputs(self) -> List[str]:
        url = f"{self.url}?method=getinputs"
        inputs = self._get(url, temp_disable_cache=True, log_on_complete=False)[0]
        as_json = json.loads(inputs)
        return as_json["input"]

    def getOutputsForInput(self, input: Input | Output) -> List[str]:
        url = f"{self.url}?method=getoutputsforinput&input={input.value.replace(' ', '').lower()}"
        valid_outputs = json.loads(self._get(url, temp_disable_cache=True, log_on_complete=False)[0].decode())
        return valid_outputs["output"]

    def getAllPathways(
        self,
        taxon: Taxon | int,
        as_dataframe: bool = False,
    ) -> pd.DataFrame | List[Dict[str, str]]:
        taxon_id = self._validate_taxon_id(taxon)[0]

        url = f"{self.url}?method=getpathways&pathways=1&taxonId={taxon_id}"
        as_json = json.loads(self._get(url)[0].decode())
        if as_dataframe:
            return pd.DataFrame(as_json)
        return as_json

    def getPathwayFromDatabase(
        self,
        pathways: Literal["reactome", "biocarta", "ncipid", "kegg"] | List[Literal["reactome", "biocarta", "ncipid", "kegg"]],
        taxon: Taxon | int = Taxon.HOMO_SAPIENS,
        as_dataframe: bool = True,
    ) -> pd.DataFrame | List[Dict[str, str]]:
        taxon_id = self._validate_taxon_id(taxon)[0]

        if isinstance(pathways, str):
            pathways = [pathways]

        url = f"{self.url}?method=getpathways&pathways={','.join(sorted(pathways))}&taxonId={taxon_id}"
        as_json = json.loads(self._get(url)[0].decode())

        if as_dataframe:
            return pd.DataFrame(as_json)
        return as_json

    def db2db(
        self,
        input_values: List[str],
        input_db: Input,
        output_db: Output | List[Output],
        taxon: Taxon | int = Taxon.HOMO_SAPIENS,
    ) -> pd.DataFrame:
        taxon_id = self._validate_taxon_id(taxon)[0]

        if not self._are_nodes_valid(input_db, output_db):
            out_db: list = [output_db] if not isinstance(output_db, list) else output_db
            raise ValueError(
                "You have provided an invalid output database(s).\n"
                "A common result of this problem is including the input database as an output database.\n"
                f"Input database: {input_db.value}\n"
                f"Output database(s): {','.join([o.value for o in out_db])}"
            )
        logger.debug("Databases are valid")

        if isinstance(output_db, Output):
            output_db_value = output_db.value.lower().replace(" ", "")
        else:
            output_db_value = ",".join(sorted([o.value.lower().replace(" ", "") for o in output_db]))
        logger.debug(f"Got an input database with a value of '{input_db.value.lower().replace(' ', '')}'")
        logger.debug(f"Got {len(output_db_value.split(','))} output databases with values of: '{output_db_value}'")

        # https://biodbnet-abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi?method=db2db

        input_values.sort()
        urls: list[str] = []
        for i in range(0, len(input_values), self._chunk_size):
            urls.append(
                f"{self.url}?method=db2db"
                f"&format=row"
                f"&input={input_db.value.lower().replace(' ', '')}"
                f"&outputs={output_db_value}"
                f"&inputValues={','.join(input_values[i: i + self._chunk_size])}"
                f"&taxonId={taxon_id}"
            )

        responses: List[bytes] = self._get(urls=urls, extensions={"force_cache": True})
        df = pd.DataFrame()
        for response in responses:
            as_json = json.loads(response.decode())
            df = pd.concat([df, pd.DataFrame(as_json)], ignore_index=True)

        df.rename(columns={"InputValue": input_db.value}, inplace=True)
        logger.debug(f"Returning dataframe with {len(df)} rows")
        return df

    def dbWalk(
        self,
        input_values: List[str],
        db_path: List[Input | Output],
        taxon: Taxon | int = Taxon.HOMO_SAPIENS,
    ) -> pd.DataFrame:
        taxon_id = self._validate_taxon_id(taxon)[0]

        for i in range(len(db_path) - 1):
            current_db = db_path[i]
            next_db = db_path[i + 1]

            if not self._are_nodes_valid(current_db, next_db, direct_output=True):
                raise ValueError(
                    "You have provided an invalid output database.\n" f"Unable to navigate from '{current_db.value}' to '{next_db.value}'"
                )
        logger.debug("Databases are valid")
        databases: list[str] = [d.value.replace(" ", "").lower() for d in db_path]

        input_values.sort()
        databases.sort()
        urls: list[str] = []
        for i in range(0, len(input_values), self._chunk_size):
            urls.append(self.url + "?method=dbwalk&format=row")
            urls[-1] += f"&inputValues={','.join(input_values[i:i + self._chunk_size])}"
            urls[-1] += f"&dbPath={'->'.join(databases)}"
            urls[-1] += f"&taxonId={taxon_id}"

        responses: List[bytes] = self._get(urls)
        df = pd.DataFrame()
        for response in responses:
            as_json = json.loads(response.decode())
            df = pd.concat([df, pd.DataFrame(as_json)], ignore_index=True)
        df = df.rename(columns={"InputValue": str(db_path[0].value)})
        logger.debug(f"Returning dataframe with {len(df)} rows")
        return df

    def dbReport(
        self,
        input_values: List[str],
        input_db: Input | Output,
        taxon: Taxon | int = Taxon.HOMO_SAPIENS,
    ):
        return NotImplementedError
        taxon_id = self._validate_taxon_id(taxon)[0]
        urls: list[str] = []
        for i in range(0, len(input_values), self._chunk_size):
            urls.append(self.url + "?method=dbreport&format=row")
            urls[-1] += f"&input={input_db.value.replace(' ', '').lower()}"
            urls[-1] += f"inputValues={','.join(input_values[i:i + self._chunk_size])}"
            urls[-1] += f"&taxonId={taxon_id}"

    def dbFind(
        self,
        input_values: List[str],
        output_db: Output | List[Output],
        taxon: Taxon | int = Taxon.HOMO_SAPIENS,
    ) -> pd.DataFrame:
        if isinstance(output_db, Output):
            output_db = [output_db]
        taxon_id = self._validate_taxon_id(taxon)[0]

        output_db.sort()
        input_values.sort()
        urls: list[str] = []
        for out_db in output_db:
            for i in range(0, len(input_values), self._chunk_size):
                urls.append(self.url + "?method=dbfind&format=row")
                urls[-1] += f"&inputValues={','.join(input_values[i:i + self._chunk_size])}"
                urls[-1] += f"&output={out_db.value}"
                urls[-1] += f"&taxonId={taxon_id}"

        responses: List[bytes] = self._get(urls=urls)
        df = pd.DataFrame()
        for response in responses:
            as_json = json.loads(response.decode())
            df = pd.concat([df, pd.DataFrame(as_json)], ignore_index=True)
        # df.rename(columns={"InputValue": input_db.value}, inplace=True)
        return df

    def dbOrtho(
        self,
        input_values: List[str],
        input_db: Input,
        output_db: Output | List[Output],
        input_taxon: Taxon | int = Taxon.HOMO_SAPIENS,
        output_taxon: Taxon | int = Taxon.MUS_MUSCULUS,
    ):
        input_taxon_value = self._validate_taxon_id(input_taxon)[0]
        output_taxon_value = self._validate_taxon_id(output_taxon)[0]
        if isinstance(output_db, Output):
            output_db = [output_db]

        output_db.sort()
        input_values.sort()
        urls: list[str] = []
        for out_db in output_db:
            for i in range(0, len(input_values), self._chunk_size):
                urls.append(self.url + "?method=dbortho")
                urls[-1] += f"&input={input_db.value.replace(' ', '').lower()}"
                urls[-1] += f"&inputValues={','.join(input_values[i:i + self._chunk_size])}"
                urls[-1] += f"&inputTaxon={input_taxon_value}"
                urls[-1] += f"&outputTaxon={output_taxon_value}"
                urls[-1] += f"&output={out_db.value.replace(' ', '').lower()}"
                urls[-1] += "&format=row"

        responses: List[bytes] = self._get(urls=urls)
        df = pd.DataFrame()
        for response in responses:
            as_json = json.loads(response.decode())
            df = pd.concat([df, pd.DataFrame(as_json)], ignore_index=True)

        # Remove potential duplicate columns
        for column in df.columns:
            if str(column).endswith("_x"):
                df = df.drop(column, axis=1)
            elif str(column).endswith("_y"):
                df.rename(columns={column: column[:-2]}, inplace=True)

        df.rename(columns={"InputValue": input_db.value}, inplace=True)

        return df

    def dbAnnot(
        self,
        input_values: List[str],
        annotations: List[
            Literal[
                "Drugs",
                "Diseases",
                "Genes",
                "GO Terms",
                "Pathways",
                "Protein Interactors",
            ]
        ],
        taxon: Taxon | int = Taxon.HOMO_SAPIENS,
    ) -> pd.DataFrame:
        taxon_id = self._validate_taxon_id(taxon)[0]
        annotations = [a.replace(" ", "").lower() for a in sorted(annotations)]

        input_values.sort()
        urls: list[str] = []
        for i in range(0, len(input_values), self._chunk_size):
            urls.append(self.url + "?method=dbannot")
            urls[-1] += f"&inputValues={','.join(input_values[i:i + self._chunk_size])}"
            urls[-1] += f"&taxonId={taxon_id}"
            urls[-1] += f"&annotations={','.join(annotations)}"
            urls[-1] += "&format=row"

        responses: list[bytes] = self._get(urls=urls)
        df = pd.DataFrame()
        for response in responses:
            as_json = json.loads(response.decode())
            df = pd.concat([df, pd.DataFrame(as_json)], ignore_index=True)
        df = df.rename(columns={"InputValue": "Input Value"})
        return df

    def dbOrg(
        self,
        input_db: Input,
        output_db: Output,
        taxon: Taxon | int = Taxon.HOMO_SAPIENS,
    ) -> pd.DataFrame:
        taxon_id = self._validate_taxon_id(taxon)
        input_db_val = input_db.value.replace(" ", "_")
        output_db_val = output_db.value.replace(" ", "_")

        url = f"https://biodbnet-abcc.ncifcrf.gov/db/dbOrgDwnld.php?file={input_db_val}__to__{output_db_val}_{taxon_id}"
        buffer = io.StringIO(self._get(url)[0].decode())
        return pd.read_csv(buffer, sep="\t", header=None, names=[input_db.value, output_db.value])


if __name__ == "__main__":
    df = pd.read_csv("/Users/joshl/Downloads/A.csv", index_col=0, nrows=250)

    biodbnet = BioDBNet(cache=False)
    result = biodbnet.db2db(
        input_values=df.index.tolist(),
        input_db=Input.GENE_SYMBOL,
        output_db=[Output.ENSEMBL_GENE_ID, Output.GENE_ID, Output.CHROMOSOMAL_LOCATION],
    )
    print(result)
