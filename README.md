<div align="center">

<img src="traj-converter-logo.jpg" alt="Scheme" width="950">
</div>

# 1- Introduction 

<p align="justify"> To analyze biomolecular simulations effectively, it is necessary to generate trajectories lasting hundreds of nanoseconds. The widely used LAMMPS simulation package produces trajectories in the <i>.lammpstrj</i> format, which can be quite large, sometimes reaching tens of gigabytes. To conserve storage space, there are two potential approaches: </p>

<div align ="justify">
<ol>
  <li> reducing the total number of frames by reading the trajectory every N frames; </li>
  <li> converting the trajectory to the .xtc format, a compressed format that is typically used by the GROMACS molecular dynamics package and is about 8 times lighter than the LAMMPSTRJ format.</li>
</ol>
</div>

<p align="justify"> However, no tool currently available allows for the manipulation of <i>.lammptrj</i> trajectories without the support of other software packages such as VMD and GROMACS. Indeed, the former reads this format, can also reduce the total number of frames; however, it saves trajectories in <i>.trr</i> format. Finally, the conversion from <i>.trr</i> to <i>.xtc</i> is possible with GROMACS. It is clear that the entire process is easy but cumbersome, as it requires two softwares.</p>

<b>trajectory-converter tool makes it easy to convert between trajectories and/or reduce the total number of frames in the trajectory.</b>

<p align="justify"> When used correctly, the program outputs the same trajectory in XTC format, regardless of the input format. The <i>.lammpstrj</i> format is one of the best choices for input trajectory because of its large size: indeed, the conversion in XTC format reduces noticeably its size. The XTC format has at least two advantages over other formats:</p>

<div align ="justify">
<ul>
  <li> It is easily read by VMD, Chimera, and other molecular visualization programs; </li>
  <li> The XTC format is compressed and lighter than any other existing trajectory format. </li>
</ul>
</div>

<br />

# 2- Requirements
<div align ="justify">
<ul>  
  <li> <b><code>Python3</code></b>: it is a powerful interpreted, object-oriented, and high-level programming language known for its dynamic semantics. It is highly recommended to use Python 3.7 or 3.9 as they are the most suitable versions. If you're working on a <i>Linux</i> or <i>macOS</i> system, Python 3 should already be installed. However, if you're using Windows, the presence of Python 3 is not guaranteed. To install Python 3, you can follow the installation guide provided <a href="https://docs.python-guide.org/starting/installation/">here</a>. Please ensure that you are working with Python 3 (preferably 3.7 or 3.9) as executing the code with Python 2 may result in errors or unexpected behavior. </li><br/>

  <li> <a href="https://www.mdanalysis.org", target="_blank"> <b><code>MDAnalysis</code></b></a>: It is an open source Python library that helps to quickly write your own analysis algorithm for studying trajectories produced by the most popular simulation packages. To install the lastest stable release with conda do:
     <pre><code>
     conda config --add channels conda-forge
     conda install mdanalysis
     </code></pre>
     On the other hand, to install the latest stable release with pip or pip3 (which should be available in all Python installations) do:
     <pre><code>
     pip3 install --upgrade MDAnalysis 
     </code></pre>
     Any other information can be found <a href="https://www.mdanalysis.org/pages/installation_quick_start/">here</a>.
  </li>
</ul>
</div>
   
<br/>
  
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

