from setuptools import setup, find_packages

setup(
    name='abqsims',
    version='1.0',
    description='A package to analyse AFM via FEM simulations',
    url='https://abaqus-afm-simulations.readthedocs.io/en/latest/index.html',
    author='J. Giblin-Burnham',
    packages=find_packages(),
    install_requires = ["numpy", "matplotlib", "scipy", "absl-py","biopython","keras","mendeleev",
                        "nglview","py3dmol","pyabaqus","pypdf","pypdf2","scp","paramiko","sphinx_rtd_theme"]
)
