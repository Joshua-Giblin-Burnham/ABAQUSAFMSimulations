# ABAQUSAFMSimulations
## Introduction
Repository for Masters project code simulating AFM imaging using ABAQUS/FEM and various FEM simulations. There are four different simulations.

### Axisymmetric Simulation of Indentation of Elastic Sphere 
![Double Contact AFM tip-1](https://github.com/Joshua-Giblin-Burnham/ABAQUSAFMSimulations/assets/97748069/34427ea5-5f61-4b48-8891-b68d9679c102)

### Three Dimensional Simulation of Compression along scanline of a Hemisphere 
![Hemisphere-Setup-Manuscript-1](https://github.com/Joshua-Giblin-Burnham/ABAQUSAFMSimulations/assets/97748069/65437d15-c4f1-46d0-b95a-1cf20c8e5d52)

### Three Dimensional Simulation of Compression along scanline of a Periodic Structure 
![Wave-SetUp-Manuscript-1](https://github.com/Joshua-Giblin-Burnham/ABAQUSAFMSimulations/assets/97748069/e67616a7-dc1d-411d-96ea-34544093488e)

### AFM Image Simulator
![ScanPositions diagram-1](https://github.com/Joshua-Giblin-Burnham/ABAQUSAFMSimulations/assets/97748069/d4e75cc7-bcda-4fda-91d0-964daafa6fab)

## Runnig Simulator
All Jupyter notebooks(.ipynb) are self contained, they produce the input files, in the specified local working directory, for each simulation so best run from own self contained directory. The notebooks contain breakdown and discription of code function.

Seperate Python(.py) files for the AFM simulation are available in the 'Python Scripts' folder. For more lightweight code the simulator can be run from separate python kernal/notebook by importing the AFM_ABAQUS_Simulation_Code.py file (the ABAQUS scripts will need to be copied into the working directory (localPath) specified in simulator).

### Importing Python files
Within a seperate python script the simulator code can be imported by either appending the script using system command and path to directory holding the AFM_ABAQUS_Simulation_Code.py file:

    import sys
    sys.path.insert(1, 'C:\\path\\to\\directory\\') 
    from AFM_ABAQUS_Simulation_Code import *
    
,or by either copying the AFM_ABAQUS_Simulation_Code.py script to the same directory or to the main python path (for jupyter notebook/spyder this will be main anaconda directory) and importing as:

        from AFM_ABAQUS_Simulation_Code import *

Then, the simulator can simply be run by defining the required variables and running main function:

        host, port, username, password, None, localPath, abqCommand, fileName, subData,              
        pdb, rotation, surfaceApprox, indentorType, rIndentor, theta_degrees, tip_length,             
        indentionDepth, forceRef, contrast, binSize, clearance, meshSurface, meshBase, meshIndentor,   
        timePeriod, timeInterval = ...
        
        AFMSimulation(host, port, username, password, None, localPath, abqCommand, fileName, subData, 
        pdb, rotation, surfaceApprox, indentorType, rIndentor, theta_degrees, tip_length,
        indentionDepth, forceRef, contrast, binSize, clearance, meshSurface, meshBase, meshIndentor,
        timePeriod, timeInterval)

## Common errors:
- Some modules may require Python 3.9 or newer. 
- You must be careful to change path syntaax if using mac or linux.
- Require the following modules: py3Dmol, nglview, biopython, mendeleev, pyabaqus==2022, paramiko

