A. Commit message:
Replace vulnerable subprocess call using shell=True with a secure alternative

B. Change summary:
Changed the subprocess call to avoid using shell=True by splitting the command into
 a list format suitable for shell=False, enhancing security.

C. Compatibility Risk:
Medium

D. Fixed Code:
import subprocess, sys

nbr = int(sys.argv[1])

cmd = ["touch", "output_folder/hej_%s" % nbr]
subprocess.call(cmd, shell=False)
