import os

# Define the path to the .pl file and the xyz folder
pl_file_path = '/home/sneha/augmen_uncertainity/structures_have_no_hydrogen.pl'  # Update this path to your .pl file
xyz_folder_path = 'data2/sneha/sneha-large-set/xyz_itsplit/40000_removed_no_hydrogen_structure/xyz'     # Update this path to your xyz folde

# Read the .pl file to get the list of file names
with open(pl_file_path, 'r') as pl_file:
    file_names_to_remove = pl_file.read().splitlines()

# Loop through each file name and try to remove it from the xyz folder
for file_name in file_names_to_remove:
    file_path = os.path.join(xyz_folder_path, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f'Removed file: {file_path}')
        except Exception as e:
            print(f'Error removing file {file_path}: {e}')
    else:
        print(f'File not found: {file_path}')

