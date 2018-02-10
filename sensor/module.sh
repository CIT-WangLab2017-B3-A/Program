#!/bin/sh
python setup.py build_ext --inplace

mv *.c C_files/
