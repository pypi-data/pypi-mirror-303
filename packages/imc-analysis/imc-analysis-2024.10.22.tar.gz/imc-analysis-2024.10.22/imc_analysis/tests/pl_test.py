# Tests
import imc_analysis as imc
from imc_analysis.logging import *

from tqdm import tqdm
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    
    logger.info('Loading sample file')
    
    import scanpy as sc
    adata = sc.read(
        'data/infected_lung_adata.h5ad',
        backup_url = 'https://zenodo.org/records/6376767/files/infected_lung_adata.h5ad?download=1')

    import numpy as np
    adata.obsm['spatial'] = np.array(adata.obs[['Y', 'X']])
    logger.debug(adata)
    # series of tests to ensure build works

    imc.pl.celltype_heatmap(adata, cluster_ids = ['cluster_1.0', 'cluster_label', 'metacluster_label'], out_dir='figures/celltype/heatmap/')
    imc.pl.umap_var(adata, outdir = 'figures/umap/')

    for ct in ['cluster_1.0', 'cluster_label', 'metacluster_label']:
        conditions = ['disease', 'phenotypes']
        
        # roi density
        density = imc.tl.celltype_density(adata, celltype = ct, condition_keys = conditions, x_coord = 'X', y_coord = 'Y')

        # roi mean
        roi_mean = imc.tl.compute_mean(adata, obs_key = 'roi', condition_keys = conditions)
        
        for data in tqdm([density, roi_mean, ]):
            imc.tl.grouped_mwu_test(data, condition_keys = conditions)
            
            logger.info('Plotting MWU plots')            
            for pval_form in ['star', 'sci_not']:
                imc.pl.plot_mwu(data, save_dir = f'figures/{ct}/', palette = None, pval_form = pval_form)
            
            