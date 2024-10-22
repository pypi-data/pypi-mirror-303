import os
import shutil
from zinley.v2_new.code.main import create_versioned_project_copy, copy_project_with_version_control

def test_create_versioned_project_copy(tmpdir):
    # Create a temporary directory for testing
    temp_dir = ".zinley"
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    # Create a dummy project directory
    project_path = os.path.join(temp_dir, "project")
    if not os.path.exists(project_path):
        os.mkdir(project_path)

    # Call the create_versioned_project_copy function
    create_versioned_project_copy(project_path)

    # Assert that the version control directory is created
    version_control_base_path = os.path.join(temp_dir, "Version_control")
    assert os.path.exists(version_control_base_path)

    # Assert that the project folder is created within the version control directory
    project_version_control_path = os.path.join(version_control_base_path, "../project")
    assert os.path.exists(project_version_control_path)


def test_copy_project_with_version_control(tmpdir):
    # Create a temporary directory for testing
    temp_dir = ".zinley"
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    # Create a dummy project directory
    project_path = os.path.join(temp_dir, "project")
    if not os.path.exists(project_path):
        os.mkdir(project_path)

    # Call the copy_project_with_version_control function
    copy_project_with_version_control(project_path)

    # Assert that the version control directory is created
    version_control_base_path = os.path.join(temp_dir, "Version_control")
    assert os.path.exists(version_control_base_path)

    # Assert that the project folder is created within the version control directory
    project_version_control_path = os.path.join(version_control_base_path, "../project")
    assert os.path.exists(project_version_control_path)