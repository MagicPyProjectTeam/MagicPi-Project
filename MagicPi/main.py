# Imports
from tendo import singleton;
import os;
import actions;
import Environment;

# Verification des droits
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.");

# Singleton : will sys.exit(-1) if other instance is running
me = singleton.SingleInstance();

#Environment Loading
env = Environment.Environment();
env.setStatics();
env.launchApplication(actions);