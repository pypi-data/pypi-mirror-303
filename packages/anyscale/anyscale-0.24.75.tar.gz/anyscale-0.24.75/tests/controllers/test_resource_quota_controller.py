from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from anyscale.client.openapi_client import Project
from anyscale.client.openapi_client.models.cloud_providers import CloudProviders
from anyscale.client.openapi_client.models.create_resource_quota import (
    CreateResourceQuota,
)
from anyscale.client.openapi_client.models.list_resource_quotas_query import (
    ListResourceQuotasQuery,
)
from anyscale.client.openapi_client.models.mini_cloud import MiniCloud
from anyscale.client.openapi_client.models.mini_user import MiniUser
from anyscale.client.openapi_client.models.organization_collaborator import (
    OrganizationCollaborator,
)
from anyscale.client.openapi_client.models.organization_permission_level import (
    OrganizationPermissionLevel,
)
from anyscale.client.openapi_client.models.quota import Quota
from anyscale.client.openapi_client.models.resource_quota import ResourceQuota
from anyscale.client.openapi_client.models.resource_quota_status import (
    ResourceQuotaStatus,
)
from anyscale.controllers.resource_quota_controller import ResourceQuotaController
from anyscale.sdk.anyscale_client.models.page_query import PageQuery
from anyscale.sdk.anyscale_client.models.text_query import TextQuery
from tests.controllers.test_service_account_controller import (
    ListResponse,
    ListResponseMetadata,
)


test_organization_collaborator = OrganizationCollaborator(
    id="test_identity_id",
    name="name",
    permission_level=OrganizationPermissionLevel.COLLABORATOR,
    created_at=datetime(2024, 7, 17),
    email="test@anyscale.com",
    user_id="user_id",
)

test_resource_quota = ResourceQuota(
    id="resource_quota_id",
    name="quota_name",
    cloud_id="cloud_id",
    project_id="project_id",
    user_id="user_id",
    is_enabled=True,
    created_at=datetime(2024, 7, 17),
    deleted_at=None,
    quota=Quota(
        num_cpus=10,
        num_instances=20,
        num_gpus=30,
        num_accelerators={"L4": 5, "T4": 10},
    ),
    creator=MiniUser(
        id="user_id", email="test@anyscale..com", name="name", username="username",
    ),
    cloud=MiniCloud(id="cloud_id", name="cloud_name", provider=CloudProviders.AWS,),
)


@pytest.fixture()
def mock_api_client(project_test_data: Project) -> Mock:
    mock_api_client = Mock()

    mock_api_client.list_organization_collaborators_api_v2_organization_collaborators_get.return_value = ListResponse(
        results=[test_organization_collaborator],
        metadata=ListResponseMetadata(total=1),
    )
    mock_api_client.find_cloud_by_name_api_v2_clouds_find_by_name_post.return_value = Mock(
        result=Mock(id="cloud_id", name="cloud_name")
    )
    mock_api_client.find_project_by_project_name_api_v2_projects_find_by_name_get.return_value = ListResponse(
        results=[project_test_data], metadata=ListResponseMetadata(total=1)
    )
    mock_api_client.create_resource_quota_api_v2_resource_quotas_post.return_value = Mock(
        result=test_resource_quota
    )
    mock_api_client.search_resource_quotas_api_v2_resource_quotas_search_post.return_value = ListResponse(
        results=[test_resource_quota], metadata=ListResponseMetadata(total=1)
    )

    return mock_api_client


@pytest.fixture()
def mock_auth_api_client(mock_api_client: Mock, base_mock_anyscale_api_client: Mock):
    mock_auth_api_client = Mock(
        api_client=mock_api_client, anyscale_api_client=base_mock_anyscale_api_client,
    )
    with patch.multiple(
        "anyscale.controllers.base_controller",
        get_auth_api_client=Mock(return_value=mock_auth_api_client),
    ):
        yield


def test_create_resource_quota(mock_auth_api_client) -> None:
    resource_quota_controller = ResourceQuotaController()

    resource_quota_controller.create(
        "quota_name",
        "cloud_name",
        "project_name",
        "test@anyscale.com",
        10,
        20,
        30,
        {"L4": 5, "T4": 10},
    )

    resource_quota_controller.api_client.create_resource_quota_api_v2_resource_quotas_post.assert_called_once_with(
        CreateResourceQuota(
            name="quota_name",
            cloud_id="cloud_id",
            project_id="project_id",
            user_id="user_id",
            quota=Quota(
                num_cpus=10,
                num_instances=20,
                num_gpus=30,
                num_accelerators={"L4": 5, "T4": 10},
            ),
        )
    )


@pytest.mark.parametrize("cloud_name", ["cloud_name", None])
def test_list_resource_quotas(cloud_name, mock_auth_api_client) -> None:
    resource_quota_controller = ResourceQuotaController()

    resource_quota_controller.list_resource_quotas(
        name="quota_name", cloud=cloud_name, creator_id="user_id", is_enabled=True,
    )

    resource_quota_controller.api_client.search_resource_quotas_api_v2_resource_quotas_search_post.assert_called_once_with(
        ListResourceQuotasQuery(
            name=TextQuery("quota_name"),
            cloud_id="cloud_id" if cloud_name else None,
            creator_id="user_id",
            is_enabled=True,
            paging=PageQuery(count=20),
        )
    )


def test_delete(mock_auth_api_client) -> None:
    resource_quota_controller = ResourceQuotaController()
    mock_resource_quota_id = "resource_quota_id"

    resource_quota_controller.delete(mock_resource_quota_id)

    resource_quota_controller.api_client.delete_resource_quota_api_v2_resource_quotas_resource_quota_id_delete.assert_called_once_with(
        mock_resource_quota_id
    )


@pytest.mark.parametrize("is_enabled", [True, False])
def test_set_status(mock_auth_api_client, is_enabled: bool) -> None:
    resource_quota_controller = ResourceQuotaController()
    mock_resource_quota_id = "resource_quota_id"

    resource_quota_controller.set_status(mock_resource_quota_id, is_enabled=is_enabled)

    resource_quota_controller.api_client.set_resource_quota_status_api_v2_resource_quotas_resource_quota_id_status_patch.assert_called_once_with(
        mock_resource_quota_id, ResourceQuotaStatus(is_enabled=is_enabled)
    )
