# Simulations Notebooks

There are four different simulations; simulations implement ABAQUS (2017) software for quasi-static, implicit computations using user subroutines UMAT. Samples are modelled as continuous, homogeneous and isotropic elastic materials with Young's modulus and Poisson ratio comparable to biomolecules. To eliminate the hourglass effect, R3D10 tetrahedral elements are employed.  Simulations impliment "surface to surface contact" interaction with "hard", nonadhesive normal contact and "rough" (Coulomb friction), non-slip tangential contact. Boundary conditions fix the base of the structures, and vertical force and indentation data are mapped and sampled via reference points at the indenter's centre.

Example notebooks are availabel for : 

* Axisymmetric Simulation of Indentation of Elastic Sphere (axisymmetric) 
* Three Dimensional Simulation of Compression along scanline of a Hemisphere (hemisphere)
* Three Dimensional Simulation of Compression along scanline of a Periodic Structure (wave)
* AFM Image Simulator (afm)

Also available are some C++ scripts for hard sphere calculations (cpp-calculations)