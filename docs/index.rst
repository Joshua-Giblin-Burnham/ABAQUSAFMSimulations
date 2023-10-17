.. abqsims documentation master file, created by
   sphinx-quickstart on Fri Oct 13 14:16:53 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ABQSIMS Package
===================================

Repository for Masters project code simulating AFM imaging using ABAQUS/FEM and various FEM simulations. There are four different simulations.

Simulations implement ABAQUS (2017) software for quasi-static, implicit computations using user subroutines UMAT. Samples are modelled as continuous, homogeneous and isotropic elastic materials with Young's modulus and Poisson ratio comparable to biomolecules. To eliminate the hourglass effect, R3D10 tetrahedral elements are employed.  Simulations impliment "surface to surface contact" interaction with "hard", nonadhesive normal contact and "rough" (Coulomb friction), non-slip tangential contact. Boundary conditions fix the base of the structures, and vertical force and indentation data are mapped and sampled via reference points at the indenter's centre.

The shape of a blunt AFM tip is a simplified construct similar to the SEM image of actual AFM tips shown by Chen et al. The tip is modelled as a rigid (incompressible) cone with opening angle \theta ending in a spherical termination of radius. The spherical portion smoothly transitions to the conical segment at the tangential contact point described by,

.. math:: X_{tangent} = R\cos\theta ; Y_{tangent} = R(1-\sin\theta)

Running Simulator
===================================
The code calculates scan variables and export them to csv files then runs ABAQUS using seperate python scripts that import the variable data. ABAQUS can be run locally, however, they are designed to be run on remote servers, using SSH to upload files and run ABAQUS on HPC queues. Cloning the git page and pip installing 'abqsims' will add all packages/ modules to your python enviroment. All Jupyter notebooks(.ipynb) are self contained, they produce the input files, in the specified local working directory, for each simulation so best run from own self contained directory. The notebooks contain breakdown and description of code function. Seperate Python(.py) files for the AFM simulation are available in the 'Python Scripts' folder. For more lightweight code the simulator can be run from separate python kernal/notebook by importing the AFM_ABAQUS_Simulation_Code.py file (the ABAQUS scripts will need to be copied into the working directory (localPath) specified in simulator).

Importing Python files:
===================================

Within a seperate python script the simulator code can be imported by either appending the package using system command and path to directory holding the files:

.. code-block:: python

    import sys
    sys.path.insert(1, 'C:\\path\\to\\directory\\abqsims') 
    
Or by either copying the abqsims package to the same directory or to the main python path (for jupyter notebook/spyder this will be main anaconda directory). Packages can be imported in various ways importing as:

.. code-block:: python

    import abqsims

    abqsims.afm.AFMSimulation(...)
    abqsims.wave.WaveSimulation(...)
    abqsims.hemisphere.HemisphereSimulation(...)

Alternative:

.. code-block:: python

    from abqsims import *

    afm.AFMSimulation(...)
    wave.WaveSimulation(...)
    hemisphere.HemisphereSimulation(...)

Alternative (can have conflicting functions do not do for all as shown):

.. code-block:: python

    from abqsims.afm import *
    from abqsims.wave import *
    from abqsims.hemisphere import *
    
    AFMSimulation(...) 
    WaveSimulation(...) 
    HemisphereSimulation(...)

Then, the simulator can simply be run by defining the required variables and running main function:

.. code-block:: python

        host, port, username, password, None, localPath, abqCommand, fileName, subData,              
        pdb, rotation, surfaceApprox, indentorType, rIndentor, theta_degrees, tip_length,             
        indentionDepth, forceRef, contrast, binSize, clearance, meshSurface, meshBase, meshIndentor,   
        timePeriod, timeInterval = ...
        
         ...AFMSimulation(host, port, username, password, None, localPath, abqCommand, fileName, subData,
        pdb, rotation, surfaceApprox, indentorType, rIndentor, theta_degrees, tip_length,
        indentionDepth, forceRef, contrast, binSize, clearance, meshSurface, meshBase, meshIndentor,
        timePeriod, timeInterval)

.. toctree::
   :maxdepth: 2
   :caption: Axisymmetric Simulation

   Axisymmetric-Simulation/Axisymmetric_sphere

.. toctree::
   :caption: Hemisphere Simulation
   :glob:

   Hemisphere-Simulation/index

.. toctree::
   :caption: Periodic Wave Simulation
   :glob:

   Wave-Simulation/index
  
.. toctree::
   :caption: AFM Image Simulation
   :glob:

   AFM-Simulation/index


Common Errors
===================================
 * ABAQUS scripts/ package files not located in working directory or system path
 * Some modules may require Python 3.9 or newer. 
 * You must be careful to change path syntaax if using mac or linux.
 * Require the following modules: py3Dmol, nglview, biopython, mendeleev, pyabaqus==2022, paramiko



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`