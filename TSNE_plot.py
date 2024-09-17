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
from xanesnet.descriptor.xtb import XTB
from xanesnet.descriptor.wacsf import WACSF
from xanesnet.descriptor.pdos import PDOS
from xanesnet.descriptor.soap import SOAP
from xanesnet.utils import list_filestems
from sklearn.manifold import TSNE
from numpy import dot
from numpy.linalg import norm
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Get Descriptor from XYZs
#wacsf_ob = XTB(method = "GFN2-xTB", accuracy = 1.0, num_points = 80, e_min = -20.0, e_max = 20.0, sigma = 0.8, max_iter = 250, use_wacsf = False, use_quad = False, use_spin = False, use_charge = False, use_occupied = False, n_g2 = 32, n_g4 = 64, z =[1,2,4,8,16,32,64,128], r_min = 0.5, r_max = 6.5)
wacsf_ob = WACSF(n_g2 = 32, n_g4 = 64, r_min = 0.5, r_max = 6.5, z=[2,4,8,16])
#wacsf_ob = SOAP(species = [26, 1, 6, 8, 7, 9, 15, 16, 17, 35, 53, 14, 5, 34, 33], n_max = 8, l_max = 6, r_cut = 6.0)
#wacsf_ob = PDOS(basis = "3-21g", init_guess = "minao", orb_type = "p", num_points = 80, e_min = -20.0, e_max = 20.0, sigma = 0.8, use_wacsf = True, use_spin = False, use_charge = False, n_g2 = 22, n_g4 = 10, r_min = 0.5, r_max = 6.5)

# Get sorted list of XYZ and Spectra
#x_path = "/home/tom/PDOS/SK-edge/10000-set/xyz"
x_path = "/home/sneha/augmen_uncertainity/bondlength_based/tp18/Final_Test_hl_9/intelligent_sampling_data/xyz"
#y_path = "/home/tom/PDOS/SK-edge/10000-set/xanes"
y_path = "/home/sneha/augmen_uncertainity/bondlength_based/tp18/Final_Test_hl_9/intelligent_sampling_data/xanes"
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

#for i, id_ in enumerate(tqdm.tqdm(sorted(ids))):
#    with open(f'{id_}.dsc', 'x') as f:
#        for j in range(len(descs[i])):
#           f.write(f'{descs[i][j]} {x1[i][j]}\n')

calculated_spectra_list = []
for i, id_ in enumerate(tqdm.tqdm(sorted(ids))):
    with open(f'{y_path}/{id_}.txt', 'r') as f:
        spectrum = np.genfromtxt(f, usecols = [1], skip_header = 2)
    calculated_spectra_list.append(spectrum)
calculated_spectra = np.vstack(calculated_spectra_list)

t1 = StandardScaler()
x2 = t1.fit_transform(calculated_spectra)
tsne = TSNE(n_components=1,perplexity=50,learning_rate=60,n_iter=1000,init='pca')
zaxis = tsne.fit_transform(x2)

#for i, id_ in enumerate(tqdm.tqdm(sorted(ids))):
#    print(id_,zaxis[i],points[i,0],points[i,1])

# Plot  
plt.scatter(
    points[:,0],
    points[:,1],
    c = zaxis,
    cmap = 'terrain',
    s = 4
)
plt.xlabel('tSNE Component 1 / Arb. Units',fontsize=12)
plt.ylabel('tSNE Component 2 / Arb. Units',fontsize=12)
plt.colorbar()
plt.savefig('fe.png', format = 'png')
plt.savefig('fe.pdf', format = 'pdf')
plt.show()

