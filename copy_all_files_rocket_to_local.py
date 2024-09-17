import os
import shutil

# Define paths
local_path = "/home/sneha/augmen_uncertainity/intelligent_sampling/IT_data/440000/fdmnes_in"
rocket_path = "nsv53@rocket.hpc:/nobackup/nsv53/IT_data/440000/fdmnes_in"

# Get list of filenames from local machine
local_files = os.listdir(local_path)

# Get list of filenames from rocket remote
rocket_files = os.listdir(rocket_path)

# Find files that are in rocket but not in local
missing_files = [file for file in rocket_files if file not in local_files]

# Copy missing files from rocket to local
for file in missing_files:
    rocket_file_path = os.path.join(rocket_path, file)
    local_file_path = os.path.join(local_path, file)
    shutil.copy(rocket_file_path, local_file_path)
    print(f"Copied {file} from rocket to local.")

print("All different files copied successfully.")
