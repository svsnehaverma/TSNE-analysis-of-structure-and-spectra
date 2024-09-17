import os
import matplotlib.pyplot as plt

# Path to the directory containing excluded_points_30.pl
file_list_path = '/home/sneha/augmen_uncertainity/excluded_points_30.pl'

# Path to the directory containing spectra data files
data_dir = '/data2/sneha/sneha-large-set/xanes-short/'

# Read the spectra names from excluded_points_30.pl
with open(file_list_path, 'r') as f:
    spectra_names = [line.strip().split(': ')[1] + '.txt' for line in f]
    print(spectra_names)

# Plot each spectrum
for spectra_name in spectra_names:
    file_path = os.path.join(data_dir, spectra_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()[2:]
            energy = [float(line.split()[0]) for line in lines]
            intensity = [float(line.split()[1]) for line in lines]
        plt.plot(energy, intensity, label=spectra_name)
    else:
        print(f"File not found: {file_path}")

# Customize plot
plt.xlabel('Energy')
plt.ylabel('Intensity')
plt.title('Spectra')
plt.legend()
plt.show()

