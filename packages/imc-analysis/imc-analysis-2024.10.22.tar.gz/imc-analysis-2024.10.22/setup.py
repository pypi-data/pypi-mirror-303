from setuptools import setup
setup()

# from setuptools import setup

# setup(
#     name="imc-analysis",
#     version="0.1.7",
#     description="A multi-file Python command line tool with commands qc, phenotype, and visualize.",
#     author="Junbum Kim",
#     author_email="jkim0810@gmail.com",
#     url="https://github.com/jkim810/imc-analysis",
#     packages=["imc_analysis"],
#     package_dir={"": "."},
#     include_package_data=True,
#     install_requires=[
#         "click",
#         "pathlib",
#         "tifffile==2023.4.12",
#         "tqdm",
#         "pandas==2.0.1",
#         "scanpy==1.9.3",
#         "anndata==0.9.1",
#         "scikit-image==0.20.0",
#         "scipy==1.9.1",
#         "seaborn",
#         "pyyaml==6.0",
#         "pydot==1.4.2",
#     ],
#     entry_points = {
#         'console_scripts': ['mybinary=imc_analysis.main:cli'],
#     },
#     test_suite="tests",
#     python_requires=">=3.6",
# )
