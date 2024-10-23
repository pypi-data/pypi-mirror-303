from pandas import DataFrame, json_normalize

from impresso.api_client.api.newspapers import find_newspapers
from impresso.api_client.models.find_newspapers_order_by import (
    FindNewspapersOrderBy,
    FindNewspapersOrderByLiteral,
)
from impresso.api_client.types import UNSET
from impresso.api_models import BaseFind, Newspaper
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.util.error import raise_for_error
from impresso.util.py import get_enum_from_literal


class FindNewspapersSchema(BaseFind):
    """Schema for the find newspapers response."""

    data: list[Newspaper]


class FindNewspapersContainer(DataContainer):
    """Response of a search call."""

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["data"]
        if len(data):
            return json_normalize(self._data.to_dict()["data"]).set_index("uid")
        return DataFrame()


class NewspapersResource(Resource):
    """Search newspapers"""

    name = "newspapers"

    def find(
        self,
        q: str | None = None,
        order_by: FindNewspapersOrderByLiteral | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> FindNewspapersContainer:

        result = find_newspapers.sync(
            client=self._api_client,
            q=q if q is not None else UNSET,
            order_by=(
                get_enum_from_literal(order_by, FindNewspapersOrderBy)
                if order_by is not None
                else UNSET
            ),
            limit=limit if limit is not None else UNSET,
            offset=offset if offset is not None else UNSET,
        )
        raise_for_error(result)
        return FindNewspapersContainer(
            result,
            FindNewspapersSchema,
            web_app_search_result_url=_build_web_app_newspapers_url(
                base_url=self._get_web_app_base_url(),
                q=q,
                order_by=order_by,
            ),
        )


def _build_web_app_newspapers_url(
    base_url: str,
    q: str | None = None,
    order_by: FindNewspapersOrderByLiteral | None = None,
) -> str:
    query_params = {
        "orderBy": order_by,
        "q": q,
    }
    query_string = "&".join(
        f"{key}={value}" for key, value in query_params.items() if value is not None
    )
    url = f"{base_url}/newspapers"
    return f"{url}?{query_string}" if query_string else url
