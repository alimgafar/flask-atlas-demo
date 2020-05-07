#!/usr/bin/env sh

# Create and activate new virtualenv environment for Flask dev
# You can create the environment 
# however, trying to activate it via the shell script won't work
# it will activate in the script and disappear when the process
# ends when the script terminates

if [ "$1" == "" ]; then
  echo "$0 usage: $0 < project name >"
else
  dirname = $1
fi

# Create the new environment
echo "mkdir $dirname"
echo "cd $dirname"
echo "virtualenv env"

# Activate the environment
echo "source env/bin/activate"

# To deactivate the virtualenv environment, type "deactivate"

# Install Flask
echo "pip install Flask"

# Install PyMongo
echo "pip install pymongo[tls] ipaddress certifi"

