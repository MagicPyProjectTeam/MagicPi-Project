# Imports
from tendo import singleton;
import os;
import actions;
import Environment;

# Verification des droits
if os.geteuid() != 0:
    exit('\033[1m' + '\033[91m' + "\n[x] You need to have root privileges to run this script.\n[x] Please try again, this time using 'sudo'. Exiting.\n" + '\033[0m');

# Singleton : will sys.exit(-1) if other instance is running
me = singleton.SingleInstance();

#Environment Loading
env = Environment.Environment();
env.setStatics();
env.launchApplication(actions);