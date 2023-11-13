import json
from pathlib import Path
from datamodel_code_generator import (
    InputFileType,
    generate,
    DataModelType,
    PythonVersion,
)

def generatePydanticModel(inputFilePathName, outputFilePathName, baseClassName: str = None):
    print("generatePydanticModel:", inputFilePathName, outputFilePathName, baseClassName)
    schema_path = Path(inputFilePathName)
    with open(schema_path) as f:
        schema = json.load(f)
    print(schema)
    # generate code

    schema = update_schema(schema, baseClassName)
    output = Path(outputFilePathName)
    generate(
        str(schema),
        input_file_type=InputFileType.JsonSchema,
        output=output,
        # set up the output model types
        output_model_type=DataModelType.PydanticV2BaseModel,
        snake_case_field=True,
        field_constraints=True,
        use_annotated=True,
        # target_python_version=PythonVersion.PY_38,
        use_title_as_name=True,
        disable_appending_item_suffix=True,
        use_standard_collections=True,
        allow_population_by_field_name=True,
        # class_name=MAIN_CLASS_NAME,
        disable_timestamp=True,
        validation=True,
    )


def update_schema(schema: dict, baseClass: str = None):
    print("update_schema")
    if schema["type"] == "object":
        if baseClass is not None:
            schema["title"] = baseClass
            print("baseClass: " + baseClass)
    return schema


if __name__ == "__main__":
    INPUT_FILE_PATH_NAME = "../testing/EnumJSONSchema.json"
    OUTPUT_FILE_PATH_NAME = "../testing/EMAContentModel.py"
    BASE_CLASS_NAME = "EMAContentModel"

    generatePydanticModel(INPUT_FILE_PATH_NAME, OUTPUT_FILE_PATH_NAME, BASE_CLASS_NAME)
