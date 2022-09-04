#!/usr/bin/env bash

cd ../
pip install virtualenv
virtualenv motion-venv
source motion-venv/bin/activate
pip install -r requirements.txt
venv_activate=$(pwd)
echo "alias capstone_venv='source $venv_activate/motion-venv/bin/activate'" >> ~/.bashrc 
source ~/.bashrc
source motion-venv/bin/activate