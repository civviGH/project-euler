#!/bin/bash
mkdir "$1"
touch "$1/main.py"
touch "$1/__init__.py"
chmod +x "$1/main.py"
echo -e "#!/usr/bin/env python3\n\nfrom aux import *\n" > "$1/main.py"
ln -s ../aux.py "$1/aux.py"
