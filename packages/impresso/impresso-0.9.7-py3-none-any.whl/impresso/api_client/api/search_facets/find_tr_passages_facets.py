from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.filter_ import Filter
from ...models.find_tr_passages_facets_facets_item import FindTrPassagesFacetsFacetsItem
from ...models.find_tr_passages_facets_group_by import FindTrPassagesFacetsGroupBy
from ...models.find_tr_passages_facets_order_by import FindTrPassagesFacetsOrderBy
from ...models.find_tr_passages_facets_range_include import FindTrPassagesFacetsRangeInclude
from ...models.find_tr_passages_facets_response_200 import FindTrPassagesFacetsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    facets: List[FindTrPassagesFacetsFacetsItem],
    order_by: Union[Unset, FindTrPassagesFacetsOrderBy] = UNSET,
    group_by: Union[Unset, FindTrPassagesFacetsGroupBy] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    range_start: Union[Unset, float] = UNSET,
    range_end: Union[Unset, float] = UNSET,
    range_gap: Union[Unset, float] = UNSET,
    range_include: Union[Unset, FindTrPassagesFacetsRangeInclude] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_facets = []
    for facets_item_data in facets:
        facets_item = facets_item_data.value
        json_facets.append(facets_item)

    params["facets"] = json_facets

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_group_by: Union[Unset, str] = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = group_by.value

    params["group_by"] = json_group_by

    json_filters: Union[List[Dict[str, Any]], Unset, str]
    if isinstance(filters, Unset):
        json_filters = UNSET
    elif isinstance(filters, list):
        json_filters = []
        for filters_type_1_item_data in filters:
            filters_type_1_item = filters_type_1_item_data.to_dict()
            json_filters.append(filters_type_1_item)

    else:
        json_filters = filters
    params["filters"] = json_filters

    params["range_start"] = range_start

    params["range_end"] = range_end

    params["range_gap"] = range_gap

    json_range_include: Union[Unset, str] = UNSET
    if not isinstance(range_include, Unset):
        json_range_include = range_include.value

    params["range_include"] = json_range_include

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/search-facets/tr-passages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, FindTrPassagesFacetsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FindTrPassagesFacetsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = Error.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = Error.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, FindTrPassagesFacetsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    facets: List[FindTrPassagesFacetsFacetsItem],
    order_by: Union[Unset, FindTrPassagesFacetsOrderBy] = UNSET,
    group_by: Union[Unset, FindTrPassagesFacetsGroupBy] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    range_start: Union[Unset, float] = UNSET,
    range_end: Union[Unset, float] = UNSET,
    range_gap: Union[Unset, float] = UNSET,
    range_include: Union[Unset, FindTrPassagesFacetsRangeInclude] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error, FindTrPassagesFacetsResponse200]]:
    """Get mutliple text reuse passages index facets

    Args:
        facets (List[FindTrPassagesFacetsFacetsItem]):
        order_by (Union[Unset, FindTrPassagesFacetsOrderBy]):
        group_by (Union[Unset, FindTrPassagesFacetsGroupBy]):
        filters (Union[List['Filter'], Unset, str]):
        range_start (Union[Unset, float]):
        range_end (Union[Unset, float]):
        range_gap (Union[Unset, float]):
        range_include (Union[Unset, FindTrPassagesFacetsRangeInclude]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FindTrPassagesFacetsResponse200]]
    """

    kwargs = _get_kwargs(
        facets=facets,
        order_by=order_by,
        group_by=group_by,
        filters=filters,
        range_start=range_start,
        range_end=range_end,
        range_gap=range_gap,
        range_include=range_include,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    facets: List[FindTrPassagesFacetsFacetsItem],
    order_by: Union[Unset, FindTrPassagesFacetsOrderBy] = UNSET,
    group_by: Union[Unset, FindTrPassagesFacetsGroupBy] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    range_start: Union[Unset, float] = UNSET,
    range_end: Union[Unset, float] = UNSET,
    range_gap: Union[Unset, float] = UNSET,
    range_include: Union[Unset, FindTrPassagesFacetsRangeInclude] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error, FindTrPassagesFacetsResponse200]]:
    """Get mutliple text reuse passages index facets

    Args:
        facets (List[FindTrPassagesFacetsFacetsItem]):
        order_by (Union[Unset, FindTrPassagesFacetsOrderBy]):
        group_by (Union[Unset, FindTrPassagesFacetsGroupBy]):
        filters (Union[List['Filter'], Unset, str]):
        range_start (Union[Unset, float]):
        range_end (Union[Unset, float]):
        range_gap (Union[Unset, float]):
        range_include (Union[Unset, FindTrPassagesFacetsRangeInclude]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, FindTrPassagesFacetsResponse200]
    """

    return sync_detailed(
        client=client,
        facets=facets,
        order_by=order_by,
        group_by=group_by,
        filters=filters,
        range_start=range_start,
        range_end=range_end,
        range_gap=range_gap,
        range_include=range_include,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    facets: List[FindTrPassagesFacetsFacetsItem],
    order_by: Union[Unset, FindTrPassagesFacetsOrderBy] = UNSET,
    group_by: Union[Unset, FindTrPassagesFacetsGroupBy] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    range_start: Union[Unset, float] = UNSET,
    range_end: Union[Unset, float] = UNSET,
    range_gap: Union[Unset, float] = UNSET,
    range_include: Union[Unset, FindTrPassagesFacetsRangeInclude] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error, FindTrPassagesFacetsResponse200]]:
    """Get mutliple text reuse passages index facets

    Args:
        facets (List[FindTrPassagesFacetsFacetsItem]):
        order_by (Union[Unset, FindTrPassagesFacetsOrderBy]):
        group_by (Union[Unset, FindTrPassagesFacetsGroupBy]):
        filters (Union[List['Filter'], Unset, str]):
        range_start (Union[Unset, float]):
        range_end (Union[Unset, float]):
        range_gap (Union[Unset, float]):
        range_include (Union[Unset, FindTrPassagesFacetsRangeInclude]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FindTrPassagesFacetsResponse200]]
    """

    kwargs = _get_kwargs(
        facets=facets,
        order_by=order_by,
        group_by=group_by,
        filters=filters,
        range_start=range_start,
        range_end=range_end,
        range_gap=range_gap,
        range_include=range_include,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    facets: List[FindTrPassagesFacetsFacetsItem],
    order_by: Union[Unset, FindTrPassagesFacetsOrderBy] = UNSET,
    group_by: Union[Unset, FindTrPassagesFacetsGroupBy] = UNSET,
    filters: Union[List["Filter"], Unset, str] = UNSET,
    range_start: Union[Unset, float] = UNSET,
    range_end: Union[Unset, float] = UNSET,
    range_gap: Union[Unset, float] = UNSET,
    range_include: Union[Unset, FindTrPassagesFacetsRangeInclude] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error, FindTrPassagesFacetsResponse200]]:
    """Get mutliple text reuse passages index facets

    Args:
        facets (List[FindTrPassagesFacetsFacetsItem]):
        order_by (Union[Unset, FindTrPassagesFacetsOrderBy]):
        group_by (Union[Unset, FindTrPassagesFacetsGroupBy]):
        filters (Union[List['Filter'], Unset, str]):
        range_start (Union[Unset, float]):
        range_end (Union[Unset, float]):
        range_gap (Union[Unset, float]):
        range_include (Union[Unset, FindTrPassagesFacetsRangeInclude]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, FindTrPassagesFacetsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            facets=facets,
            order_by=order_by,
            group_by=group_by,
            filters=filters,
            range_start=range_start,
            range_end=range_end,
            range_gap=range_gap,
            range_include=range_include,
            limit=limit,
            offset=offset,
        )
    ).parsed
