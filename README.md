# tts

Interface with Azure's Text-to-Speech API

## Getting started

### Add .env file

```bash
cp .env.example .env
# Update environment variables
```

### Docker setup

```bash
# Run in VSCode command palette:
# > Dev Containers: Reopen in Container
```

### Local setup

#### Install dependencies for ubuntu

https://learn.microsoft.com/en-us/azure/ai-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=linux%2Cubuntu%2Cdotnetcli%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cpypi#platform-requirements

#### Issue with openssl resolved with

```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb
```

from https://stackoverflow.com/questions/76697185/how-to-fix-azure-cognitive-services-speech-sdk-quickstart-tutorial-gives-error-o
