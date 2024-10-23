from datetime import datetime
from unittest.mock import Mock, patch

import anyscale
from anyscale._private.anyscale_client.anyscale_client import AnyscaleClient
from anyscale.client.openapi_client.models import Dataset as InternalDataset
from anyscale.llm.dataset import Dataset


def test_sdk():
    internal_dataset = InternalDataset(
        filename="test.jsonl",
        description="description",
        name="my_dataset",
        project_id="prj_123",
        id="dataset_123",
        creator_id="usr_123",
        created_at=datetime(2024, 1, 1),
        cloud_id="cld_123",
        num_versions=3,
        storage_uri="s3://bucket/path/to/test.jsonl",
        version=3,
    )

    def do_assertion(dataset: Dataset):
        assert dataset == Dataset(
            id="dataset_123",
            name="my_dataset",
            filename="test.jsonl",
            storage_uri="s3://bucket/path/to/test.jsonl",
            version=3,
            num_versions=3,
            created_at=datetime(2024, 1, 1),
            creator_id="usr_123",
            project_id="prj_123",
            cloud_id="cld_123",
            description="description",
        )

    with patch.multiple(
        AnyscaleClient,
        **{
            AnyscaleClient.__init__.__name__: Mock(return_value=None),
            AnyscaleClient.upload_dataset.__name__: Mock(return_value=internal_dataset),
            AnyscaleClient.get_dataset.__name__: Mock(return_value=internal_dataset),
            AnyscaleClient.download_dataset.__name__: Mock(return_value="hi".encode()),
        }
    ):
        dataset = anyscale.llm.dataset.upload("test.jsonl", "my_dataset")
        do_assertion(dataset)
        dataset = anyscale.llm.dataset.get("my_dataset")
        do_assertion(dataset)
        assert anyscale.llm.dataset.download("my_dataset").decode() == "hi"
