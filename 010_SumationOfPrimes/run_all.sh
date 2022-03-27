#!/bin/bash
echo "======="
echo "|Python|"
echo "======="
python3 SumationOfPrimes.py 
echo " "

echo "====="
echo "|Cpp|"
echo "====="
g++ -std=c++17 SumationOfPrimes.cpp -o SumationOfPrimes -O
./SumationOfPrimes
rm SumationOfPrimes
echo " "

echo "======="
echo "|Swift|"
echo "======="
swift -O SumationOfPrimes.swift
echo " "

echo "======="
echo "|Dart|"
echo "======="
dart run SumationOfPrimes.dart
echo " "


echo "======="
echo "|GO|"
echo "======="
go run SumationOfPrimes.go
echo " "