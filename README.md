# Trajectory-conversion
This tool allows to make conversion between trajectories and/or to reduce the total number of frames of the trajectory itself.

In particular, it could be very useful to trasform from .lammpstrj format to .xtc one. The reason lies in the fact that 
an XTC file, is a compressed trajectory format used by the GROMACS molecular dynamics package, about 8 times _lighther_ than LAMMPSTRJ one. 

If using this code correctly, starting from LAMMPSTRJ trajectory, the program returns in output the same trajectory in XTC format.
Other starting trajectory format are feasible, whereas the output trajectory format is always XTC because is easily read by VMD, Chimera, 
and any other molecular visualization program. Moreover, and more important, the XTC format has a compressed format and _lighther_ than 
any other existing trajectory format. 


# Requirements

* **`Python3`**: it is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
  The installation guide is provided [Here](https://docs.python-guide.org/starting/installation/). 
  If you are working on _Linux_ or _MacOs_ system, Python3 should be already installed. 
  On the other hand, if you are using Windows operating system, it is not certain for its presence.
  Please, be care of working with Python3 (3.7 or 3.9 is the best choice) as the code could return an error if using Python2.

* **`MDAnalysis`**: It is an open source Python library that helps you to quickly write your own analysis algorithm for studying trajectories produced by the most popular simulation packages. To install the lastest stable release with conda do:

   ```awk
   conda config --add channels conda-forge
   conda install mdanalysis
   ```
   
   On the other hand, to install the latest stable release with pip or pip3 (which should be available in all Python installations) do:

   ```bash
   pip3 install --upgrade MDAnalysis
   ```
