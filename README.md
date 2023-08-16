# ABAQUSAFMSimulations
Repository for Masters project code simulating AFM imaging using ABAQUS/FEM and various FEM simulations. 


## Runnig Simulator
All Jupyter notebooks(.ipynb) are self contained, they produce the input files, in the specified local working directory, for each simulation so best run from own self contained directory. Seperate Python(.py) files for the AFM simulation are available in the 'Python Scripts' folder. For more lightweight code the simulator can be run from separate python kernal/notebook by importing the AFM_ABAQUS_Simulation_Code.py file (the ABAQUS scripts will need to be copied into the working directory (localPath) specified in simulator).

### Importing Python files
Within a seperate python script the simulator code can be imported by either appending the script using system command and path to directory holding the AFM_ABAQUS_Simulation_Code.py file:

`import sys \n
sys.path.insert(1, 'C:\\path\\to\\directory\\') \n
from AFM_ABAQUS_Simulation_Code import *`

or by either copying the AFM_ABAQUS_Simulation_Code.py script to the same directory or to the main python path (for jupyter notebook/spyder this will be main anaconda directory) and importing as:

`from AFM_ABAQUS_Simulation_Code import *`


## Common errors:
- Some modules may require Python 3.9 or newer. 
- You must be careful to change path syntaax if using mac or linux.
- Require the following modules: py3Dmol, nglview, biopython, mendeleev, pyabaqus==2022, paramiko

