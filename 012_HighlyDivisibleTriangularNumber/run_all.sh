#!/bin/bash
echo "======="
echo "|Python|"
echo "======="
python3 HighlyDivisibleTriangularNumber.py 
echo " "

echo "====="
echo "|Cpp|"
echo "====="
g++ -std=c++17 HighlyDivisibleTriangularNumber.cpp -o HighlyDivisibleTriangularNumber -O
./HighlyDivisibleTriangularNumber
rm HighlyDivisibleTriangularNumber
echo " "

echo "======"
echo "|Rust|"
echo "======"
rustc HighlyDivisibleTriangularNumber.rs -O
./HighlyDivisibleTriangularNumber
rm  HighlyDivisibleTriangularNumber
echo " "

echo "======="
echo "|Swift|"
echo "======="
swift -O HighlyDivisibleTriangularNumber.swift
echo " "

echo "======="
echo "|Dart|"
echo "======="
#dart HighlyDivisibleTriangularNumber.dart
#dart run HighlyDivisibleTriangularNumber.dart
#dart compile exe HighlyDivisibleTriangularNumber.dart
#./HighlyDivisibleTriangularNumber.exe
/opt/homebrew/Cellar/dart-beta/2.15.0-268.18.beta/bin/dart run HighlyDivisibleTriangularNumber.dart
echo " "