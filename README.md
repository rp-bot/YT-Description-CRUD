# YouTube Channel CRUD

Create-Read-Update-Delete stuff in your youtube channel. Makes things like updating old descriptions, titles and thumbnails very easy.

## Installation

-   ```sh
    pipenv install
    ```
-   make a copy of the `/.secrets.template` directory and rename it `/.secrets`
-   Make sure the directory grays out if you are using git in vscode
-   Rename the `.env.template` file to `.env`

## Setup

-   [(Option 1)](#read-only) **Read Only** features - [API Keys](https://developers.google.com/youtube/v3/getting-started)
-   [(Option 2)](#crud) **CRUD** features - [OAuth 2.0 Client ID](https://support.google.com/cloud/answer/6158849)

#### Read Only

1. [Google API Console](https://console.cloud.google.com/?hl=vi), Copy the **API Key** and paste it into the `.env` file.
2.

#### CRUD

1. [Google API Console](https://console.cloud.google.com/?hl=vi), Move the downloaded `client_secret.json` file into the `/.secrets` directory.
2. run the `authorize_token.py`, Once the authorization succeeds, A `token.json` is generated.
3.

## `Dev`

```sh
pyuic5 -x mainGUI.ui -o mainGUI.py
```

## Usage

-   [X] Get videos and any public facing data
-   [X] Get and update description of a video

## Chat GPT ?

-   [ ] to analyze what to keep and what not to keep in description
-   [ ] to improve a title by understanding the context based on previous title.
