# Name-Entity-Recognition


## Workflows

 - constants
 - config_entity
 - artifact_entity
 - components
 - pipeline
 - app.py



## Live matarials docs

[link](https://docs.google.com/document/d/1UFiHnyKRqgx8Lodsvdzu58LbVjdWHNf-uab2WmhE0A4/edit?usp=sharing)


## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```


## AWS GCP Configuration

```bash
#Gcloud cli download link: https://cloud.google.com/sdk/docs/install#windows

Download the Google Cloud CLI installer (in windows and follow the steps)

gcloud init
```


## How to run?

```bash
conda create -n ner-env python=3.8 -y
```

```bash
conda activate ner-env
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```
## Test application
 - http://localhost:8080/docs

## GCP CICD Deployment with CircleCI:

 - artifact registry --> create a repository
 - change line 42,50,72,76,54 in circleci config
 - Open circleci --> create a project

## Set Environment variables in CircleCI
 - GCLOUD_SERVICE_KEY --> service account
 - GOOGLE_COMPUTE_ZONE = asia-south1
 - GOOGLE_PROJECT_ID


## Create a VM instances & setup scriptssd


