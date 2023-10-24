abqsims.afm.PDB
-------------------------------
.. code-block:: python 
    
    abqsims.afm.PDB(pdbid, localPath, **kwargs)

This function imports the relevant PDB file (and takes care of the directory) in which it is saved etc for the user, returning the structure and the view using a widget.

    Parameters:
        pdbid (str) - PDB (or CSV) file name of desired biomolecule
        
        kwargs:
            CustomPDB - Extract data from local custom pd as opposed to from PDB online
        
    Returns:
        structure (class) - Class containing proteins structural data (Atom coords/positions and masses etc...)
        
        view (class)      - Class for visualising the protein

    

abqsims.afm.TipStructure
-------------------------------
.. code-block:: python 
    
    abqsims.afm.TipStructure(rIndentor, theta_degrees, tip_length) 

Produce list of tip structural parameters. Change principle angle to radian. Calculate tangent point where sphere smoothly transitions to cone for capped conical indentor.

    Parameters:
        theta_degrees (float) - Principle conical angle from z axis in degrees
        
        rIndentor (float)     - Radius of spherical tip portion
        
        tip_length (float)    - Total cone height
        
    Returns:
        tipDims (list) - Geometric parameters for defining capped tip structure     

    

abqsims.afm.Zconical
-------------------------------
.. code-block:: python 
    
    abqsims.afm.Zconical(r, r0, r_int, z_int, theta, R, tip_length)

Calculates and returns spherically capped conical tip surface heights from radial  position r. Uses radial coordinate along xy plane from centre as tip is axisymmetric around z axis (bottom of tip set as zero point such z0 = R).

    Parameters:
        r (float/1D arr)   - xy radial coordinate location for tip height to be found
        
        r0 (float)         - xy radial coordinate for centre of tip
        
        r_int (float)      - xy radial coordinate of tangent point (point where sphere smoothly transitions to cone)
        
        z_int (float)      - Height of tangent point, where sphere smoothly transitions to cone (defined for tip centred at spheres center, as calculations assume tip centred at indentors bottom the value must be corrected to, R-z_int) 
        
        theta (float)      - Principle conical angle from z axis in radians
        
        R (float)          - Radius of spherical tip portion
        
        tip_length (float) - Total cone height
        
    Returns:
        Z (float/1D arr)- Height of tip at xy radial coordinate 

    
abqsims.afm.Zspherical
-------------------------------
.. code-block:: python 
    
    abqsims.afm.Zspherical(r, r0, r_int, z_int, theta, R, tip_length)

Calculates and returns spherical tip surface heights from radial  position r. Uses radial coordinate along xy plane from centre as tip is axisymmetric around z axis (bottom of tip set as zero point such z0 = R).

    Parameters:
        r (float/1D arr)   - xy radial coordinate location for tip height to be found
        
        r0 (float)         - xy radial coordinate for centre of tip
        
        r_int (float)      - xy radial coordinate for tangent point (point where sphere smoothly transitions to cone)
        
        z_int (float)      - Height of tangent point (point where sphere smoothly transitions to cone)
        
        theta (float)      - Principle conical angle from z axis in radians
        
        R (float)          - Radius of spherical tip portion
        
        tip_length (float) - Total cone height
        
    Returns:
        Z (float/1D arr)- Height of tip at xy radial coordinate 

    

abqsims.afm.Rotate
-------------------------------
.. code-block:: python 
    
    abqsims.afm.Rotate(domain, rotation)

Rotate coordinates of a domain around each coordinate axis by angles given.

    Parameters:
        domain (arr)    - Array of [x,y,z] coordinates in domain to be rotated (Shape: (3) or (N,3) )
        
        rotation (list) - Array of [xtheta, ytheta, ztheta] rotational angle around coordinate axis:
                            
                            xtheta(float), angle in degrees for rotation around x axis (Row)
                            
                            ytheta(float), angle in degrees for rotation around y axis (Pitch)
                            
                            ztheta(float), angle in degrees for rotation around z axis (Yaw)
    Returns:
            rotate_domain(arr) - Rotated coordinate array


    
abqsims.afm.MolecularStructure
-------------------------------
.. code-block:: python 
    
    abqsims.afm.MolecularStructure(structure, rotation, tipDims, indentorType, binSize, surfaceApprox)
 
Extracts molecular data from structure class and returns array of molecules atomic coordinate and element names. Alongside, producing dictionary of element radii and calculating base dimensions. All distances given in Angstroms (x10-10 m).

    Parameters:
        structure (class)     - Class containing proteins structural data (Atom coords/positions and masses etc...)
        
        rotation (list)       - Array of [x,y,z] rotational angle around coordinate axis'
        
        tipDims (list)        - Geometric parameters for defining capped tip structure     
        
        indentorType (str)    - String defining indentor type (Spherical or Capped)
        
        binSize (float)       - Width of bins that subdivid xy domain during raster scanning/ spacing of the positions sampled over
        
        surfaceApprox (float) - Percentage of biomolecule assumed to be not imbedded in base/ substrate. Range: 0-1 
    
    Returns:
        atom_coord (arr)      - Array of coordinates [x,y,z] for atoms in biomolecule 
        
        atom_element (arr)    - Array of elements names(str) for atoms in biomolecule 
        
        atom_radius (dict)    - Dictionary containing van der waals radii each the element in the biomolecule 
        
        surfaceHeight (float) - Maximum height of biomolecule in z direction
        
        baseDims (arr)        - Geometric parameters for defining base/ substrate structure [width, height, depth]           

    

abqsims.afm.ScanGeometry
-------------------------------
.. code-block:: python 
    
    abqsims.afm.ScanGeometry(atom_coord, atom_radius, atom_element, indentorType, tipDims, baseDims, surfaceHeight, binSize, clearance)
 
Produces array of scan locations and corresponding heights/ tip positions above surface in Angstroms (x10-10 m). Also return an array including only positions where tip interact with the sample. The scan positions are produced creating a rectangular grid over bases extent with widths bin size.Heightss, at each position, are calculated by set tip above sample and calculating vertical distance between of tip and molecules surface over the indnenters area. Subsequently, the minimum vertical distance corresponds to the position where tip is tangential.

    Parameters:
        atom_coord (arr)      - Array of coordinates [x,y,z] for atoms in biomolecule 
        
        atom_radius (dict)    - Dictionary containing van der waals radii each the element in the biomolecule 
        
        atom_element (arr)    - Array of elements names(str) for atoms in biomolecule 
        
        indentorType (str)    - String defining indentor type (Spherical or Capped)
        
        tipDims (list)        - Geometric parameters for defining capped tip structure     
        
        baseDims (arr)        - Geometric parameters for defining base/ substrate structure [width, height, depth] 
        
        surfaceHeight (float) - Maximum height of biomolecule in z direction
        
        binSize (float)       - Width of bins that subdivid xy domain during raster scanning/ spacing of the positions sampled over
        
        clearance (float)     - Clearance above molecules surface indentor is set to during scan
        
    Returns:
        scanPos (arr)         - Array of coordinates [x,y,z] of scan positions to image biomolecule and initial heights/ hard sphere boundary
        
        clipped_scanPos (arr) - Array of clipped (containing only positions where tip and molecule interact) scan positions and initial heights [x,y,z] to image biomolecule

    

abqsims.afm.DotPlot
-------------------------------
.. code-block:: python 
    
    abqsims.afm.DotPlot(atom_coord, atom_radius, atom_element, scanPos, clipped_scanPos, pdb, **kwargs)
 
Plot the molecules atoms surfaces and scan positions to visualise and check positions.

    Parameters:
        atom_coord (arr)        - Array of coordinates [x,y,z] for atoms in biomolecule 
        
        atom_radius (dict)      - Dictionary containing van der waals radii each the element in the biomolecule 
        
        atom_element (arr)      - Array of elements names(str) for atoms in biomolecule 
        
        scanPos (arr)           - Array of coordinates [x,y,z] of scan positions to image biomolecule and initial heights/ hard sphere boundary
        
        clipped_scanPos (arr)   - Array of clipped (containing only positions where tip and molecule interact) scan positions and initial heights [x,y,z] to image biomolecule
        
        pdb (str)               - PDB (or CSV) file name of desired biomolecule
        
        kwargs: 
                    SaveImages (str)  - If Contour images to be saved include kwarg specifying the file path to folder

    

abqsims.afm.ExportVariables
-------------------------------
.. code-block:: python 
    
    abqsims.afm.ExportVariables(atom_coord, atom_element, atom_radius, clipped_scanPos, scanPos, variables, baseDims, tipDims, indentorType)
 
Export simulation variables as csv and txt files to load in abaqus python scripts.

    Parameters:
        atom_coord (arr)      - Array of coordinates [x,y,z] for atoms in biomolecule 
        
        atom_element (arr)    - Array of elements names(str) for atoms in biomolecule 
        
        atom_radius (dict)    - Dictionary containing van der waals radii each the element in the biomolecule 
        
        clipped_scanPos (arr) - Array of clipped (containing only positions where tip and molecule interact) scan positions and initial heights [x,y,z] to image biomolecule            
        
        scanPos (arr)         - Array of coordinates [x,y,z] of scan positions to image biomolecule and initial heights/ hard sphere boundary
        
        variables (list)      - List of simulation variables: [timePeriod, timeInterval, binSize, meshSurface, meshBase, meshIndentor, indentionDepth, surfaceHeight]
        
        baseDims (arr)        - Geometric parameters for defining base/ substrate structure [width, height, depth] 
        
        tipDims (list)        - Geometric parameters for defining capped tip structure     
        
        indentorType (str)    - String defining indentor type (Spherical or Capped)



abqsims.afm.ImportVariables
-------------------------------
.. code-block:: python 
    
    abqsims.afm.ImportVariables()

Import simulation geometry variables from csv files.

    Return:
        atom_coord (arr)        - Array of coordinates [x,y,z] for atoms in biomolecule 
        
        atom_element (arr)      - Array of elements names(str) for atoms in biomolecule 
        
        atom_radius (dict)      - Dictionary containing van der waals radii each the element in the biomolecule 
        
        variables (list)        - List of simulation variables: [timePeriod, timeInterval, binSize, meshSurface, meshBase, meshIndentor, indentionDepth, surfaceHeight]
        
        baseDims (arr)          - Geometric parameters for defining base/ substrate structure [width, height, depth]             
        
        scanPos (arr)           - Array of coordinates [x,y,z] of scan positions to image biomolecule and initial heights/ hard sphere boundary
        
        clipped_scanPos (arr)   - Array of clipped (containing only positions where tip and molecule interact) scan positions and initial heights [x,y,z] to image biomolecule

    

abqsims.afm.RemoteSCPFiles
-------------------------------
.. code-block:: python 
    
    abqsims.afm.RemoteSCPFiles(host, port, username, password, files, remotePath)
    
Function to make directory and transfer files to SSH server. A new Channel is opened and the files are transfered. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        files (str/list) - File or list of file to transfer
        
        remotePath (str) - Path to remote file/directory

    

abqsims.afm.RemoteCommand
-------------------------------
.. code-block:: python 
    
    abqsims.afm.RemoteCommand(host, port, username, password, script, remotePath, command)

Function to execute a command/ script submission on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        script (str)     - Script to run via bash command 
        
        remotePath (str) - Path to remote file/directory
        
        command (str)    - Abaqus command to execute and run script

    

abqsims.afm.BatchSubmission
-------------------------------
.. code-block:: python 
    
    abqsims.afm.BatchSubmission(host, port, username, password, fileName, subData, scanPos, remotePath, **kwargs)
 
Function to create bash script for batch submission of input file, and run them on remote server.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        fileName (str)   - Base File name for abaqus input files
        
        subData (str)    - Data for submission to serve queue [walltime, memory, cpus]
        
        scanPos (arr)    - Array of coordinates [x,y] of scan positions to image biomolecule (can be clipped or full) 
        
        remotePath (str) - Path to remote file/directory
        
        kwargs:
            Submission ('serial'/ 'paralell') - optional define whether single serial script or seperate paralell submission to queue {Default: 'serial'}  

    

abqsims.afm.QueueCompletion
-------------------------------
.. code-block:: python 
    
    abqsims.afm.QueueCompletion(host, port, username, password)

Function to check queue statis and complete when queue is empty.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.

    

abqsims.afm.RemoteFTPFiles
-------------------------------
.. code-block:: python 
    
    abqsims.afm.RemoteFTPFiles(host, port, username, password, files, remotePath, localPath)
 
Function to transfer files from directory on SSH server to local machine. A new Channel is opened and the files are transfered. The function uses FTP file transfer.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        files (str )     - File to transfer
        
        remotePath (str) - Path to remote file/directory
        
        localPath (str)  - Path to local file/directory

    

abqsims.afm.Remote_Terminal
-------------------------------
.. code-block:: python 
    
    abqsims.afm.Remote_Terminal(host, port, username, password)
    
Function to emulate cluster terminal. Channel is opened and commands given are executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.

    Parameters:
        host (str)       - Hostname of the server to connect to
        
        port (int)       – Server port to connect to 
        
        username (str)   – username to authenticate as (defaults to the current local username)        -  
        
        password (str)   - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.

    
    
abqsims.afm.LocalSubmission
-------------------------------
.. code-block:: python 
    
    abqsims.afm.LocalSubmission()

 Submit Abaqus scripts locally
    

abqsims.afm.RemoteSubmission
-------------------------------
.. code-block:: python 
    
    abqsims.afm.RemoteSubmission(host, port, username, password, remotePath, localPath,  csvfiles, abqfiles, abqCommand, fileName, subData, clipped_scanPos, **kwargs)

Function to run simulation and scripts on the remote servers. Files for variables are transfered, ABAQUS scripts are run to create parts and input files. A bash file is created and submitted to run simulation for batch of inputs. Analysis of odb files is performed and data transfered back to local machine.Using keyword arguments invidual parts of simulation previously completed can be skipped.

    Parameters:
        host (str)              - Hostname of the server to connect to
        
        port (int)              – Server port to connect to 
        
        username (str)          – Username to authenticate as (defaults to the current local username)        -  
        
        password (str)          - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        remotePath (str)        - Path to remote file/directory
        
        localPath (str)         - Path to local file/directory
        
        csvfiles (list)         - List of csv and txt files to transfer to remote server
        
        abqfiles (list)         - List of abaqus script files to transfer to remote server
        
        abqCommand (str)        - Abaqus command to execute and run script
        
        fileName (str)          - Base File name for abaqus input files
        
        subData (str)           - Data for submission to serve queue [walltime, memory, cpus]
        
        clipped_scanPos (arr)   - Array of clipped (containing only positions where tip and molecule interact) scan positions and  initial heights [x,y,z] to image biomolecule    
        
        kwargs:
            submission ('serial'/ 'paralell') - Type of submission, submit pararlell scripts or single serial script for scan locations {Default: 'serial'}
            
            Transfer (bool)                   - If false skip file transfer step of simulation {Default: True}
            
            Part (bool)                       - If false skip part creation step of simulation {Default: True}
            
            Input (bool)                      - If false skip input file creation step of simulation {Default: True}
            
            Batch (bool)                      - If false skip batch submission step of simulation {Default: True}
            
            Queue (bool)                      - If false skip queue completion step of simulation {Default: True}
            
            Analysis (bool)                   - If false skip odb analysis step of simulation {Default: True}
            
            Retrieval (bool)                  - If false skip data file retrivial from remote serve {Default: True}



abqsims.afm.DataProcessing
-------------------------------
.. code-block:: python 
    
    abqsims.afm.DataProcessing(clipped_RF, clipped_U2, scanPos, clipped_scanPos, clipped_ErrorMask, indentionDepth, timePeriod, timeInterval)   

Function to load variables from files in current directory and process data from simulation in U2/RF files. Process data from clipped scan positionsto include full data range over all scan positions.
    
    Parameters:
        clipped_RF              - Array of indentors z displacement over clipped scan position
        
        clipped_U2              - Array of reaction force on indentor reference point over clipped scan positions
        
        scanPos (arr)           - Array of coordinates [x,y,z] of scan positions to image biomolecule and initial heights/ hard sphere boundary
        
        clipped_scanPos (arr)   - Array of clipped (containing only positions where tip and molecule interact) scan positions and initial heights [x,y,z] to image biomolecule
        
        clipped_ErrorMask (arr) - Boolean array specifying mask for clipped scan positions which errored in ABAQUS
        
        indentionDepth (float)  - Maximum indentation depth into surface 
        
        timePeriod(float)       - Total time length for ABAQUS simulation/ time step (T)
        
        timeInterval(float)     - Time steps data sampled over for ABAQUS simulation/ time step (dt)
        
    Return:
        U2 (arr)        - Array of indentors z displacement over scan position
        
        RF (arr)        - Array of reaction force on indentor reference point
        
        ErrorMask (arr) - Boolean array specifying mask for all scan positions which errored in ABAQUS
        
        N (int)         - Number of frames in ABAQUS simulation/ time step  



abqsims.afm.DataPlot
-------------------------------
.. code-block:: python 
    
    abqsims.afm.DataPlot(scanPos, U2, RF, N)
 
Produces scatter plot of indentation depth and reaction force to visualise and check simulation data.

    Parameters:
        scanPos (arr) - Array of coordinates [x,y] of scan positions to image biomolecule 
        
        U2 (arr)      - Array of indentors z displacement over scan position
        
        RF (arr)      - Array of reaction force on indentor reference point
        
        N (int)       - Number of frames in  ABAQUS simulation/ time step 


abqsims.afm.ForceContours
-------------------------------
.. code-block:: python 
    
    abqsims.afm.ForceContours(U2, RF,forceRef, scanPos, baseDims, binSize)
 
Function to calculate contours/z heights of constant force in simulation data for given threshold force.

    Parameters:
        U2 (arr)         - Array of indentors z displacement over scan position
        
        RF (arr)         - Array of reaction force on indentor reference point
        
        forceRef (float) - Threshold force to evaluate indentation contours at (pN)
        
        scanPos (arr)    - Array of coordinates [x,y,z] of scan positions to image biomolecule 
        
        baseDims (arr)   - Geometric parameters for defining base/ substrate structure [width, height, depth]           
        
        binSize (float)  - Width of bins that subdivid xy domain during raster scanning/ spacing of the positions sampled over
        
    Return:
        X (arr) - 2D array of x coordinates over grid positions 
        
        Y (arr) - 2D array of y coordinates over grid positions 
        
        Z (arr) - 2D array of z coordinates of force contour over grid positions  


abqsims.afm.ContourPlot
-------------------------------
.. code-block:: python 
    
    abqsims.afm.ContourPlot(X, Y, Z, ErrorMask, baseDims, binSize, forceRef, contrast, pdb, **kwargs)
 
Function to plot force contor produced from simulation. Plots 3D wire frame image and a 2D AFM image.

    Parameters:          
        X (arr)          - 2D array of x coordinates over grid positions 
        
        Y (arr)          - 2D array of y coordinates over grid positions 
        
        Z (arr)          - 2D array of z coordinates of force contour over grid positions 
        
        ErrorMask (arr)  - Boolean array specifying mask for all scan positions which errored in ABAQUS
        
        baseDims (arr)   - Geometric parameters for defining base/ substrate structure [width, height, depth]
        
        binSize (float)  - Width of bins that subdivid xy domain during raster scanning/ spacing of the positions sampled over
        
        forceRef (float) - Threshold force to evaluate indentation contours at (pN)
        
        contrast (float) - Contrast between high and low values in AFM heat map (0-1)
        
        pdb (str)        - PDB (or CSV) file name of desired biomolecule
        
    kwargs:
        Noise (list)         - If listed adds noise to AFM images [strength, mean, standard deviation]
        
        ImagePadding (float) - Black space / padding around image as percentage of dimensions of molecule extent
        
        SaveImages (str)     - If Contour images to be saved include kwarg specifying the file path to folder


abqsims.afm.HardSphereAFM
-------------------------------
.. code-block:: python 
    
    abqsims.afm.HardSphereAFM(scanPos, baseDims, binSize, clearance, contrast,  pdb, **kwargs)
 
Plot the molecules atoms surfaces and scan positions to visualise and check positions.

    Parameters:
        scanPos (arr)      - Array of coordinates [x,y,z] of scan positions to image biomolecule and initial heights/ hard sphere boundary
        
        baseDims (arr)     - Geometric parameters for defining base/ substrate structure [width, height, depth] 
        
        binSize (float)    - Width of bins that subdivid xy domain during raster scanning/ spacing of the positions sampled over
        
        clearance (float)  - Clearance above molecules surface indentor is set to during scan
        
        contrast (float)   - Contrast between high and low values in AFM heat map (0-1)  
        
        pdb (str)          - PDB (or CSV) file name of desired biomolecule
    
    kwargs:
        Noise (list)         - If listed adds noise to AFM images [strength, mean, standard deviation]
        
        ImagePadding (float) - Black space / padding around image as percentage of dimensions of molecule extent
        
        SaveImages (str)     - If Contour images to be saved include kwarg specifying the file path to folder
  

abqsims.afm.AFMSimulation
-------------------------------
.. code-block:: python 
    
    abqsims.afm.AFMSimulation(host, port, username, password, remotePath, localPath, abqCommand, fileName, subData, 
                    pdb, rotation, surfaceApprox, indentorType, rIndentor, theta_degrees, tip_length, 
                    indentionDepth, forceRef, contrast, binSize, clearance, meshSurface, meshBase, meshIndentor, 
                    timePeriod, timeInterval, **kwargs)

Final function to automate simulation. User inputs all variables and all results are outputted. The user gets a optionally get a surface plot of scan positions. Produces a heatmap of the AFM image, and 3D plots of the sample surface for given force threshold.

    Parameters:
        host (str)             - Hostname of the server to connect to
        
        port (int)             - Server port to connect to 
        
        username (str)         - Username to authenticate as (defaults to the current local username)        -  
        
        password (str)         - password (str) – Used for password authentication; is also used for private key decryption if passphrase is not given.
        
        remotePath (str)       - Path to remote file/directory
        
        localPath (str)        - Path to local file/directory
        
        abqCommand (str)       - Abaqus command to execute and run script
        
        fileName (str)         - Base File name for abaqus input files
        
        subData (list)         - Data for submission to serve queue [walltime, memory, cpus]
        
        pdb (str)              - PDB (or CSV) file name of desired biomolecule
        
        rotation (list)        - Array of [xtheta, ytheta, ztheta] rotational angle around coordinate axis'
        
        surfaceApprox (float)  - Percentage of biomolecule assumed to be not imbedded in base/ substrate. Range: 0-1 
        
        indentorType (str)     - String defining indentor type (Spherical or Capped)
        
        rIndentor (float)      - Radius of spherical tip portion
        
        theta_degrees (float)  - Principle conical angle from z axis in degrees
        
        tip_length (float)     - Total cone height
        
        indentionDepth (float) - Maximum indentation depth into surface 
        
        forceRef (float)       - Threshold force to evaluate indentation contours at, mimics feedback force in AFM (pN)
        
        contrast (float)       - Contrast between high and low values in AFM heat map (0-1)
        
        binSize(float)         - Width of bins that subdivid xy domain during raster scanning/ spacing of the positions sampled over
        
        clearance(type:float)  - Clearance above molecules surface indentor is set to during scan
        
        meshSurface (float)    - Value of indentor mesh given as bin size for vertices of geometry in Angstrom (x10-10 m)
        
        meshBase (float)       - Value of indentor mesh given as bin size for vertices of geometry in Angstrom (x10-10 m)
        
        meshIndentor (float)   - Value of indentor mesh given as bin size for vertices of geometry in Angstrom (x10-10 m) 
        
        timePeriod(float)      - Total time length for ABAQUS simulation/ time step (T)
        
        timeInterval(float)    - Time steps data sampled over for ABAQUS simulation/ time step (dt)
        
        kwargs:
            Submission ('serial'/ 'paralell') - Type of submission, submit pararlell scripts or single serial script for scan locations {Default: 'serial'}
            
            CustomPDB - Extract data from local custom pd as opposed to from PDB online
            
            Preprocess (bool)  - If false skip preprocessing step of simulation {Default: True}
            
            DotPlot (bool)     - If false skip surface plot of biomolecule and scan positions {Default: False}
            
            HSPlot (bool)      - If false skip Hard Sphere AFM plot of biomolecule {Default: False}
            
            MoleculeView(bool) - If false skip interactive sphere model of biomolecule {Default: False}
            
            Transfer (bool)    - If false skip file transfer step of simulation {Default: True}
            
            Part (bool)        - If false skip part creation step of simulation {Default: True}
            
            Input (bool)       - If false skip input file creation step of simulation {Default: True}
            
            Batch (bool)       - If false skip batch submission step of simulation {Default: True}
            
            Queue (bool)       - If false skip queue completion step of simulation {Default: True}
            
            Analysis (bool)    - If false skip odb analysis step of simulation {Default: True}
            
            Retrieval (bool)   - If false skip data file retrivial from remote serve {Default: True}
            
            Postprocess (bool) - If false skip postprocessing step to produce AFM image from data {Default: True}
            
            DataPlot (bool)    - If false skip scatter plot of simulation data {Default: True} 
            
            ReturnData (bool)  - If true returns simulation data to analysis {Default: False} 
            
            Noise (list)         - If listed adds noise to AFM images [strength, mean, standard deviation]
            
            imagePadding (float) - Black space / padding around image as percentage of dimensions of molecule extent
            
            SaveImages (str)     - If Contour images to be saved include kwarg specifying the file path to folder