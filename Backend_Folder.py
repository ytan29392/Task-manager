import os

# Base directory
base_dir = "backend"

# Folder structure definition
structure = {
    "app": {
        "": ["main.py", "config.py", "database.py"],
        "models": ["task.py", "subtask.py", "alarm.py"],
        "schemas": ["task_schema.py", "subtask_schema.py", "alarm_schema.py"],
        "crud": ["task_crud.py", "subtask_crud.py", "alarm_crud.py"],
        "routers": ["task_router.py", "subtask_router.py", "alarm_router.py", "dashboard_router.py"],
        "services": ["alarm_service.py"],
        "utils": ["helpers.py"],
    },
    "": ["requirements.txt"]
}

def create_structure(base, struct):
    for folder, content in struct.items():
        # Build folder path
        path = os.path.join(base, folder) if folder else base

        # Create folder if not empty string
        if folder:
            os.makedirs(path, exist_ok=True)

        # Create files in this folder (content that is a list)
        if isinstance(content, list):
            for file in content:
                file_path = os.path.join(path, file)
                with open(file_path, "w") as f:
                    pass  # Create empty file
                print(f"Created file: {file_path}")

        # If content is a dict → create subfolders
        elif isinstance(content, dict):
            for subfolder, files in content.items():
                sub_path = os.path.join(path, subfolder)
                if subfolder:  # skip empty string
                    os.makedirs(sub_path, exist_ok=True)

                # Create files inside subfolder
                for file in files:
                    file_path = os.path.join(sub_path, file)
                    with open(file_path, "w") as f:
                        pass
                    print(f"Created file: {file_path}")


# Run the function
create_structure(base_dir, structure)

print("\nFolder structure created successfully!")
