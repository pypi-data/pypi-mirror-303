import os
from fasthexgen.core.base import BaseTemplate
from fasthexgen.gen import hexproject

DIR_STRUCTURE = {
    "app" : {
        "core": [
            "__init__.py", 
            "commands.py", 
            {
                "entities": [
                    "__init__.py", 
                    "models.py", 
                    "schemas.py"
                ], 
                "interfaces":[
                    "__init__.py", 
                    "base.py", 
                    "services.py", 
                    "repositories.py"
                ]
            }
        ],
        "pkgs": [
            "__init__.py", 
            "logs.py", 
            "database.py", 
            "utils.py"
        ],
        "server": [
            "__init__.py", 
            "deps.py", 
            "middlewares.py", 
            {
                "routers": [
                        "__init__.py"
                    ]
            }
        ],
        "services": [
            "__init__.py"
        ],
        "repositoies":[
            "__init__.py"
        ],
        "main.py": [],
        "settings.py": [],
        "__init__.py": []
    },
    "tests": {
        "__init__.py":[]
    }
}

class HexTemplate(BaseTemplate):
    base_structure = DIR_STRUCTURE
    generator_map = {
        "services.py": getattr(hexproject, "generate_services_content"),
        "repositories.py": getattr(hexproject, "generate_repositories_content"),
        "base.py": getattr(hexproject, "generate_base_content"),
        "commands.py": getattr(hexproject, "generate_commands_content"),
        "main.py": getattr(hexproject, "generate_main_content"),
        "logs.py": getattr(hexproject, "generate_log_content"),
        "database.py": getattr(hexproject, "generate_dbconfig_content"),
        "models.py": getattr(hexproject, "generate_models_content"),
        "schemas.py": getattr(hexproject, "generate_schemas_content"),
        "settings.py": getattr(hexproject, "generate_setting_content"),
        "core": {
            "__init__.py": getattr(hexproject, "generate_init_core_content")
        },
        "routers": {
            "__init__.py": getattr(hexproject, "generate_init_routes_content")
        },
        "server": {
          "__init__.py": getattr(hexproject, "generate_init_server_content")
        },
        "pkgs": {
          "__init__.py": getattr(hexproject, "generate_init_pkgs_content")
        }
    }
    
    def __init__(self, project_name: str | None = None) -> None:
        self.base = os.getcwd()
        if project_name is not None:
            self.base_structure[project_name] = self.base_structure.pop("app")
            
    def make_directory(self, path: str) -> None:
        # Create folder
        os.makedirs(path, exist_ok=True)
        
    def get_folder_of_file(self, file_path: str):
        # Get the full path of the current file
        current_file_path = os.path.abspath(file_path)
        # Get the directory name (folder) of the current file
        full_path_folder_name = os.path.dirname(current_file_path)
        folder_name = os.path.basename(full_path_folder_name)
        return folder_name
    
    def make_file(self, file_path:str, filename: str) -> None:
        if filename == "__init__.py":
            # Get folder of __init__.py
            folder_name = self.get_folder_of_file(file_path)
            if folder_name in {"core", 'routers', 'server', 'pkgs'}:
                genfunc = self.generator_map.get(folder_name)
                init_genfunc = dict(genfunc).get("__init__.py")
                if init_genfunc is None:
                    return None
                content = init_genfunc()
                with open(file_path, 'w') as file:
                    file.write(content)
            else:
                genfunc = self.generator_map.get(folder_name)
                if genfunc is None:
                    content = ''
                    with open(file_path, 'w') as file:
                        file.write(content)
        else:
            genfunc = self.generator_map.get(filename)
            if genfunc is None:
                content = ''
                with open(file_path, 'w') as file:
                    file.write(content)
            else:
                content = genfunc()
                with open(file_path, 'w') as file:
                    file.write(content)
        return None

    def join_path(self, path: str, filename: str) -> str:
        # Join filename with path
        file_path = os.path.join(path, filename)
        return file_path
                
    def create_file_system(self, base_path: str, structure: dict | list):
        """
        Recursively creates directories and files based on the given structure.
        Args:
        - base_path (str): The path where the file system will be created.
        - structure (dict): A dictionary representing the folder and file structure.
        """
        for name, content in structure.items():
            path = self.join_path(base_path, name)
            # If it's a subfolder (dict)
            if isinstance(content, dict):
                self.make_directory(path)
                # Recursive call for subfolders
                self.create_file_system(path, content)
            # If it's a list of files and/or subfolders
            elif isinstance(content, list):
                if len(content) == 0:
                    # Get filename
                    filename = os.path.basename(path)
                    # If filename is not .py skip
                    if ".py" not in filename:
                        continue
                    self.make_file(path, filename)
                else:
                    self.make_directory(path)
                    for filename in content:
                        # If filename is a file
                        if isinstance(filename, str):
                            file_path = self.join_path(path, filename)
                            self.make_file(file_path, filename)
                        # If filename is a subfolder
                        elif isinstance(filename, dict):
                            # Recursive call for subfolder
                            self.create_file_system(path, filename)
        return "ok"
    
    def generate(self):
        result = self.create_file_system(self.base, self.base_structure)
        if isinstance(result, str):
            print("Generate template complete!!!")     

