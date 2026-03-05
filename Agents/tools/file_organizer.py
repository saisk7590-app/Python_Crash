import os
import shutil

def organize_folder(path):
    extensions = {
        "PDFs": [".pdf", ".docx", ".pptx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Apps": [".exe", ".msi"],
        "Archives": [".zip", ".rar", ".7z", ".tar"],
        "Code": [".py", ".ts", ".js", ".html", ".json", ".md"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".webm", ".wmv", ".flv", ".m4v", ".3gp", ".mts", ".m2ts", ".vob"],
        "Data": [".csv", ".xlsx", ".sql"]
    }

    if not os.path.exists(path):
        return f"Folder path '{path}' does not exist."

    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if os.path.isfile(full_path):
            file_ext = os.path.splitext(file)[1].lower()
            target_folder = "Others"
            for folder_name, exts in extensions.items():
                if file_ext in exts:
                    target_folder = folder_name
                    break

            dest_dir = os.path.join(path, target_folder)
            os.makedirs(dest_dir, exist_ok=True)

            # Handle file name conflict
            dest_path = os.path.join(dest_dir, file)
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(file)
                i = 1
                while os.path.exists(os.path.join(dest_dir, f"{base}_{i}{ext}")):
                    i += 1
                dest_path = os.path.join(dest_dir, f"{base}_{i}{ext}")

            shutil.move(full_path, dest_path)

    return "Folder organized successfully."