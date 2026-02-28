#!/usr/bin/env bash

pip install -e .
pip install notebook

jupyter notebook --ip=0.0.0.0 --port=$PORT --no-browser --allow-root