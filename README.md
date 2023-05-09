# Introduction
This tool allows to make conversion between trajectories and/or to reduce the total number of frames of the trajectory itself.

In particular, it could be very useful to trasform from .lammpstrj format to .xtc one. The reason lies in the fact that 
an XTC file, is a compressed trajectory format used by the GROMACS molecular dynamics package, about 8 times _lighther_ than LAMMPSTRJ one. 

If using this code correctly, starting from LAMMPSTRJ trajectory, the program returns in output the same trajectory in XTC format.
Other starting trajectory format are feasible, whereas the output trajectory format is always XTC because is easily read by VMD, Chimera, 
and any other molecular visualization program. Moreover, and more important, the XTC format has a compressed format and _lighther_ than 
any other existing trajectory format. 

<br />

# Requirements

* **`Python3`**: it is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
  The installation guide is provided [Here](https://docs.python-guide.org/starting/installation/). 
  If you are working on _Linux_ or _MacOs_ system, Python3 should be already installed. 
  On the other hand, if you are using Windows operating system, it is not certain for its presence.
  Please, be care of working with Python3 (3.7 or 3.9 is the best choice) as the code could return an error if using Python2.

* **`MDAnalysis`**: It is an open source Python library that helps you to quickly write your own analysis algorithm for studying trajectories produced by the most popular simulation packages. To install the lastest stable release with conda do:

   ```bash
   conda config --add channels conda-forge
   conda install mdanalysis
   ```
   
   On the other hand, to install the latest stable release with pip or pip3 (which should be available in all Python installations) do:

   ```bash
   pip3 install --upgrade MDAnalysis
   ```
   
   Any other information can be found [Here](https://www.mdanalysis.org/pages/installation_quick_start/).
   
<br />

# Usage 
 
The typical usage of the program consists in a call to _trajectories-conversion.py_ code by using Python3. 
This code has the scope of converting trajectories between any format to xtc one. In particular, it could be very useful 
to transform LAMMPSTRJ format to XTC because the latter is about 8 times _slighter_ than the former. Moreover, 
this code has a second purpose of reducing the number of frames of the input trajectory. 

This script requires two mandatory files: the coordinates file or the topology of all-atom structure of the biomolecule (_`gro, pdb, xyz,...`_) and the trajectory file in any format (_`lammpstrj, dcd, trr, ...`_) On the other hand, two arguments are optional: 

* _`SelectAtoms`_: it is a string that specifies the atoms of trajectory that will be converted from any format to xtc.
                 the default value is 'all' that means **all** the atoms will be token in account. 
                 Another choice could be `name CA` where only the C-alpha atoms will be considered.
                 The complete list of possible string can be found in [MDAnalysis documentation](https://docs.mdanalysis.org/stable/documentation_pages/selections.html)
                 
* _`Step`_: It is an integer number. If set, 'Step' option allows to reduce the total number of frames of input trajectory.
The dafult value is 1, that is **all** the frames are read. On the other hand, if an integer number _X_ between 1 and the total number of frames
is set, the input trajectory is read every _X_ steps. 

In order to launch the **trajectories-conversion.py** scripts, the command-line is the following:

```sh
python3 trajectories-conversion.py -r <Coordinate FILE> -t <Trajectory FILE> [-a <SelectAtoms>] [-s <step>] 

   or:

python3 trajectories-conversion.py --ref <Coordinate FILE> --traj <Trajectory FILE> [--atoms <SelectAtoms>] [--step <step>] 
```

Before running the python scripts, read carefully the next section that provides a detailed explaination of each argument.

<br />

## Arguments 

As shown in **Sec. XX** the coordinate/topology file of all-atom structure of the biomolecule (_`gro, pdb, xyz,...`_) and the trajectory file that requires a format conversion and/or reduction of frames, are always mandatory. Moreover, the string specifying which atoms of trajectory will be token in account (_`SelectAtoms`_), and the the number correspodning at how often the trajectory will be read (_`Step`_) are optional. A short explaination of the above mentioned files is the following:
