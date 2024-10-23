from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from oarepo_runtime.services.components import CustomFieldsComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from nr_metadata.common.records.api import CommonRecord
from nr_metadata.common.services.records.permissions import CommonPermissionPolicy
from nr_metadata.common.services.records.results import (
    CommonRecordItem,
    CommonRecordList,
)
from nr_metadata.common.services.records.schema_common import NRCommonRecordSchema
from nr_metadata.common.services.records.search import CommonSearchOptions


class CommonServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """CommonRecord service config."""

    result_item_cls = CommonRecordItem

    result_list_cls = CommonRecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/nr-metadata-common/"

    base_permission_policy_cls = CommonPermissionPolicy

    schema = NRCommonRecordSchema

    search = CommonSearchOptions

    record_cls = CommonRecord

    service_id = "common"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordServiceConfig.components,
        CustomFieldsComponent,
    ]

    model = "nr_metadata.common"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{+api}/nr-metadata-common/{id}"),
            "self_html": RecordLink("{+ui}/nr-metadata-common/{id}"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-common/{?args*}"),
        }
