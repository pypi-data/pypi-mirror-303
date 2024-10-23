from imc_analysis.types import Path
import typing as tp

def parse_yaml(yaml_file: Path) -> tp.Union[dict, None]:
    """
    Parse project config yaml file
    """
    import yaml

    with open(yaml_file, "r") as stream:
        try:
            metadata = yaml.safe_load(stream)
            return metadata
        except yaml.YAMLError as exc:
            print(exc)


def init(project, yaml, panel):
    """
    Create a IMC project directory
    """
    import os

    os.makedirs(f'{project}/data', exist_ok = True)
    os.makedirs(f'{project}/processed', exist_ok = True)
    os.makedirs(f'{project}/metadata', exist_ok = True)
    os.makedirs(f'{project}/figures', exist_ok = True)
    os.makedirs(f'{project}/images', exist_ok = True)

    yaml_str = f"---\n# {project} Project Config YAML File\n\n"

    for p in panel:
        yaml_str += f"""\
{p}:
    AnnData:
        unlabeled_file_name: 'results/unlabeled.h5ad'
        labeled_file_name: 'results/clustered.h5ad'
        phenotyped_file_name: 'results/celltyped.h5ad'
        phenotyped_umap_name: 'results/celltyped.umap.h5ad'
        utag_file_name: 'results/celltyped.utag.h5ad'

    glob_pattern:
        IMAGE_FILE_PATTERN: 'processed/{p}/*/tiffs/*_full.tiff'
        MASK_FILE_PATTERN: 'processed/{p}/*/tiffs/*_full_mask.tiff'
        NUCMASK_FILE_PATTERN: 'processed/{p}/*/tiffs/*_full_nucmask.tiff'
        CSV_FILE_PATTERN: 'processed/{p}/*/tiffs/*_full.csv'

    image_metadata:
        ROI_AREA_FILE: 'metadata/{p}_ROI_area.csv'
        ROI_MEAN_FILE: 'metadata/{p}_ROI_mean.csv'
        ROI_VAR_FILE: 'metadata/{p}_ROI_var.csv'
        ROI_NUC_FILE: 'metadata/{p}_ROI_nuc.csv'
        ROI_CYTO_FILE: 'metadata/{p}_ROI_cyto.csv'
        ROI_SPILLOVER_FILE: 'metadata/{p}_ROI_spillover.csv'

    UMAP_FRACTION: 0.1

    var_celltype_groups:
        'Epithelial': ['PanCytokeratin(Pt198)']
        'Stromal': ['CD31(Eu151)', 'aSMA(Pt196)', 'Vimentin(Nd143)']
        'Prolif.': ['Ki67(Er168)']

        'Mono.': ['HLADR(Pr141)',  'CD14(Nd144)',]
        'Mac.': ['CD14(Nd144)', 'CD16(Nd146)', 'CD68(Tb159)']

        'T': ['CD3(Er170)', 'CD45(Sm152)', 'CD27(Yb171)',]
        'CD4': [ 'CD4(Gd156)']
        'CD8': ['CD8a(Dy162)',]
        'B': ['CD20(Dy161)',]
        'NK': ['CD11b(Dy164)', 'CD56(Dy163)', 'CD57(Tm169)',]

    plot_config : {{
        'Epithelial': {{
            38: ['KRT5', 0.1],
            31: ['KRT818', 0.01],
            10: ['ECad', 0.1],
            46: ['DNA', 0.003]
        }}
    }},

"""
    with open(f'{project}/{yaml}', 'w') as file:
        file.write(yaml_str)
        file.close()

