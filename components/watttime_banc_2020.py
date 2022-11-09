import pandas as pd 
import os.path
import glob

path = "data"

#only want 2020 for now

all_files = glob.glob(os.path.join(path, "*2020*.csv"))

WattTimeDf = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

wattsub = 'wattTime Banc data'