# main.py

import click
from imc_analysis.utils import parse_yaml
import os

@click.group()
def cli():
    """A Imaging Mass Cytometry analysis command line tool. Current commands include qc, phenotype, and visualize."""

@cli.command()
@click.option('-p', '--project', 'project', type=click.Path(), default = 'imc_project/')
@click.option('-y', '--yaml', 'yaml', type=click.Path(), default = 'metadata/project.yml', )
@click.option('--panel','panel', type=list, default = ['PANEL'])
def init(project, yaml, panel):
    """
    Create a IMC project directory
    """
    from imc_analysis.utils import init

    init(project, yaml, panel)


@cli.command()
@click.option('-y', '--yaml', 'yaml', type=click.Path(exists=True), default = 'metadata/project.yml')
@click.option('-p', '--panel','panel', type=str)
@click.option('-o', '--outdir','outdir', type=click.Path(exists=True), default='figures/QC/')
def qc(yaml, panel, outdir):
    """
    Run quality control check on an IMC project.

    yaml: Path to yaml file storing project configs.
    panel: Panel to apply qc 
    """
    click.echo(f"Plotting QC figures using metadata stored in {yaml}.")
    metadata = parse_yaml(yaml)
    assert(panel in metadata)

    from imc_analysis.qc.qc import quality_control

    path = f'{outdir}/{panel}'
    os.makedirs(path, exist_ok=True)
    quality_control(metadata[panel], outdir = path)

    click.echo(f"Command QC completed")

@cli.command()
@click.option('-y', '--yaml','yaml', type=click.Path(exists=True), default = 'metadata/project.yml')
@click.option('-p', '--panel', 'panel', type=str)
def phenotype(yaml):
    """Analyze phenotypes."""
    from imc_analysis.phenotype.phenotype import phenotype
    phenotype()

@cli.command()
@click.option('-y', '--yaml','yaml', type=click.Path(exists=True), default = 'metadata/project.yml')
@click.option('-m', '--mode','mode', type=click.Choice(['stack', 'rgb']), default = 'stack')
@click.option('-p', '--panel', 'panel', type=str)
@click.option('-o', '--outdir','outdir', type=click.Path(exists=True), default='images/')
def visualize(mode, yaml, panel, outdir):
    """Visualize data."""

    metadata = parse_yaml(yaml)

    from imc_analysis.visualize.visualize import visualize_stack
    
    path = f'{outdir}/{mode}/{panel}/'
    os.makedirs(path, exist_ok=True)
    
    visualize_stack(metadata, panel, outdir = path, mode = mode)


@cli.command()
@click.option('-y', '--yaml', 'yaml', type=click.Path(exists=True), default = 'metadata/project.yml')
@click.option('-p', '--panel','panel', type=str)
def celltype(yaml):
    """Perform cell phenotyping"""

@cli.command()
@click.option('-y', '--yaml', 'yaml', type=click.Path(exists=True), default = 'metadata/project.yml')
@click.option('-p', '--panel','panel', type=str)
def stats(yaml):
    """Perform statistical testing either on single cell level, ROI level, or Patient level"""


@cli.command()
@click.option('-y', '--yaml', 'yaml', type=click.Path(exists=True), default = 'metadata/project.yml')
@click.option('-p', '--panel', 'panel', type=str)
@click.option('-m', '--mode', 'mode', type=click.Choice(['roi', 'patient']), default = 'roi')
@click.option('-k', '--key', 'key', type=str, default = 'roi')
def agg(yaml, panel, mode, key):
    """Aggregate single cell matrix on ROI level or Patient level"""
    click.echo(f"Aggregate {panel} single cell matrix on {mode} level {yaml}.")
    metadata = parse_yaml(yaml)
    assert(panel in metadata)

    
if __name__ == "__main__":
    cli()
