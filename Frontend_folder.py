import os

base_dir = "src"

structure = {
    "api": [
        "axiosClient.js",
        "taskApi.js",
        "subtaskApi.js",
        "alarmApi.js",
        "dashboardApi.js"
    ],
    "components": {
        "Layout": [
            "Sidebar.js",
            "Topbar.js"
        ],
        "": [
            "CalendarView.js",
            "TaskCard.js",
            "SubtaskModal.js",
            "NotificationPopup.js"
        ]
    },
    "pages": [
        "HomePage.js",
        "DashboardPage.js"
    ],
    "utils": [
        "statusColors.js",
        "dateHelpers.js"
    ],
    "": [
        "App.js",
        "index.js"
    ]
}


def create_structure(base, struct):
    os.makedirs(base, exist_ok=True)

    for folder, content in struct.items():
        # If folder is empty string -> base directory files
        current_path = os.path.join(base, folder) if folder else base
        if folder:
            os.makedirs(current_path, exist_ok=True)

        if isinstance(content, list):
            # Create files directly inside folder
            for file_name in content:
                file_path = os.path.join(current_path, file_name)
                with open(file_path, "w") as f:
                    pass
                print(f"Created file: {file_path}")

        elif isinstance(content, dict):
            # Create subfolders and their files
            for subfolder, files in content.items():
                sub_path = os.path.join(current_path, subfolder) if subfolder else current_path
                if subfolder:
                    os.makedirs(sub_path, exist_ok=True)

                for file_name in files:
                    file_path = os.path.join(sub_path, file_name)
                    with open(file_path, "w") as f:
                        pass
                    print(f"Created file: {file_path}")


create_structure(base_dir, structure)
print("\nFrontend folder structure created successfully!")
