import os
from typing import Optional
from .utils import create_directory, create_files_in_directory, copy_and_create_template

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIRECTORY = os.path.join(BASE_DIRECTORY, "conf")

BASE_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "base_template")
DATABASE_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "database_template")
JOB_MANAGER_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "job_manager_template")
ROOT_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "root_template")
ROUTERS_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "routers_template")
SCHEMAS_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "schemas_template")
SERVICES_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "services_template")


def create_database_template(project_name: str, destination_directory: str):
    """
    Create a database template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print("\nCreating database files")
    database_destination_directory = os.path.join(destination_directory, "database")

    create_directory(database_destination_directory)

    copy_and_create_template(
        src_dir=DATABASE_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=database_destination_directory,
    )


def create_job_manager_template(project_name: str, destination_directory: str):
    """
    Create a job manager template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print("\nCreating job manager")
    job_manager_destination_directory = os.path.join(destination_directory, "job_manager")

    create_directory(job_manager_destination_directory)

    copy_and_create_template(
        src_dir=JOB_MANAGER_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=job_manager_destination_directory,
    )


def create_root_template(project_name: str, destination_directory: str):
    """
    Create a root template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print("\nCreating root content")
    root_destination_directory = os.path.join(destination_directory, "root")

    create_directory(root_destination_directory)

    copy_and_create_template(
        src_dir=ROOT_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=root_destination_directory,
    )


def create_routers_template(project_name: str, destination_directory: str):
    """
    Create a routers template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """

    print("\nCreating routers")
    router_destination_directory = os.path.join(destination_directory, "routers")

    create_directory(router_destination_directory)

    copy_and_create_template(
        src_dir=ROUTERS_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=router_destination_directory,
    )


def create_schemas_template(project_name: str, destination_directory: str):
    """
    Create a schemas template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print("\nCreating schemas")
    schemas_destination_directory = os.path.join(destination_directory, "schemas")

    create_directory(schemas_destination_directory)

    copy_and_create_template(
        src_dir=SCHEMAS_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=schemas_destination_directory,
    )


def create_services_template(project_name: str, destination_directory: str):
    """
    Create a services template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """

    print("\nCreating services")
    services_destination_directory = os.path.join(destination_directory, "services")

    create_directory(services_destination_directory)

    copy_and_create_template(
        src_dir=SERVICES_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=services_destination_directory,
    )


def create_base_template(project_name: str, destination_directory: str):

    print("\nCreating base template")

    copy_and_create_template(
        src_dir=BASE_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=destination_directory,
    )


def create_fast_template(
    project_name: str,
    root_directory: Optional[str] = None,
    create_venv: bool = True,
):
    """
    Create a FastAPI template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
        create_venv (bool): Create a virtual environment and install dependencies.
    """

    if root_directory is None:
        root_directory = os.path.join(os.getcwd(), project_name)

    if root_directory != ".":
        print(f"Creating template in {root_directory}")
        create_directory(root_directory)

    destination_directory = os.path.join(root_directory, project_name)
    create_directory(destination_directory)

    create_base_template(project_name, root_directory)

    create_database_template(project_name, destination_directory)
    create_job_manager_template(project_name, destination_directory)
    create_root_template(project_name, destination_directory)
    create_routers_template(project_name, destination_directory)
    create_schemas_template(project_name, destination_directory)
    create_services_template(project_name, destination_directory)

    if create_venv:

        if not os.path.exists(f"{root_directory}/venv"):
            os.system(f"cd {root_directory} && python3 -m venv venv")

        os.system(
            f"cd {root_directory} && source venv/bin/activate && pip install -r requirements.txt && pip freeze > requirements.txt"
        )
        print("Virtual environment created and dependencies installed.")
    else:
        os.system(f"cd {root_directory} && pip install -r requirements.txt && pip freeze > requirements.txt")
        print("Template created successfully.")


if __name__ == "__main__":
    create_fast_template(
        root_directory="/Users/akandepeter/DevProjects/Backend/cloned/test2",
        project_name="test2",
    )
