
from pyudcp.InterfaceCLI import InterfaceCLI
import os


class EnigmaCLI(InterfaceCLI):
    def __init__(self):
        super(InterfaceCLI, self).__init__()
        self.cli_exe_root_path = None

    def setExecute(self, cli_exe_root_path):
        self.cli_exe_root_path = cli_exe_root_path

    def run_help(self, command=None):
        print("EnigmaCLI.run_enigma_cli()")
        # Run the enigma cli tool
        # cd to the directory where the enigma cli tool is located
        os.chdir(self.cli_exe_root_path)
        if command is not None:
            cmd_str = "java -jar leap_cli.jar " + str(command) + " --help"
        else:
            cmd_str = "java -jar leap_cli.jar --help"
        print(cmd_str)
        os.system(cmd_str)

    def run_repo_listing(self):
        print("EnigmaCLI.run_repo_listing()")
        # Run the enigma cli tool
        # cd to the directory where the enigma cli tool is located
        # exit out of the current directory
        owd = os.getcwd()
        try:
            # first change dir to build_dir path
            os.chdir(self.cli_exe_root_path)
            cmd_str = "java -jar leap_cli.jar repo -l"
            os.system(cmd_str)
        finally:
            # change dir back to original working directory (owd)
            os.chdir(owd)

    def downloadData(self, directory, uri: None):
        owd = os.getcwd()
        try:
            os.chdir(self.cli_exe_root_path)
            cmd_str = "java -jar leap_cli.jar download -d " + directory + " --uri " + uri
            print(cmd_str)
            os.system(cmd_str)
        finally:
            # change dir back to original working directory (owd)
            os.chdir(owd)

    def uploadData(self, directory, repository_id, metadata_file_path: None, description: None):

        # get the current directory
        owd = os.getcwd()
        try:
            os.chdir(self.cli_exe_root_path)
            # java -jar leap_cli.jar upload --process ae0f62d0-854b-4696-8c7d-54e89e04308e -d ./output/dat/126/0/ -f ./input/metadata_tags.json -m "MRI Data Upload from VU"

            cmd_str = ("java -jar leap_cli.jar upload -d " + directory + " -repo " + str(repository_id) + " -f " +
                       str(metadata_file_path) + " -m \"" + str(description) + "\"")
            print(cmd_str)
            os.system(cmd_str)
        finally:
            # change dir back to original working directory (owd)
            os.chdir(owd)

    def downloadJSONSchema(self, repository_id, directory=None, filename=None):
        print("EnigmaCLI.generateJSONSchema()")

        # get the current directory
        owd = os.getcwd()
        try:
            os.chdir(self.cli_exe_root_path)
            cmd_str = "java -jar leap_cli.jar repo -j --repo " + repository_id + " --dir " + directory + " --file " + filename
            print(cmd_str)
            os.system(cmd_str)
        finally:
            # change dir back to original working directory (owd)
            os.chdir(owd)
        return filename
