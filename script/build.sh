# move to this file
cd `dirname $0`

# define variables
base=".."

# build static file
python "${base}/freeze.py"