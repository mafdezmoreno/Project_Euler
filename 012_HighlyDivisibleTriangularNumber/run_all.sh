#!/bin/bash
echo "## Python"
python3 HighlyDivisibleTriangularNumber.py 
echo " "

echo "## Cpp"
g++ -std=c++17 HighlyDivisibleTriangularNumber.cpp -o HighlyDivisibleTriangularNumber -O
./HighlyDivisibleTriangularNumber
rm HighlyDivisibleTriangularNumber
echo " "

echo "## C"
gcc -std=c17 HighlyDivisibleTriangularNumber.c -o HighlyDivisibleTriangularNumber -O
./HighlyDivisibleTriangularNumber
rm HighlyDivisibleTriangularNumber
echo " "

echo "## Rust"
rustc HighlyDivisibleTriangularNumber.rs -O
./HighlyDivisibleTriangularNumber
rm  HighlyDivisibleTriangularNumber
echo " "

echo "## Swift"
swift -O HighlyDivisibleTriangularNumber.swift
echo " "

echo "## Dart"
#dart HighlyDivisibleTriangularNumber.dart
dart run HighlyDivisibleTriangularNumber.dart
#dart compile exe HighlyDivisibleTriangularNumber.dart
#./HighlyDivisibleTriangularNumber.exe
echo " "