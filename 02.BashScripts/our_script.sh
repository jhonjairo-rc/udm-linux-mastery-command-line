#!/bin/bash


mkdir -p ../90.Testing/Magic
cd ../90.Testing/Magic
touch file{1..10}

# it does not work
#ls -lh ../90.Testing/Magic > ../90.Testing/magic.log