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

In this tutorial, we will walk through how to programmatically tag the data using the python binding.

Step 1: We will be leveraging Pydantic Python classes to represent the content type objects in Python.
To build the Pydantic Python Class, we will first need to have the JSONSchema for the content type.
The JSONSchema for the content type is available through the UDCP CLI. We can invoke the `metadataModelCodeGen` method
to generate the Pydantic Python Class for the content type.

Let's first define the configuration for the metadataModelCodeGen method:

```python
# This defines the path where the generated pydantic model will be saved
CODE_GENERATED_OUTPUT_DIR = "./DPCodeGen"
# This defines the name of the content type
CONTENT_TYPE_NAME = "DigitalPhenotyping"

# This defines the repository id from which the json schema will be downloaded
REPOSITORY_ID = "e0de6a4a-5257-4f2c-b3ce-470e3299fc4a"

# This defines the path where the LEAP CLI jar is located
LEAP_CLI_JAR_PATH = "LEAP_CLI_DIR"

# This defines the path where the populated metadata will be saved
POPULATED_METADATA_FILE_PATH = "./input/metadataUpload.json"
```
Next we define the method to generate the pydantic model for the content type:

```python
import pyudcp
def generatePydanticModel():
    cli = pyudcp.UDCPPythonBinding()
    cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)
    # Here we are generating the pydantic model for the CONTENT_TYPE_NAME
    # We first have to set the repository id (REPOSITORY_ID), output directory (CODE_GENERATED_OUTPUT_DIR), 
    # json schema file name (CONTENT_TYPE_NAME + "Schema.json"), output Python file name(CONTENT_TYPE_NAME + "ContentModel.py") 
    # and base class name(CONTENT_TYPE_NAME + "ContentModel")
    # The base class name is the name of the class that will be generated in the pydantic model
    # The output file name is the name of the file that will be generated in the directory
    # The json schema file name is the name of the json schema file that will be downloaded from the repository
    # The directory is the directory where the json schema file will be downloaded and the pydantic model will be generated
    # The repository id is the id of the repository from which the json schema file will be downloaded

    cli.metadataModelCodeGen(REPOSITORY_ID,
                             CODE_GENERATED_OUTPUT_DIR,
                             CONTENT_TYPE_NAME + "Schema.json",
                             CONTENT_TYPE_NAME + "ContentModel.py",
                             CONTENT_TYPE_NAME + "ContentModel")
```


This will generate the DigitalPhenotypingContentModel.py file in the `./DPCodegen` directory.
The DigitalPhenotypingContentModel.py file will contain the Pydantic Python Class for the content type.
DigitalPhenotypingContentModel.py file can be imported and used in the python code to represent the content type.
`e0de6a4a-5257-4f2c-b3ce-470e3299fc4a` is the repository ID for the Digital Phenotyping content type.
`DigitalPhenotypingSchema.json` is the JSONSchema for the Digital Phenotyping content type.
`DigitalPhenotypingContentModel` is the name of the Pydantic Python Class that will be generated inside the DigitalPhenotypingContentModel.py file.


Step 2: Populate the metadata with the values for the content type.
We can use the Pydantic Python Class to populate the metadata for the content type.
The Pydantic Python Class will have the same fields as the JSONSchema for the content type.
We can populate the metadata for the content type using the Pydantic Python Class.

```python

def captureMetadataInfo():

    # Here we are importing from the generated pydantic model
    import DPCodegen.DigitalPhenotypingContentModel as model

    mymodel = model.DigitalPhenotypingContentModel()
    mymodel.participant = model.Participant()
    mymodel.participant.participant_info = model.ParticipantInfo()
    mymodel.participant.participant_info.participant_id = "12334"
    mymodel.participant.participant_info.participant_status = model.Dropout(dropout={})
    generatedJSON = mymodel.model_dump_json(indent=2, by_alias=True, exclude_unset=False, exclude_none=True)
    return generatedJSON

```
Here we populate the metadata for the content type using the Pydantic Python Class.
We can then use the generatedJSON object to tag the data.

Before we tag the data, we will need to create a metadata tag file.
The metadata tag file is a JSON file that contains the metadata for the content type.


```python

def savePopulatedMetadata(file_path: "./test/metadataUpload.json"):
    import json
    metadataUpload = json.dumps(createMetadataJSON(), indent=2)
    # Save the generated file
    with open(file_path, "w") as outfile:
        outfile.write(metadataUpload)
        outfile.close()


# This function appends the Taxonomy Version to the populated metadata
def createMetadataJSON():
    import json
    tmpjson = {
        'taxonomyVersion': json.loads(open(CODE_GENERATED_OUTPUT_DIR + "/taxonomyVersion.json").read()),
        'taxonomyTags': [json.loads(captureMetadataInfo())]
    }
    return tmpjson
```

Here we are creating the metadata tag file using the `createMetadataJSON` method and saving it to the `./test/metadataUpload.json` file.
The `taxonomyVersion.json` file contains the taxonomy version for the content type that is generated when we invoke the `metadataModelCodeGen` method.


Step 3: Upload the data to the UDCP platform using the metadata tag file.

```python
def uploaddata():
    import datetime
    # Upload the test data to the sandbox repository
    # Upload data to the Sandbox Content type(Test Repo2)
    cli = pyudcp.UDCPPythonBinding()
    cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)
    cli.uploadData("./upload/uploads",
                   "ae0f62d0-854b-4696-8c7d-54e89e04308e",
                   POPULATED_METADATA_FILE_PATH,
                   "Tutorial-2, Uploaded on " + str(datetime.datetime.now()))
```













