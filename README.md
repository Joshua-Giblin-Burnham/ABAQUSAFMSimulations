# ABAQUS AFM Simulations
## Introduction
Repository for Masters project code simulating AFM imaging using ABAQUS/FEM and various FEM simulations. 

View documentation here, https://abaqus-afm-simulations.readthedocs.io/en/latest/index.html .

There are four different simulations; simulations implement ABAQUS (2017) software for quasi-static, implicit computations using user subroutines UMAT. Samples are modelled as continuous, homogeneous and isotropic elastic materials with Young's modulus and Poisson ratio comparable to biomolecules. To eliminate the hourglass effect, R3D10 tetrahedral elements are employed.  Simulations impliment "surface to surface contact" interaction with "hard", nonadhesive normal contact and "rough" (Coulomb friction), non-slip tangential contact. Boundary conditions fix the base of the structures, and vertical force and indentation data are mapped and sampled via reference points at the indenter's centre.

The shape of a blunt AFM tip is a simplified construct similar to the SEM image of actual AFM tips shown by Chen et al. The tip is modelled as a rigid (incompressible) cone with opening angle $\theta = 20^o$ ending in a spherical termination of radius. The spherical portion smoothly transitions to the conical segment at the tangential contact point described by,

$$ X_{tangent} = R\cos\theta ; Y_{tangent} = R(1-\sin\theta)$$

### Axisymmetric Simulation of Indentation of Elastic Sphere 
<p align="center">
   <img width="460" height="300" src="https://github.com/Joshua-Giblin-Burnham/ABAQUS-AFM-Simulations/blob/main/docs/_images/Double%20Contact%20AFM%20tip-1.png">
</p>

Applying ABAQUS to AFM indentation into elastic spheres of varying radii provides a robust validation of simulation accuracy through comparison with the theoretical contact models. Following the common experimental determination of Young modulus, theoretical contact models are used to fit the Young modulus for simulated indentation force curves of elastic spheres. The elastic sphere moves freely with a fixed, rigid base beneath. Restricting indentation to the z-axis allows the modelling to be asymmetrically centred around the z-axis.

### Three Dimensional Simulation of Compression along scanline of a Hemisphere 
<p align="center">
   <img width="360" height="300" src="https://github.com/Joshua-Giblin-Burnham/ABAQUS-AFM-Simulations/blob/main/docs/_images/Hemisphere-Setup-Manuscript-1.png">
</p>

To establish how AFM measures the topography and nanomechanics of simple geometries, we probed imaging of elastic hemispheres. Simulations focused on the perceived compression of the structure's central scanline. The spherical/cylindrical structures model the two-dimensional compression of DNA imaging along the transverse axis The hemisphere is modelled as a three-dimensional elastic part in ABAQUS with a fixed, rigid base beneath. Unlike the indentation of a full sphere with a single contact point at the base, the fixed base of a hemisphere alleviates the compression of the surface. 

### Three Dimensional Simulation of Compression along scanline of a Periodic Structure 
<p align="center">
   <img width="360" height="300" src="https://github.com/Joshua-Giblin-Burnham/ABAQUS-AFM-Simulations/blob/main/docs/_images/Wave-SetUp-Manuscript-1.png">
</p>

AFM resolution is commonly indicated by reference to structures that are at least locally periodic, for example, in atomic resolution mapping at a solid-liquid interface, in identification of recurrent features in a two-dimensional lattice of membrane proteins, or the distinction of the two strands of the double helix along a DNA molecule. Therefore, we considered AFM measurements on a periodic soft material where simulations focused on the compression produced from a single scan along the centre axis of the structures. As shown above, the structure has a wavelength $\lambda = 10nm$ and amplitude, $A_{Sample} = 10nm $. 

### AFM Image Simulator
<p align="center">
   <img width="650" height="300" src="https://github.com/Joshua-Giblin-Burnham/ABAQUS-AFM-Simulations/blob/main/docs/_images/ScanPositions%20diagram-1.png">
</p>
    
Simulating AFM images requires the calculation of contours of constant indentation force across a sample. Using Finite Element Modelling (FEM), the sample surface and probe tip geometry are recreated, and AFM raster scan dynamics are replicated by performing independent indentations across the surface. Biological structures are produced using Protein Data Bank (PDB) files with geometric dimensions in Angstroms. For simplicity, the biomolecule is modelled as an elastic material produced from the assembly of the individual atoms (with van der Waals radius). The molecule is partially embedded in a rigid base/ substrate and fixed at its base to simulate a soft molecule absorbed onto a solid support. The structure is assumed to be a continuous, homogeneous and isotropy elastic material. 

Scan positions are determined by subdividing the XY domain and calculating corresponding initial indenter heights. Initial heights are computed from hard-sphere/ tangential contact points, ensuring consistent indentation depths across the surface. The tangent points between the surfaces are calculated by setting the tip above the sample and determining the minimum vertical distance between the tip and the molecule's surface. Above illustrates the calculations. By computing the vertical distances between the indenter's surface and atoms within the indenter's boundary ($R_{Boundary}$), an array of height differences ($\Delta Z$) is obtained. As illustrated the minimum $\Delta Z$ value corresponds to the tangential contact position. % Only positions where the tip and molecule interact are included for computational efficiency.

Extracting simulated vertical forces and displacements produces a four-dimensional array of indenter positions and forces. Subsequently, contours are computed using a reference force, generating the final AFM images. Contours are calculated from force-indentation data via list comprehension, extracting the depth at which the indentation force exceeds a given reference force. Linear or power normalisation is applied depending on detail contrast, and images are interpolated using bi-cubic interpolation to increase pixel density.

## Running Simulator
<p align="center">
   <img width="650" height="300" src="https://github.com/Joshua-Giblin-Burnham/ABAQUS-AFM-Simulations/blob/main/docs/_images/AFM Simulation Code Flow chart.png">
</p>
The code calculates scan variables and export them to csv files then runs ABAQUS using seperate python scripts that import the variable data. ABAQUS can be run locally, however, they are designed to be run on remote servers, using SSH to upload files and run ABAQUS on HPC queues. Cloning the git page and pip installing 'abqsims' will add all packages/ modules to your python enviroment. All Jupyter notebooks(.ipynb) are self contained, they produce the input files, in the specified local working directory, for each simulation so best run from own self contained directory. The notebooks contain breakdown and description of code function. For more lightweight code the simulator can be run from separate python kernal/notebook by importing the abqsims module in a python file as show in the 'simulation-notebooks/afm/SimulationInterface.py' file (the ABAQUS scripts will need to be copied into the working directory (localPath) specified in simulator).

### Importing Python files
Within a seperate python script the simulator code can be imported by either appending the package using system command and path to directory holding the files:

    import sys
    sys.path.insert(1, 'C:\\path\\to\\directory\\abqsims') 
    
Or by either copying the abqsims package to the same directory or to the main python path (for jupyter notebook/spyder this will be main anaconda directory). Packages can be imported in various ways importing as:

     import abqsims

     abqsims.afm.AFMSimulation(...)
     abqsims.wave.WaveSimulation(...)
     abqsims.hemisphere.HemisphereSimulation(...)

Alternative:

     from abqsims import *

     afm.AFMSimulation(...)
     wave.WaveSimulation(...)
     hemisphere.HemisphereSimulation(...)

Alternative (can have conflicting functions do not do for all as shown):

     from abqsims.afm import *
     from abqsims.wave import *
     from abqsims.hemisphere import *
     
     AFMSimulation(...) 
     WaveSimulation(...) 
     HemisphereSimulation(...)

Then, the simulator can simply be run by defining the required variables and running main function:

      host, port, username, password, None, localPath, abqCommand, fileName, subData,              
      pdb, rotation, surfaceApprox, indentorType, rIndentor, theta_degrees, tip_length,             
      indentionDepth, forceRef, contrast, binSize, clearance, meshSurface, meshBase, meshIndentor,   
      timePeriod, timeInterval = ...
           
      ...AFMSimulation(host, port, username, password, None, localPath, abqCommand, fileName, subData, 
      pdb, rotation, surfaceApprox, indentorType, rIndentor, theta_degrees, tip_length,
      indentionDepth, forceRef, contrast, binSize, clearance, meshSurface, meshBase, meshIndentor,
      timePeriod, timeInterval)

## Common errors:
- ABAQUS scripts/ package files not located in working directory or system path
- Some modules may require Python 3.9 or newer. 
- You must be careful to change path syntaax if using mac or linux.
- Require the following modules: py3Dmol, nglview, biopython, mendeleev, pyabaqus==2022, paramiko

