# Tests
from imc_analysis.tl import impute_roi_area
import imc_analysis as imc
from imc_analysis.logging import *
from tqdm import tqdm
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    
    logger.info('Downloading sample file')
    
    import scanpy as sc
    adata = sc.read(
        'data/healthy_lung_adata.h5ad',
        backup_url='https://zenodo.org/record/6376767/files/healthy_lung_adata.h5ad?download=1')

    logger.debug(adata)



    for ct in ['cell type']:
        for ck in [[], ['Age']]:
            logger.debug(f"Condition: {ck}")
            # roi density
            density = imc.tl.celltype_density(adata, celltype = ct, condition_keys = ck)
            # patient density
            p_density = imc.tl.patient_density(adata, patient_key = 'Patient', celltype_key = ct, condition_keys = ck)
            # roi mean
            logger.debug(f"Measuring ROI Mean")
            roi_mean = imc.tl.compute_mean(adata, obs_key = 'roi', condition_keys = ck)
            # patient mean
            logger.debug(f"Measuring Patient Mean")
            p_mean = imc.tl.compute_mean(adata, obs_key = 'Patient', condition_keys = ck)
            
            for data in tqdm([density, p_density, roi_mean, p_mean]):
                imc.tl.grouped_mwu_test(data, condition_keys = ck)