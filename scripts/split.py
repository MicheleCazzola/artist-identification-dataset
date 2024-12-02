import os
import random

def collect_file_paths(root_dir: str):
    """
    Collects all file paths in a subtree, relative to the root directory.
    
    Parameters:
        root_dir (str): The root directory of the subtree.
    
    Returns:
        list[str]: List of file paths relative to the root directory.
    """
    relative_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(full_path, root_dir)
            relative_paths.append(full_path)
    return relative_paths

def divide_data(file_paths: list[str], train_ratio: float = 0.8):
    """
    Divides file paths into training and testing datasets.
    
    Parameters:
        file_paths (list[str]): List of file paths to divide.
        train_ratio (float): Proportion of files to allocate to training.
    
    Returns:
        tuple[list[str], list[str]]: Training and testing datasets.
    """
    random.shuffle(file_paths)  # Shuffle the paths randomly
    train_size = int(len(file_paths) * train_ratio)
    train_files = file_paths[:train_size]
    test_files = file_paths[train_size:]
    return train_files, test_files

def write_to_file(file_list: list[str], output_file: str):
    """
    Writes a list of file paths to a text file.
    
    Parameters:
        file_list (list[str]): List of file paths to write.
        output_file (str): Output file path.
    """
    with open(output_file, "w") as f:
        for file_path in file_list:
            f.write(file_path + "\n")

# Example usage
if __name__ == "__main__":
    root_directory = "artist_dataset"  # Replace with your subtree root path
    train_file = "train.txt"
    test_file = "test.txt"
    
    # Step 1: Collect file paths
    all_files = collect_file_paths(root_directory)
    
    # Step 2: Divide into train and test datasets
    train_files, test_files = divide_data(all_files, train_ratio=0.8)
    
    # Step 3: Write to output files
    write_to_file(train_files, train_file)
    write_to_file(test_files, test_file)

    print(f"Training data written to {train_file}")
    print(f"Testing data written to {test_file}")
