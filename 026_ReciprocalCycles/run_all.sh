#!/bin/bash

echo "# Cpp Clang"

clang++ -std=c++20 ReciprocalCycles.cpp -o ReciprocalCycles -O
./ReciprocalCycles
rm ReciprocalCycles
echo " "

echo "# Cpp Gnu - 11"
c++-11 -std=c++20 ReciprocalCycles.cpp -o ReciprocalCycles -O
./ReciprocalCycles
rm ReciprocalCycles
echo " "