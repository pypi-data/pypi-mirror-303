# Quickstart Guide

## Google Cloud

You will need:

A Google Cloud Account: [https://cloud.google.com/](https://cloud.google.com/) with a project.

### Installation and Initialization

[Install](https://cloud.google.com/sdk/docs/install) the Google Cloud CLI, then initialize it by running the following command:
```shell
gcloud init
```

## Environment Variables

You will need to set the following environment variables (for example in a .env file):

```
MY_DEFAULT_PROJECT='my-autogs'
MY_PROCESSOR_LOCATION='us'
MY_ORC_PROCESSOR='my-orc-processor'
```


- `python` 3.10 or greater: [https://www.python.org/downloads/](https://www.python.org/downloads/)

*Your-contribution* is a part of the `autora` package:

```shell
pip install -U autogs-core
```


Check your installation by running:
```shell
python -c "from autogs.your_contribution import something"
```
