This code provides a complete workflow to process and visualize XYZ data and X-ray absorption near-edge structure (XANES) spectra using t-SNE (t-distributed stochastic neighbor embedding) dimensionality reduction. Here's a brief breakdown:

Imports: It uses essential libraries such as NumPy, matplotlib, tqdm, sklearn, and scipy, among others, to handle numerical data, plotting, progress visualization, and distance computations.

WACSF Descriptor Calculation:

It initializes a WACSF descriptor object, which is used to describe atomic structures from XYZ files.
The descriptors for each XYZ file are computed and stored.
t-SNE on Descriptors:

After the WACSF descriptors are calculated, they are scaled using StandardScaler and reduced to two dimensions via t-SNE for visualization.
The calculated_spectra is similarly preprocessed and transformed using t-SNE.
Distance Computations:

The pairwise distance between points in the t-SNE space is calculated using the pdist function, which is optimized by splitting the distance calculation into batches.
The spectral and spatial thresholds are defined to filter points where their t-SNE distances are below a spatial threshold, but the spectra show significant differences (above the spectral threshold).
Filtering and Plotting:

Points are filtered based on the distance conditions, and the original and filtered t-SNE results are plotted side by side.
The plots are saved as PNG and PDF formats.


