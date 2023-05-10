import MDAnalysis as mda
import sys 
import argparse
import os 

                   ####################
#####################  1. Functions  ####################################
                   ####################

# F.1: it checks if X is Integer or Float (Note that isdigit returns True only if X is Integer) 
def isIntFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
        

# F.2 - It checks if an argument of argparse (that will be treated always as string) is integer, float, or string. The function returns "x" 
def check_Int_Float_Str(x):
    if(isIntFloat(x)):
        try:
            x = int(x)
        except:
            x = float(x)
    return x

# F.3 - It checks if an argument of argparse (that will be treated always as string) is integer, float, or string. The function returns "x" 
def check_Int_Float_Str(x):
    if(isIntFloat(x)):
        try:
            x = int(x)
        except:
            x = float(x)
    return x


# F.4 - It prints the main usage this code 
def print_usage():
    print("Usage: python3 {} -r <Coordinate FILE> -t <Trajectory FILE> [-a <SelectAtoms>] [-s <step>] ".format(sys.argv[0]))
    print("   or: python3 {} --ref <Coordinate FILE> --traj <Trajectory FILE> [--atoms <SelectAtoms>] [--step <step>] ".format(sys.argv[0]))

    print("\nTry python3 {} -h or {} --help for more information.\n".format(sys.argv[0], sys.argv[0]))


# F.5 - It prints the main help of this code 
def print_help():  
    print("Usage: python3 {} -r <Coordinate FILE> -t <Trajectory FILE> [-a <SelectAtoms>] [-s <step>] ".format(sys.argv[0]))
    print("   or: python3 {} --ref <Coordinate FILE> --traj <Trajectory FILE> [--atoms <SelectAtoms>] [--step <step>] ".format(sys.argv[0]))
    
    print("\n-----------------------------------------------------------------------------------------------------")

    print("*{}* requires the following inputs:\n".format(sys.argv[0]))
    print("   Coordinate FILE                MANDATORY          File of atom Coordinates (xyz, gro, pdb, psf, ..., formats are accepted)\n")                                                   
    print("   Trajectory FILE                MANDATORY          File containing the Trajectory of the biomolecule.")
    print("                                                     (trr, dcd,..). lammpstrj format is also accepted.\n")

    print("  [SelectAtoms]                   OPTIONAL           String that specifies the atoms of trajectory")
    print("                                                     that will be converted from any format to xtc.")
    print("                                                     The default value is 'all' [-a/--atoms all]")
    print("                                                     that means that all the atoms will be token in account.")
    print("                                                     Another choice could be -a 'name CA' where only the C-alpha atoms will be considered")
    print("                                                     Be careful, because if the string is made up of more than one word separated by spaces")
    print("                                                     the latter must be written between apex.")
    print("                                                     Example: ● -a name CA   --> IT DOES NOT WORK (*name CA* has two words: it requires apex)")
    print("                                                              ● -a 'name CA' --> IT WORKS")
    print("                                                              ● -a 'all'     --> IT WORKS")
    print("                                                              ● -a all       --> IT WORKS (*all* has one word: not require apex)")
    print("                                                     The complete list of possible string can be found in MDAnalysis documentation, i.e:")
    print("                                                     https://docs.mdanalysis.org/stable/documentation_pages/selections.html\n")
    print("  [Step]                          OPTIONAL           By using this option it is possible to reduce the number of frames")
    print("                                                     of trajectory. By default all the frames are read. On the other hand,")
    print("                                                     insert an integer number X between 1 and the total number of frames")
    print("                                                     in order to read trajectory every X frames.")
    print("                                                     The default value is 1, that is all frames are read.\n")

    print("-----------------------------------------------------------------------------------------------------");
    print("Hereafter the list of flags:\n")
    print("   -r   --ref                     FILE               Coordinate FILE (gro, pdb, psf, ..., format)")
    print("   -t   --traj                    FILE               Trajectory FILE (any format, included lammpstrj is accepted)")
    print("  [-a] [--atoms]                  STR                Selection of atoms that will be converted from any format to xtc (default = 'all')")
    print("  [-s] [--step]                   INT                The trajectory is read every X frames. (default: X=1, i.e. all frames are read)") 
    print("  [-h] [--help]                                      Give this help list\n")
    print("Report bugs to <raffaele.fiorentini@unitn.it>\n")
  
    

# F.6 - It checks for not accepted flags for this code
def check_argv_errors():
    for i in range(1, len(sys.argv)):
        if(i%2 != 0):

            if(sys.argv[i][0] == '-' and len(sys.argv[i]) == 1):
                print("\n####################################################################################")
                print("ERROR. '-' is not accepted as flag. Use, for example, '-r' instead of '-'")
                print("Look below for further help.")
                print("####################################################################################\n\n")
                print_help()
                quit()

            if(sys.argv[i][0] == '-' and sys.argv[i][1] != '-' and  len(sys.argv[i]) > 2):
                print("\n####################################################################################")
                print("ERROR. Each flag must contain '-' plus ONLY ONE letter. Example: -r")
                print("       Otherwise each flag can also contain '--' plus a STRING. Example: --ref")
                print("       Look below for further help.")
                print("####################################################################################\n\n")
                print_help()
                quit()

            if(sys.argv[i][0] == '-' and sys.argv[i][1] == '-' and  len(sys.argv[i]) == 2):
                print("\n####################################################################################")
                print("ERROR. '--' not allowed. Each flag must contain '-' plus ONLY ONE letter. Example: -r")
                print("       Otherwise each flag can also contain '--' plus a STRING. Example: --ref")
                print("       Look below for further help.")
                print("####################################################################################\n\n")
                print_help()
                quit()


# F.7 - Parsing arguments, printing error and help message if this code presents not allowed arguments, and checking if mandatory files are present
def checking_valid_arguments(parser):
    try:
        args  = parser.parse_args()
    except SystemExit:
        print("\n####################################################################################")    
        print("ERROR. Arguments with no flag are not allowed. Check that each flag (e.g. -r) is followed by its specific argument")
        print("       Moreover, if the error is due to '-a/--atoms' flag for selecting atoms")
        print("       be careful, because if the string is made up of more than one word separated by spaces")
        print("       the latter must be written between apex.")
        print("       Example: ● -a name CA   --> IT DOES NOT WORK (*name CA* has two words: it requires apex for working.)")
        print("                ● -a 'name CA' --> IT WORKS") 
        print("                ● -a 'all'     --> IT WORKS") 
        print("                ● -a all       --> IT WORKS (*all* has one word: it does not require apex for working.)")
        print("       Check it out the MDAnalsys website and look below for further help.")
        print("       Look below for more information.")
        print("####################################################################################\n\n")
        print_help()
        quit()    
        
        
# F.8 - It checks if mandatory files in this code are present 
def mandatory_files_present(RefFile, TrajFile):
    if (RefFile is None):
        print("\n####################################################################################")
        print("ERROR. The Coordinate file is missing")
        print("       Look below for further help.")
        print("####################################################################################\n\n")
        print_help()
        quit()

    if (TrajFile is None):
        print("\n####################################################################################")
        print("ERROR. The file containing the Trajectory is missing")
        print("       Look below for further help.")
        print("####################################################################################\n\n")
        print_help()
        quit()


# F.9 - Checking if a mandatory file actually found or not. 
def checking_file_found(FileName):
    if not os.path.isfile(FileName):
        print("\n####################################################################################")
        print("ERROR. Error while opening the file. '{}' does not exist.\n".format(FileName))
        print("####################################################################################\n\n")
        print_usage()
        quit()


# F.10 - It checks if the file is empty
def check_empty_file(file):
    if(os.path.getsize(file) == 0):
        print("\n####################################################################################")
        print("ERROR. Your file is empty. Please, fill out {} with significant data or use another file".format(file))
        print("####################################################################################\n\n")
        print_usage()
        quit()
        
        
# F.11 - Checking if the optional argument 'SelectAtoms' is set 
#        String that specifies the atoms of trajectory that will be converted from lammpstrj format to xtc.
#        The default value is 'all' [-a/--atoms all] that means that all atoms will be token in account.
#        An example example could be '-a name CA' where only the C-alpha atoms will be considered
#        The complete list of possible string can be found in MDAnalysis documentation, i.e:
#        https://docs.mdanalysis.org/stable/documentation_pages/selections.html
#
#        Please, take in account that, after defining arguments, the latter are treated always as STRING, therefore we have to check if we are deal with INT, FLOAT or STRINGS. 
def checking_errors_SelectAtoms_opt_arg(SelectAtoms):
    if(SelectAtoms is not None):   # If 'SelectAtoms' exists...
        SelectAtoms = check_Int_Float_Str(SelectAtoms)    # it returns "SelectAtoms" accordingly with its nature: integer, float, or string     
       
        if(not isinstance(SelectAtoms.strip(), str)):             # If "SelectAtoms" is not string (i.e. integer or float)
            print("\n####################################################################################")
            print("ERROR. '-a/--atoms {} set but not recognized.".format(SelectAtoms))    
            print("       This optional argument must be a string that specifies the atoms of trajectory")
            print("       that will be converted from any format to xtc.")
            print("       The default value is 'all' [-a/--atoms all] that means that all atoms will be token in account.")
            print("       Another choice could be the string 'name CA' [-a 'name CA']")
            print("       in which only the C-alpha atoms will be considered for the trajectory conversion.")
            print("       However, be careful, because if the string is made up of more than one word separated by spaces")
            print("       the latter must be written between apex.")
            print("       Example: ● -a name CA   --> IT DOES NOT WORK (*name CA* has two words: it requires apex for working.)")
            print("                ● -a 'name CA' --> IT WORKS") 
            print("                ● -a 'all'     --> IT WORKS") 
            print("                ● -a all       --> IT WORKS (*all* has one word: it does not require apex for working.)")
            print("       The complete list of possible string can be found in MDAnalysis documentation, i.e:")
            print("       https://docs.mdanalysis.org/stable/documentation_pages/selections.html")
            print("       Check it out of MDAnalsys website and look below for further help.")
            print("####################################################################################\n\n")
            print_help()
            quit()
        else: 
            print("\n● '-a/--atoms {}' set. The atoms token in account for lammpstrj to xtc format conversion are '{}'.\n".format(SelectAtoms, SelectAtoms))
                               
            
    if(SelectAtoms is None):
        SelectAtoms = 'all' 
        print("\n● '-a/--atoms {}' set. All the atoms of trajectory will be taken in account for lammpstrj to xtc format conversion.\n".format(SelectAtoms))
        

    return SelectAtoms 


# F.12 - Checking if the optional argument 'Step' is set. It is an integer number that specifies how often the trajectory is read.
#        This brings to a reduction of the total number of frames. Only an integer number between 1 and Nframes is allowed. 
#
#        Please, take in account that, after defining arguments, the latter are treated always as STRING, 
#        therefore we have to check if we are deal with INT, FLOAT or STRINGS.   
def checking_errors_Step_opt_arg(Step, Nframes):
    if(Step is not None):   # If 'Step' exists...
        Step = check_Int_Float_Str(Step)    # it returns "Step" accordingly with its nature: integer, float, or string   

        if(not isinstance(Step, int)):             # If "Step" is not int (i.e. string or float)
            print("\n####################################################################################")
            print("ERROR. '-s/--step {} set but not recognized.".format(Step))
            print("       Please, insert an integer number X between 1 and {} (total number of frames)".format(Nframes))
            print("       in order to read the trajectory every X frames.")
            print("       Thus, a string, a float or an integer number X<1 or X>{} is not allowed".format(Nframes))
            print("       The default value is 1, that is all the frames are read")
            print("       Look below for further help") 
            print("####################################################################################\n\n")
            print_help()
            quit()

        else:
            if(Step<1 or Step>Nframes): 
                print("\n####################################################################################")
                print("ERROR. '-s/--step {} set but not recognized.".format(Step))
                print("       Please, insert an integer number X between 1 and {} (total number of frames)".format(Nframes))
                print("       in order to read the trajectory every X frames.")
                print("       Thus, a string, a float or an integer number X<1 or X>{} is not allowed".format(Nframes))
                print("       The default value is 1, that is all the frames are read")
                print("       Look below for further help")
                print("####################################################################################\n\n")
                print_help()
                quit()
        print("\n● '-s/--step {}' set. The trajectory will be read every {} frames.\n".format(Step, Step))
    
    if(Step is None):
        Step = 1 
        print("\n● '-s/--step {}' set. All frames of trajectory will be read.\n".format(Step))  

    return Step     
 
 

                   ########################################################
#####################  2. Input, parsing arguments, and checking errors  ####################################
                   ########################################################



# 2.1 Input Arguments ------------------------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, add_help=False) 

group_in=parser.add_argument_group("Required Arguments") 
group_in.add_argument('-r', '--ref',    dest='RefFile',  action='store',      metavar = 'FILE', help = argparse.SUPPRESS)        # Mandatory
group_in.add_argument('-t', '--traj',   dest='TrajFile', action='store',      metavar = 'FILE', help = argparse.SUPPRESS)        # Mandatory 
group_in.add_argument('-a', '--atoms',  dest='SelectAtoms',  metavar = 'STR', help = argparse.SUPPRESS)                          # Optional
group_in.add_argument('-s', '--step',   dest='Step',  metavar = 'STR', help = argparse.SUPPRESS)                                 # Optional
group_in.add_argument('-h', '--help',   action='help',   help = argparse.SUPPRESS)                                               # Optional
# --------------------------------------------------------------------------------------------------------------------------------------

# 2.2 Printing on terminal that this code is running 
print("\n####################################################\n")
print("'{}' running...".format(os.path.basename(sys.argv[0]))) 
print("---------------------------------\n")



# 2.3 Printing help message if the script does not have any arguments  
if len(sys.argv)==1:
    print_usage()
    quit()
    
if(sys.argv[1].strip() == "--usage") or (sys.argv[1].strip() == "-u"):
    print_usage()
    quit()

if(sys.argv[1].strip() == "--help" or sys.argv[1].strip() == "-h"):
    print_help()
    quit()
    


# 2.4 Printing help message if the script does not present valid arguments
check_argv_errors()

 
# 2.5 Printing error and help message if code presents not allowed arguments
checking_valid_arguments(parser)


# 2.6 Parsing arguments
args           = parser.parse_args()

RefFile        = args.RefFile           # Mandatory 
TrajFile       = args.TrajFile          # Mandatory  
SelectAtoms    = args.SelectAtoms       # Optional 
Step           = args.Step              # Optional 

# 2.7 Checking if mandatory files are present 
mandatory_files_present(RefFile, TrajFile)


# 2.8 Checking if RefFile is actually found and that it is not empty 
checking_file_found(RefFile)     
check_empty_file(RefFile)

print("\n● '-r/--ref {}' set. Coordinate file correctly read...\n".format(os.path.basename(RefFile)))  # Print ONLY Filename


# 2.9 Checking if TrajFile is actually found and that it is not empty 
checking_file_found(TrajFile)     
check_empty_file(TrajFile)

print("\n● '-t/--traj {}' set. Trajectory file correctly read...\n".format(os.path.basename(TrajFile)))


# 2.10 Creating the Universe of trajectory and computing the total number of frames (Nframes)
if(os.path.basename(TrajFile).strip()[-9:] == "lammpstrj"):
    u = mda.Universe(RefFile,TrajFile, format='LAMMPSDUMP')
else:
    u = mda.Universe(RefFile,TrajFile)
 
Nframes = u.trajectory.n_frames

# 2.11 Checking if the optional argument "SelectAtoms" is set. An error occurs if no-string is inserted. Only a string recognized by MDAnalysis is accepted. 
SelectAtoms = checking_errors_SelectAtoms_opt_arg(SelectAtoms)

# 2.12 Checking if the optioanl argument "Step" is set. An error occurs if float or a string is inserted. Only an integer number higher than 1 
#      and lower than the total number of frames is allowed. 
Step = checking_errors_Step_opt_arg(Step, Nframes) 




                   #################################
#####################  3. Conversion Trajectory  ####################################
                   #################################

# 3.1 Selection of the atoms for trajectory conversion. 
try:
    Ref  = u.select_atoms(SelectAtoms)
except mda.exceptions.SelectionError:
    print("\n####################################################################################")
    print("ERROR. The selection chosen ({}) is not recognized".format(SelectAtoms))
    print("       The error is due to '-a/--atoms' flag for selecting atoms")
    print("       As first, check that the string is recognized by MDAnalsysis.")
    print("       The complete list of possible strings can be found is MDAnalysis documentation, i.e:")
    print("       https://docs.mdanalysis.org/stable/documentation_pages/selections.html")
    print("       Second, if the string is made up of more than one word separated by spaces")
    print("       the latter must be written between apex.")
    print("       Example: ● -a name CA   --> IT DOES NOT WORK (*name CA* has two words: it requires apex for working.)")
    print("                ● -a 'name CA' --> IT WORKS") 
    print("                ● -a 'all'     --> IT WORKS") 
    print("                ● -a all       --> IT WORKS (*all* has one word: it does not require apex for working.)")
    print("       Check it out the MDAnalsys website and look below for further help.")
    print("####################################################################################\n\n")
    print_help()
    quit() 


# 3.2 Writing the Trajectory File(.xtc) every X step 
with mda.Writer("Trajectory.xtc", Ref.n_atoms) as W:
    for ts in u.trajectory[::Step]:
        W.write(Ref)

