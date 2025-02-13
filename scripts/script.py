import os

def modify(full_path: str) -> str:
    """
    Modify the file name based on the full path
    """
    fields = full_path.strip().split("\\")
    path, name = fields[0:-1], fields[-1]
    newname = "-".join(name.strip().split("_")[1:]) if "_" in name else name
    return newname

def rename_files_in_subtree(root_dir: str):
    """
    Recursively traverse a directory subtree and rename files
    """
    success = True
    for dirpath, _, filenames in os.walk(root_dir):
        print(dirpath)
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            try:
                if len(full_path) > 260:
                    print(f"Fail: {full_path}")
                    success = False
            except FileNotFoundError:
                    print(f"Error: {full_path}")
    if success:
        print("OK")

if __name__ == "__main__":
    root_directory = "artist_dataset"  # Replace with your root directory
    rename_files_in_subtree(root_directory)
