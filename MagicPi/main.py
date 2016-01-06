# Imports
from tendo import singleton;

import actions;
import Environment;

# Singleton : will sys.exit(-1) if other instance is running
me = singleton.SingleInstance();

#Environment Loading
env = Environment.Environment();
env.launchApplication(actions);