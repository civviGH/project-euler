#!/bin/bash
mkdir "$1"
touch "$1/main.py"
touch "$1/__init__.py"
chmod +x "$1/main.py"
ln -s ~/python/euler/aux.py "$1/aux.py"
