import hashlib
from tempfile import NamedTemporaryFile, TemporaryDirectory
from unittest.mock import Mock, patch

from click.testing import CliRunner

import anyscale
from anyscale.commands.llm.dataset_commands import download_dataset


def test_download():
    runner = CliRunner()

    # 1. Errors if file already exists
    with NamedTemporaryFile() as f:
        # anyscale llm dataset download my_dataset -o /tmp/existing_file
        result = runner.invoke(download_dataset, args=["my_dataset", "-o", f.name])
        assert result.exception
        assert "File already exists" in result.output

    # 2. Downloads the dataset to the specified file
    unique_str = hashlib.md5().hexdigest()
    with patch.object(
        anyscale.llm.dataset,
        anyscale.llm.dataset.download.__name__,
        new=Mock(return_value=unique_str.encode()),
    ), TemporaryDirectory() as tmp_dir:
        file_path = tmp_dir + "/my_dataset"
        result = runner.invoke(download_dataset, args=["my_dataset", "-o", file_path])
        assert "Dataset 'my_dataset' downloaded to" in result.output
        with open(file_path, "r") as output_file:
            assert output_file.read() == unique_str
