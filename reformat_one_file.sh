#!/bin/bash
file=$1
source .venv/bin/activate

python -m autoflake --in-place --remove-unused-variables $file
python -m isort --profile black $file
python -m black $file --skip-string-normalization
python -m flake8 $file
