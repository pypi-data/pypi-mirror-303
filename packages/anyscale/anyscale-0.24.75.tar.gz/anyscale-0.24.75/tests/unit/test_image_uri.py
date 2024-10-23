import re
from unittest.mock import Mock

from common import OPENAPI_NO_VALIDATION
import pytest

from anyscale._private.models.image_uri import ImageURI
from anyscale.sdk.anyscale_client.models.cluster_environment import ClusterEnvironment
from anyscale.sdk.anyscale_client.models.cluster_environment_build import (
    ClusterEnvironmentBuild,
)


class TestImageURI:
    @pytest.mark.parametrize(
        ("image_uri_str", "expected_name"),
        [
            ("docker.us.com/my/fakeimage:latest", "docker-us-com-my-fakeimage-latest"),
            ("library/ubuntu@sha256:45b23dee08", "library-ubuntu-sha256-45b23dee08"),
        ],
    )
    def test_image_uri_to_cluster_env_name(
        self, image_uri_str, expected_name,
    ):
        image_uri = ImageURI.from_str(image_uri_str)
        assert image_uri.to_cluster_env_name() == expected_name

    def test_empty_image_uri(self,):
        assert str(ImageURI.from_str("")) == ""

    @pytest.mark.parametrize(
        ("image_uri_str", "is_legacy_cluster_env_image"),
        [("docker.us.com/my/fakeimage:laest", False), ("anyscale/image/name:5", True),],
    )
    def test_image_uri_is_legacy_cluster_env_image(
        self, image_uri_str, is_legacy_cluster_env_image
    ):
        assert (
            ImageURI.from_str(image_uri_str).is_cluster_env_image()
            == is_legacy_cluster_env_image
        )

    @pytest.mark.parametrize(
        ("image_uri", "valid"),
        [
            ("anyscale/cluster_env/default_cluster_env_2.9.3_py39:1", True),
            ("docker.io/libaray/ubuntu:latest", True),
            ("ubuntu:latest", True),
            ("python:3.8", True),
            ("myregistry.local:5000/testing/test-image:1.0.0", True),
            ("localhost:5000/myusername/myrepository:latest", True),
            ("localhost:5000/myusername/my/repository:latest", True),
            ("valid/withouttag", True),
            ("valid_name/withtag_and_digest:v2@sha213", True),
            ("valid_name/withtag_and_digest@sha213", True),
            ("valid_name/withtag_and_digest:@sha213", False),
            ("http://myregistry.local:5000/testing/test-image:1.0.0", False),
            (
                "us-docker.pkg.dev/anyscale-workspace-templates/workspace-templates/rag-dev-bootcamp-mar-2024:raynightly-py310",
                True,
            ),
            (
                "241673607239.dkr.ecr.us-west-2.amazonaws.com/aviary:release-endpoints_aica-e8873f9361e29289bcea2de47d967bdd5291ac46",
                True,
            ),
        ],
    )
    def test_image_uri_validation(self, image_uri: str, valid: bool):
        if valid:
            assert str(ImageURI.from_str(image_uri)) == image_uri
        else:
            with pytest.raises(
                ValueError,
                match=re.escape(
                    f"Invalid image URI: '{image_uri}'. Must be in the format: '[registry_host/]user_name/repository[:tag][@digest]'."
                ),
            ):
                ImageURI.from_str(image_uri)

    @pytest.mark.parametrize(
        ("build", "use_image_alias", "expected_image_uri"),
        [
            pytest.param(
                Mock(
                    is_byod=True,
                    config_json=None,
                    containerfile=None,
                    revision=3,
                    docker_image_name="docker.io/libaray/ubuntu:latest",
                ),
                True,
                "anyscale/image/cluser_env_name:3",
                id="use_image_alias",
            ),
            pytest.param(
                Mock(
                    is_byod=True,
                    config_json=None,
                    containerfile=None,
                    revision=3,
                    docker_image_name="docker.io/libaray/ubuntu:latest",
                ),
                False,
                "docker.io/libaray/ubuntu:latest",
                id="not_use_image_alias",
            ),
            pytest.param(
                Mock(
                    is_byod=False,
                    config_json=None,
                    containerfile="something",
                    revision=3,
                ),
                False,
                "anyscale/image/cluser_env_name:3",
                id="non-byod-build",
            ),
            pytest.param(
                Mock(
                    is_byod=False,
                    config_json=Mock(),
                    containerfile=None,
                    cluster_environment_id="DEFAULT_APP_CONFIG_ID_2.8.1_py39",
                    revision=1,
                ),
                False,
                # expect cluster_env.name is used. When it's a default build, cluster_env.name will be the default build id, e.g. "anyscale/ray:2.36.1-slim-py312-cu123".
                "cluser_env_name",
                id="default_build",
            ),
        ],
    )
    def test_from_cluster_env_build(
        self,
        build: ClusterEnvironmentBuild,
        use_image_alias: bool,
        expected_image_uri: str,
    ):
        cluster_env = ClusterEnvironment(
            name="cluser_env_name", local_vars_configuration=OPENAPI_NO_VALIDATION,
        )
        assert (
            ImageURI.from_cluster_env_build(
                cluster_env, build, use_image_alias
            ).image_uri
            == expected_image_uri
        )
