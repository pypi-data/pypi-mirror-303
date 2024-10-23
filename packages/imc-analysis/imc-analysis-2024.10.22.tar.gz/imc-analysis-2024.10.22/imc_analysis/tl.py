from tqdm import tqdm

import typing as tp
from imc_analysis.types import Path
from imc_analysis.logging import *

import pandas as pd
import numpy as np
import scanpy as sc
import anndata

import scipy

# import warnings
# warnings.simplefilter("ignore", UserWarning)

def grouped_mwu_test(
    adata: anndata.AnnData,
    condition_keys: list = None,
    multicomp: str = 'BH',
    verbose: bool = False
) -> anndata.AnnData:
    """ Apply MWU test for (cell type density / marker mean expression) matrix either on ROI or patient level

    Args:
        adata (anndata.AnnData): cell type density or marker mean expression matrix on either ROI or patient level.
        condition_keys (list, optional): list of conditions to apply test. Runs all comparisons on obs layer if none provided.
        multicomp (str, optional): Multiple hypothesis correction method. Defaults to BH for Benjamini-Hochberg.

    Returns:
        anndata.AnnData: _description_
    """
    logger.info("Applying Double sided Mann-Whitney U test.")
    import pingouin as pg

    for key in condition_keys:
        assert key in adata.obs.columns
            
    if condition_keys == None:
        condition_keys = adata.obs.columns
        
        # if not categorical, make into categorical variable
        if not isinstance(adata.obs[key].dtype, pd.CategoricalDtype):
            logger.debug(f"Replacing {key} as a categorical variable")
            adata.obs[key] = pd.Categorical(adata.obs[key])
            
            if len(adata.obs[key].cat.categories) > 10:
                logger.warning(f'there is more than 10 categories in key: {key}')
    
    density = adata.to_df()
    adata.uns['mwu'] = dict()
    
    pval_df = pd.DataFrame(columns = ['celltype', 'condition', 'pair', 'U-val', 'p-val'])
    # 'adj. p-val'
    
    for ct in density.columns:
        for cond in condition_keys:

            from itertools import combinations
            comb = list(combinations(adata.obs[cond].cat.categories, 2))

            pd.options.mode.chained_assignment = None  # default='warn'
            #pvals = pd.concat([pg.mwu(density[adata.obs[cond] == p1][ct].tolist(), density[adata.obs[cond] == p2][ct].tolist()) for p1, p2 in comb])
            pval_list = []
            for p1, p2 in comb:
                x = density[adata.obs[cond] == p1][ct].tolist()
                y = density[adata.obs[cond] == p2][ct].tolist()
                
                if len(x) and len(y):
                    pval_list.append(pg.mwu(x, y))
            pvals = pd.concat(pval_list)
            
            mini_pval_df = pvals[['U-val','p-val']]
            mini_pval_df['celltype'] = ct
            mini_pval_df['condition'] = cond
            mini_pval_df['pair'] = comb
            pval_df = pd.concat([pval_df, mini_pval_df])
            
            # BH_pvals = pg.multicomp(pvals['p-val'].tolist(), method = multicomp)
            # BH_pvals = pd.DataFrame({'Significant': BH_pvals[0], 'adj. p-val': BH_pvals[1]}, index = comb)

            # if verbose:
            #     logger.info(BH_pvals)
    def pval_to_star(pval):
        if pval < 0.0001:
            return ' **** '
        elif pval < 0.001:
            return ' *** '
        elif pval < 0.01:
            return ' ** '
        elif pval < 0.05:
            return ' * '
        else:
            return ' ns '
    def pval_to_sci_not(pval):
        return "{:.2E}".format(pval)

    BH_pvals = pg.multicomp(pval_df['p-val'].tolist(), method = multicomp)  
    pval_df['adj. p-val'] = BH_pvals[1]
    pval_df['significance'] = pval_df['adj. p-val'].apply(pval_to_star)
    pval_df['adj. p-val sci'] = pval_df['adj. p-val'].apply(pval_to_sci_not)
    pval_df.reset_index(drop = True, inplace = True)
    adata.uns['mwu'] = pval_df

def celltype_density(
    data: anndata.AnnData,
    celltype: str = 'celltype',
    condition_keys: list = [],
    roi_key: str = 'roi',
    **kwargs: tp.Any,
) -> anndata.AnnData:
    """ Compute cell density for a given celltype in IMC data. Return density matrix as AnnData with specified conditions from the original AnnData.
    
    Args:
        data (anndata.AnnData): Cell Matrix in AnnData with celltyping and roi information in obs layer. Each observation should be a cell. 
        celltype (str, optional): Celltype key to be used. Defaults to 'celltype'.
        condition_keys (list, optional): Condition keys from AnnData obs to store in the return AnnData. Defaults to [].
        roi_key (str, optional): ROI key to be used. Defaults to 'roi'.
        
        y_coord (str, optional): Y coordinate of cells. Defaults to 'Y_centroid'.
        x_coord (str, optional): X coordinate of cells. Defaults to 'X_centroid'.
        
    Returns:
        anndata.AnnData: Cell density matrix as AnnData. Each sample is an ROI, and each column is a cell type.
    """
    logger.info("Calculating cell type density.")
    
    # check for necessary inputs
    assert celltype in data.obs, f"Error: '{celltype}' missing from `data.obs` layer."
    assert roi_key in data.obs, f"Error: '{roi_key}' missing from `data.obs` layer."
    for k in condition_keys:
        assert k in data.obs, f"Error: '{k}' missing from `data.obs` layer."
        
    # Impute ROI area
    if 'ROI_area' not in data.obs:
        impute_roi_area(
            data,
            roi_key = roi_key,
            overwrite = True,
            **kwargs,
        )
    
    keys = [roi_key, 'ROI_area'] + condition_keys
    
    # retrieve cell count matrix
    cell_counts = data.obs.groupby([roi_key,celltype]).count()['sample'].reset_index().pivot(index = roi_key, columns = celltype, values = 'sample')
    # retreive metadata for new obs layer
    data_meta = data.obs[keys].drop_duplicates()
    
    logger.debug(cell_counts)
    logger.debug(data_meta)
    # assert cell count matches metadata length
    assert len(cell_counts) == len(data_meta), 'Error: non-matching cell counts and metadata length. Check for whether condition is unique per sample.'
    
    # set index as roi_key
    data_meta = data_meta.set_index(roi_key)
    
    # create AnnData Object
    density = anndata.AnnData(X = cell_counts.astype(np.float32), obs = data_meta.loc[cell_counts.index])
    density.var.index = cell_counts.columns

    if roi_key in density.obs:
        density.obs = density.obs.set_index(roi_key)

    density.X = density.X / np.array(density.obs['ROI_area'])[:, None]
    
    return density

def impute_roi_area(
    data: anndata.AnnData,
    roi_key: str = 'roi',
    roi_area_key: str = 'ROI_area',
    y_coord: str = 'Y_centroid',
    x_coord: str = 'X_centroid',
    overwrite: bool = False,
    return_data: bool = False,
    **kwargs: tp.Any,
) -> tp.Optional[anndata.AnnData]:
    """ Function to store imputed ROI area to `obs` layer of AnnData from x and y coordinates.

    Args:
        data (anndata.AnnData): Input AnnData object
        roi_key (str, optional): Identifier from roi. Defaults to 'roi'.
        roi_area_key (str, optional): ROI area key to save the result. Defaults to 'ROI_area'.
        y_coord (str, optional): Y coordinate of cells. Defaults to 'Y_centroid'.
        x_coord (str, optional): X coordinate of cells. Defaults to 'X_centroid'.
        
        overwrite (bool, optional): Whether to overwrite existing roi area. Defaults to False.
        return_data (bool, optional): Whether to return a copy of the data. The original AnnData is modified by default when this is set as False. Defaults to False.

    Returns:
        anndata.AnnData: AnnData object with stored ROI area. Optionally returned when return_data is turned on.
    """
    logger.info(f'Imputing ROI area for data')
    assert roi_key in data.obs, f"Error: {roi_key} not in 'data.obs'"
    
    if return_data:
        data = data.copy()
        
    if not overwrite and roi_area_key in data.obs:
        logger.debug(f'Function not in overwrite mode and {roi_area_key} found in data.obs')
        return

    if overwrite:
        logger.info(f"Overwriting existing {roi_area_key}.")
    
    # Ensure x and y coordinate is in data.obs
    assert y_coord in data.obs, f"Error: {y_coord} not in 'data.obs'"
    assert x_coord in data.obs, f"Error: {x_coord} not in 'data.obs'"
    
    # If spatial missing from obsm, create it based on x and y coord
    if 'spatial' not in data.obsm:
        logger.info(f"Storing `obs[[{y_coord}, {x_coord}]]` to `obsm['spatial']`.")
        data.obsm['spatial'] = np.array(data.obs[[y_coord, x_coord]])

    # cells / mm^2
    data.obs[roi_area_key] = data.obsm['spatial'][:,0] * data.obsm['spatial'][:,1] / 1e6
    # maximum projection per ROI
    data.obs[roi_area_key] = data.obs.groupby(roi_key)[roi_area_key].transform('max')
    
    if return_data:
        return data

def patient_density(
    adata: anndata.AnnData,
    patient_key: str = 'ID',
    celltype_key: str = 'celltype',
    condition_keys: tp.Union[list,None] = None,
    roi_key: str = 'roi'
)->anndata.AnnData:
    """ Calculates celltype density at patient level. 

    Args:
        adata (anndata.AnnData): Cell matrix
        patient_key (str, optional): Patient identifier in obs layer of adata. Defaults to 'ID'.
        celltype_key (str, optional): Cell type identifier in obs layer of adata. Defaults to 'celltype'.
        roi_key (str, optional): Roi identifier in obs layer of adata. Defaults to 'roi'.
        condition_keys (tp.Union[list,None], optional): List of conditions to store in the output anndata obs layer. 
    Returns:
        anndata.AnnData: Cell type density on patient level. Each samples are patient, and each columns are cell types.
    """
    logger.debug(f'celltype key: {celltype_key}')
    logger.debug(f'adata: {adata}')
    
    assert patient_key in adata.obs, f'{patient_key} not in adata.obs layer.'
    if patient_key not in condition_keys:
        condition_keys = condition_keys + [patient_key]
        
    density = celltype_density(
        adata,
        celltype = celltype_key,
        roi_key = roi_key,
        condition_keys = condition_keys
    )
    
    # convert density to count by multiplying area per ROI
    density_df = density.to_df()
    count = density_df * np.array(density.obs['ROI_area'])[:,None]
    count[patient_key] = density.obs[patient_key]
    count = count.groupby(patient_key).sum() # store total roi area
    #count = count.set_index(patient_key)

    features = (density.obs.groupby(patient_key).nunique() <= 1).all()
    patient_metadata = density.obs[features[features].index.tolist() + [patient_key]].drop_duplicates()
    patient_metadata = patient_metadata.set_index(patient_key)

    # create anndata with 
    res = anndata.AnnData(X = count, obs = patient_metadata.loc[count.index])
    res.obs['ROI_area'] = density.obs.groupby(patient_key)['ROI_area'].sum().tolist()
    res.X = res.X / np.array(res.obs['ROI_area'])[:,None]

    # density = adata.to_df()
    # count = density * np.array(adata.obs[roi_area])[:,None]
    # count[patient_key] = adata.obs[patient_key]
    # count = count.groupby(patient_key).sum()
    # #count = count.set_index(patient_key)

    # features = (adata.obs.groupby(patient_key).nunique() <= 1).all()
    # patient_metadata = adata.obs[features[features].index.tolist() + [patient_key]].drop_duplicates()
    # patient_metadata = patient_metadata.set_index(patient_key)

    # res = anndata.AnnData(X = count, obs = patient_metadata.loc[count.index])
    # res.obs[roi_area] = adata.obs.groupby(patient_key)[roi_area].sum().tolist()

    #return res
    return res
  
def grouped_obs_mean(
    adata: anndata.AnnData,
    group_key: str,
    layer=None,
    gene_symbols=None) -> np.array:
    if layer is not None:
        getX = lambda x: x.layers[layer]
    else:
        getX = lambda x: x.X
    if gene_symbols is not None:
        new_idx = adata.var[idx]
    else:
        new_idx = adata.var_names

    grouped = adata.obs.groupby(group_key)
    out = pd.DataFrame(
        np.zeros((adata.shape[1], len(grouped)), dtype=np.float64),
        columns=list(grouped.groups.keys()),
        index=adata.var_names
    )

    for group, idx in grouped.indices.items():
        X = getX(adata[idx])
        out[group] = X.mean(axis=0, dtype=np.float64).tolist()
    return out.T


def compute_mean(
    data: anndata.AnnData,
    condition_keys: list = [],
    obs_key: str = 'roi',
) -> anndata.AnnData:
    """ Compute mean intensity of all markers for a cell matrix grouped by obs_key.

    Args:
        data (anndata.AnnData): cell matrix
        condition_keys (list, optional): list of conditions to keep. Defaults to [].
        obs_key (str, optional): _description_. Defaults to 'roi'.

    Returns:
        anndata.AnnData: Mean expression AnnData. Each sample is on obs_key, and each column is var from input AnnData.
    """
    logger.info(f'Computing mean grouped by: {obs_key}')
    keys = [obs_key] + condition_keys
    for k in keys:
        assert(k in data.obs)

    mean = grouped_obs_mean(data, group_key = obs_key)
    data_meta = data.obs[keys].drop_duplicates()
    logger.debug(mean)
    logger.debug(data_meta)
    # assert cell count matches metadata length
    assert len(mean) == len(data_meta), 'Error: non-matching groups of obs and metadata. Check for whether condition is unique per observation.'
    
    # set index as obs_key
    data_meta = data_meta.set_index(obs_key)
    # mean.index = data_meta.index

    mean_adata = anndata.AnnData(X = mean.astype(np.float32), obs = data_meta.loc[mean.index])
    mean_adata.var.index = mean.columns

    if obs_key in mean_adata.obs:
        mean_adata.obs = mean_adata.obs.set_index(obs_key)
    
    return mean_adata
