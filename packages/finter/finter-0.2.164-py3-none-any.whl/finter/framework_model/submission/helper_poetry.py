from finter.settings import logger
import os


def prepare_docker_submit_files(model_name):
    """
    Copy the poetry.lock and pyproject.toml files to the model directory.
    """

    if os.path.exists("poetry.lock") and os.path.exists("pyproject.toml"):
        os.system(f"cp poetry.lock pyproject.toml {model_name}")
        logger.info("The poetry.lock and pyproject.toml files have been copied from the current directory to the model directory.")
    elif os.path.exists(os.path.expanduser("~/poetry.lock")) and os.path.exists(os.path.expanduser("~/pyproject.toml")):
        os.system(f"cp ~/poetry.lock ~/pyproject.toml {model_name}")
        logger.info("The poetry.lock and pyproject.toml files have been copied from the home directory to the model directory.")
    elif not os.path.exists(os.path.join(model_name, "poetry.lock")) or not os.path.exists(os.path.join(model_name, "pyproject.toml")):
        raise FileNotFoundError("The poetry.lock or pyproject.toml file does not exist in the model directory.")

    docker_file = """ARG PYTHON_VERSION

FROM public.ecr.aws/docker/library/python:${PYTHON_VERSION}-slim-bullseye

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry==1.8.3 && \\
    python -m poetry config virtualenvs.create false && \\
    poetry install --no-interaction --no-ansi --no-root

COPY . /app/"""

    file_name = "Dockerfile"

    full_path = os.path.join(model_name, file_name)

    with open(full_path, "w") as file:
        file.write(docker_file)

    logger.info(f"{file_name} saved to {full_path}")
