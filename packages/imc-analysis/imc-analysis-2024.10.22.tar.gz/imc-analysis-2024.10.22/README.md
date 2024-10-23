# imc-analysis

Toolkit to perform IMC analysis. The package is under development and although some of the content is tested, there might be bugs here and there. Proceed at your own risk.
The package is free to edit and reuse.

## Installation
Preferred installation for a bit more stable version that has been tested:
```
pip install imc-analysis
```
or alternatively as editable package.
```
git clone https://github.com/ElementoLab/imc-analysis.git
cd imc-analysis
pip install -e .
```

## Tutorial

Current toolkit includes following command:

1. `imc-analysis init`: generates IMC project repository
2. `imc-analysis qc`: generates QC metadata and plots
3. `imc-analysis visualize`: visualizes IMC images in grayscale stacks or RGB images

Some functionalities of the package can be used directly in python as following:

```python
# Use Scanpy to get a h5ad file with provided data
import scanpy as sc
import imc_analysis as imc

adata = sc.read(
    'data/healthy_lung_adata.h5ad',
    backup_url='https://zenodo.org/record/6376767/files/healthy_lung_adata.h5ad?download=1')

# adata = sc.read(
#   'data/infected_lung_adata.h5ad',
#   backup_url = 'https://zenodo.org/records/6376767/files/infected_lung_adata.h5ad?download=1')

celltype = 'cell type'
condition = ['Age']

imc.pl.celltype_heatmap(adata, cluster_ids = ['cell type'], out_dir='figures/celltype/heatmap/')

# roi density
density = imc.tl.celltype_density(adata, celltype = celltype, condition_keys = condition)

# patient density
p_density = imc.tl.patient_density(adata, patient_key = 'Patient', celltype_key = celltype, condition_keys = condition)

# roi mean
roi_mean = imc.tl.compute_mean(adata, obs_key = 'roi', condition_keys = condition)

# patient mean
p_mean = imc.tl.compute_mean(adata, obs_key = 'Patient', condition_keys = condition)

imc.tl.grouped_mwu_test(density, condition_keys = condition)
imc.pl.plot_mwu(density, save_dir=f'figures/celltype/', palette=None, pval_form='star')
imc.pl.plot_mwu(density, kind = 'box', save_dir=f'figures/celltype/', palette=None, pval_form='star')
imc.pl.plot_mwu(density, kind = 'bar', save_dir=f'figures/celltype/', palette=None, pval_form='star')

```

Detailed description of each commands

## init
Creates project repository.

Arguments:
  - `project`: name of the project. Defaults to `imc_project/`
  - `yaml`: name of YAML file for the project. Defaults to `metadata/project.yml` and is placed under `project folder`
  - `panel`: name of panels, provided as a list. All projects initialize as single panel, unless specified otherwise.


Created IMC file structure is as below.
```
+-- data 
| +-- sample.mcd    # RAW mcd files, will need to be added by the user
+-- processed
| +-- sample/
|   +-- tiffs/
|     +-- sample_roi_full.tiff    # full stack tiff files
|     +-- sample_roi_full.csv     # csv files containing channel info 
|     +-- sample_roi_full_mask.tiff   # cell segmentation mask
+-- results
| +-- cell.h5ad     # AnnData objects containing cell info 
+-- metadata
| +-- project.yml   # YAML file containing project info
+-- figures       # folder for figures
+-- images        # folder for IMC image visualizations
```

Refer to [imc](https://github.com/ElementoLab/imc) project repository to learn more about how to process raw mcd/txt files.

## qc
Performs quality control check on provided data.

Arguments:
  - `yaml`: YAML file for the project. Defaults to `metadata/project.yml`.
  - `panel`: name of panel. Defaults to `PANEL`.
  - `outdir`: directory to store output QC figures. Resulting figures are stored in `outdir/panel/`


## visualize
Visualizes images as stacks.

Arguments:
  - `yaml`: YAML file for the project. Defaults to `metadata/project.yml`.
  - `mode`: `stack` option draws full stacks of images. `rgb` draws RGB stacks of images using `plot_config` keyword of yaml file.
  - `panel`: name of panel. Defaults to `PANEL`.
  - `outdir`: directory to store output QC figures. Resulting figures are stored in `outdir/panel/`


Currently there are two modes to the visualize command: `stack` and `rgb`. `stack` option draws full stacks of images. `rgb` draws RGB stacks of images using `plot_config` keyword of yaml file.

