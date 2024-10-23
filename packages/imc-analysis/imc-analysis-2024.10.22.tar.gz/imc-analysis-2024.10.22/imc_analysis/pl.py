from tqdm import tqdm
from glob import glob
import tifffile
import matplotlib.pyplot as plt

import typing as tp
from imc_analysis.types import Path, AnnData

import os

import pandas as pd
import numpy as np

import scanpy as sc
import anndata

from skimage.exposure import adjust_gamma
from skimage import filters
import scipy.ndimage as ndi
import scipy

import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.simplefilter("ignore", UserWarning)
from imc_analysis.logging import *

import matplotlib

# matplotlib.use('Agg')
sc.settings.set_figure_params(dpi=200, dpi_save=300, fontsize=12)
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42
matplotlib.rcParams["axes.grid"] = False

def plot_mwu(
    adata: AnnData,
    line_width:float = 0.5,
    save_dir: Path = 'figures/',
    palette: list = [],
    kind = 'box', # either box or bar
    pval_form: str = 'star',
    show: bool = False,
    nrow = 3,
    ncol = 6,
    y_max = None,
    figsize = (12,8),
):

    if 'mwu' not in adata.uns:
        logger.error("'mwu' not found in adata.uns layer. Run imc_analysis.tl.grouped_mwu_test()")
        return
    
    density = adata.to_df()
    mwu_ = adata.uns['mwu']
    # for each conditions
    for cond in tqdm(mwu_['condition'].unique()):
        
        logger.info(f'Producing figure for condition: {cond}')
        
        fig, axes = plt.subplots(nrow,ncol, dpi = 300, figsize = figsize)
        
        # for each celltype
        for i, ax in enumerate(axes.flatten()):
        
            if i >= density.shape[1]:
                ax.axis('off')
            else:
                
                ct = density.columns[i]
                # create swarmboxen plot
                if kind == 'box':
                    sns.boxplot(y = density[ct], x = adata.obs[cond], hue = adata.obs[cond], ax = ax, fliersize = 0, palette = palette, dodge = False)
                    sns.swarmplot(y = density[ct], x = adata.obs[cond], color = 'black', ax = ax, s = 3)
                elif kind == 'bar':
                    sns.barplot(y = density[ct], x = adata.obs[cond], hue = adata.obs[cond], ax = ax, palette = palette, dodge = False, width = 0.7)
                elif kind == 'violin':
                    sns.violinplot(y = density[ct], x = adata.obs[cond], hue = adata.obs[cond], ax = ax, palette = palette, dodge = False, width = 0.7)
                else:
                    logger.error("'kind' must equal either 'box', 'bar', or 'violin'")
                    return
                ax.set_title(ct)
                ax.set_ylabel('')
                ax.set_xlabel('')
                if y_max:
                    ax.set_ylim(0, y_max)

                y1 = density[ct].max() * 1.05
                r = y1 * 0.03
                l = adata.obs[cond].cat.categories.tolist()

                sig_mwu_ = mwu_[(mwu_['celltype'] == ct) & (mwu_['condition'] == cond) & (mwu_['adj. p-val'] < 0.05)]

                sig_n = 0
                for i, idx in enumerate(sig_mwu_.index):
                    pair = sig_mwu_.loc[idx, 'pair']
                    
                    if pval_form == 'star':
                        pval = sig_mwu_.loc[idx, 'significance']
                    else:
                        pval = sig_mwu_.loc[idx, 'adj. p-val sci']
                    
                    if len(sig_mwu_) == 1:

                        ax.plot([pair[0], pair[1]], [y1 + r*i, y1 + r*i], lw=line_width, c='black')
                        ax.text(s = pval, x = 0.5, y = y1, fontsize = 8, va = 'bottom', ha = 'center')

                    else:
                        p = sig_mwu_.iloc[i]['adj. p-val']
                        
                        ax.plot([pair[0], pair[1]], [y1 + r*sig_n, y1 + r*sig_n], lw=line_width, c='black')
                        ax.text(s = pval, x = pair[1], y = y1 + r*sig_n, fontsize = 8, va = 'top', ha = 'left')
                        sig_n += 1
                ax.legend().remove()
                sns.despine()
        plt.tight_layout()

        dir_path = f'{save_dir}/{cond}_{pval_form}.pdf'
        # check if directory exists
        if not os.path.exists(save_dir):
            # create directory if it doesn't exist
            os.makedirs(save_dir)
            print(f"Directory '{save_dir}' created.")
        plt.savefig(dir_path, bbox_inches = 'tight')
        
        if show:
            plt.show()
        
        plt.close()

def celltype_heatmap(
    adata: anndata.AnnData,
    var_names: dict = None,
    umap_adata: anndata.AnnData = None,
    cluster_ids: list = ['cluster_0.5', 'cluster_1.0', 'cluster_1.5', 'cluster_2.5', 'celltype', 'celltype_cid', 'celltype_broad'],
    panel: str = 'panel',
    plot_umap: bool = True,
    cmap: str = 'Spectral_r',
    out_dir: Path = 'figures/cell phenotyping/'
):
    
    os.makedirs(out_dir, exist_ok = True)
    if var_names == None:
        logger.info(f"'var_names' was not provided. Defaulting to original var indices")
        var_names = adata.var.index
        
    for cluster_id in cluster_ids:
        
        if cluster_id not in adata.obs:
            logger.info(f'{cluster_id} not in "adata.obs" layer. Skipping...')
            continue

        # Plot Raw Matrixplot
        mp = sc.pl.matrixplot(
            adata,
            groupby = cluster_id,
            var_names = var_names,
            log = True,
            cmap = cmap,
            vmax = 1.5,
            return_fig = True,
            use_raw = False
        )
        mp.add_totals().style(cmap = cmap, edge_color='black')
        mp.savefig(f'{out_dir}/matrixplot_raw_{cluster_id}.pdf')
        plt.close()

        # Plot Normalized Matrixplot
        mp = sc.pl.matrixplot(
            adata,
            groupby = cluster_id,
            var_names = var_names,
            log = True,
            cmap = cmap,
            standard_scale = 'var',
            return_fig = True,
            use_raw = False
        )
        mp.add_totals().style(cmap = cmap, edge_color='black')
        mp.savefig(f'{out_dir}/matrixplot_normalized_{cluster_id}.pdf')
        plt.close()

        if plot_umap and 'X_umap' in adata.obsm:
            fig = sc.pl.umap(adata, color = cluster_id, frameon = False, title = '', show = False, return_fig = True, use_raw = False)
            plt.tight_layout()
            fig.savefig(f'{out_dir}/umap_{cluster_id}.pdf', bbox_inches = 'tight')
            plt.close()
        
    if 'celltype' in adata.obs:
        adata.obs.groupby(['celltype']).count().plot.pie(y = 'sample', autopct = '%1.1f%%', cmap = 'PiYG')
        plt.legend().remove()
        plt.ylabel('')
        plt.savefig(f'{out_dir}/celltype_proportion.pdf', bbox_inches = 'tight')
        plt.close()



def add_scale_box_to_fig(
    img,
    ax,
    box_width: int = 100,
    box_height: float = 3,
    color: str = 'white'
):    
    import matplotlib.patches as patches
    x = img.shape[1]
    y = img.shape[0]
    
    # Create a Rectangle patch
    rect = patches.Rectangle((x - box_width, y * (1-box_height/100)), box_width, y * (box_height/100), linewidth=0.1, edgecolor='black', facecolor=color)
    
    
    # Add the patch to the Axes
    ax.add_patch(rect)
    return ax

def visualize_grayscale(
    img_name: str,
    csv_name: str,
    out_dir: str = 'images'
) -> None:
    fig_dict = {
        'nrow': [5, 6, 6, 8],
        'ncol': [8, 8, 10, 10],
        'figsize': [(20,15), (20,15), (20,15), (25,20)],
    }
    
    img = tifffile.imread(img_name)
    roi = img_name.split('/')[-1].replace('_full.tiff', '')
    df = pd.read_csv(csv_name, index_col = 0)
    df['channel'] = df['channel'].str.replace('[0-9]{2,3}[A-Z][a-z]', '', regex = True)
    n_feature = df.shape[0]

    for i in range(4):
        if n_feature < fig_dict['nrow'][i] * fig_dict['ncol'][i]:
            break

    fig, axs = plt.subplots(
        fig_dict['nrow'][i],
        fig_dict['ncol'][i],
        figsize = fig_dict['figsize'][i],
        dpi = 300
    )
    
    for i, ax in enumerate(fig.axes):

        if i < len(df):
            rescaled_img = adjust_gamma(img[i], gamma = 0.2, gain = 1)

            ax.imshow(rescaled_img, cmap = 'viridis')

            ax.set_title(df.iloc[i]['channel'], fontsize = 10)
            add_scale_box_to_fig(rescaled_img, ax, box_width = 200)

            ax.annotate(
                text = 'min: {:.2f}\nmax: {:.2f}'.format(img[i].min(), img[i].max()),
                xy = (rescaled_img.shape[1], 0),
                ha = 'right',
                va = 'bottom',
                fontsize = 6
            )
            
            ax.annotate(
                text = '200μm',
                xy = (rescaled_img.shape[1], rescaled_img.shape[0]),
                ha = 'right',
                va = 'top',
                fontsize = 6
            )
        ax.axis('off')

    plt.suptitle(roi)
    plt.tight_layout()
    plt.savefig(f'{out_dir}/{roi}.pdf', bbox_inches = 'tight')
    plt.savefig(f'{out_dir}/{roi}.png', bbox_inches = 'tight')
    plt.close()

def visualize_rgb(
    metadata: dict,
    image_name: Path,
    csv_name: Path,
    outdir: Path,
    plot_config_string: str = 'plot_config',
):
    
    assert(plot_config_string in metadata)
    plot_config = metadata[plot_config_string]
    plot_keys = list(plot_config.keys())

    try:
        image = tifffile.imread(img_name)
        csv = pd.read_csv(csv_name)
    except FileNotFoundError:
        print(f'Either {img_name} or {csv_name} not found')

    img_name = img_name.split('/')[-1]
    fig, axes = plt.subplots(2,4,dpi=300, figsize = (24,12))

    for i, ax in enumerate(axes.flatten()):
        
        if i < len(plot_keys):
            plot_key = plot_keys[i]
            image_sub = [image[k] * float(v[1]) for k, v in plot_config[plot_key].items()]
            image1 = np.clip(np.stack(image_sub[:-1], axis = 2) + image_sub[-1][:,:,np.newaxis], 0, 1)
            image1[-int(image.shape[1] * 0.03):, -200:, :] = 1
            title = plot_key + '\n'
            for idx, key in enumerate(plot_config[plot_key]):
                title += f'{plot_config[plot_key][key][0]}, '
            ax.imshow(image1)
            ax.set_title(title[:-2])
            ax.axis('off')

    filename = img_name.replace('.tiff','')
    title = filename

    plt.suptitle(title, fontsize = 14)
    plt.tight_layout()
    plt.savefig(Path(f'{out_dir}/{filename}_RGB.pdf'), bbox_inches = 'tight')
    plt.savefig(Path(f'{out_dir}/{filename}_RGB.png'), bbox_inches = 'tight')
    
    plt.close()

def umap_var(
    adata: anndata.AnnData = None,
    metadata: dict = None,
    anndata_key: str = None,
    outdir: Path = 'figures/',
):
    if metadata != None and anndata_key != None:
        adata = sc.read(metadata[anndata_key])

    assert(isinstance(adata, anndata.AnnData))
    os.makedirs(outdir, exist_ok=True)
    # Plot UMAP Marker
    print('Plotting marker UMAP')
    fig_dict = {
        'nrow': [5, 6, 6, 8],
        'ncol': [8, 8, 10, 10],
        'figsize': [(20,15), (20,15), (20,15), (25,20)],
    }
    
    for i in range(4):
        if len(adata.var) < fig_dict['nrow'][i] * fig_dict['ncol'][i]:
            break

    fig, axs = plt.subplots(
        fig_dict['nrow'][i],
        fig_dict['ncol'][i],
        figsize = fig_dict['figsize'][i],
        dpi = 300
    )

    for i, ax in tqdm(enumerate(fig.axes)):
        if i < len(adata.var.index):
            var = adata.var.index[i]
            sc.pl.umap(
                adata,
                color = var,
                use_raw = False,
                size = 1,
                frameon = False,
                ax = ax,
                show = False,
                colorbar_loc = None,
                vmin = 0,
                vmax = 3
            )
            
        else:
            ax.axis('off')
            
    plt.suptitle(f'Cell Marker Scaled Expression UMAP\nPlotting {len(adata)} cells')
    plt.tight_layout()
    
    plt.savefig(
        f'{outdir}/umap_marker_normalized.pdf',
        bbox_inches = 'tight'
    )
    plt.close()


    for i in range(4):
        if len(adata.var) < fig_dict['nrow'][i] * fig_dict['ncol'][i]:
            break

    fig, axs = plt.subplots(
        fig_dict['nrow'][i],
        fig_dict['ncol'][i],
        figsize = fig_dict['figsize'][i],
        dpi = 300
    )

    for i, ax in tqdm(enumerate(fig.axes)):
        if i < len(adata.var.index):
            var = adata.var.index[i]
            sc.pl.umap(
                adata,
                color = var,
                use_raw = True,
                size = 1,
                frameon = False,
                ax = ax,
                show = False,
                colorbar_loc = None,
            )
            
        else:
            ax.axis('off')
            
    plt.suptitle(f'Cell Marker Raw Expression UMAP\nPlotting {len(adata)} cells')
    plt.tight_layout()
    plt.savefig(
        f'{outdir}/umap_marker_raw.pdf',
        bbox_inches = 'tight'
    )
    plt.close()
