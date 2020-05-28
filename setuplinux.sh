#!/bin/bash

echo "activating env"

source env/bin/activate

echo "installing requirements"

pip3 install -r requirements.txt
