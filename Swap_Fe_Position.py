import os
import shutil

# Source and destination folders
source_folder = '/home/sneha/augmen_uncertainity/augmen_datapoints/2_fe/'
destination_folder = '/home/sneha/augmen_uncertainity/augmen_datapoints/2_fe_22/'


# Swap the Fe row 2 will be on the place of row and and row 1 will be on the place of row 2 
# Iterate through all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".xyz"):
        source_filepath = os.path.join(source_folder, filename)

        # Read the content of the .xyz file
        with open(source_filepath, 'r') as file:
            lines = file.readlines()

        # Find indices of 'Fe' in the first column
        fe_indices = [i for i, line in enumerate(lines) if line.split()[0].lower() == 'fe']

        # Swap positions of the first and second occurrences of 'Fe' in the first column
        if len(fe_indices) >= 2:
            first_fe_index, second_fe_index = fe_indices[:2]
            lines[first_fe_index], lines[second_fe_index] = lines[second_fe_index], lines[first_fe_index]

            # Create a new filename by appending '_modified' to the original filename
            new_filename = filename.replace('.xyz', '_swap_0_1.xyz')
            destination_filepath = os.path.join(destination_folder, new_filename)

            # Write the modified content to a new file in the destination folder
            with open(destination_filepath, 'w') as new_file:
                new_file.writelines(lines)

            print(f"Modified and saved {filename} to {destination_filepath}")

print("Process completed.")
'''
import os
import shutil
 #for swap_0_1 and swap_0_2
def swap_fe_rows(file_lines, index1, index2):
    # Swap the rows at index1 and index2
    file_lines[index1], file_lines[index2] = file_lines[index2], file_lines[index1]


# Source and destination folders
source_folder = '/home/sneha/augmen_uncertainity/augmen_datapoints/24_fe/'
destination_folder = '/home/sneha/augmen_uncertainity/augmen_datapoints/24_fe_24/'


# Iterate through all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".xyz"):
        filepath = os.path.join(source_folder, filename)
        destination_filepath = os.path.join(destination_folder, filename)

        # Read the content of the .xyz file
        with open(filepath, 'r') as file:
            file_lines = file.readlines()

        # Find indices of 'Fe' rows
        fe_indices = [i for i, line in enumerate(file_lines) if 'Fe' in line]

        # Specify the range of swaps you want to perform (e.g., 0 to 23)
        swap_range = range(0,23)

        # Iterate through the specified range of swaps and swap the rows
        for j in swap_range:
            # Check if the index is valid before swapping
            if j < len(fe_indices):
                # Copy the original lines to avoid modifying the same list during iterations
                modified_lines = file_lines.copy()

                # Swap 'Fe' rows
                swap_fe_rows(modified_lines, fe_indices[0], fe_indices[j])

                # Save the modified content to a new file in the destination folder
                with open(destination_filepath.replace('.xyz', f'_swap_0_{j}.xyz'), 'w') as new_file:
                    new_file.writelines(modified_lines)

            
                 
print("Process completed.")


'''
