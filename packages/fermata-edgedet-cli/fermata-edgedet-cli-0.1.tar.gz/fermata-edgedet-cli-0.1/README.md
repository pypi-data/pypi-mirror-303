# Fermata CLI

Fermata CLI is a command-line tool that allows users to interact with the Fermata API. It includes functionality to authenticate via AWS Cognito, upload data to AWS S3, and call the Fermata API to analyze image data. 

## Features

- **Login**: Authenticate users via AWS Cognito and store the access token for future requests.
- **Analyze**: Send requests to the Fermata API to analyze images stored in an S3 bucket.

## Installation

### Prerequisites

- Python 3.8 or later
- `pip` package manager

### Install the CLI locally

```bash
pip install .

