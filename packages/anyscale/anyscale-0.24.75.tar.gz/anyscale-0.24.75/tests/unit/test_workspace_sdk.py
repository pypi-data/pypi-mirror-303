import os
import re
import tempfile
from typing import Optional, Tuple
from unittest import mock
from unittest.mock import patch

from common import TEST_CONTAINERFILE, TestLogger
import pytest
from tests.unit.common import verify_file_content

from anyscale import Anyscale
from anyscale._private.anyscale_client import FakeAnyscaleClient
from anyscale._private.sdk.timer import FakeTimer
from anyscale.client.openapi_client.models.session_ssh_key import SessionSshKey
from anyscale.compute_config.models import ComputeConfig, HeadNodeConfig
from anyscale.workspace import WorkspaceSDK
from anyscale.workspace.models import (
    UpdateWorkspaceConfig,
    WorkspaceConfig,
    WorkspaceState,
)


@pytest.fixture()
def workspace_sdk_with_fakes(
    sdk_with_fakes: Tuple[Anyscale, FakeAnyscaleClient, TestLogger, FakeTimer]
) -> Tuple[WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer]:
    sdk, client, logger, timer = sdk_with_fakes
    return sdk.workspace, client, logger, timer


EXPECTED_SSH_TEMPLATE = """
Host Head-Node
  HostName {head_node_ip}
  User ubuntu
  IdentityFile {key_path}
  StrictHostKeyChecking false
  IdentitiesOnly yes

Host {name}
  HostName 0.0.0.0
  ProxyJump Head-Node
  Port 5020
  User ray
  IdentityFile {key_path}
  StrictHostKeyChecking false
  IdentitiesOnly yes
"""


class TestCreate:
    @pytest.mark.parametrize(
        "config", [WorkspaceConfig(name=None, project=None, cloud=None), None,],
    )
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
        config: Optional[WorkspaceConfig],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="Workspace name must be configured"):
            sdk.create(config=config)

    def test_basic(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"

    def test_with_container_image(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(
                name="test_workspace", containerfile=TEST_CONTAINERFILE,
            )
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        builds = fake_client.get_non_default_cluster_env_builds()
        assert len(builds) == 1
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert created_workspace.environment_id == builds[0].id

    def test_with_image_uri(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", image_uri="test_image_uri",)
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)
        builds = fake_client.get_non_default_cluster_env_builds()
        assert len(builds) == 1
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert created_workspace.environment_id == builds[0].id

    def test_with_compute_config(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(
                name="test_workspace",
                compute_config=ComputeConfig(
                    cloud=fake_client.DEFAULT_CLOUD_NAME,
                    head_node=HeadNodeConfig(
                        instance_type="head-node-instance-type", flags={},
                    ),
                    flags={},
                ),
            )
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)
        workspace_compute_config_id = created_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert compute_config.config.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert (
            compute_config.config.head_node_type.instance_type
            == "head-node-instance-type"
        )

    def test_with_idle_termination(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", idle_termination_minutes=180,)
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        workspace_compute_config_id = created_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert compute_config.idle_timeout_minutes == 180

    def test_with_requirements(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", requirements=["emoji"],)
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert fake_client._workspaces_dependencies[created_workspace.id] == ["emoji"]

    def test_with_env_vars(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", env_vars={"key": "value"},)
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert fake_client._workspaces_env_vars[created_workspace.id] == {
            "key": "value"
        }

    def test_with_full_config(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(
                name="test_workspace",
                idle_termination_minutes=180,
                containerfile=TEST_CONTAINERFILE,
                compute_config=ComputeConfig(
                    cloud=fake_client.DEFAULT_CLOUD_NAME,
                    head_node=HeadNodeConfig(
                        instance_type="head-node-instance-type", flags={},
                    ),
                    flags={},
                ),
                env_vars={"key": "value"},
                requirements=["emoji"],
            )
        )
        assert workspace_id is not None
        created_workspace = fake_client.get_workspace(id=workspace_id)

        builds = fake_client.get_non_default_cluster_env_builds()
        workspace_compute_config_id = created_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert len(builds) == 1
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert created_workspace.environment_id == builds[0].id
        assert created_workspace.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert created_workspace.creator_id == fake_client.DEFAULT_USER_ID
        assert created_workspace.creator_email == fake_client.DEFAULT_USER_EMAIL
        assert created_workspace.organization_id == fake_client.DEFAULT_ORGANIZATION_ID

        # verify compute config
        assert compute_config.idle_timeout_minutes == 180
        assert compute_config.config.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert (
            compute_config.config.head_node_type.instance_type
            == "head-node-instance-type"
        )

        # verify dependencies
        assert fake_client._workspaces_dependencies[created_workspace.id] == ["emoji"]
        assert fake_client._workspaces_env_vars[created_workspace.id] == {
            "key": "value"
        }


class TestStart:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.start(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.start(id=workspace_id)
        created_workspace_status = sdk.status(id=workspace_id)
        assert created_workspace_status == WorkspaceState.RUNNING

    def test_basic_with_name(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.start(name="test_workspace")
        created_workspace_status = sdk.status(id=workspace_id)
        assert created_workspace_status == WorkspaceState.RUNNING


class TestTerminate:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.terminate(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.terminate(id=workspace_id)
        created_workspace_status = sdk.status(id=workspace_id)
        assert created_workspace_status == WorkspaceState.TERMINATED

    def test_basic_with_name(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.terminate(name="test_workspace")
        created_workspace_status = sdk.status(id=workspace_id)
        assert created_workspace_status == WorkspaceState.TERMINATED


class TestStatus:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.status(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        status = sdk.status(id=workspace_id)
        assert status == "TERMINATED"

    def test_basic_with_name(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        status = sdk.status(name="test_workspace")
        assert status == "TERMINATED"

    def test_not_found(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        name = "test_workspace"
        with pytest.raises(
            ValueError, match=f"Workspace with name '{name}' was not found."
        ):
            sdk.status(name=name)


class TestWait:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.wait(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start
        sdk.start(id=workspace_id)

        sdk.wait(id=workspace_id)
        created_workspace_status = sdk.status(id=workspace_id)
        assert created_workspace_status == WorkspaceState.RUNNING

    def test_basic_with_name(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start
        sdk.start(id=workspace_id)

        sdk.wait(name="test_workspace")
        created_workspace_status = sdk.status(id=workspace_id)
        assert created_workspace_status == WorkspaceState.RUNNING

    def test_not_found(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        name = "test_workspace"
        with pytest.raises(
            ValueError, match=f"Workspace with name '{name}' was not found."
        ):
            sdk.wait(name=name)

    def test_custom_state(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.wait(id=workspace_id, state="TERMINATED")
        created_workspace_status = sdk.status(id=workspace_id)
        assert created_workspace_status == WorkspaceState.TERMINATED

    def test_timeout(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, _, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # wait on a workspace that is not started and verify a timeout error is raised
        with pytest.raises(
            TimeoutError,
            match=re.escape(
                f"Workspace '{workspace_id}' did not reach target state RUNNING within 1s. Last seen state: TERMINATED."
            ),
        ):
            sdk.wait(id=workspace_id, state="RUNNING", timeout_s=1)


class TestGenerateSSHConfigFile:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.generate_ssh_config_file(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            host_name, config_path = sdk.generate_ssh_config_file(
                id=workspace_id, ssh_config_path=temp_dir
            )
            assert host_name == fake_workspace.name

            verify_file_content(
                config_path,
                EXPECTED_SSH_TEMPLATE.format(
                    name=fake_workspace.name,
                    head_node_ip="1.1.1.1",
                    key_path=os.path.join(temp_dir, "fake_key_name.pem",),
                ),
            )

    def test_basic_with_name(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            host_name, config_path = sdk.generate_ssh_config_file(
                id=workspace_id, ssh_config_path=temp_dir
            )
            assert host_name == fake_workspace.name

            verify_file_content(
                config_path,
                EXPECTED_SSH_TEMPLATE.format(
                    name=fake_workspace.name,
                    head_node_ip="1.1.1.1",
                    key_path=os.path.join(temp_dir, "fake_key_name.pem",),
                ),
            )

    def test_not_found(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        name = "test_workspace"
        with pytest.raises(
            ValueError, match=f"Workspace with name '{name}' was not found."
        ):
            sdk.generate_ssh_config_file(name=name)


class TestRunCommand:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.run_command(
                name=None, id=None, cloud=None, project=None, command="ray --version"
            )

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        command = "ray --version"

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        # mock subprocess.run and verify it is called
        with patch("subprocess.run") as mock_subprocess_run:
            sdk.run_command(id=workspace_id, command=command)
            expected_call_subset = ["ssh", "-F", mock.ANY, "test_workspace", command]
            first_call = mock_subprocess_run.call_args_list[0]
            contains_expected_call = all(
                arg in first_call[0][0] for arg in expected_call_subset
            )
            assert (
                contains_expected_call
            ), "The expected subset of arguments was not found in the actual calls."

    def test_basic_with_extra_run_args(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        command = "ray --version"

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        # mock subprocess.run and verify it is called
        with patch("subprocess.run") as mock_subprocess_run:
            sdk.run_command(
                id=workspace_id, command=command, check=False, capture_output=True
            )
            expected_call_subset = ["ssh", "-F", mock.ANY, "test_workspace", command]
            first_call = mock_subprocess_run.call_args_list[0]
            contains_expected_call = all(
                arg in first_call[0][0] for arg in expected_call_subset
            )
            assert (
                contains_expected_call
            ), "The expected subset of arguments was not found in the actual calls."
            assert first_call[1]["check"] is False
            assert first_call[1]["capture_output"] is True

    def test_not_found(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        name = "test_workspace"
        with pytest.raises(
            ValueError, match=f"Workspace with name '{name}' was not found."
        ):
            sdk.run_command(name=name, command="ray --version")


class TestPull:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.pull(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        # mock subprocess.run and verify rsync is called
        with patch("subprocess.run") as mock_subprocess_run:
            local_dir = "/path/to/local/dir"
            sdk.pull(id=workspace_id, local_dir=local_dir)

            expected_call_subset = [
                "rsync",
                "-rvzl",
                "-e",
                mock.ANY,
                "ray@test_workspace:~/default/",
                local_dir,
                "--delete",
                "--exclude",
                ".git",
                "--exclude",
                ".git/objects/info/alternates",
                "--exclude",
                ".anyscale.yaml",
            ]

            first_call = mock_subprocess_run.call_args_list[0]
            contains_expected_call = all(
                arg in first_call[0][0] for arg in expected_call_subset
            )
            assert (
                contains_expected_call
            ), "The expected subset of arguments was not found in the actual calls."

    def test_basic_with_pull_git_state(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        # mock subprocess.run and verify rsync is called
        with patch("subprocess.run") as mock_subprocess_run:
            local_dir = "/path/to/local/dir"
            sdk.pull(id=workspace_id, local_dir=local_dir, pull_git_state=True)

            # verify repacing git first
            repac_call = mock_subprocess_run.call_args_list[1]
            expected_call_subset = [
                "python",
                "-m",
                "snapshot_util",
                "repack_git_repos",
            ]
            contains_expected_call = all(
                arg in repac_call[0][0] for arg in expected_call_subset
            )

            # verify rsync call
            expected_call_subset = [
                "rsync",
                "-rvzl",
                "-e",
                mock.ANY,
                "ray@test_workspace:~/default/",
                local_dir,
                "--delete",
            ]

            rsync_call = mock_subprocess_run.call_args_list[1]
            contains_expected_call = all(
                arg in rsync_call[0][0] for arg in expected_call_subset
            )
            assert (
                contains_expected_call
            ), "The expected subset of arguments was not found in the actual calls."

            # verify git is not excluded
            assert ".git" not in rsync_call[0][0]

    def test_basic_with_extra_rsync_args(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        # mock subprocess.run and verify rsync is called
        with patch("subprocess.run") as mock_subprocess_run:
            local_dir = "/path/to/local/dir"
            rsync_args = ["--exclude", "file"]
            sdk.pull(id=workspace_id, local_dir=local_dir, rsync_args=rsync_args)

            expected_call_subset = [
                "rsync",
                "-rvzl",
                "-e",
                mock.ANY,
                "ray@test_workspace:~/default/",
                local_dir,
                "--exclude",
                "file",
            ]
            first_call = mock_subprocess_run.call_args_list[0]
            contains_expected_call = all(
                arg in first_call[0][0] for arg in expected_call_subset
            )
            assert (
                contains_expected_call
            ), "The expected subset of arguments was not found in the actual calls."


class TestPush:
    def test_missing_arg(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        with pytest.raises(ValueError, match="One of 'name' or 'id' must be provided."):
            sdk.push(name=None, id=None, cloud=None, project=None)

    def test_basic_with_id(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        # mock subprocess.run and verify rsync is called
        with patch("subprocess.run") as mock_subprocess_run:
            local_dir = "/path/to/local/dir/"
            sdk.push(id=workspace_id, local_dir=local_dir)

            expected_call_subset = [
                "rsync",
                "-rvzl",
                "-e",
                mock.ANY,
                local_dir,
                "ray@test_workspace:~/default/",
                "--delete",
                "--exclude",
                ".git",
                "--exclude",
                ".git/objects/info/alternates",
                "--exclude",
                ".anyscale.yaml",
            ]

            first_call = mock_subprocess_run.call_args_list[0]
            contains_expected_call = all(
                arg in first_call[0][0] for arg in expected_call_subset
            )
            assert (
                contains_expected_call
            ), "The expected subset of arguments was not found in the actual calls."

    def test_basic_with_push_git_state(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1."
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        # mock subprocess.run and verify rsync is called
        with patch("subprocess.run") as mock_subprocess_run:
            local_dir = "/path/to/local/dir/"
            sdk.push(id=workspace_id, local_dir=local_dir, push_git_state=True)

            expected_call_subset = [
                "rsync",
                "-rvzl",
                "-e",
                mock.ANY,
                local_dir,
                "ray@test_workspace:~/default/",
                "--delete",
                "--exclude",
                ".git/objects/info/alternates",
                "--exclude",
                ".anyscale.yaml",
            ]

            first_call = mock_subprocess_run.call_args_list[0]
            contains_expected_call = all(
                arg in first_call[0][0] for arg in expected_call_subset
            )
            assert (
                contains_expected_call
            ), "The expected subset of arguments was not found in the actual calls."

            # verify that the .git directory is not excluded
            assert ".git" not in first_call[0][0]

    def test_basic_with_extra_rsync_args(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create first
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        # start it
        sdk.start(id=workspace_id)

        # update the fake client
        fake_workspace = fake_client._workspaces[workspace_id]
        fake_client._clusters_headnode_ip[fake_workspace.cluster_id] = "1.1.1.1"
        fake_client._clusters_ssh_key[fake_workspace.cluster_id] = SessionSshKey(
            key_name="fake_key_name", private_key="fake_key",
        )

        # mock subprocess.run and verify rsync is called
        with patch("subprocess.run") as mock_subprocess_run:
            local_dir = "/path/to/local/dir/"
            rsync_args = ["--exclude", "file"]
            sdk.push(id=workspace_id, local_dir=local_dir, rsync_args=rsync_args)

            expected_call_subset = [
                "rsync",
                "-rvzl",
                "-e",
                mock.ANY,
                local_dir,
                "ray@test_workspace:~/default/",
                "--exclude",
                "file",
            ]
            first_call = mock_subprocess_run.call_args_list[0]
            contains_expected_call = all(
                arg in first_call[0][0] for arg in expected_call_subset
            )
            assert (
                contains_expected_call
            ), "The expected subset of arguments was not found in the actual calls."


class TestUpdate:
    def test_basic(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        # create a workspace
        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.update(
            id=workspace_id, config=UpdateWorkspaceConfig(name="test_workspace_2")
        )
        created_workspace = fake_client.get_workspace(id=workspace_id)
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace_2"

    def test_with_container_image(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.update(
            id=workspace_id,
            config=UpdateWorkspaceConfig(containerfile=TEST_CONTAINERFILE),
        )

        created_workspace = fake_client.get_workspace(id=workspace_id)

        builds = fake_client.get_non_default_cluster_env_builds()
        assert len(builds) == 1
        assert created_workspace is not None
        assert created_workspace.name == "test_workspace"
        assert created_workspace.environment_id == builds[0].id

    def test_with_image_uri(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.update(
            id=workspace_id, config=UpdateWorkspaceConfig(image_uri="test_image_uri",)
        )

        updated_workspace = fake_client.get_workspace(id=workspace_id)
        builds = fake_client.get_non_default_cluster_env_builds()
        assert len(builds) == 1
        assert updated_workspace is not None
        assert updated_workspace.name == "test_workspace"
        assert updated_workspace.environment_id == builds[0].id

    def test_with_compute_config(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace",))
        assert workspace_id is not None

        sdk.update(
            id=workspace_id,
            config=UpdateWorkspaceConfig(
                compute_config=ComputeConfig(
                    cloud=fake_client.DEFAULT_CLOUD_NAME,
                    head_node=HeadNodeConfig(
                        instance_type="head-node-instance-type", flags={},
                    ),
                    flags={},
                ),
            ),
        )

        updated_workspace = fake_client.get_workspace(id=workspace_id)
        workspace_compute_config_id = updated_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert updated_workspace is not None
        assert updated_workspace.name == "test_workspace"
        assert compute_config.config.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert (
            compute_config.config.head_node_type.instance_type
            == "head-node-instance-type"
        )

    def test_with_idle_termination(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", idle_termination_minutes=180,)
        )
        assert workspace_id is not None

        sdk.update(
            id=workspace_id, config=UpdateWorkspaceConfig(idle_termination_minutes=500,)
        )
        updated_workspace = fake_client.get_workspace(id=workspace_id)

        workspace_compute_config_id = updated_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert updated_workspace is not None
        assert updated_workspace.name == "test_workspace"
        assert compute_config.idle_timeout_minutes == 500

    def test_with_requirements(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", requirements=["emoji"],)
        )
        assert workspace_id is not None

        sdk.update(
            id=workspace_id, config=UpdateWorkspaceConfig(requirements=["pytorch"],)
        )
        updated_workspace = fake_client.get_workspace(id=workspace_id)

        assert updated_workspace is not None
        assert updated_workspace.name == "test_workspace"
        assert fake_client._workspaces_dependencies[updated_workspace.id] == ["pytorch"]

    def test_with_env_vars(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(
            config=WorkspaceConfig(name="test_workspace", env_vars={"key": "value"},)
        )
        assert workspace_id is not None

        sdk.update(
            id=workspace_id,
            config=UpdateWorkspaceConfig(
                name="test_workspace", env_vars={"key2": "value2"},
            ),
        )
        updated_workspace = fake_client.get_workspace(id=workspace_id)

        assert updated_workspace is not None
        assert updated_workspace.name == "test_workspace"
        assert fake_client._workspaces_env_vars[updated_workspace.id] == {
            "key2": "value2"
        }

    def test_with_full_config(
        self,
        workspace_sdk_with_fakes: Tuple[
            WorkspaceSDK, FakeAnyscaleClient, TestLogger, FakeTimer
        ],
    ):
        sdk, fake_client, _, _ = workspace_sdk_with_fakes

        workspace_id = sdk.create(config=WorkspaceConfig(name="test_workspace"))
        assert workspace_id is not None

        sdk.update(
            id=workspace_id,
            config=UpdateWorkspaceConfig(
                name="test_workspace_2",
                idle_termination_minutes=180,
                containerfile=TEST_CONTAINERFILE,
                compute_config=ComputeConfig(
                    cloud=fake_client.DEFAULT_CLOUD_NAME,
                    head_node=HeadNodeConfig(
                        instance_type="head-node-instance-type", flags={},
                    ),
                    flags={},
                ),
                env_vars={"key": "value"},
                requirements=["emoji"],
            ),
        )

        updated_workspace = fake_client.get_workspace(id=workspace_id)

        builds = fake_client.get_non_default_cluster_env_builds()
        workspace_compute_config_id = updated_workspace.compute_config_id
        compute_config = fake_client.get_compute_config(workspace_compute_config_id)
        assert len(builds) == 1
        assert updated_workspace is not None
        assert updated_workspace.name == "test_workspace_2"
        assert updated_workspace.environment_id == builds[0].id
        assert updated_workspace.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert updated_workspace.creator_id == fake_client.DEFAULT_USER_ID
        assert updated_workspace.creator_email == fake_client.DEFAULT_USER_EMAIL
        assert updated_workspace.organization_id == fake_client.DEFAULT_ORGANIZATION_ID

        # verify compute config
        assert compute_config.idle_timeout_minutes == 180
        assert compute_config.config.cloud_id == fake_client.DEFAULT_CLOUD_ID
        assert (
            compute_config.config.head_node_type.instance_type
            == "head-node-instance-type"
        )

        # verify dependencies
        assert fake_client._workspaces_dependencies[updated_workspace.id] == ["emoji"]
        assert fake_client._workspaces_env_vars[updated_workspace.id] == {
            "key": "value"
        }
