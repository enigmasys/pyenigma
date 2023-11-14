## Tutorial on using the Python Binding for the UDCP CLI

### Introduction
The UDCP CLI is a command line interface that allows users to interact with the UDCP platform.
The UDCP CLI is a Java application that can be run on any platform that supports Java.
The UDCP CLI can be used to upload and download data from the UDCP platform.

The UDCP CLI can be used in two ways:
- Using the command line interface
- Using the python binding

In this tutorials, we will walk through using the python binding for the UDCP CLI.


### Installation and Setup
First download the UDCP CLI from the GitHub Repository [here.](https://github.com/enigmasys/enigma/releases)
Look for the latest release and download the binary **leap_cli.jar** from the assets.

To use the python binding, you will need to install the following dependencies:
- Python 3.7 or higher

Next, install the python binding using pip:
```bash
pip install pyudcp
```

We will walk through using the python package through series of examples/tutorials.

### Tutorial 1: Setting up the UDCP CLI
In this tutorial, we will walk through setting up the UDCP CLI using the python binding.
Code samples used in this tutorial can be found in the 

First, we will need to import the package:
```python
import pyudcp
```

Next, we will need to create a UDCP CLI object and set the Executable Jar Root Directory:


```python
import pyudcp

LEAP_CLI_JAR_PATH = "/path/to/udcp_cli.jar"
cli = pyudcp.UDCPPythonBinding()
cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)

```

Next, we will try to invoke different commands using the UDCP CLI object.
Let's start by invoking the help command:

```python
import pyudcp
LEAP_CLI_JAR_PATH = "/path/to/udcp_cli.jar"
cli = pyudcp.UDCPPythonBinding()
cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)

cli.run_command("help")
```

To see the list of repositories available, we can run the following command:

```python
import pyudcp

LEAP_CLI_JAR_PATH = "/path/to/udcp_cli.jar"
cli = pyudcp.UDCPPythonBinding()
cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)
cli.run_repo_listing()
```

Download Test data from the UDCP CLI. First make sure to create the local download directory(in our case it is `output1`) to download the data to:

```python
import pyudcp
LEAP_CLI_JAR_PATH = "/path/to/udcp_cli.jar"
cli = pyudcp.UDCPPythonBinding()
cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)
cli.downloadData("./output1", "pdp://leappremonitiondev.azurewebsites.net/sandbox_dfv1/e0de6a4a-5257-4f2c-b3ce-470e3299fc4a/12/0")
```


Next we can test uploading test data using the below snippet:

```python
import pyudcp
LEAP_CLI_JAR_PATH = "/path/to/udcp_cli.jar"
cli = pyudcp.UDCPPythonBinding()
cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)

cli.uploadData("./upload/uploads",
                "ae0f62d0-854b-4696-8c7d-54e89e04308e",
                "./test/metadataUpload.json",
                "Test Description goes here, Uploaded on " + str(datetime.datetime.now()))
```
Here we are uploading the data from the `./upload/uploads/` directory. 
The data will be uploaded to the repository with the ID `ae0f62d0-854b-4696-8c7d-54e89e04308e`.
The metadata tag file is located at `./test/metadataUpload.json`.
The description of the upload is `Test Description goes here, Uploaded on " + str(datetime.datetime.now())`. 
One can set the description which is relevant and unique to this upload.


### Tutorial 2: Programmatic metadata tagging of the data










