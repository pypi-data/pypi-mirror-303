import typer
from typing import Optional

from .fast_template import create_fast_template

app = typer.Typer()


@app.callback()
def callback():
    """
    FastAPI project generator.
    """
    pass


@app.command(name="init")
def init(
    project_name: str,
    root_directory: Optional[str] = None,
    create_venv: bool = True,
):
    """
    Initialize a FastAPI project from template.
    """
    create_fast_template(
        project_name=project_name,
        root_directory=root_directory,
        create_venv=create_venv,
    )
