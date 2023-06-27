# CONCHA: Contact-based characterization of conformational ensembles of highly flexible proteins


Welcome to CONCHA, an ensemble characterization tool. The method implemented in this jupyter notebook computes residue-specific distances between a pair of IDP conformational ensembles, together with an overall distance for the entire ensemble. The comparison is simultaneously made at two scales:
* **Global scale**: distances between the distributions of the relative positions of all residue pairs in both ensembles. For each pair of residues, we compute the (2-Wasserstein) distance between a pair of probability distributions supported on the three-dimensional euclidean space (point clouds).
* **Local scale**: distances between the (phi, psi) angle distributions of each ensemble, for each residue along the sequence. For each residue, we compute the (2-Wasserstein) distance between a pair of probability distributions supported on the two dimensional flat torus.

The result of the comparison analysis is represented through a matrix, denoted $`\mathcal{W}`$. We will denote as $`\mathcal{W}_{ij}`$ the entries of $`\mathcal{W}`$, where $`i,j\in\lbrace 1,\ldots,L\rbrace`$ are respectively the row and column indexes. The matrix will be lower triangular (i.e. $`\mathcal{W}_{ij}=0`$ if $`j>i`$). The following figure illustrates the main elements of the matrix representation, which are described below.

<br />
<br />
<br />
<div align="center">
<img src="toymatrix.png"  width="460" height="400">
</div>
<br />
<br />
<br />

- [1] The matrix is headed by a title describing the comparison, introduced by the user. 
- [2,3] Below the title, the overall local and global discrepancies are depicted. By default, they are computed by aggregating and weighting the corrected distances. These features can be modified by the user.
- [4,5] The matrix entries are represented using two unrelated color scales, for local and global differences. Both scales correspond to the proportion of intra-ensemble distances that is added to the intra-ensemble distances to reach the encountered inter-ensemble distances. In the legend, $`\tilde{W}`$ corresponds to the difference between the inter-ensemble and the intra-ensemble distances, and $`W_{\mathrm{intra}}`$ indicates the intra-ensemble differences. In other words, this scale represents **how different are the inter-ensemble distances with respect to the intra-ensemble ones** (e.g. the "net" distance that has been added to uncertainty represents the 150% of such uncertainty). This was set as the easiest interpretable scale, using uncertainty as a reference to which compare the inter-ensemble differences. This score can be computed when several independent replicas of each ensemble are available. Otherwise, distances can not be corrected by uncertainty and the scale will correspond to the (non-corrected) inter-ensemble local and global distances.
- [6] The entries $`\mathcal{W}_{ij}`$ for $`i< j`$ correspond to the previously defined scores computed for the $`i,j`$-th global structural descriptors, i.e. the score comparing the relative position distribution of the $`i`$-th and $`j`$-th residues in the two ensembles. If no independent replicas are available, the entry corresponds to the $`i,j`$-th global inter-ensemble distance.
- [7] The entries $`\mathcal{W}_{ii}`$ correspond to the previously defined scores computed for the $`i`$-th local structural descriptors, i.e. the score comparing the $`(\phi,\psi)`$ distribution of the $`i`$-th residue in the two ensembles. If no independent replicas are available, the entry corresponds to the $`i`$-th local inter-ensemble distance.
- [8] The entries $`\mathcal{W}_{ii}`$ may be marked with a star if their associated $p$-value is less than the significance level $`\alpha=0.05`$.
- [9] The axes labels correspond to the residue position, counting from the N-terminal, relative to the sequence segment that is being compared (and not to the absolute position in the entire sequence).

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
