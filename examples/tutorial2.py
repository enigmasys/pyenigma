import pyudcp

def createMetadataJSON():
    import json
    tmpjson = {
        'taxonomyVersion': json.loads(open("./codegen/taxonomyVersion.json").read()),
        'taxonomyTags': [json.loads(captureMetadataInfo())]
    }
    return tmpjson

# Populate the metadata with the values for the content types
def captureMetadataInfo():

    # Here we are importing from the generated pydantic model
    import codegen.DigitalPhenotypingContentModel as model


    mymodel = model.DigitalPhenotypingContentModel()
    mymodel.participant = model.Participant()
    mymodel.participant.participant_info = model.ParticipantInfo()
    mymodel.participant.participant_info.participant_id = "12334"
    mymodel.participant.participant_info.participant_status = model.Dropout(dropout={})
    generatedJSON = mymodel.model_dump_json(indent=2, by_alias=True, exclude_unset=False, exclude_none=True)
    return generatedJSON



# Here we are saving the populated metadata to a file in json format
def savePopulatedMetadata(file_path: "./test/metadataUpload.json"):
    import json
    metadataUpload = json.dumps(createMetadataJSON(), indent=2)
    # Save the generated file
    with open(file_path, "w") as outfile:
        outfile.write(metadataUpload)
        outfile.close()


# generate pydantic model from the json schema
# Step 1: Download the JSONSChema of the Content type
# Step 2: Generate the pydantic model from the JSON Schema

def generatePydanticModel():
    cli= pyudcp.UDCPPythonBinding()

    LEAP_CLI_JAR_PATH = "/Users/yogeshbarve/Projects/rest-tutorials/Pydantic-test/LEAP_CLI"
    cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)

    # Here we are generating the pydantic model for the Digital Phenotyping Content Type
    # We first have to set the repository id, directory, json schema file name, output file name and base class name
    # The base class name is the name of the class that will be generated in the pydantic model
    # The output file name is the name of the file that will be generated in the directory
    # The json schema file name is the name of the json schema file that will be downloaded from the repository
    # The directory is the directory where the json schema file will be downloaded and the pydantic model will be generated
    # The repository id is the id of the repository from which the json schema file will be downloaded

    cli.metadataModelCodeGen("e0de6a4a-5257-4f2c-b3ce-470e3299fc4a",
                             "./DPCodegen",
                             "DigitalPhenotypingSchema.json",
                             "DigitalPhenotypingContentModel.py",
                             "DigitalPhenotypingContentModel")


def uploaddata():
    pass


if __name__ == '__main__':


    print('UDCP CLI Tutorial 1')
    # Download the jsonschema

    # Step 1: Generate the metadata pydantic model for the content type
    generatePydanticModel()

    # Step 2: Populate the metadata with the values for the content type
    savePopulatedMetadata("./test/metadataUpload.json")

    # Step 3: Upload the metadata and the data to the repository
    uploaddata()


