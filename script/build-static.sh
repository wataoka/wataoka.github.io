# move to this file
cd `dirname $0`

# define variables
base=".."

# build static file
python "${base}/freeze.py"

# rename build to docs
rm -rf ${base}/docs
mv ${base}/build ${base}/docs

# remove other docs dir
rm -rf ${base}/docs/static/node_modules/bootstrap-4.1.3/site/docs

# show page
open "${base}/docs/index.html"