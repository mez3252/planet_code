# planet_code

# Environment Setup: 
Build conda environment that includes gdal and matplotlib (matplotlib is handy but not necessary):

conda create --prefix ./envs gdal matplotlib

Activate environment:

conda activate ./envs


# View help: planet_code.py --help

$ python planet_code.py --h

usage: planet_code.py [-h] [--fn_in FN_IN] [--fn_out FN_OUT] [-t THRESH] [-v]

options:
  -h, --help            show this help message and exit
  --fn_in FN_IN         input filename
  --fn_out FN_OUT       output filename
  -t THRESH, --thresh THRESH
                        ndvi threshold
  -v, --verbose         increase output verbosity



# Three different options for running the code. 
Option 1: place the data in a subdirectory called 'data' and call the planet_code.py script. The relative path './data/20210827_162545_60_2262_3B_AnalyticMS_8b.tif' is hardcoded as a default option the 'planet_code.py' script. 

Option 2: call the 'calculate_ndvi_epsg_4326' method within planet_code.py from python. See the 'run_example.py' script for this option. Pass filename input, filename output, and ndvi threshold to the method.  

Option 3: call the 'planet_code.py' from the commandline. As explained above in the help, planet_code.py uses argparse to take input arguements for ndvi threadhold and input/output filenames . Example commandline input:

$ python planet_code.py -t=.5 --fn_in=./data/20210827_162545_60_2262_3B_AnalyticMS_8b.tif --fn_out=./data/20210827_162545_60_2262_3B_AnalyticMS_8b_epsg_4326.tif

