import ast
import subprocess
import sys
from typing import List, Tuple
import pkgutil


def get_imported_modules(file_path: str) -> List[str]:
    standard_libs = {
        "abc", "aifc", "argparse", "array", "ast", "asynchat", "asyncio", 
        "asyncore", "base64", "bdb", "binascii", "bisect", "builtins", 
        "bz2", "calendar", "cgi", "cgitb", "chunk", "code", "codecs", 
        "collections", "collections.abc", "concurrent", "configparser", 
        "contextlib", "copy", "copyreg", "csv", "ctypes", "datetime", 
        "dbm", "decimal", "difflib", "dis", "doctest", "email", 
        "encodings", "enum", "fnmatch", "fractions", "ftplib", 
        "functools", "gc", "getopt", "getpass", "gettext", "glob", 
        "gzip", "hashlib", "heapq", "http", "importlib", "inspect", 
        "io", "json", "logging", "lzma", "mailbox", "mailcap", 
        "marshal", "math", "mimetypes", "modulefinder", "multiprocessing", 
        "netrc", "nntplib", "numbers", "operator", "optparse", 
        "os", "pathlib", "pickle", "pprint", "profile", "pstats", 
        "queue", "random", "re", "readline", "reprlib", "shlex", 
        "shutil", "signal", "site", "smtplib", "socket", "sqlite3", 
        "sre_compile", "sre_constants", "sre_parse", "ssl", "stat", 
        "string", "stringprep", "subprocess", "sys", "tabnanny", 
        "tarfile", "telnetlib", "tempfile", "textwrap", "threading", 
        "time", "timeit", "tkinter", "turtle", "types", "unicodedata", 
        "unittest", "urllib", "uuid", "venv", "warnings", "weakref", 
        "xml", "xmlrpc"
    }
    
    exception_modules = {
        'sklearn': 'scikit-learn',
        'PIL': 'Pillow',
        'html5lib': 'html5lib',
    }
    
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read(), filename=file_path)

    imported_modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported_modules.add(node.module.split(".")[0])
                
    non_standard_imports = []
    for module in imported_modules:
        if module not in standard_libs:
            non_standard_imports.append(exception_modules.get(module, module))
            
    return non_standard_imports


def get_module_version(module_name: str) -> str:
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", module_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for line in result.stdout.splitlines():
            if line.startswith("Version:"):
                return line.split()[1]
    except Exception as e:
        print(f"Error getting version for module {module_name}: {e}")
    return ""


def read_existing_requirements(file_path: str) -> List[str]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def write_requirements_file(
    modules: List[Tuple[str, str]], output_file: str = "requirements.txt"
) -> None:
    
    # 버전이 기존화 바뀐 경우 반영 되지 않음
    # existing_requirements = read_existing_requirements(output_file)
    # existing_modules = {line.split("==")[0] for line in existing_requirements}

    with open(output_file, "a", encoding="utf-8") as file:
        for module_name, version in modules:
            # if module_name not in existing_modules:
                if version:
                    file.write(f"{module_name}=={version}\n")
                else:
                    file.write(f"{module_name}\n")


def generate_requirements(
    file_path: str, output_file: str = "requirements.txt"
) -> None:
    modules = get_imported_modules(file_path)
    module_versions = [(module, get_module_version(module)) for module in modules]
    write_requirements_file(module_versions, output_file)
    print(f"Requirements appended to {output_file}")


# Example usage
if __name__ == "__main__":
    python_file_path = "your_script.py"  # Replace with your Python file path
    generate_requirements(python_file_path)
