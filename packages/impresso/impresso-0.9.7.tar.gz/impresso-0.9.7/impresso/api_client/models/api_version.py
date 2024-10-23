from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.api_version_api_version import APIVersionApiVersion
    from ..models.api_version_documents_date_span import APIVersionDocumentsDateSpan
    from ..models.api_version_features import APIVersionFeatures
    from ..models.api_version_mysql import APIVersionMysql
    from ..models.api_version_newspapers import APIVersionNewspapers
    from ..models.api_version_solr import APIVersionSolr


T = TypeVar("T", bound="APIVersion")


@_attrs_define
class APIVersion:
    """Version of the API. Contains information about the current version of the API, features, etc.

    Attributes:
        solr (APIVersionSolr):
        mysql (APIVersionMysql):
        version (str):
        api_version (APIVersionApiVersion):
        documents_date_span (APIVersionDocumentsDateSpan):
        newspapers (APIVersionNewspapers):
        features (APIVersionFeatures):
    """

    solr: "APIVersionSolr"
    mysql: "APIVersionMysql"
    version: str
    api_version: "APIVersionApiVersion"
    documents_date_span: "APIVersionDocumentsDateSpan"
    newspapers: "APIVersionNewspapers"
    features: "APIVersionFeatures"

    def to_dict(self) -> Dict[str, Any]:
        solr = self.solr.to_dict()

        mysql = self.mysql.to_dict()

        version = self.version

        api_version = self.api_version.to_dict()

        documents_date_span = self.documents_date_span.to_dict()

        newspapers = self.newspapers.to_dict()

        features = self.features.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "solr": solr,
                "mysql": mysql,
                "version": version,
                "apiVersion": api_version,
                "documentsDateSpan": documents_date_span,
                "newspapers": newspapers,
                "features": features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_version_api_version import APIVersionApiVersion
        from ..models.api_version_documents_date_span import APIVersionDocumentsDateSpan
        from ..models.api_version_features import APIVersionFeatures
        from ..models.api_version_mysql import APIVersionMysql
        from ..models.api_version_newspapers import APIVersionNewspapers
        from ..models.api_version_solr import APIVersionSolr

        d = src_dict.copy()
        solr = APIVersionSolr.from_dict(d.pop("solr"))

        mysql = APIVersionMysql.from_dict(d.pop("mysql"))

        version = d.pop("version")

        api_version = APIVersionApiVersion.from_dict(d.pop("apiVersion"))

        documents_date_span = APIVersionDocumentsDateSpan.from_dict(d.pop("documentsDateSpan"))

        newspapers = APIVersionNewspapers.from_dict(d.pop("newspapers"))

        features = APIVersionFeatures.from_dict(d.pop("features"))

        api_version = cls(
            solr=solr,
            mysql=mysql,
            version=version,
            api_version=api_version,
            documents_date_span=documents_date_span,
            newspapers=newspapers,
            features=features,
        )

        return api_version
