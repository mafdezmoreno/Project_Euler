#!/bin/bash

echo "|Python|"
echo " "
python3 LargeSum.py
echo " "

echo "|GO|"
echo " "
go run LargeSum.go
echo " "

: '
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
'

echo "|Dart|"
echo " "
dart run LargeSum.dart
echo " "