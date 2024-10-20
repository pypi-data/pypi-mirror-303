import click
from autotasker.managers.docker_manager import DockerManager
from InquirerPy import prompt, inquirer


@click.group()
@click.version_option(version="0.2.0", message=f"autotasker 0.2.0")
def cli():
    """Application for Automating Processes."""
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--only-image', is_flag=True, default=False,
              help='Creates only the image, without starting the container.')
@click.option('--only-dockerfile', is_flag=True, default=False,
              help='Generates only the Dockerfile without building the image or starting the container.')
@click.option('-e', '--env', 'env', default=None, multiple=True,
              help='Sets environment variables to be passed to the container during creation.')
@click.option('--env-file', type=click.Path(exists=True),
              help='''Path to a file containing additional environment variables. Each line of the file should
contain a key-value pair formatted as `KEY=value`. These variables are read and also included
in the Dockerfile as `ENV` instructions.''')
@click.option('-p', "--port", default=80, help='Specifies the port on which the container will expose its services. '
                                               'Defaults to port 80 if not specified.')
@click.option('-v', "--version", default='lts', help='Defines the version of the language or runtime environment to be '
                                                     'used. If not provided, the latest available version will be used'
                                                     ' by default.')
def docker(path: str, only_image: bool, only_dockerfile: bool, env: tuple, env_file: str, port: int, version: str):
    """Creates a Docker container based on user input."""

    click.echo(click.style(" Select the programming language:", bold=True, fg='cyan'))
    languages = [
        {"name": "Django", "value": "django"},
        {"name": "Vite", "value": "vite"},
        {"name": "React (Vanilla)", "value": "react"},
        {"name": "Next.js", "value": "nextjs"},
    ]

    questions = [
        {
            "type": "list",
            "message": "Seleccione un lenguaje:",
            "choices": languages,
            "default": "python",
        }
    ]

    selected_language = prompt(questions)

    selected_lang = selected_language[0]
    if not only_dockerfile:
        image_name = inquirer.text(message="Enter the name of the Docker image:").execute()

        container_name = None
        if not only_image:
            container_name = inquirer.text(message="Enter the name of the Docker container:").execute()

        dockermanager = DockerManager(dockerfile_path=path, language=selected_lang, image=image_name, port=port,
                                      container=container_name, version=version, envs=env, env_file=env_file)

        dockermanager.create_dockerfile()

        dockermanager.create_image()

        if not only_image:
            dockermanager.create_container()
    else:
        dockermanager = DockerManager(dockerfile_path=path, language=selected_lang, envs=env, port=port,
                                      version=version, env_file=env_file, image=None)

        dockermanager.create_dockerfile()


# Hay que añadir contexto en la database


@cli.group()
def database():
    """Comandos para gestionar bases de datos."""


@database.command()
def importar_info():
    """Importar datos a una base de datos"""
    click.echo("datos importados")


@database.command()
def copias_seguridad():
    """Crea copias de seguridad"""
    click.echo("copia creada")


if __name__ == '__main__':
    cli()
