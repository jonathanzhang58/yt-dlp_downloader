import shutil
import os

# Define the source directory path and the target thumbnail directory path

def move_files_to_thumbnail_directory(source_directory, thumbnail_directory):
    # Ensure the thumbnail directory exists
    os.makedirs(thumbnail_directory, exist_ok=True)

    # Loop through the files in the source directory
    for file in os.listdir(source_directory):
        filename = os.fsdecode(file)
        # Check if the file has one of the specified extensions
        if filename.endswith(".webp") or filename.endswith(".jpg") or filename.endswith(".png"): 
            # Create the full file path
            source_filepath = os.path.join(source_directory, filename)
            # Create the target file path in the thumbnail directory
            target_filepath = os.path.join(thumbnail_directory, filename)
            # Move the file to the thumbnail directory
            shutil.move(source_filepath, target_filepath)
            print(f'Moved: {source_filepath} to {target_filepath}')
