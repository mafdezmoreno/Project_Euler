#!/bin/bash

echo "## Python"
echo " "
python3 CoinSums.py
echo " "

echo "## cpp"
echo " "
clang++ -std=c++20 CoinSums.cpp -O && ./a.out && rm a.out
echo " "
