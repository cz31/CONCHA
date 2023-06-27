# CONCHA: Contact-based characterization of conformational ensembles of highly flexible proteins

Welcome to CONCHA, an ensemble characterization tool. CONCHA represents an ensemble as a weighted family of contact maps. Contact is redefined by a continuous function taking values in $[0,1]$ that incorporates the relative orientation of the interacting residues as well as the sequence information. Then, the featured data is embedded into a 10-dimensional [UMAP](https://umap-learn.readthedocs.io/en/latest/index.html) space and clustered using the [HDBSCAN](https://hdbscan.readthedocs.io/en/latest/#) algorithm. Finally, the average values of the contact function across each cluster conformation are represented as cluster-specific contact maps. The maps are assigned with a weight given by the cluster occupancy.

#### Running CONCHA

To run CONCHA to characterize an ensemble, the user can directly execute the [contact_clustering](contact_clustering.ipynb) notebook, which contains the detailed pipeline and allows a step-by-step implementation of the tool.

## Installing CONCHA

CONCHA and its required dependencies can be automatically installed if Python >=3.8 is available. We recommend to perform the installation inside a [Python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/). It can be created as follows
```
python3 -m venv pythonEnv
source pythonEnv/bin/activate
```
Then, CONCHA is installed with
```
pip install git+https://gitlab.laas.fr/moma/CONCHA.git
```
Once the installation is completed, the command
```
concha-notebooks
```
opens the ready-to-use jupyter notebook.

The installation procedure works correctly with recent versions of Linux and MacOS operating systems. If you encounter any trouble to install CONCHA, please file an [issue](https://gitlab.laas.fr/moma/WASCO/-/issues) or [contact us](mailto:javier.gonzalez-delgado@math.univ-toulouse.fr).
