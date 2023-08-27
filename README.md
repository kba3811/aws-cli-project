# AWS Secrets Manager CLI
Command line tool to easily set environment variables from secrets in AWS Secrets Manager.

## Usage
```bash
eval $(aws_secrets_manager_cli --name=secret_name --key=secret_key --env=environment_variable)

$environment_variable # my_secret_value
```

## Installation
```bash
pip install git+https://github.com/kba3811/aws-secrets-manager-cli#egg=aws_secrets_manager_cli
```
