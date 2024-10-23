import subprocess
import pexpect
import os
import re


def handle_metadata(cell_code: str):
    # Define regular expression pattern for metadata
    metadata_pattern = r"^//\| (\w+): (.*)$"

    # Split string into metadata and code
    metadata_lines, code = re.split(r"(?m)^(?!\/\/\|)", cell_code, maxsplit=1)

    # Extract metadata dictionary from metadata lines
    metadata_dict = {}
    for line in metadata_lines.split("\n"):
        match = re.match(metadata_pattern, line)
        if match:
            metadata_dict[match.group(1)] = match.group(2)
    return metadata_dict, code


def has_main_function(c_code):
    """
    Check if there is a main function in the given C code.
    """
    # Check if there is at least one line starting with #include
    if not re.search(r"^\s*#include", c_code, re.MULTILINE):
        return False

    # Search for main function definition
    main_func_pattern = r"^\s*(int|void)\s+main\s*\(([^)]*)\)\s*{(?s:.*?)}"
    main_func_match = re.search(main_func_pattern, c_code, re.MULTILINE)

    return bool(main_func_match)


def compile_run_c(c_code: str, metadata_dict: dict):
    if not has_main_function(c_code):
        c_code = f"""#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {{
{c_code}
return 0;
}}"""

    try:
        # Step 1: Compile the C code from the string
        compile_command = "gcc -std=c99 -Wall -x c -o jupygcc_code - -lm".split()
        compile_process = subprocess.run(
            compile_command,
            input=c_code,
            encoding="utf-8",
            check=True,
            capture_output=True,
        )

        if compile_process.stdout:
            print("Compilation output:", compile_process.stdout)
        if compile_process.stderr:
            print("Compilation errors:", compile_process.stderr)

        # Step 2: Run the compiled executable using pexpect
        stdin = metadata_dict.get("stdin", "")
        child = pexpect.spawn("./jupygcc_code")

        # Split inputs on lines or spaces
        stdins = stdin.split("\\n")
        if len(stdins) == 1:
            stdins = stdin.split(" ")

        for stdin in stdins:
            child.sendline(stdin)

        # Wait for the program to finish and capture the output
        child.expect(pexpect.EOF)
        output = child.before.decode("utf-8")

        print(output)

        # Clean up: Remove the compiled executable
        os.remove("jupygcc_code")

    except subprocess.CalledProcessError as e:
        print(f"Execution Error: {e}\n{e.stderr}")
    except pexpect.exceptions.ExceptionPexpect as e:
        print(f"Pexpect Error: {e}")
