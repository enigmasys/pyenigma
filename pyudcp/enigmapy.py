# Here we will create a python binding for the Enigma CLI tool.
# The Enigma CLI tool is a command line tool that can be used to communicate with the TaxonomyServer
# It is a java jar tool that can be run from the command line.


import os

from pyudcp import taxonomycodegen
from pyudcp.EnigmaCLI import EnigmaCLI


# Create a python binding class


# Following are the commands options for the leap_cli.jar tool
# Usage: <main class> [-hV] [-t=<token>] [COMMAND]
# Command for accessing the UDCP
#   -h, --help            Show this help message and exit.
#   -t, --token=<token>   Auth Token to pass when using Auth Passthrough Mode!
#   -V, --version         Print version information and exit.
# Commands:
#   process, proc, repository, repo
#   download, pull
#   upload, push
#   userinfo, user

# lets create a python wrapper around this.

class UDCPPythonBinding:

    def __init__(self):
        self.CLI = EnigmaCLI()

    def main(self):
        print("EnigmaCLI.main()")
        self.run_help()

    def setExecutableRootDir(self, cli_jar_root_path):
        self.CLI.setExecute(cli_jar_root_path)

    def run_help(self, command=None):
        self.CLI.run_help(command)

    def run_repo_listing(self):
        self.CLI.run_repo_listing()

    def downloadData(self, directory, uri: None):
        if directory is None:
            raise ValueError("directory cannot be None")
        if uri is None:
            raise ValueError("uri cannot be None")
        # Next download the data using the leap_cli.jar tool
        # !java -jar leap_cli.jar download -d ./output1 --uri pdp://leappremonitiondev.azurewebsites.net/cornellfmriprocessing/64784524-cedd-486c-a301-e1fcbbad4774/11/0
        # get the absolute path for the directory
        if directory is not None:
            directory = os.path.abspath(directory)
        else:
            directory = os.getcwd()
        self.CLI.downloadData(directory, uri)

    def uploadData(self, directory, repository_id, metadata_file_path: None, description: None):
        # do initial checks
        if directory is None:
            raise ValueError("directory cannot be None")

        if repository_id is None:
            raise ValueError("repository_id cannot be None")

        if metadata_file_path is None:
            raise ValueError("metadata_file_path cannot be None")

        if description is None:
            raise ValueError("description cannot be None")

        # get the absolute path for the directory
        if directory is not None:
            directory = os.path.abspath(directory)
        else:
            directory = os.getcwd()

        # get the absolute path for the metadata_file_path
        if metadata_file_path is not None:
            metadata_file_path = os.path.abspath(metadata_file_path)
        else:
            metadata_file_path = os.getcwd()

        self.CLI.uploadData(directory, repository_id, metadata_file_path, description)

    def downloadJSONSchema(self, repository_id, directory=None, filename=None):

        # Run the enigma cli tool
        # cd to the directory where the enigma cli tool is located
        if directory is None:
            directory = os.getcwd()
            # get the current working directory
        if filename is None:
            filename = repository_id + ".json"

        # get the absolute path for the directory
        directory = os.path.abspath(directory)

        print("directory: " + directory)
        return self.CLI.downloadJSONSchema(repository_id, directory, filename)

    def metadataModelCodeGen(self, repository_id, directory=None, json_schema_filename=None, output_file_name=None,
                             base_classname=None):

        # check if the input parameters are valid
        if repository_id is None:
            raise ValueError("repository_id cannot be None")

        if output_file_name is None:
            raise ValueError("output_file_name cannot be None")

        if json_schema_filename is None:
            raise ValueError("json_schema_filename cannot be None")

        if directory is None:
            raise ValueError("directory cannot be None")

        # if output_file_name is a path then raise error
        if os.path.dirname(output_file_name) != "":
            raise ValueError("output_file_name cannot be a path")

        # Get the abosolute path of the directory path if set
        if directory is not None:
            directory = os.path.abspath(directory)
        else:
            directory = os.getcwd()

        self.__generatePydanticModel(base_classname, directory, json_schema_filename, output_file_name, repository_id)

    def __generatePydanticModel(self, base_classname, directory, json_schema_filename, output_file_name, repository_id):
        # Download the JSON Schema
        _jsonschemafileName = json_schema_filename if json_schema_filename is not None else repository_id + ".json"
        _outputFilePathName = output_file_name if output_file_name is not None else repository_id + ".py"
        _directory = directory if directory is not None else os.getcwd()
        _filename = self.downloadJSONSchema(repository_id, _directory, _jsonschemafileName)
        inputFilePathName = os.path.join(_directory, _filename)
        _outputFilePathName = os.path.join(_directory, _outputFilePathName)
        # Print all the variables to be used in generatePydanticModel function
        print("inputFilePathName: " + inputFilePathName)
        print("_outputFilePathName: " + _outputFilePathName)
        print("baseClassName: " + base_classname)
        taxonomycodegen.generatePydanticModel(inputFilePathName,
                                              _outputFilePathName,
                                              base_classname)


if __name__ == "__main__":
    print("EnigmaCLI.__main__")

    LEAP_CLI_JAR_PATH = "/Users/yogeshbarve/Projects/rest-tutorials/Pydantic-test/LEAP_CLI"
    enigma_cli = UDCPPythonBinding()
    enigma_cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)
    # enigma_cli.run_help()
    # enigma_cli.downloadJSONSchema("586370a0-0a42-4c02-a051-174095d894af")

    enigma_cli.metadataModelCodeGen("586370a0-0a42-4c02-a051-174095d894af", "./", "EMATaxonomyJSON.json",
                                    "EMATaxonomy.py", "EMATaxonomy")

    # enigma_cli.downloadData("./output1", "pdp://leappremonitiondev.azurewebsites.net/cornellfmriprocessing/64784524-cedd-486c-a301-e1fcbbad4774/11/0")

    # enigma_cli.downloadData("./output1", "pdp://leappremonitiondev.azurewebsites.net/sandbox_dfv1/e0de6a4a-5257-4f2c-b3ce-470e3299fc4a/12/0")

    # enigma_cli.uploadData("./output1", "e0de6a4a-5257-4f2c-b3ce-470e3299fc4a", "./input/metadata_tags.json", "MRI Data Upload from VU")
