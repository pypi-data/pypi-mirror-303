from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from oarepo_runtime.services.components import CustomFieldsComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from nr_metadata.datacite.records.api import DataciteRecord
from nr_metadata.datacite.services.records.permissions import DatacitePermissionPolicy
from nr_metadata.datacite.services.records.results import (
    DataciteRecordItem,
    DataciteRecordList,
)
from nr_metadata.datacite.services.records.schema import DataCiteRecordSchema
from nr_metadata.datacite.services.records.search import DataciteSearchOptions


class DataciteServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """DataciteRecord service config."""

    result_item_cls = DataciteRecordItem

    result_list_cls = DataciteRecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/nr-metadata-datacite/"

    base_permission_policy_cls = DatacitePermissionPolicy

    schema = DataCiteRecordSchema

    search = DataciteSearchOptions

    record_cls = DataciteRecord

    service_id = "datacite"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordServiceConfig.components,
        CustomFieldsComponent,
    ]

    model = "nr_metadata.datacite"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{+api}/nr-metadata-datacite/{id}"),
            "self_html": RecordLink("{+ui}/nr-metadata-datacite/{id}"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-datacite/{?args*}"),
        }
