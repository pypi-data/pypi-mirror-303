# ComputeNest-CLI

## Project Description

`computenest-cli` is a command-line tool that integrates the creation, updating, and deployment of artifacts, as well as
the creation and updating of services within the ComputeNest framework. It allows users to manage their services,
construct artifacts, and handle custom operations, such as custom image creation.

## Requirements

- Python >= 3.7

## Installation

`computenest-cli` can be installed using the pip package manager.

```shell
# Install the computenest-cli 
pip install computenest-cli
```

## Usage

To use `computenest-cli`, simply run the corresponding command with the required parameters. Each command comes with
a `--help` option to display help information about the command's usage.

### Login to the ComputeNest

#### Description

Login to the ComputeNest.

#### Parameters

| Parameter             | Required | Description                                         | Example Value          |
|-----------------------|----------|-----------------------------------------------------|------------------------|
| `--access_key_id`     | Yes      | The Access Key ID needed for authentication.        | `AKID1234567890`       |
| `--access_key_secret` | Yes      | The Access Key Secret required for authentication.  | `secret1234567890`     |
| `--security_token`    | No       | Security Token needed for authentication; optional. | `security_token_value` |

#### Example：

```bash
computenest-cli login \
    --access_key_id AKID1234567890 \
    --access_key_secret secret1234567890
```

### List Supported Service Templates

#### Description

List the supported service templates. Use this command to obtain the supported service templates and get the project
name,
you can use `computenest-cli init-project --project_name xxx` to initial a project.

#### Parameters

| Parameter        | Required | Description                                              | Example Value |
|------------------|----------|----------------------------------------------------------|---------------|
| `--service_type` | No       | Type of service. Options include `private` or `managed`. | `private`     |

#### Example：

```bash
computenest-cli list-projects --service_type private
```

### Initializing a Project

#### Description

Initialize a project by specifying the project name. This command will download the specified project to the
output_path,
and you can quickly use `computenest-cli import` to create a ComputeNest service by the downloaded project.

#### Parameters

| Parameter        | Required | Description                                                           | Example Value     |
|------------------|----------|-----------------------------------------------------------------------|-------------------|
| `--project_name` | Yes      | Name of the project.                                                  | `MyProject`       |
| `--output_path`  | Yes      | Path to the output directory where the generated files will be saved. | `/path/to/output` |

#### Example：

```bash
computenest-cli init-project --project_name springboot-package-ecs-demo --output_path .
```

### Importing Services

#### Description

Create or update a service by importing a configuration file.

#### Parameters

| Parameter             | Required | Description                                                                                                                                                                                          | Example Value                          |
|-----------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `--access_key_id`     | No       | The Access Key ID needed for authentication. After logging in using the `login` command, there is no need to use it again. If specified, the `access_key_id` of that command will be used.           | `AKID1234567890`                       |
| `--access_key_secret` | No       | The Access Key Secret required for authentication. After logging in using the `login` command, there is no need to use it again. If specified, the `access_key_secret` of that command will be used. | `secret1234567890`                     |
| `--file_path`         | Yes      | Path to the file required for the import process.                                                                                                                                                    | `/path/to/your/config.yaml`            |
| `--region_id`         | No       | The ID of the region where the service is located.                                                                                                                                                   | `cn-hangzhou`                          |
| `--service_id`        | No       | Unique identifier for the service. If provided, the command will attempt to match this `service_id`.                                                                                                 | `service-12345`                        |
| `--service_name`      | No       | Name of the service. If `service_id` is not provided, this will be used to match the service name.                                                                                                   | `my-service`                           |
| `--version_name`      | No       | Name of the specific version of the service.                                                                                                                                                         | `v1.0`                                 |
| `--desc`              | No       | A brief description of the service.                                                                                                                                                                  | `Sample service`                       |
| `--update_artifact`   | No       | Specify whether the artifact needs to be updated. Accepts `True` or `False`.                                                                                                                         | `True`                                 |
| `--icon`              | No       | URL to the custom icon for the service, hosted on OSS (Object Storage Service).                                                                                                                      | `https://xxx/icon.png`                 |
| `--security_token`    | No       | Security Token needed for authentication; optional.                                                                                                                                                  | `security_token_value`                 |
| `--parameters`        | No       | Parameters in JSON format as a string. Optional, defaults to an empty JSON object `{}`.                                                                                                              | `{"key1": "value1", "key2": "value2"}` |
| `--parameter_path`    | No       | Path to a parameter file. If provided, this will override the `--parameters` option.                                                                                                                 | `/path/to/parameters.json`             |

Note:

- If --service_id is provided, the command will attempt to match it uniquely and the service name can be modified. If
  not found, it will raise a ServiceNotFound error.
- If --service_id is not provided but --service_name is, the command will match based on the service name.

#### Example

```bash
computenest-cli import \
    --region_id cn-hangzhou \
    --update_artifact True \
    --service_id service-12345 \
    --service_name my-service \
    --version_name v1.0 \
    --icon https://xxx/icon.png \
    --desc "Sample service" \
    --file_path /path/to/your/config.yaml \
    --parameter_path /path/to/parameters.json
```

Replace `$ACCESS_KEY_ID` and `$ACCESS_KEY_SECRET` with your AccessKey ID and AccessKey Secret respectively.
How to get the AccessKey pair: https://help.aliyun.com/zh/id-verification/cloudauth/obtain-an-accesskey-pair

### Exporting Services

#### Description

Export a service by specifying the service ID and the output directory.

#### Parameters

| Parameter               | Required | Description                                                                                                                                                                                          | Example Value          |
|-------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `--region_id`           | Yes      | The ID of the region where the service is located.                                                                                                                                                   | `cn-hangzhou`          |
| `--service_id`          | Yes      | Unique identifier for the service.                                                                                                                                                                   | `service-12345`        |
| `--output_dir`          | Yes      | Path to the output directory where the exported files will be saved.                                                                                                                                 | `/path/to/output`      |
| `--version_name`        | No       | Name of the specific version of the service.                                                                                                                                                         | `v1.0`                 |
| `--export_type`         | No       | Type of export. Options include `CONFIG_ONLY` and `FULL_SERVICE`.                                                                                                                                    | `config_only`          |
| `--export_project_name` | No       | Name of the project being exported.                                                                                                                                                                  | `MyExportedProject`    |
| `--export_file_name`    | No       | Name of the exported configuration file; defaults to `config.yaml`.                                                                                                                                  | `my_config.yaml`       |
| `--access_key_id`       | No       | The Access Key ID needed for authentication. After logging in using the `login` command, there is no need to use it again. If specified, the `access_key_id` of that command will be used.           | `AKID1234567890`       |
| `--access_key_secret`   | No       | The Access Key Secret required for authentication. After logging in using the `login` command, there is no need to use it again. If specified, the `access_key_secret` of that command will be used. | `secret1234567890`     |
| `--security_token`      | No       | Security Token needed for authentication; optional.                                                                                                                                                  | `security_token_value` |

#### Example：

```bash
computenest-cli export \
    --region_id cn-hangzhou \
    --service_id service-12345 \
    --version_name v1.0 \
    --export_type config_only \
    --output_dir /path/to/output \
    --export_project_name MyExportedProject \
    --export_file_name my_config.yaml
```

### Generating Files or Projects

#### Description

Generate a file or project by specifying the output directory.

#### Parameters

| Parameter           | Required | Description                                                                                      | Example Value              |
|---------------------|----------|--------------------------------------------------------------------------------------------------|----------------------------|
| `--output_path`     | Yes      | Path to the output directory where the generated files will be saved.                            | `/path/to/output`          |
| `--file_path`       | No       | Path to the specific file to be generated.                                                       | `/path/to/file.txt`        |
| `--type`            | No       | Type of generation. Options include `file` for a single file or `project` for the whole project. | `file`                     |
| `--parameters`      | No       | Parameters in JSON format as a string. Defaults to an empty JSON object `{}`.                    | `{"key1": "value1"}`       |
| `--parameter_path`  | No       | Path to a parameter file. If provided, this will override the `--parameters` option.             | `/path/to/parameters.json` |
| `--overwrite`, `-y` | No       | Confirm to overwrite the output file without a prompt if set.                                    | (no example, just a flag)  |

#### Example：

```bash
computenest-cli generate \
    --type file \
    --file_path /path/to/file.txt \
    --parameters '{"key1": "value1", "key2": "value2"}' \
    --output_path /path/to/output \
    --parameter_path /path/to/parameters.json \
    --overwrite
```

### Getting Help

To obtain help for a specific command, add `--help` after the command:

```shell
computenest-cli import --help
```

## How to Get the AccessKey Pair

Follow the instructions to create an AccessKey
pair: [Create an AccessKey pair](https://www.alibabacloud.com/help/en/ram/user-guide/create-an-accesskey-pair)
