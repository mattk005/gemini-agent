import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write file content to (existing or new), relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written into the file",
            ),
        },
    ),
)


def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        with open(abs_file_path, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"write_files(working_directory, file_path, content) ran with the following error: {e}"
