
from pyudcp.InterfaceCLI import InterfaceCLI
import os
import logging
# lets add logging to this module
logger = logging.getLogger(__name__)

class EnigmaCLI(InterfaceCLI):

    def __init__(self):

        super(InterfaceCLI, self).__init__()
        self.cli_exe_root_path = None



    def setExecute(self, cli_exe_root_path):
        #make sure to only grab the absolute directory path and not the file name
        cli_exe_root_path = os.path.abspath(cli_exe_root_path)
        self.cli_exe_root_path = cli_exe_root_path
        logger.debug("EnigmaCLI.setExecute() cli_exe_root_path: " + str(cli_exe_root_path))

    def run_help(self, command=None):
      #  print("EnigmaCLI.run_enigma_cli()")
        # Run the enigma cli tool
        # cd to the directory where the enigma cli tool is located
        # exit out of the current directory
        # Store the current working directory in a variable
        current_dir = os.getcwd()
        os.chdir(self.cli_exe_root_path)
        if command is not None:
            cmd_str = "java -jar leap_cli.jar " + str(command) + " --help"
        else:
            cmd_str = "java -jar leap_cli.jar --help"

        logger.debug("EnigmaCLI.run_enigma_cli() current_dir: " + str(os.getcwd()))
        logger.debug("EnigmaCLI.run_enigma_cli() cmd_str: " + str(cmd_str))

        print(cmd_str)
        os.system(cmd_str)
        # change dir back to original working directory (owd)
        os.chdir(current_dir)

    def run_repo_listing(self):
        #print("EnigmaCLI.run_repo_listing()")
        # Run the enigma cli tool
        # cd to the directory where the enigma cli tool is located
        # exit out of the current directory
        owd = os.getcwd()
        try:
            # first change dir to build_dir path
            os.chdir(self.cli_exe_root_path)
            cmd_str = "java -jar leap_cli.jar repo -l"

            logger.debug("EnigmaCLI.run_repo_listing() current_dir: " + os.getcwd())
            logger.debug("EnigmaCLI.run_repo_listing() cmd_str: " + cmd_str)
            # Print the output of the command

            t = os.system(cmd_str)
            logger.debug("EnigmaCLI.run_repo_listing() : " + str(t))

        finally:
            # change dir back to original working directory (owd)
            os.chdir(owd)

    def downloadData(self, directory, uri: None):
        owd = os.getcwd()
        try:
            os.chdir(self.cli_exe_root_path)
            cmd_str = "java -jar leap_cli.jar download -d " + directory + " --uri " + uri

            logger.debug("EnigmaCLI.downloadData() current_dir: " + os.getcwd())
            logger.debug("EnigmaCLI.downloadData() cmd_str: " + cmd_str)
            t = os.system(cmd_str)
            logger.debug("EnigmaCLI.downloadData() : " + str(t))

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

            logger.debug("EnigmaCLI.uploadData() current_dir: " + os.getcwd())
            logger.debug("EnigmaCLI.uploadData() cmd_str: " + cmd_str)
            t = os.system(cmd_str)
            logger.debug("EnigmaCLI.uploadData() : " + str(t))
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

            logger.debug("EnigmaCLI.downloadJSONSchema() current_dir: " + os.getcwd())
            logger.debug("EnigmaCLI.downloadJSONSchema() cmd_str: " + cmd_str)
            t = os.system(cmd_str)
            logger.debug("EnigmaCLI.downloadJSONSchema() : " + str(t))
        finally:
            # change dir back to original working directory (owd)
            os.chdir(owd)
        return filename
