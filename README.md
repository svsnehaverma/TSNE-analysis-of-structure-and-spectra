This code is a comprehensive machine learning pipeline designed to analyze and visualize structural and spectral data using t-SNE (t-distributed stochastic neighbor embedding). It performs feature extraction on XYZ molecular structures and compares them with corresponding spectral data, ultimately filtering and visualizing the results based on spatial and spectral distances.

The process begins by importing the necessary libraries, including modules for numerical computations (`numpy`), visualization (`matplotlib`), and handling files (`glob`, `pathlib`, `os`). Two notable libraries are used: `tblite` for calculating molecular descriptors and `xanesnet` for handling X-ray absorption near-edge structure (XANES) data. The code leverages the `WACSF` (weighted atom-centered symmetry functions) descriptor to extract features from atomic coordinates (XYZ format) to represent molecular structures in a numerical form suitable for machine learning.

The first part of the code loads molecular structures from XYZ files and transforms them into descriptors using the `WACSF` object. The corresponding spectral data (XANES spectra) are read from text files. A list of molecular IDs common to both the XYZ and spectral files is created, ensuring the data is aligned.

For dimensionality reduction, t-SNE is applied to both the molecular descriptors and spectral data to project them into lower-dimensional spaces (2D for visualization). The t-SNE projection is further standardized using `StandardScaler` to normalize the features.

The second part of the code computes pairwise distances between data points in the t-SNE space using the `pdist` function from `scipy.spatial.distance`. It compares these spatial distances with differences in spectral properties. Points that are spatially close but spectrally distinct are flagged, and their indices are excluded from further analysis.

Finally, the code visualizes the results. Two scatter plots are generated using `matplotlib`: one showing the original t-SNE projection of all data points and another showing the filtered data points where spatial and spectral anomalies have been removed. The scatter plots use a color map (`terrain`) to encode spectral information on the z-axis. Both the original and filtered t-SNE plots are saved as PNG and PDF files, and the visualizations are displayed using `plt.show()`.

In summary, this code builds a pipeline for visualizing molecular structure descriptors and spectral properties, filtering out anomalies based on pre-defined thresholds for spatial and spectral distances, and producing detailed scatter plots to illustrate the relationships in the dataset.


For more details please refer https://github.com/NewcastleRSE/xray-spectroscopy-ml


