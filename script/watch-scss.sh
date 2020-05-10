# move to this file
cd `dirname $0`

# define variables
base=".."

# watch scss
sass --watch "${base}/static/scss/main.scss":"${base}/static/css/main.css"