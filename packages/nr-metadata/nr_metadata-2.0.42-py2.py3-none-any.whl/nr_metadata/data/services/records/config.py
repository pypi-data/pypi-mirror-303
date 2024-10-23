from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from oarepo_runtime.services.components import CustomFieldsComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from nr_metadata.data.records.api import DataRecord
from nr_metadata.data.services.records.permissions import DataPermissionPolicy
from nr_metadata.data.services.records.results import DataRecordItem, DataRecordList
from nr_metadata.data.services.records.schema import NRDataRecordSchema
from nr_metadata.data.services.records.search import DataSearchOptions


class DataServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """DataRecord service config."""

    result_item_cls = DataRecordItem

    result_list_cls = DataRecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/nr-metadata-data/"

    base_permission_policy_cls = DataPermissionPolicy

    schema = NRDataRecordSchema

    search = DataSearchOptions

    record_cls = DataRecord

    service_id = "data"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordServiceConfig.components,
        CustomFieldsComponent,
    ]

    model = "nr_metadata.data"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{+api}/nr-metadata-data/{id}"),
            "self_html": RecordLink("{+ui}/nr-metadata-data/{id}"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-data/{?args*}"),
        }
