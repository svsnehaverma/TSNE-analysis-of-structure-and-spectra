import glob
import numpy as np
from tblite.interface import Calculator
import matplotlib.pyplot as plt
import matplotlib as mpl
from pathlib import Path
import sys
import tqdm as tqdm
import os
from xanesnet.utils import load_xyz
from ase import Atoms
#from xanesnet.descriptor.xtb import XTB
from xanesnet.descriptor.wacsf import WACSF
#from xanesnet.descriptor.soap import SOAP
from xanesnet.utils import list_filestems
from sklearn.manifold import TSNE
from numpy import dot
from numpy.linalg import norm
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist, squareform

# Initialize the WACSF descriptor object
wacsf_ob = WACSF(n_g2 = 32, n_g4 = 64, r_min = 0.5, r_max = 6.5, z =[1,2,4,8,16,32,64,128])

# Get sorted list of XYZ and Spectra
x_path = "/data2/sneha/sneha-large-set/xyz_itsplit/20000/xyz"
y_path = "/data2/sneha/sneha-large-set/xanes-short"
x_files = glob.glob(os.path.join(x_path, "*.xyz"))
x_file_stems = {os.path.splitext(os.path.basename(file))[0] for file in x_files}
y_files = glob.glob(os.path.join(y_path, "*.txt"))
y_file_stems = {os.path.splitext(os.path.basename(file))[0] for file in y_files}
ids = sorted(x_file_stems.intersection(y_file_stems))

descs_list = []
for i, id_ in enumerate(tqdm.tqdm(sorted(ids))):
    with open(f'{x_path}/{id_}.xyz', 'r') as f:
         atoms = load_xyz(f)
         tmp = wacsf_ob.transform(atoms)
    descs_list.append(tmp)
descs = np.vstack(descs_list)
s1 = StandardScaler()
x1 = s1.fit_transform(descs)
tsne = TSNE(n_components=2,perplexity=50,learning_rate=60,n_iter=1000,init='pca')
points = tsne.fit_transform(x1)

calculated_spectra_list = []
for i, id_ in enumerate(tqdm.tqdm(sorted(ids))):
    with open(f'{y_path}/{id_}.txt', 'r') as f:
        spectrum = np.genfromtxt(f, usecols = [1], skip_header = 2)
    calculated_spectra_list.append(spectrum)
calculated_spectra = np.vstack(calculated_spectra_list)

t1 = StandardScaler()
x2 = t1.fit_transform(calculated_spectra)
tsne = TSNE(n_components=2,perplexity=50,learning_rate=60,n_iter=1000,init='pca')
zaxis = tsne.fit_transform(calculated_spectra)


t1 = StandardScaler()
x2 = t1.fit_transform(calculated_spectra)
tsne = TSNE(n_components=1,perplexity=50,learning_rate=60,n_iter=1000,init='pca')
zaxis = tsne.fit_transform(x2)

#for i, id_ in enumerate(tqdm.tqdm(sorted(ids))):
#    print(id_,zaxis[i],points[i,0],points[i,1])


# Calculate pairwise distances between points
distances = squareform(pdist(points))

# Define thresholds for spatial and spectral distances
spatial_threshold = 2.0  # Maximum allowable distance between two points in the tSNE plot to consider them spatially close
spectral_threshold = 30.0  # Maximum allowable difference in the zaxis values to consider them spectrally different.

exclude_indices = set()

for i in range(len(points)):
    for j in range(i+1, len(points)):
        if distances[i, j] < spatial_threshold and abs(zaxis[i, 0] - zaxis[j, 0]) > spectral_threshold:
            exclude_indices.add(i)
            exclude_indices.add(j)

# Filter out the points to exclude
filtered_points = np.array([points[i] for i in range(len(points)) if i not in exclude_indices])
filtered_zaxis = np.array([zaxis[i, 0] for i in range(len(zaxis)) if i not in exclude_indices])

# Print excluded structures and spectra names
excluded_ids = [ids[i] for i in exclude_indices]
for eid in excluded_ids:
    print(f"Excluded ID: {eid}")

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot the original data
sc1 = axes[0].scatter(
    points[:,0],
    points[:,1],
    c = zaxis,
    cmap = 'terrain',
    s = 4
)
axes[0].set_xlabel('tSNE Component 1 / Arb. Units', fontsize=12)
axes[0].set_ylabel('tSNE Component 2 / Arb. Units', fontsize=12)
axes[0].set_title('Original tSNE', fontsize=12, fontweight='bold')
fig.colorbar(sc1, ax=axes[0])

# Plot the filtered data
sc2 = axes[1].scatter(
    filtered_points[:,0],
    filtered_points[:,1],
    c = filtered_zaxis,
    cmap = 'terrain',
    s = 4
)
axes[1].set_xlabel('tSNE Component 1 / Arb. Units', fontsize=12)
axes[1].set_ylabel('tSNE Component 2 / Arb. Units', fontsize=12)
axes[1].set_title('Filtered tSNE', fontsize=12, fontweight='bold')
fig.colorbar(sc2, ax=axes[1])

# Save the combined plot
plt.savefig('combined_tSNE.png', format='png')
plt.savefig('combined_tSNE.pdf', format='pdf')
plt.show()
