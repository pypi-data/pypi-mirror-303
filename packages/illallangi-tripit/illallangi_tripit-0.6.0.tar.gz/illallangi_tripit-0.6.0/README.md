# Illallangi TripIt

Illallangi TripIt is a collection of command line tools to interact with TripIt.

## Requirements

- Python >= 3.10.12

## Installation

### Using Python

1. Install the dependencies:

    ```sh
    uv sync --frozen --no-dev
    ```

2. Install the project:

    ```sh
    uv sync --frozen
    ```

## Usage

### Command Line Interface

The main entry point for the CLI is `tripit-tools`. You can see the available commands by running:

```sh
tripit-tools --help
```

### Example Commands

List trips:

```sh
tripit-tools trips
```

List trips in JSON format:

```sh
tripit-tools trips --json
```

## Development

### Code Formatting and Linting

To format and lint the code, use the following command:

```sh
make ruff
```

### Cleaning Up

To clean up the project directory, use the following command:

```sh
make clean
```

### Building and Pushing Docker Image

To build the Docker image, use the following command:

```sh
make image
```

To push the Docker image to a registry defined in the `DEV_REGISTRY` environment variable, use the following command:

```sh
make push
```
