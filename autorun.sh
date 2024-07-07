#!/bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt install python3 -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

