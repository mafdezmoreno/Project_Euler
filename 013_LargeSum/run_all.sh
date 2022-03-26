#!/bin/bash

echo "## Python"
echo " "
python3 LargeSum.py
echo " "

echo "# GO"
echo " "
go run LargeSum.go
echo " "

: '
echo "====="
echo "|Cpp|"
echo "====="
g++ -std=c++17 __.cpp -o __ -O
./__
rm __
echo " "

echo "======"
echo "|Rust|"
echo "======"
rustc __.rs -O
./__
rm  __
echo " "
'
echo "# Swift"
echo " "
swift -O LargeSum.swift
echo " "


echo "# Dart"
echo " "
dart run LargeSum.dart
echo " "