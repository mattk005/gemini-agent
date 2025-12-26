import os
import argparse
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if abs_file_path.split(".")[-1] != "py":
            return f'Error: "{file_path}" is not a Python file'

        # parser = argparse.ArgumentParser(description="Run python file")
        # parser.add_argument("extra_args", type=str, help="additional arguments")
        # extra_args = parser.parse_args()

        command = ["python", abs_file_path]
        if args:
            command += [args]
        # command += args.extra_args
        # print(command)
        foo = subprocess.run(
            command, capture_output=True, cwd=working_directory, text=True, timeout=30
        )
        # print(foo)
        my_soon_to_be_output_list = []
        if foo.returncode != 0:
            my_soon_to_be_output_list.append(
                f"Process exited with code {foo.returncode}"
            )
        if not foo.stderr and not foo.stdout:
            my_soon_to_be_output_list.append("No oututput was produced")
        if foo.stdout:
            my_soon_to_be_output_list.append(f"STDOUT: {foo.stdout}")
        if foo.stderr:
            my_soon_to_be_output_list.append(f"STDERR: {foo.stderr}")

        return ", ".join(my_soon_to_be_output_list)

    except Exception as e:
        return f"Error: executing Python file: {e}"


def main():
    run_python_file(
        "/home/matt/workspace/github.com/mattk005/gemini-agent",
        "main.py",
        "Tell my girlfriend she's beautiful, please.",
    )


if __name__ == "__main__":
    print(main())
