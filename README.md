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

  <li> <a href="https://www.mdanalysis.org"><b><code>MDAnalysis</code></b></a>: It is an open source Python library that helps to quickly write your own analysis algorithm for studying trajectories produced by the most popular simulation packages. To install the lastest stable release with conda do:
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

<p align="justify"> The typical usage of the program involves calling the <b>trajectory-converter.py</b> code using Python 3. This code is designed to convert a trajectory from any format to the <i>XTC</i> format. The conversion from <i>LAMMPSTRJ</i> to <i>XTC</i> is particularly useful as the <i>XTC</i> format is approximately 8 times <i>lighter</i> than LAMMPSTRJ. Additionally, the code also allows for reducing the number of frames in the input trajectory. 

<p align="justify"> The script requires two mandatory files: the coordinates file or the topology of the all-atom structure of the biomolecule (<i>gro, pdb, xyz</i>, etc.), and the trajectory file in any format (<i>lammpstrj, dcd, trr</i>, etc.). There are also two optional arguments: </p>

<div align ="justify">
<ul>  
<li> </p> <i><code>SelectAtoms</code></i>: It is a string that specifies the atoms from the trajectory to be converted to <i>XTC</i>. The default value is <b>all</b>, which includes all atoms. Alternatively, you can specify <b>'name CA'</b> to only consider the Carbon alpha (C<sub>α</sub>) atoms. A complete list of possible strings can be found in the <a href="https://docs.mdanalysis.org/stable/documentation_pages/selections.html">MDAnalysis</a> documentation. </li> <br>

<li> <i><code>Step</code></i>: It is an integer number. When set, the 'Step' option allows for reducing the total number of frames in the input trajectory. The default value is 1, which means <b>all</b> frames are read. However, if an integer number <i>X</i> between 1 and the total number of frames is provided, the input trajectory is read every <i>X</i> steps. </li> <br>

</ul>
</div>

<div align ="justify"> In order to launch the <b>trajectory-converter.py**</b> scripts, the command-line is the following: </p>

```sh
python3 trajectory-conversion.py -r <Coordinate FILE> -t <Trajectory FILE> [-a <SelectAtoms>] [-s <step>] 

   or:

python3 trajectory-conversion.py --ref <Coordinate FILE> --traj <Trajectory FILE> [--atoms <SelectAtoms>] [--step <step>] 
```

<p align="justify"> The output of the program is the new trajectory in format xtc (and with a reduces number of frames if <code>-s/--step [INT]</code> is set). For further information, please type on terminal <code>python3 trajectory-conversion.py</code> or <code>python3 trajectory-conversion.py -h</code>. </p>

<p align="justify"> Before running the python scripts, read carefully the next section that provides a detailed explaination of each argument.</p>

<br />

# 4- Arguments 

<p align="justify"> As shown in <a href="#3--usage"><b>Section 3</b></a> the coordinate/topology file of all-atom structure of the biomolecule (<i>gro, pdb, xyz</i>,...) and the trajectory file that requires a format conversion and/or reduction of frames, are always mandatory. Moreover, the string specifying which atoms of trajectory will be token in account (<i><code>SelectAtoms</code></i>), and the the number corresponding at how often the trajectory will be read (<i><code>Step</code></i>) are optional. A short explaination of the above mentioned files is the following: </p>

<div align ="justify">
<ul>  
  <li> <b><code>Coordinate FILE</code></b>: Mandatory File (<code>-r/--ref</code>) containing the atom coordinates of the biomolecule (<i>xyz, gro, pdb, psf</i>, ..., formats are accepted). </li> <br>

  <li> <b><code>Trajectory FILE</code></b>: Mandatory File (<code>-t/--traj</code>) containing the trajectory of the biomolecule containing the atom coordinates of the biomolecule (<i>trr, dcd, lammpstrj</i>,..., formats are accepted.) </li> <br>

  <li> <b><code>SelectAtoms</code></b>: Optional string (<code>-a/--atoms</code>) that specifies the atoms of trajectory that will be converted from any format to xtc. The default value is <b>'all'</b> (<b>-a/--atoms all</b>) that means that all the atoms will be token in account. Another choice could be <b>-a 'name CA'</b> where only the C-alpha atoms will be considered. <b>Be careful, because if the string is made up of more than one word separated by spaces the latter must be written between apex. </b> For instance: 
  <ul>
   <br> <li> <code> -a name CA   </code>   -->  IT DOES NOT WORK (<b>name CA</b> has two words: it requires apex) </li>
    <li> <code> -a 'name CA' </code> --> IT WORKS </li>
    <li> <code> -a 'all'     </code>     --> IT WORKS </li>
    <li> <code> -a all       </code>       --> IT WORKS (<b>all</b> has one word: not require apex) </li>
  </ul>
  <br> The complete list of possible string can be found in <a href="https://docs.mdanalysis.org/stable/documentation_pages/selections.html">MDAnalysis</a> </li> <br>

  <li> <b><code> Step </code></b>: Optional integer number (<code>-s/--step</code>)whose scope is to reduce the number of frames of input trajectory. The default value is <b>1</b>, that is all frames are read. On the other hand, if an integer number <i>X</i> between 1 and the total number of frames is set, than the trajectory is read every <i>X</i> frames.</li>

</ul>
</div>

<br />

# 5- Examples 

<p align="justify"> Hereafter, for the sake of clarity, six examples are reported. Read them carefully </p> 

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

Raffaele (Elio) Fiorentini: raffaele.fiorentini@unitn.it or elio.fiorentini90@gmail.com

