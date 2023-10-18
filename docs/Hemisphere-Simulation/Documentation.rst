abqsims.hemisphere.TipStructure
-------------------------------
.. code-block:: python 
    
    abqsims.hemisphere.TipStructure(rIndentor, theta_degrees, tip_length)

Produce list of tip structural parameters. Change principle angle to radian. Calculate tangent point where sphere smoothly transitions to cone for capped conical indentor.

    Parameters:
        theta_degrees (float) - Principle conical angle from z axis in degrees
        
        rIndentor (float)     - Radius of spherical tip portion
        
        tip_length (float)    - Total cone height
        
    Returns:
        tipDims (list) - Geometric parameters for defining capped tip structure     


abqsims.hemisphere.Fconical
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.Fconical(r, r0, r_int, z_int, theta, R, tip_length)

Calculates and returns spherically capped conical tip surface heights from radial  position r. Uses radial coordinate along xz plane from centre as tip is axisymmetric around z axis (bottom of tip set as zero point such z0 = R).

    Parameters:
        r (float/1D arr)   - xz radial coordinate location for tip height to be found
        
        r0 (float)         - xz radial coordinate for centre of tip
        
        r_int (float)      - xz radial coordinate of tangent point (point where sphere smoothly transitions to cone)
        
        z_int (float)      - Height of tangent point, where sphere smoothly transitions to cone (defined for tip centred at spheres center, as calculations assume tip centred at indentors bottom the value must be corrected to, R-z_int) 
        
        theta (float)      - Principle conical angle from z axis in radians
        
        R (float)          - Radius of spherical tip portion
        
        tip_length (float) - Total cone height
        
    Returns:
        Z (float/1D arr)- Height of tip at xz radial coordinate 


abqsims.hemisphere.F_TipConvolution
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.F_TipConvolution(x, rSurface, rIndentor)
    
Function to calculate hard sphere tip convolution of tip and semi-sphere using mathematics above


abqsims.hemisphere.ScanGeometry
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ScanGeometry(indentorType, tipDims, baseDims, rSurface, Nb, clearance)

Produces array of scan locations and corresponding heights/ tip positions above surface in Angstroms (x10-10 m).The scan positions are produced creating a straight line along the centre of the surface with positions spaced by the bin size. Heights, at each position, are calculated for conical indentor by set tip above sample and calculating vertical distance between of tip and molecules surface over the indnenters area. Subsequently, the minimum vertical distance corresponds to the position where tip is tangential. Spherical indentors are calculated explicitly.

    Parameters:
        indentorType (str) - String defining indentor type (Spherical or Capped)
        
        tipDims (list)     - Geometric parameters for defining capped tip structure     
        
        baseDims (list)    - Geometric parameters for defining base/ substrate structure [width, height, depth] 
        
        rSurface (float)   - Radius of semi-sphere surface
        
        Nb (int)           - Number of scan positions along x axis of base
        
        clearance (float)  - Clearance above molecules surface indentor is set to during scan
        
    Returns:
        rackPos (arr) - Array of coordinates [x,z] of scan positions to image biomolecule 



abqsims.hemisphere.ExportVariables
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ExportVariables(rackPos, variables, baseDims, tipDims, indentorType, elasticProperties )

Export simulation variables as csv and txt files to load in abaqus python scripts.

    Parameters:
        rackPos (arr)           - Array of coordinates [x,z] of scan positions to image biomolecule 
        
        variables (list)        - List of simulation variables: [timePeriod, timeInterval, binSize, meshSurface, meshBase, meshIndentor, indentionDepth, surfaceHeight]
        
        baseDims (list)         - Geometric parameters for defining base/ substrate structure [width, height, depth] 
        
        tipDims (list)          - Geometric parameters for defining capped tip structure     
        
        indentorType (str)      - String defining indentor type (Spherical or Capped)
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]



abqsims.hemisphere.ImportVariables
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ImportVariables()

Import simulation geometry variables from csv files.

    Return:
        variables (list)        - List of simulation variables: [timePeriod, timeInterval, binSize, meshSurface, meshBase, meshIndentor, indentionDepth, surfaceHeight]
        
        baseDims (list)         - Geometric parameters for defining base/ substrate structure [width, height, depth]             
        
        rackPos (arr)           - Array of coordinates [x,z] of scan positions to image biomolecule  



abqsims.hemisphere.RemoteSCPFiles
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.RemoteSCPFiles(host, port, username, password, files, remotePath)

Function to make directory and transfer files to SSH server. A new Channel is opened and the files are transfered. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.
    
    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        files (str/list) - File or list of file to transfer
        
        remotePath (str) - Path to remote file/directory


abqsims.hemisphere.RemoteCommand
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.RemoteCommand(host, port, username, password, script, remotePath, command)
    
Function to execute a command/ script submission on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        script (str)     - Script to run via bash command 
        
        remotePath (str) - Path to remote file/directory
        
        command (str)    - Abaqus command to execute and run script
    
    
abqsims.hemisphere.BatchSubmission
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.BatchSubmission(host, port, username, password, fileName, subData, rackPos, remotePath, **kwargs)

Function to create bash script for batch submission of input file, and run them on remote server.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        fileName (str)   - Base File name for abaqus input files
        
        subData (str)    - Data for submission to serve queue [walltime, memory, cpus]
        
        rackPos (arr)    - Array of coordinates [x,z] of scan positions to image biomolecule (can be clipped or full) 
        
        remotePath (str) - Path to remote file/directory
        
        kwargs:
            Submission ('serial'/ 'paralell') - optional define whether single serial script or seperate paralell submission to queue {Default: 'serial'}  


abqsims.hemisphere.QueueCompletion
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.QueueCompletion(host, port, username, password)

Function to check queue statis and complete when queue is empty.

    Parameters:
        host (str)     - Hostname of the server to connect to
        
        port (int)     – Server port to connect to 
        
        username (str) – username to authenticate as (defaults to the current local username)        -  
        
        password (str) - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.



abqsims.hemisphere.RemoteFTPFiles
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.RemoteFTPFiles(host, port, username, password, files, remotePath, localPath)

Function to transfer files from directory on SSH server to local machine. A new Channel is opened and the files are transfered. The function uses FTP file transfer.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        files (str )     - File to transfer
        
        remotePath (str) - Path to remote file/directory
        
        localPath (str)  - Path to local file/directory



abqsims.hemisphere.Remote_Terminal
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.Remote_Terminal(host, port, username, password)

Function to emulate cluster terminal. Channel is opened and commands given are executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.



abqsims.hemisphere.RemoteSubmission
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.RemoteSubmission(host, port, username, password, remotePath, localPath,  csvfiles, abqfiles, abqCommand, fileName, subData, rackPos, **kwargs)

Function to run simulation and scripts on the remote servers. Files for variables are transfered, ABAQUS scripts are run to create parts and input files. A bash file is created and submitted to run simulation for batch of inputs. Analysis of odb files is performed and data transfered back to local machine. Using keyword arguments can submitt the submission files in parrallel.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – Username to authenticate as (defaults to the current local username)        
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        remotePath (str) - Path to remote file/directory
        
        localPath (str)  - Path to local file/directory
        
        csvfiles (list)  - List of csv and txt files to transfer to remote server
        
        abqfiles (list)  - List of abaqus script files to transfer to remote server
        
        abqCommand (str) - Abaqus command to execute and run script
        
        fileName (str)   - Base File name for abaqus input files
        
        subData (str)    - Data for submission to serve queue [walltime, memory, cpus]
        
        rackPos (arr)    - Array of scan positions and initial heights [x,z] to image 
        
        kwargs           - Passes "Submmission" if present to batchSubmission function 
             


abqsims.hemisphere.DataRetrieval
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.DataRetrieval(host, port, username, password, scratch, wrkDir, localPath, csvfiles, dataFiles, indentorRadius, **kwargs)

Function to retrieve simulation data transfered back to local machine. Using keyword arguments to change to compilation of simulations data.

    Parameters:
        host (str)           - Hostname of the server to connect to
        
        port (int)           – Server port to connect to 
        
        username (str)       – Username to authenticate as (defaults to the current local username)        -  
        
        password (str)       - Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        remotePath (str)     - Path to remote file/directory
        
        localPath (str)      - Path to local file/directory
        
        csvfiles (list)      - List of csv and txt files to transfer to remote server
        
        datafiles (list)     - List of abaqus script files to transfer to remote server
        
        indentorRadius (arr) - Array of indentor radii of spherical tip portion varied for seperate  simulations
        
        kwargs:
            Compile(int)     - If passed, simulation data is compiled from seperate sets of simulations in directory in remote server to combine complete indentations. Value is set as int representing the range of directories to compile from (directories must have same root naming convention with int denoting individual directories)
                                
    Return:
        variables (list) - List of simulation variables: [timePeriod, timeInterval, binSize, meshSurface, meshIndentor, indentionDepth, surfaceHeight]
        
        TotalU2 (arr)    - Array of indentors z displacement in time over scan position and  for all indenter [Ni, Nb, Nt]
        
        TotalRF (arr)    - Array of reaction force in time on indentor reference point over scan position  and for all indenter [Ni, Nb, Nt]
        
        NrackPos (arr)   - Array of initial scan positions for each indenter [Ni, Nb, [x, z] ]    
    


abqsims.hemisphere.ForceGrid2D
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ForceGrid2D(X, Z, U2, RF, rackPos, courseGrain, **kwargs)

Function to produce force heat map over scan domain.

    Parameters:
        X (arr)             - 1D array of postions over x domain of scan positions
        
        Z (arr)             - 1D array of postions over z domain of scan positions, discretised into bins of courseGrain value
        
        U2 (arr)            - Array of indentors y indentor position over scan, discretised into bins of courseGrain value ( As opposed to displacement into surface given from simulation and used elsewhere)
        
        RF (arr)            - Array of reaction force on indentor reference point
        
        rackPos (arr)       - Array of coordinates (x,z) of scan positions to image biomolecule [Nb,[x,z]]
        
        courseGrain (float) - Width of bins that subdivid xz domain of raster scanning/ spacing of the positions sampled over

        kwargs:
            Symmetric - If false skip postprocessing step to produce AFM image from data {Default: True}
    
    Return:
        forceGrid (arr)        - 2D Array of force heatmap over xz domain of scan i.e. grid of xz positions with associated force [Nx,Nz] 
        
        forceGridmask (arr)    - 2D boolean array giving mask for force grid with exclude postions with no indentation data [Nx,Nz] 
        
        forceContour (arr)     - 2D Array of coordinates for contours of constant force given by reference force across scan positons 
        
        forceContourmask (arr) - 2D boolean array giving mask for force contour for zero values in which no reference force 
 


abqsims.hemisphere.ForceContour2D
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ForceContour2D(U2, RF, rackPos, forceRef, **kwargs)

Function to calculate contours/z heights of constant force in simulation data for given threshold force.

    Parameters:
        U2 (arr)            - Array of indentors y indentor position over scan ( As opposed to displacement into surface given from simulation and used elsewhere)
        
        RF (arr)            - Array of reaction force on indentor reference point
        
        rackPos (arr)       - Array of coordinates (x,z) of scan positions to image biomolecule [Nb,[x,z]]
        
        forceRef (float)    - Threshold force to evaluate indentation contours at (pN)
        
        kwargs:
            Symmetric - If false skip postprocessing step to produce AFM image from data {Default: True}
            
    Return:
        forceContour (arr)     - 2D Array of coordinates for contours of constant force given by reference force across scan positons 
        
        forceContourmask (arr) - 2D boolean array giving mask for force contour for zero values in which no reference force 
    



abqsims.hemisphere.F_Hertz
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.F_Hertz(U, E, rIndentor, rSurface, elasticProperties)
    
Hertzian fit for indentation data 



abqsims.hemisphere.ForceInterpolation
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ForceInterpolation(Xgrid, Zgrid, U2, RF, rackPos, rIndentor, rSurface, elasticProperties, Nt)

Calculate a 2D force heatmap over the xz domain, produced from interpolated forces using Hertz model.

    Parameters:             
        Xgrid (arr)             - 2D array/ grid of postions over xz domain of scan positions
        
        Zgrid (arr)             - 2D array/ grid of postions over xz domain of scan positions       
        
        U2 (arr)                - Array of indentors y displacement in time over scan position and for one indenter [Ni, Nb, Nt]
        
        RF (arr)                - Array of reaction force in time on indentor reference point over scan position  and for one indenter [Nb, Nt]
        
        rackPos (arr)           - Array of initial scan positions for one indenter [Nb, [x, z]] 
        
        rIndentor (float)       - Indentor radius of spherical tip portion varied for seperate  simulations
        
        rSurface (float)        - Radius of semi-sphere surface
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        Nt (int)                - Number of time steps
        
    Return:
        E_hertz (arr)      - Array of fitted elastic modulus value over scan positions for each indentor [Ni,Nb]
        
        F (arr)            - Array of interpolated force values over xz grid for all indentors and reference force [Ni, Nb, Nz] 


abqsims.hemisphere.FWHM_Volume
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.FWHM_Volume(forceContour, NrackPos, Nf, Ni, indentorRadius, rSurface)

Calculate Full Width Half Maxima and Volume for Force Contours of varying reference force using splines

    Parameters:          
        forceContour (arr)      - 2D Array of coordinates for contours of constant force given by reference force across scan positons for all indentor and reference force [Nf,Ni, Nb, [x,z]] (With mask applied).
        
        NrackPos (arr)          - Array of initial scan positions for each indenter [Ni, Nb, [x, z]] 
        
        Nf                      - Number if reference force values
        
        Ni                      - Number if indentor radii/ values
        
        indentorRadius (arr)    - Array of indentor radii of spherical tip portion varied for seperate  simulations
        
        rSurface (float)        - Radius of semi-sphere surface
        
    Return:
        FWHM (arr)         - Array of full width half maxima of force contour for corresponding indentor and reference force [Nf,Ni]
        
        Volume (arr)       - Array of volume under force contour for corresponding indentor and reference force [Nf,Ni]


abqsims.hemisphere.Postprocessing
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.Postprocessing(TotalU2, TotalRF, NrackPos, Nb, Nt, courseGrain, refForces, indentorRadius, baseDims, rSurface, elasticProperties, **kwargs):

Calculate a 2D force heatmap produced from simulation over the xz domain.

    Parameters:          
        TotalU2 (arr)           - Array of indentors y displacement in time over scan position and  for all indenter [Ni, Nb, Nt]
        
        TotalRF (arr)           - Array of reaction force in time on indentor reference point over scan position  and for all indenter [Ni, Nb, Nt]
        
        NrackPos (arr)          - Array of initial scan positions for each indenter [Ni, Nb, [x, z]] 
        
        Nb (int)                - Number of scan positions along x axis of base
        
        Nt (int)                - Number of time steps
        
        courseGrain (float)     - Width of bins that subdivid xz domain of raster scanning/ spacing of the positions sampled over
        
        refForces (arr)         - Array of threshold force to evaluate indentation contours at (pN)
        
        indentorRadius (arr)    - Array of indentor radii of spherical tip portion varied for seperate  simulations
        
        baseDims (list)         - Geometric parameters for defining base/ substrate structure [width, height, depth]
        
        rSurface (float)        - Radius of semi-sphere surface
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
    Return:
        X (arr)            - 1D array of postions over x domain of scan positions
        
        Z (arr)            - 1D array of postions over z domain of scan positions, discretised into bins of courseGrain value
        
        forceGrid (arr)    - 2D Array of force heatmap over xz domain of scan i.e. grid of xz positions with associated force for all indentors and reference force [Nf, Ni, Nb, Nz] (With mask applied). 
        
        forceContour (arr) - 2D Array of coordinates for contours of constant force given by reference force across scan positons for all indentor and reference force [Nf,Ni, Nb, [x,z]] (With mask applied).
        
        FWHM (arr)         - Array of full width half maxima of force contour for corresponding indentor and reference force [Nf,Ni]
        
        Volume (arr)       - Array of volume under force contour for corresponding indentor and reference force [Nf,Ni]
        
        E_hertz (arr)      - Array of fitted elastic modulus value over scan positions for each indentor [Ni,Nb,Nt]
        
        F (arr)            - Array of interpolated force values over xz grid for all indentors and reference force [Ni, Nb, Nz] 





abqsims.hemisphere.HemisphereSimulation
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.HemisphereSimulation(host, port, username, password, scratch, wrkDir, localPath, abqCommand, fileName, subData, 
                  indentorType, indentorRadius, theta_degrees, tip_length, indentionDepths, baseDims, rSurface, 
                  refForces, courseGrain, binSize, clearance, meshSurface, meshIndentor, timePeriod, timeInterval, 
                  elasticProperties, **kwargs)

Final function to automate simulation. User inputs all variables and all results are outputted. The user gets a optionally get a surface plot of scan positions.
Produces a heatmap of the AFM image, and 3D plots of the sample surface for given force threshold.

    Parameters:
        host (str)              - Hostname of the server to connect to
        
        port (int)              - Server port to connect to 
        
        username (str)          - Username to authenticate as (defaults to the current local username)        -  
        
        password (str)          - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        scratch                 - Path to remote scratch directory
        
        wrkDir (str)            - Working directory extension
        
        localPath (str)         - Path to local file/directory
        
        abqCommand (str)        - Abaqus command to execute and run script
        
        fileName (str)          - Base File name for abaqus input files
        
        subData (str)           - Data for submission to serve queue [walltime, memory, cpus]
        
        indentorType (str)      - String defining indentor type (Spherical or Capped)
        
        indentorRadius (arr)    - Array of indentor radii of spherical tip portion varied for seperate  simulations
        
        theta_degrees (float)   - Principle conical angle from z axis in degrees
        
        tip_length (float)      - Total cone height
        
        indentionDepths (arr)   - Array of maximum indentation depth into surface 
        
        baseDims (list)         - Dimension of base
        
        rSurface (float)        - Radius of semi-sphere
        
        refForces (float)       - Threshold force to evaluate indentation contours at, mimics feedback force in AFM (pN)
        
        courseGrain (float)     - Width of bins that subdivid xz domain of raster scanning/ spacing of the positions sampled over
        
        binSize(float)          - Width of bins that subdivid xz domain during raster scanning/ spacing of the positions sampled over
        
        clearance (float)       - Clearance above molecules surface indentor is set to during scan
        
        meshSurface (float)     - Value of indentor mesh given as bin size for vertices of geometry in nm (x10-9 m)
        
        meshIndentor (float)    - Value of indentor mesh given as bin size for vertices of geometry in nm (x10-9 m) 
        
        timePeriod(float)       - Total time length for ABAQUS simulation/ time step (T)
        
        timeInterval(float)     - Time steps data sampled over for ABAQUS simulation/ time step (dt)
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        kwargs:
            Submission ('serial'/ 'paralell') - Type of submission, submit pararlell scripts or single serial script for scan locations {Default: 'serial'}
            
            Main (bool)        - If false skip preprocessing step of simulation {Default: True}
            
            SurfacePlot (bool) - If false skip surface plot of biomolecule and scan positions {Default: True}
            
            Queue (bool)       - If false skip queue completion step of simulation {Default: True}
            
            Analysis (bool)    - If false skip odb analysis step of simulation {Default: True}
            
            Retrieval (bool)   - If false skip data file retrivial from remote serve {Default: True}
            
            Compile(int)       - If passed, simulation data is compiled from seperate sets of simulations in directory in remote server to combine complete indentations. Value is set as int representing the range of directories to compile from (directories must have same root naming convention with int denoting individual directories)                     - 
            
            Postprocess (bool) - If false skip postprocessing step to produce AFM image from data {Default: True}
            
            DataPlot (bool)    - If false skip scatter plot of simulation data {Default: True}
            
            Symmetric          - If false skip postprocessing step to produce AFM image from data {Default: True}
            
    Returns:
        X (arr)            - 1D array of postions over x domain of scan positions, discretised into bins of courseGrain value [Nx]
        
        Z (arr)            - 1D array of postions over z domain of scan positions, discretised into bins of courseGrain value [Nz]
        
        TotalU2 (arr)      - Array of indentors z displacement in time over scan position and  for all indenter [Ni, Nb, Nt]
        
        TotalRF (arr)      - Array of reaction force in time on indentor reference point over scan position  and for all indenter [Ni, Nb, Nt]
        
        NrackPos (arr)     - Array of initial scan positions for each indenter [Ni, Nb, [x, z]] 
        
        forceGrid (arr)    - 2D Array of force heatmap over xz domain of scan i.e. grid of xz positions with associated force [Nx,Nz] (With mask applied). 
        
        forceContour (arr) - 2D Array of coordinates for contours of constant force given by reference force across scan positons (With mask applied).
        
        FWHM (arr)         - Array of full width half maxima of force contour for corresponding indentor and reference force [Nf,Ni]
        
        Volume (arr)       - Array of volume under force contour for corresponding indentor and reference force [Nf,Ni]
        
        E_hertz (arr)      - Array of fitted elastic modulus value over scan positions for each indentor [Ni,Nb]
        
        F (arr)            - Array of interpolated force values over xz grid for all indentors and reference force [Ni, Nb, Nz] 


abqsims.hemisphere.ContourPlotMan
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ContourPlotMan(X, Z, forceGrid, forceContour, indentorRadius, clearance, rSurface, baseDims, theta_degrees, tip_length, binSize, elasticProperties, normalizer, maxRF, contrast, n0, n1, n2)

Function to plot a 2D force heatmap produced from simulation over the xz domain for single indenter and refereance force.

    Parameters:          
        X (arr)                 - 1D array of x coordinates over scan positions 
        
        Z (arr)                 - 1D array of z coordinates over scan positions 
        
        rackPos (arr)           - Array of initial scan positions for indenter [Nb, [x, z] ] 
        
        forceGrid (arr)         - 2D Array of force grid of xz positions 
        
        forceContour( arr)      - 2D Array of coordinates for contours of constant force given by reference force 
        
        indentorRadius (arr)    - Array of indentor radii of spherical tip portion varied for seperate  simulations
        
        clearance(float)        - Clearance above molecules surface indentor is set to during scan
        
        rSurface (float)        - Radius of semi-sphere
        
        baseDims (list)         - Dimension of base
        
        waveDims (list)         - Geometric parameters for defining base/ substrate structure [width, height, depth]
        
        theta_degrees (float)   - Principle conical angle from z axis in degrees
        
        tip_length (float)      - Total cone height
        
        binSize (float)         - Width of bins that subdivid xz domain during raster scanning/ spacing of the positions sampled over
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        normalizer (obj)        - Normalisation of cmap
        
        maxRF (float)           - Maximum Force value
        
        contrast (float)        - Contrast between high and low values in AFM heat map (0-1)


abqsims.hemisphere.SurfacePlot
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.SurfacePlot(rackPos, Nb, baseDims, tipDims, rSurface, binSize, clearance)

Plot the surfaces and scan positions to visualise and check positions. 

    Parameters:
        rackPos (arr)      - Array of coordinates [x,z] of scan positions to image biomolecule  
        
        Nb (int)           - Number of scan positions along x axis of base
        
        baseDims (list)    - Geometric parameters for defining base/ substrate structure [width, height, depth] 
        
        tipDims (list)     - Geometric parameters for defining capped tip structure  
        
        rSurface (float)   - Radius of spherical surface
        
        clearance (float)  - Clearance above molecules surface indentor is set to during scan


abqsims.hemisphere.DataPlot
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.DataPlot(NrackPos, TotalU2, TotalRF, Nb, Nt, n)
 
Produces scatter plot of indentation depth and reaction force to visualise and check simulation data.

    Parameters:
        NrackPos (arr) - Array of initial scan positions for each indenter [Ni, Nb, [x, z] ]              
        
        TotalU2 (arr)  - Array of indentors z displacement in time over scan position and  for all indenter [Ni, Nb, Nt]
        
        TotalRF (arr)  - Array of reaction force in time on indentor reference point over scan position  and for all indenter [Ni, Nb, Nt]
        
        Nb (int)       - Number of scan positions along x axis of base
        
        Nt(int)        - Number of frames in  ABAQUS simulation/ time step 
        
        n (int)        - Index of indenter data to plot corresponding to indices in indenterRadius




abqsims.hemisphere.ContourPlot
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ContourPlot(X, Z, forceGrid, forceContour, refForces, baseDims, tipDims, rSurface, elasticProperties, normalizer, maxRF, contrast)
    
Function to plot a 2D force heatmap produced from simulation over the xz domain for single indenter and refereance force.

    Parameters:          
        X (arr)                 - 1D array of x coordinates over scan positions 
        
        Z (arr)                 - 1D array of z coordinates over scan positions 
        
        forceGrid (arr)         - 2D Array of force grid of xz positions 
        
        forceContour( arr)      - 2D Array of coordinates for contours of constant force given by reference force 
        
        refForces (float)       - Threshold force to evaluate indentation contours at (pN)
        
        baseDims (list)         - Dimension of base
        
        tipDims (list)          - Geometric parameters for defining capped tip structure     
        
        rSurface (float)        - Radius of semi-sphere
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        normalizer (obj)        -  Normalisation of cmap
        
        maxRF (float)           - Maximum Force value
        
        contrast (float)        - Contrast between high and low values in AFM heat map (0-1)
    



abqsims.hemisphere.ContourPlot2
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ContourPlot2(X, Z, forceGrid, forceContour, refForces, baseDims, tipDims, rSurface, elasticProperties, normalizer, maxRF, contrast)
     
Function to plot a 2D force heatmap produced from simulation over the xz domain for single indenter and refereance force.

    Parameters:          
        X (arr)                 - 1D array of x coordinates over scan positions 
        
        Z (arr)                 - 1D array of z coordinates over scan positions 
        
        forceGrid (arr)         - 2D Array of force grid of xz positions 
        
        forceContour( arr)      - 2D Array of coordinates for contours of constant force given by reference force 
        
        refForces (float)       - Threshold force to evaluate indentation contours at (pN)
        
        baseDims (list)         - Dimension of base
        
        tipDims (list)          - Geometric parameters for defining capped tip structure     
        
        rSurface (float)        - Radius of semi-sphere
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        normalizer (obj)        -  Normalisation of cmap
        
        maxRF (float)           - Maximum Force value
        
        contrast (float)        - Contrast between high and low values in AFM heat map (0-1)
    



abqsims.hemisphere.ContourPlotNI
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.ContourPlotNI(X, Z, forceGrid, forceContour, refForces, baseDims, tipDims, rSurface, elasticProperties, normalizer, maxRF, contrast)

Function to plot a 2D force heatmap produced from simulation over the xz domain for single indenter and refereance force.

    Parameters:          
        X (arr)                 - 1D array of x coordinates over scan positions 
        
        Z (arr)                 - 1D array of z coordinates over scan positions 
        
        RF(arr)                 - Array of reaction force on indentor reference point
        
        forceGrid (arr)         - 2D Array of force grid of xz positions 
        
        forceContour( arr)      - 2D Array of coordinates for contours of constant force given by reference force 
        
        refForces (float)       - Threshold force to evaluate indentation contours at (pN)
        
        baseDims (list)         - Dimension of base
        
        tipDims (list)          - Geometric parameters for defining capped tip structure     
        
        rSurface (float)        - Radius of semi-sphere
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        normalizer (obj)        -  Normalisation of cmap
        
        maxRF (float)           - Maximum Force value
        
        contrast (float)        - Contrast between high and low values in AFM heat map (0-1)




abqsims.hemisphere.LineContourPlot
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.LineContourPlot(X, forceContour, refForces, rSurface, tipDims, elasticProperties, normalizer, maxRF, contrast)

Function to plot fitted contour lines produced from simulation over the xz domain for single indenter and  range reference force.Interpolate/none.

    Parameters:          
        X (arr)                 - 1D array of x coordinates over scan positions 
        
        RF(arr)                 - Array of reaction force on indentor reference point
        
        forceContour( arr)      - 2D Array of coordinates for contours of constant force given by reference force 
        
        refForces (float)       - Threshold force to evaluate indentation contours at (pN)
        
        rIndentor (arr)         - Array of indentor radii of spherical tip portion varied for seperate  simulations
        
        rSurface (float)        - Radius of semi-sphere
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        normalizer (obj)        -  Normalisation of cmap
        
        maxRF (float)           - Maximum Force value
        
        contrast (float)        - Contrast between high and low values in AFM heat map (0-1)




abqsims.hemisphere.FInterpolatePlot
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.FInterpolatePlot(X, Z, F, baseDims, tipDims, rSurface, elasticProperties, normalizer, maxRF, contrast)
    
Function to plot a 2D force heatmap produced from simulation over the xz domain for single indenter and refereance force.

    Parameters:          
        X (arr)                 - 1D array of x coordinates over scan positions 
        
        Z (arr)                 - 1D array of z coordinates over scan positions 
        
        F (arr)                 - Array of interpolated force values over xz grid for all indentors and reference force [Ni, Nb, Nz] 
        
        baseDims (list)         - Dimension of base
        
        tipDims (list)          - Geometric parameters for defining capped tip structure     
        
        rSurface (float)        - Radius of semi-sphere
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        normalizer (obj)        - Normalisation of cmap
        
        maxRF (float)           - Maximum Force value
        
        contrast (float)        - Contrast between high and low values in AFM heat map (0-1)




abqsims.hemisphere.FWHMPlot
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.FWHMPlot(FWHM, indentorRadius, refForces, rSurface, elasticProperties)

Function to plot Full Width Half Maxima of force contour for each indentor for varying reference force.

    Parameters:          
        FWHM (arr)              - 2D array of y coordinates over grid positions 
        
        indentorRadius (arr)    - 2D array of z coordinates of force contour over grid positions 
        
        refForces (float)       - Threshold force to evaluate indentation contours at (pN)
        
        rSurface (float)        - Radius of semi-sphere
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]




abqsims.hemisphere.VolumePlot
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.VolumePlot(Volume, indentorRadius, refForces, rSurface, elasticProperties)

Function to plot volume under force contour for each indentor for varying reference force.

    Parameters: 
        Volume (arr)            - Array of volume under force contour for corresponding indentor and reference force [Nf,Ni]
        
        indentorRadius (arr)    - Array of indentor radii of spherical tip portion varied for seperate  simulations
        
        refForces (float)       - Threshold force to evaluate indentation contours at, mimics feedback force in AFM 
        
        rSurface (float)        - Radius of semi-sphere
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]



abqsims.hemisphere.YoungPlot
-------------------------------
.. code-block:: python
    
    abqsims.hemisphere.YoungPlot(E_hertz, TotalRF, indentorRadius, NrackPos, rSurface, elasticProperties, basePos)

Function to plot elastic modulus over scan position for each indentor.

    Parameters:          
        E_hertz (arr)           - Array of fitted elastic modulus value over scan positions for each indentor [Ni,Nb]
        
        TotalRF (arr)           - Array of reaction force in time on indentor reference point over scan position  and for all indenter [Ni, Nb, Nt]
        
        indentorRadius (arr)    - Array of indentor radii of spherical tip portion varied for seperate  simulations
        
        NrackPos (arr)          - Array of initial scan positions for each indenter [Ni, Nb, [x, z]] 
        
        rSurface (float)        - Radius of semi-sphere
        
        elasticProperties (arr) - Array of surface material properties, for elastic surface [Youngs Modulus, Poisson Ratio]
        
        basePos                 - Index of position along scan to consider vatioation in fitted E against force
