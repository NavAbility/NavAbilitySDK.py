import os
import toml
import re

from gql import gql  # used to parse GraphQL queries
from graphql import DocumentNode, GraphQLSyntaxError  # used to handle GraphQL errors

# Define a class to represent a GraphQL fragment with a name and data
class FragmentData:
    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data

    def __str__(self) -> str:
        return f"{self.name}\n{self.data}"

# Define a class to represent a group of related GraphQL fragments with a common name
class Fragment:
    def __init__(self, name: str, data: list[FragmentData]):
        self.name = name
        self.data = data
    
    def __str__(self) -> str:
        return f"{self.name}:\n" + "\n".join([str(d) for d in self.data])

# Define a class to represent a GraphQL operation (query, mutation, or subscription) with a type and data
class Operation:
    def __init__(self, operation_type: str, data: str):
        self.operation_type = operation_type
        self.data = data
    
    def __str__(self) -> str:
        return f"{self.operation_type}:\n{self.data}"

# Define a function to get all files with a given extension from a given folder path
def get_files(folder_path: str, extension: str) -> list[str]:
    files = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            files += get_files(file_path, extension)
        elif file.endswith(extension):
            files.append(file_path)
    return files

# Define a function to extract the name of a fragment from its string representation
def get_fragment_name(fragment_string: str) -> str:
    pattern = r"fragment\s+(\S+)\s+on"
    match = re.search(pattern, fragment_string)
    if match:
        return match.group(1)
    else:
        return None

# Define a function to read all TOML files in a given folder path and return a dictionary of operation names mapped to their corresponding Operation objects
def get_operations(folder_path: str) -> dict[str, Operation]:
    files = get_files(folder_path, ".toml")

    fragments = []
    operations = {}

    for file in files:
        with open(file, "r") as f:
            data = toml.load(f)

            fragment_data_map = {}

            # Extract and store all fragments from the TOML file
            for fragment_data in data["fragment"]:
                name = fragment_data["name"]
                fragmentData_objects = [FragmentData(get_fragment_name(d["data"]), d["data"]) for d in fragment_data["data"]]
                fragment = Fragment(name = name, data = fragmentData_objects)
                fragments.append(fragment)
                for fd in fragmentData_objects:
                    if fd.name not in fragment_data_map:
                        fragment_data_map[fd.name] = []
                    fragment_data_map[fd.name].append(fd)

            # Extract and store all operations from the TOML file
            for operation_data in data["operation"]:
                name = operation_data["name"]
                operation = Operation(operation_type = "", data = operation_data["data"])
                for fd_name, fd_list in fragment_data_map.items():
                    if fd_name in operation_data["data"]:
                        for fd in fd_list:
                            operation.data += "\n" + "\n" + fd.data
                try:
                    # Parse the operation data using the gql function and set the operation type

                    # [Alucard] @GearsAD So we need to make a choice here, either we have Operation contain just a DocumentNode
                    # or we just use a string, but I'll leave that to you.
                    parsed_data = gql(operation.data)
                    operation.operation_type = parsed_data.definitions[0].operation
                    operations[name] = operation
                except GraphQLSyntaxError as e:
                    # If there is an error parsing the operation data, print an error message
                    print(f"Error: Error parsing operation data: {e} \n {operation.data}")

    return operations

# Define a list of symbols to export from this module
__all__ = ['get_operations']

# Load all GraphQL operations from the "sdkCommonGQL" folder and export them
GQL_OPERATIONS = get_operations(os.path.join(".", "sdkCommonGQL"))