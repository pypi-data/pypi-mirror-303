import os
import tempfile
import shutil
import pytest
from ara_cli.file_lister import generate_markdown_listing

@pytest.fixture
def setup_test_environment():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create nested directories and files
    os.makedirs(os.path.join(temp_dir, 'dir1'))
    os.makedirs(os.path.join(temp_dir, 'dir2', 'subdir1'))

    # Create files
    open(os.path.join(temp_dir, 'file1.py'), 'a').close()
    open(os.path.join(temp_dir, 'file2.txt'), 'a').close()
    open(os.path.join(temp_dir, 'dir1', 'file3.py'), 'a').close()
    open(os.path.join(temp_dir, 'dir2', 'file4.py'), 'a').close()
    open(os.path.join(temp_dir, 'dir2', 'subdir1', 'file5.py'), 'a').close()

    yield temp_dir

    # Cleanup
    shutil.rmtree(temp_dir)


def test_generate_markdown_listing_multiple_directories(setup_test_environment):
    temp_dir = setup_test_environment
    another_temp_dir = tempfile.mkdtemp()

    try:
        os.makedirs(os.path.join(another_temp_dir, 'dir3'))
        open(os.path.join(another_temp_dir, 'file6.py'), 'a').close()

        output_file_path = os.path.join(temp_dir, "output_multiple_dirs.md")

        expected_content = [
            f"# {os.path.basename(temp_dir)}",
            " - [] file1.py",
            "## dir1",
            "     - [] file3.py",
            "## dir2",
            "     - [] file4.py",
            "### subdir1",
            "         - [] file5.py",
            f"# {os.path.basename(another_temp_dir)}",
            " - [] file6.py",
            "## dir3"
        ]

        generate_markdown_listing([temp_dir, another_temp_dir], ['*.py'], output_file_path)

        with open(output_file_path, 'r') as f:
            output_content = f.read().splitlines()

        assert output_content == expected_content

    finally:
        shutil.rmtree(another_temp_dir)
