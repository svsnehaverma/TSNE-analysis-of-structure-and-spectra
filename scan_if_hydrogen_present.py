import os

folder_path = "/home/sneha/augmen_uncertainity/bondlength_based/tp18/Final_test/intelligent_sampling_data/IT_held_out/xyz"

# List all files in the folder
files = os.listdir(folder_path)

# Iterate through each file
for file_name in files:
    if file_name.endswith(".xyz"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r") as file:
            lines = file.readlines()[2:]
            #molecules = [float(line.split()[0]) for line in lines]  if want to scan by atomic numbers 
            molecules = [line.split()[0] for line in lines]
            #print(molecules)

# Check if only 1 is not present in the first column values
            if 'H' not in molecules:
                #print(f"File {file_name} has a missing value in the first column.")
                os.remove(file_path)
                print(f"{file_name}")
