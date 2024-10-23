from typing import Literal

from pandas import DataFrame, json_normalize

from impresso.api_client.api.entities import find_entities, get_entity
from impresso.api_client.models.find_entities_order_by import (
    FindEntitiesOrderBy,
    FindEntitiesOrderByLiteral,
)
from impresso.api_client.types import UNSET
from impresso.api_models import BaseFind, EntityDetails, Filter
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.structures import AND, OR
from impresso.util.error import raise_for_error
from impresso.util.filters import and_or_filter, filters_as_protobuf
from impresso.util.py import get_enum_from_literal


class FindEntitiesSchema(BaseFind):
    """Schema for the find entities response."""

    data: list[EntityDetails]


class FindEntitiesContainer(DataContainer):
    """Response of a find call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["data"]
        if len(data):
            return json_normalize(self._data.to_dict()["data"]).set_index("uid")
        return DataFrame()


class GetEntityContainer(DataContainer):
    """Response of a get call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()
        if len(data):
            return json_normalize([self._data.to_dict()]).set_index("uid")
        return DataFrame()


EntityType = Literal["person", "location"]


class EntitiesResource(Resource):
    """Work with entities"""

    name = "entities"

    def find(
        self,
        q: str | None = None,
        wikidata_id: str | AND[str] | OR[str] | None = None,
        entity_id: str | AND[str] | OR[str] | None = None,
        entity_type: EntityType | AND[EntityType] | OR[EntityType] | None = None,
        order_by: FindEntitiesOrderByLiteral | None = None,
        load_wikidata: bool = False,
        limit: int | None = None,
        offset: int | None = None,
    ) -> FindEntitiesContainer:
        """Find entities."""

        filters: list[Filter] = []
        if entity_type is not None:
            filters.extend(and_or_filter(entity_type, "type"))  # type: ignore
        if wikidata_id is not None:
            filters.extend(and_or_filter(wikidata_id, "wikidata_id"))
        if entity_id is not None:
            filters.extend(and_or_filter(entity_id, "uid"))

        filters_pb = filters_as_protobuf(filters or [])

        result = find_entities.sync(
            client=self._api_client,
            q=q if q is not None else UNSET,
            order_by=(
                get_enum_from_literal(order_by, FindEntitiesOrderBy)
                if order_by is not None
                else UNSET
            ),
            limit=limit if limit is not None else UNSET,
            offset=offset if offset is not None else UNSET,
            filters=filters_pb if filters_pb else UNSET,
            resolve=load_wikidata,
        )
        raise_for_error(result)
        return FindEntitiesContainer(
            result,
            FindEntitiesSchema,
            web_app_search_result_url=(
                _build_web_app_find_entities_url(
                    base_url=self._get_web_app_base_url(),
                    q=q,
                )
                if wikidata_id is None and entity_type is None
                else None
            ),
        )

    def get(self, id: str) -> GetEntityContainer:
        """Get entity by ID."""

        result = get_entity.sync(
            client=self._api_client,
            id=id,
        )
        raise_for_error(result)
        return GetEntityContainer(
            result,
            FindEntitiesSchema,
            web_app_search_result_url=_build_web_app_get_entity_url(
                base_url=self._get_web_app_base_url(),
                id=id,
            ),
        )


def _build_web_app_find_entities_url(
    base_url: str,
    q: str | None = None,
) -> str:
    query_params = {
        "q": q,
    }
    query_string = "&".join(
        f"{key}={value}" for key, value in query_params.items() if value is not None
    )
    url = f"{base_url}/entities"
    return f"{url}?{query_string}" if query_string else url


def _build_web_app_get_entity_url(
    base_url: str,
    id: str,
) -> str:
    return f"{base_url}/entities/{id}"
