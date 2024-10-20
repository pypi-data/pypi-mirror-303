# Autotasker
>[!WARNING]
>  This project is still a work in progress, so you may encounter errors while using it.

[![GPL License](https://img.shields.io/badge/license-GPL-blue.svg)](http://www.gnu.org/licenses/gpl-3.0) 
![Version](https://img.shields.io/badge/version-0.1.1-green.svg)
[![Download Stats](https://img.shields.io/pypi/dm/autotasker)](https://pypistats.org/packages/autotasker)
[![Github repository](https://img.shields.io/badge/GitHub-autotasker-purple)](https://github.com/mramosg7/autotasker)


## Application Overview

AutoTasker is a console application designed to simplify and automate repetitive tasks without the need for programming skills. With AutoTasker, you can easily set up a variety of automated tasks, saving you time and effort in your daily activities.

## Installation 
### PyPI
>[!WARNING]
>  If you install this application via PyPI, please ensure you do so within a virtual environment.

To install the application via `PyPI`, please execute the following command: 
```bash 
pip install autotasker
```
### pipx
To install the application using `pipx`, please follow these steps:

- **Install pipx**: If you're unsure how to install pipx, please refer to the official documentation at [pipx documentation](https://pipx.pypa.io/stable/).
- **Install autotasker**:
```bash 
pipx install autotasker 
```
## Commands
This application includes a variety of commands designed to simplify your tasks and enhance productivity. Below are the available commands, each with a brief description and usage instructions.
### Docker Commands
#### Create containers and images with a single command

The `autotasker` command allows you to create Docker containers and images with just one simple command.

#### Usage:
```bash
autotasker docker [OPTIONS] PATH
```

#### Arguments: 
| Argument                  | Description |
|---------------------------|-------------|
| `path`                    | The directory path where the Dockerfile and related files will be created.|

#### Options

| Option                 | Description                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------|
| `--only-image`        | If set, creates only the Docker image without starting the container.      
| `--only-dockerfile`        | Generates only the Dockerfile without building the image or starting the container.                      |
| `-e`, `--env`                | Sets environment variables to be passed to the container during creation.                   |
| `--env-file`          | Specifies a file containing environment variables to be loaded into the container.           |
| `-p`, `--port`        | Specifies the port on which the container will expose its services.                         |
| `-v`, `--version`     | Defines the version of the language or runtime environment to be used.                      |

#### Usage examples

  - Create a docker image:
  ```bash
    autotasker docker --only-image /path/to/your/directory
  ```
  - Create a dockerfile:
  ```bash
    autotasker docker --only-dockerfile /path/to/your/directory
  ```
  - Create a docker container with environment variables:
  ```bash
    autotasker docker --env NAME=Mario --env AGE=21 /path/to/your/directory
  ```
  ```bash
    autotasker docker --env-file /path/to/your/environment/variables /path/to/your/directory
  ```
  - Create a docker container with custom port:
  ```bash
  autotasker docker -p 8000 /path/to/your/directory
  ```
  - Create  a docker container with a specific version:
  ```bash
  autotasker docker -v 3.12 /path/to/your/directory
  ```

#### Additional information
- Make sure you have docker installed on your machine before running this command.

#### Supported Frameworks

- Django
- React
- Vite
- Next.js