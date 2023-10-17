.. abqsims documentation master file, created by
   sphinx-quickstart on Fri Oct 13 14:16:53 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ABQSIMS Documentation
===================================

Repository for Masters project code simulating AFM imaging using ABAQUS/FEM and various FEM simulations. There are four different simulations.

Simulations implement ABAQUS (2017) software for quasi-static, implicit computations using user subroutines UMAT. Samples are modelled as continuous, homogeneous and isotropic elastic materials with Young's modulus and Poisson ratio comparable to biomolecules. To eliminate the hourglass effect, R3D10 tetrahedral elements are employed.  Simulations impliment "surface to surface contact" interaction with "hard", nonadhesive normal contact and "rough" (Coulomb friction), non-slip tangential contact. Boundary conditions fix the base of the structures, and vertical force and indentation data are mapped and sampled via reference points at the indenter's centre.

The shape of a blunt AFM tip is a simplified construct similar to the SEM image of actual AFM tips shown by Chen et al. The tip is modelled as a rigid (incompressible) cone with opening angle \theta ending in a spherical termination of radius. The spherical portion smoothly transitions to the conical segment at the tangential contact point described by,

.. math:: X_{tangent} = R\cos\theta ; Y_{tangent} = R(1-\sin\theta)

.. toctree::
   :maxdepth: 2
   :caption: Axisymmetric Simulation of Indentation of Elastic Sphere

   misc/Axisymmetric-sphere

.. toctree::
   :caption: Three Dimensional Simulation of Compression along scanline of a Hemisphere
   :glob:

   Hemisphere-Simulation/index

.. toctree::
   :caption: Three Dimensional Simulation of Compression along scanline of a Periodic Structure 
   :glob:

   Wave-Simulation/index
  
.. toctree::
   :caption: AFM Image Simulator
   :glob:

   AFM-Simulation/index
 

.. toctree::
   :maxdepth: 2
   :caption:  Running Simulator

      misc/Running-simulator

.. toctree::
   :maxdepth: 2
   :caption:  Common errors:

      misc/Common-errors


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`