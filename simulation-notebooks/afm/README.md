# AFM Image Simulator
<p align="center">
   <img width="650" height="300" src="https://github.com/Joshua-Giblin-Burnham/ABAQUS-AFM-Simulations/blob/main/docs/_images/ScanPositions%20diagram-1.png">
</p>
    
Simulating AFM images requires the calculation of contours of constant indentation force across a sample. Using Finite Element Modelling (FEM), the sample surface and probe tip geometry are recreated, and AFM raster scan dynamics are replicated by performing independent indentations across the surface. Biological structures are produced using Protein Data Bank (PDB) files with geometric dimensions in $\AA$. For simplicity, the biomolecule is modelled as an elastic material produced from the assembly of the individual atoms (with van der Waals radius). The molecule is partially embedded in a rigid base/ substrate and fixed at its base to simulate a soft molecule absorbed onto a solid support. The structure is assumed to be a continuous, homogeneous and isotropy elastic material. 

Scan positions are determined by subdividing the XY domain and calculating corresponding initial indenter heights. Initial heights are computed from hard-sphere/ tangential contact points, ensuring consistent indentation depths across the surface. The tangent points between the surfaces are calculated by setting the tip above the sample and determining the minimum vertical distance between the tip and the molecule's surface. Above illustrates the calculations. By computing the vertical distances between the indenter's surface and atoms within the indenter's boundary ($R_{Boundary}$), an array of height differences ($\Delta Z$) is obtained. As illustrated the minimum $\Delta Z$ value corresponds to the tangential contact position. % Only positions where the tip and molecule interact are included for computational efficiency.

Extracting simulated vertical forces and displacements produces a four-dimensional array of indenter positions and forces. Subsequently, contours are computed using a reference force, generating the final AFM images. Contours are calculated from force-indentation data via list comprehension, extracting the depth at which the indentation force exceeds a given reference force. Linear or power normalisation is applied depending on detail contrast, and images are interpolated using bi-cubic interpolation to increase pixel density.

## Running Simulator
<p align="center">
   <img width="650" height="300" src="https://github.com/Joshua-Giblin-Burnham/ABAQUS-AFM-Simulations/blob/main/docs/_images/AFM Simulation Code Flow chart.png">
</p>

The code can be run from the jupyter notebook or using the SimulationInterface.py. DataAnalysis.py and ExperimentalDataAnalysis.py are used for analysis of simulation and experimental data, respectively.

The code calculates scan variables and export them to csv files then runs ABAQUS using seperate python scripts that import the variable data. ABAQUS can be run locally, however, they are designed to be run on remote servers, using SSH to upload files and run ABAQUS on HPC queues. Cloning the git page and pip installing 'abqsims' will add all packages/ modules to your python enviroment. All Jupyter notebooks(.ipynb) are self contained, they produce the input files, in the specified local working directory, for each simulation so best run from own self contained directory. The notebooks contain breakdown and description of code function. For more lightweight code the simulator can be run from separate python kernal/notebook by importing the abqsims module in a python file as show in the 'simulation-notebooks/afm/SimulationInterface.py' file (the ABAQUS scripts will need to be copied into the working directory (localPath) specified in simulator).

