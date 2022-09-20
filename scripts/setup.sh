#!/usr/bin/env bash

cd ../
pip install virtualenv
virtualenv motion-venv
source motion-venv/bin/activate
pip install -r requirements.txt
pip install -r examples/dash-image-processing/requirements.txt
pip install -r examples/dash-manufacture-spc-dashboard/requirements.txt
pip install -r examples/dash-object-detection/requirements.txt
venv_activate=$(pwd)
echo "alias capstone_venv='source $venv_activate/motion-venv/bin/activate'" >> ~/.bashrc 
source ~/.bashrc
source motion-venv/bin/activate