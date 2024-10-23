from __future__ import annotations

import json
from typing import Any, Literal, Mapping

from fast_bioservices.base import BaseModel
from fast_bioservices.fast_http import FastHTTP
from fast_bioservices.settings import default_workers


class BiGG(BaseModel, FastHTTP):
    _download_url: str = "http://bigg.ucsd.edu/static/models"

    def __init__(self, max_workers: int = default_workers, cache: bool = True):
        self._url: str = "http://bigg.ucsd.edu/api/v2"
        BaseModel.__init__(self, url=self._url)
        FastHTTP.__init__(self, cache=cache, workers=max_workers, max_requests_per_second=10)

    @property
    def url(self) -> str:
        return self._url

    @property
    def download_url(self) -> str:
        return self._download_url

    def version(self, temp_disable_cache: bool = False) -> Mapping[Any, Any]:
        response = self._get(f"{self.url}/database_version", temp_disable_cache=temp_disable_cache)[0]
        return json.loads(response)

    def models(self, temp_disable_cache: bool = False) -> Mapping[Any, Any]:
        response = self._get(f"{self.url}/models", temp_disable_cache=temp_disable_cache)[0]
        return json.loads(response)

    def model_details(
        self,
        model_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(f"{self.url}/models/{model_id}", temp_disable_cache=temp_disable_cache)[0]
        return json.loads(response)

    def json(
        self,
        model_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(f"{self.url}/models/{model_id}/download", temp_disable_cache=temp_disable_cache)[0]
        return json.loads(response)

    def download(
        self,
        model_id: str,
        format: Literal["json", "xml", "mat", "json.gz", "xml.gz", "mat.gz"],
        download_path: str | None = None,
        temp_disable_cache: bool = False,
    ) -> None:
        if download_path is None:
            download_path = f"{model_id}.{format}"
        elif not download_path.endswith(f"{model_id}.{format}"):
            download_path = f"{download_path}/{model_id}.{format}"

        response = self._get(f"{self.download_url}/{model_id}.{format}", temp_disable_cache=temp_disable_cache)

        if format == "json":
            json.dump(response[0], open(download_path, "w"), indent=2)
        else:
            with open(download_path, "wb") as o_stream:
                o_stream.write(response[0])

    def model_reactions(
        self,
        model_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(f"{self.url}/models/{model_id}/reactions", temp_disable_cache=temp_disable_cache)[0]
        return json.loads(response)

    def model_reaction_details(
        self,
        model_id: str,
        reaction_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(
            f"{self.url}/models/{model_id}/reactions/{reaction_id}",
            temp_disable_cache=temp_disable_cache,
        )[0]
        return json.loads(response)

    def model_metabolites(
        self,
        model_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(
            f"{self.url}/models/{model_id}/metabolites",
            temp_disable_cache=temp_disable_cache,
        )[0]
        return json.loads(response)

    def model_metabolite_details(
        self,
        model_id: str,
        metabolite_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(
            f"{self.url}/models/{model_id}/metabolites/{metabolite_id}",
            temp_disable_cache=temp_disable_cache,
        )[0]
        return json.loads(response)

    def model_genes(
        self,
        model_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(f"{self.url}/models/{model_id}/genes", temp_disable_cache=temp_disable_cache)[0]
        return json.loads(response)

    def model_gene_details(
        self,
        model_id: str,
        gene_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(
            f"{self.url}/models/{model_id}/genes/{gene_id}",
            temp_disable_cache=temp_disable_cache,
        )[0]
        return json.loads(response)

    def universal_reactions(self, temp_disable_cache: bool = False) -> Mapping[Any, Any]:
        response = self._get(f"{self.url}/universal/reactions", temp_disable_cache=temp_disable_cache)[0]
        return json.loads(response)

    def universal_reaction_details(
        self,
        reaction_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(
            f"{self.url}/universal/reactions/{reaction_id}",
            temp_disable_cache=temp_disable_cache,
        )[0]
        return json.loads(response)

    def universal_metabolites(self, temp_disable_cache: bool = False) -> Mapping[Any, Any]:
        response = self._get(f"{self.url}/universal/metabolites", temp_disable_cache=temp_disable_cache)[0]
        return json.loads(response)

    def universal_metabolite_details(
        self,
        metabolite_id: str,
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(
            f"{self.url}/universal/metabolites/{metabolite_id}",
            temp_disable_cache=temp_disable_cache,
        )[0]
        return json.loads(response)

    def search(
        self,
        query: str,
        search_type: Literal["metabolites", "genes", "models", "reactions"],
        temp_disable_cache: bool = False,
    ) -> Mapping[Any, Any]:
        response = self._get(
            f"{self.url}/search?query={query}&search_type={search_type}",
            temp_disable_cache=temp_disable_cache,
        )[0]
        return json.loads(response)
