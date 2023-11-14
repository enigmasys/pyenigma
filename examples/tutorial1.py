import datetime

import pyudcp

# this tutorial will focus on interacting with the UDCP using the python package 'pyudcp'
# first make sure one has the latest version of the UDCP CLI
# One can donwload the latest from


LEAP_CLI_JAR_PATH = "/Users/yogeshbarve/Projects/rest-tutorials/Pydantic-test/LEAP_CLI"


def main():
    c = pyudcp.UDCPPythonBinding()
    c.setExecutableRootDir(LEAP_CLI_JAR_PATH)
    # c.run_help()
    # c.run_help()
    # c.run_repo_listing()
    # c.metadataModelCodeGen("586370a0-0a42-4c02-a051-174095d894af", "./", "EMATaxonomyJSON.json",
    #                                 "EMATaxonomy.py", "EMATaxonomy")

    # c.metadataModelCodeGen("586370a0-0a42-4c02-a051-174095d894af", "./codegen", "EMATaxonomyJSON.json",
    #                                 "EMATaxonomy.py", "EMATaxonomy")

    # c.metadataModelCodeGen("e0de6a4a-5257-4f2c-b3ce-470e3299fc4a",
    #                          "./codegen",
    #                          "DigitalPhenotypingSchema.json",
    #                          "DigitalPhenotypingContentModel.py",
    #                          "DigitalPhenotypingContentModel")
    #

    # c.downloadData("./output1", "pdp://leappremonitiondev.azurewebsites.net/sandbox_dfv1/e0de6a4a-5257-4f2c-b3ce-470e3299fc4a/12/0")
    c.uploadData("./upload/uploads", "ae0f62d0-854b-4696-8c7d-54e89e04308e", "./test/metadataUpload.json",
                 "Testing Python CLI Upload nov 13.a")


def run_help():
    cli = pyudcp.UDCPPythonBinding()
    cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)
    cli.run_help()


def run_repolisting():
    cli = pyudcp.UDCPPythonBinding()
    cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)
    cli.run_repo_listing()


def run_download():
    cli = pyudcp.UDCPPythonBinding()
    cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)

    DOWNLOAD_URI = "pdp://leappremonitiondev.azurewebsites.net/vutest/6e9da372-8cc7-4b11-bf85-23ed9d83a301/60/0"
    cli.downloadData("./output1", DOWNLOAD_URI)


def run_upload():
    cli = pyudcp.UDCPPythonBinding()
    cli.setExecutableRootDir(LEAP_CLI_JAR_PATH)
    # Upload data to the Sandbox Content type(Test Repo2)
    cli.uploadData("./upload/uploads",
                   "ae0f62d0-854b-4696-8c7d-54e89e04308e",
                   "./test/metadataUpload.json",
                   "Test Description goes here, Uploaded on " + str(datetime.datetime.now()))


if __name__ == '__main__':
    print('UDCP CLI Tutorial 1')
    # Run the Help Command of the UDCP CLI
    run_help()
    # Run the Repo Listing Command
    run_repolisting()
    # Download test data
    run_download()
    # Upload the test data
    run_upload()
