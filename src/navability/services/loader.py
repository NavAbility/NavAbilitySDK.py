import os
import toml
import re

from gql import gql

class FragmentData:
    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data

    def __str__(self) -> str:
        return f"{self.name}\n{self.data}"

class Fragment:
    def __init__(self, name: str, data: list[FragmentData]):
        self.name = name
        self.data = data
    
    def __str__(self) -> str:
        return f"{self.name}:\n" + "\n".join([str(d) for d in self.data])

class Query:
    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data
    
    def __str__(self) -> str:
        return f"{self.name}:\n{self.data}"

def get_files(folder_path: str, extension: str) -> list[str]:
        files = []
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isdir(file_path):
                files += get_files(file_path, extension)
            elif file.endswith(extension):
                files.append(file_path)
        return files

def get_fragment_name(fragment_string: str) -> str:
    pattern = r"fragment\s+(\S+)\s+on"
    match = re.search(pattern, fragment_string)
    if match:
        return match.group(1)
    else:
        return None

def get_queries(folder_path: str) -> dict[str, Query]:
    files = get_files(folder_path, ".toml")

    fragments = []
    queries = {}

    for file in files:
        with open(file, "r") as f:
            data = toml.load(f)

            fragment_data_map = {}

            for fragment_data in data["fragment"]:
                name = fragment_data["name"]
                fragmentData_objects = [FragmentData(get_fragment_name(d["data"]), d["data"]) for d in fragment_data["data"]]
                fragment = Fragment(name = name, data = fragmentData_objects)
                fragments.append(fragment)
                for fd in fragmentData_objects:
                    if fd.name not in fragment_data_map:
                        fragment_data_map[fd.name] = []
                    fragment_data_map[fd.name].append(fd)


            for query_data in data["queries"]:
                name = query_data["name"]
                query = Query(name = name, data = query_data["data"])
                for fd_name, fd_list in fragment_data_map.items():
                    if fd_name in query_data["data"]:
                        for fd in fd_list:
                            query.data += "\n" + "\n" + fd.data
                # GQL interpret the query/mutation
                query.data = gql(query.data)
                # Add to dictionary
                queries[name] = query

    return queries

__all__ = ['get_queries']

# Load and export 
GQL_QUERIES = get_queries(os.path.join(".", "sdkCommonGQL"))