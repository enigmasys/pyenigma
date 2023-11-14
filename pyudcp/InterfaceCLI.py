# Make an abstract class for the CLI interface
# Path: src/pyudcp/InterfaceCLI.py
# Compare this snippet from EnigmaPythonBinding/pyenigma.py:
#
from abc import ABCMeta, abstractmethod



class InterfaceCLI(metaclass=ABCMeta):
    def __init__(self):
        self.cli_exe_root_path = None

    @abstractmethod
    def setExecute(self, executable_root_path):
        self.cli_exe_root_path = executable_root_path

    @abstractmethod
    def run_help(self, command=None):
        pass

    @abstractmethod
    def downloadData(self, directory, uri: None):
        pass

    @abstractmethod
    def uploadData(self, directory, repository_id, metadata_file_path: None, description: None):
        pass

    @abstractmethod
    def downloadJSONSchema(self, repository_id, directory=None, filename=None):
        pass
