# 1- Introduction 

Simulations of biomolecules that last hundreds of nanoseconds are required to produce trajectories that can be analyzed later. In particular, the LAMMPS simulation package generates trajectories in the _.lammpstrj_ format, which are generally quite large (in some cases, tens of gigabytes are possible). In order to free up storage space, there are two possible approaches:

1. reducing the total number of frames by reading the trajectory every N frames; 
2. converting the trajectory to the .xtc format, a compressed format that is typically used by the GROMACS molecular dynamics package and is about 8 times lighter than the LAMMPSTRJ format.

However, no tool currently available allows for the manipulation of _.lammptrj_ trajectories without the support of other software packages such as VMD and GROMACS. Indeed, the former reads this format, can also reduce the total number of frames; however, it saves trajectories in _.trr_ format. Finally, the conversion from _.trr_ to _.xtc_ is possible with GROMACS. It is clear that the entire process is easy but cumbersome, as it requires two softwares. 


**This tool makes it easy to convert between trajectories and/or reduce the total number of frames in the trajectory.**

When used correctly, the program outputs the same trajectory in XTC format, regardless of the input format. The _.lammpstrj_ format is one of the best choices for input trajectory because of its large size: indeed, the conversion in XTC format reduces noticeably its size. The XTC format has at least two advantages over other formats:

* It is easily read by VMD, Chimera, and other molecular visualization programs; 
* The XTC format is compressed and lighter than any other existing trajectory format.

<br />

# 2- Requirements

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

# 3- Usage 
 
The typical usage of the program consists in a call to _trajectory-conversion.py_ code by using Python3. 
This code has the scope of converting a trajectory between any format to xtc one. In particular, it could be very useful 
to transform _LAMMPSTRJ_ format to _XTC_ because the latter is about 8 times _slighter_ than the former. Moreover, 
this code has a second purpose of reducing the number of frames of the input trajectory. 

This script requires two mandatory files: the coordinates file or the topology of all-atom structure of the biomolecule (_`gro, pdb, xyz,...`_) and the trajectory file in any format (_`lammpstrj, dcd, trr, ...`_) On the other hand, two arguments are optional: 

* _`SelectAtoms`_: it is a string that specifies the atoms of trajectory that will be converted from any format to xtc.
                 the default value is 'all' that means **all** the atoms will be token in account. 
                 Another choice could be `name CA` where only the C-alpha atoms will be considered.
                 The complete list of possible string can be found in [MDAnalysis documentation](https://docs.mdanalysis.org/stable/documentation_pages/selections.html)
                 
* _`Step`_: It is an integer number. If set, 'Step' option allows to reduce the total number of frames of input trajectory.
The dafult value is 1, that is **all** the frames are read. On the other hand, if an integer number _X_ between 1 and the total number of frames
is set, the input trajectory is read every _X_ steps. 

In order to launch the **trajectory-conversion.py** scripts, the command-line is the following:

```sh
python3 trajectory-conversion.py -r <Coordinate FILE> -t <Trajectory FILE> [-a <SelectAtoms>] [-s <step>] 

   or:

python3 trajectory-conversion.py --ref <Coordinate FILE> --traj <Trajectory FILE> [--atoms <SelectAtoms>] [--step <step>] 
```

The output of the program is the new trajectory in format xtc (and with a reduces number of frames if -s/--step [INT] is set). For further information, please type on terminal `python3 trajectory-conversion.py` or `python3 trajectory-conversion.py -h`. 

Before running the python scripts, read carefully the next section that provides a detailed explaination of each argument.

<br />

# 4- Arguments 

As shown in **Sec. 3** the coordinate/topology file of all-atom structure of the biomolecule (_`gro, pdb, xyz,...`_) and the trajectory file that requires a format conversion and/or reduction of frames, are always mandatory. Moreover, the string specifying which atoms of trajectory will be token in account (_`SelectAtoms`_), and the the number corresponding at how often the trajectory will be read (_`Step`_) are optional. A short explaination of the above mentioned files is the following:

* **`Coordinate FILE`**: Mandatory File of atom Coordinates (xyz, gro, pdb, psf, ..., formats are accepted). 

* **`Trajectory FILE`**: Mandatory File containing the trajectory of the biomolecule (trr, dcd, lammpstrj,..., formats are accepted.)

* **`SelectAtoms`**: Optional string that specifies the atoms of trajectory that will be converted from any format to xtc. The default value is 'all' [-a/--atoms all] that means that all the atoms will be token in account. Another choice could be -a 'name CA' where only the C-alpha atoms will be considered. Be careful, because if the string is made up of more than one word separated by spaces the latter must be written between apex. 
Example: 
  * -a name CA   --> IT DOES NOT WORK (*name CA* has two words: it requires apex)
  * -a 'name CA' --> IT WORKS
  * -a 'all'     --> IT WORKS
  * -a all       --> IT WORKS (*all* has one word: not require apex)
The complete list of possible string can be found in [MDAnalysis documentation](https://docs.mdanalysis.org/stable/documentation_pages/selections.html)

* **`Step`**: Optional integer number whose scope is to reduce the number of frames of input trajectory. The default value is **1**, that is all frames are read. On the other hand, if an integer number _X_ between 1 and the total number of frames is set, than the trajectory is read every _X_ frames.


<br />

# 5- Examples 

Hereafter, for the sake of clarity, six examples are reported. Read them carefully. 

```perl
# *Example 1* : Transforming lammpstrj trajectory in xtc (all frames and all atoms are read)
#
#             o input_trajectory  =  protein.lammpstrj 
#             o coordinate_file   =  protein.gro
#             o frames_read       =  all (default value, thus it does not require -s/--step <INT> flag)
#             o atoms selected    =  all (default value, thus it does not require -a/--atoms <STR> flag) 
#             o output_trajectory =  Trajectory.xtc   

python3 trajectory-conversion.py -r protein.gro -t protein.lammpstrj 
```
  
```perl
# *Example 2* : Transforming dcd trajectory in xtc (all frames and all atoms are read) 
#
#             o input_trajectory  =  protein.dcd
#             o coordinate_file   =  protein.pdb
#             o frames_read       =  all (default value, thus it does not require -s/--step <INT> flag)
#             o atoms selected    =  all (default value, thus it does not require -a/--atoms <STR> flag) 
#             o output_trajectory =  Trajectory.xtc   

python3 trajectory-conversion.py -r protein.pdb -t protein.dcd
```
  
```perl
# *Example 3* : Transforming lammpstrj trajectory in xtc (all frames are read, whereas only C-alpha atoms and hydrogens are token in account)
#  
#             o input_trajectory  =  protein.lammpstrj 
#             o coordinate_file   =  protein.gro
#             o frames_read       =  all (default value, thus it does not require -s/--step <INT> flag)
#             o atoms selected    =  only C-alpha atoms and hydrogens (it requires -a/--atoms 'name CA and type H' flag) 
#             o output_trajectory =  Trajectory.xtc   

python3 trajectory-conversion.py -r protein.gro -t protein.lammpstrj -a 'name CA and type H'
```

  
```perl
# *Example 4* : Transforming lammpstrj trajectory in xtc (the trajectory will be read every 10 frames, whereas all atoms are token in account) 
#
#             o input_trajectory  =  protein.lammpstrj 
#             o  coordinate_file  =  protein.gro
#             o  frames_read      =  every 10 (thus it requires -s/--step 10 flag)
#             o  atoms selected   =  all (default value, thus it does not requires -a/--atoms <STR> flag) 
#             o output_trajectory =  Trajectory.xtc   

python3 trajectory-conversion.py -r protein.gro -t protein.lammpstrj -s 10 
```
  
```perl
# *Example 5* : Transforming lammpstrj trajectory in xtc (the trajectory will be read every 20 frames, whereas only hydrogen atoms are token in account) 
#
#             o input_trajectory  =  protein.lammpstrj 
#             o coordinate_file   =  protein.gro
#             o frames_read       =  every 20 (thus it requires -s/--step 20 flag)
#             o atoms selected    =  only hydrogens (thus it requires -a/--atoms 'type H' flag) 
#             o output_trajectory =  Trajectory.xtc   

python3 trajectory-conversion.py -r protein.gro -t protein.lammpstrj -s 10 -a 'type H' 
```
  
```perl
# *Example 6* : Trasforming xtc trajectory reading it every 50 frames (all atoms are token in account) 
#
#             o input_trajectory  =  protein.xtc
#             o coordinate_file   =  protein.gro
#             o frames_read       =  every 50 (thus it requires -s/--step 20 flag)
#             o atoms selected    =  all (default value, thus it does not requires -a/--atoms <STR> flag)
#             o output_trajectory =  Trajectory.xtc   

python3 trajectory-conversion.py -r protein.gro -t protein.xtc -s 50 
```

<br />

# 6 - Contacts 

Raffaele (Elio) Fiorentini: elio.fiorentini90@gmail.it

