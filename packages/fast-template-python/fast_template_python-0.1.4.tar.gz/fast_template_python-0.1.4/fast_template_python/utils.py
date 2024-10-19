import os
import shutil

from typing import List


def is_binary(file_path: str) -> bool:
    """
    Check if a file is binary.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is binary, False otherwise.
    """
    try:
        with open(file_path, "rb") as file:
            # Read a small chunk of the file to check if it's binary
            chunk = file.read(1024)
            if b"\0" in chunk:
                return True
        return False
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return True

    return True


def create_directory(directory: str):
    """
    Create a directory if it does not exist.

    Args:
        directory (str): Path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_files_in_directory(
    destination_directory: str,
    source_directory: str,
    files: List[str],
    project_name: str,
):
    """
    Create files in the specified directory.

    Args:
        destination_directory (str): Path to the root directory.
        source_directory (str): Path to the source directory.
        files (list[str]): List of files to create.
    """

    for file in files:

        # Remove the .tpl extension from the filename
        filename = file.replace("-tpl", "")

        src_file_path = os.path.join(source_directory, file)
        dest_file_path = os.path.join(destination_directory, filename)

        # Check if the file is binary
        if is_binary(src_file_path):
            # Just copy binary files without modifying them
            shutil.copyfile(src_file_path, dest_file_path)
            continue

        print(f"Creating file: {dest_file_path}")

        # Try to read the file as text, replace keywords, and write the modified content
        try:
            with open(src_file_path, "r", encoding="utf-8") as src_file:
                content = src_file.read()
                # new_content = content.format(project_name=project_name)
                new_content = content.replace("{{ project_name}}", project_name)

            with open(dest_file_path, "w", encoding="utf-8") as dest_file:
                dest_file.write(new_content)

        except (UnicodeDecodeError, IOError) as e:
            print(f"Could not process file {src_file_path} due to error: {e}")
            # Copy the file without changes if there are any issues
            shutil.copyfile(src_file_path, dest_file_path)


def copy_and_create_template(src_dir: str, destination_dir: str, project_name: str):
    """
    Copies the template and create the needed file in the specified directory

    Args:
        src_dir (str): Path to the source directory (parent folder).
        destination_dir (str): Path to the destination directory (new folder).
        project_name (str): Name of the project.

    """

    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        # Determine the destination path for the current directory
        relative_path = os.path.relpath(root, src_dir)
        new_dir = os.path.join(destination_dir, relative_path)

        # Create the new directory if it does not exist
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        # Copy files with keyword replacement
        create_files_in_directory(
            source_directory=root,
            destination_directory=new_dir,
            files=files,
            project_name=project_name,
        )
