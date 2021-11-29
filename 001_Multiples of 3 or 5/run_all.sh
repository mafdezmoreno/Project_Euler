#!/bin/bash
echo "# Python"
python3 Multiples_of_3_or_5.py 
echo " "

echo "# Lua"
luac Multiples_of_3_or_5.lua 
lua luac.out
rm luac.out
echo " "

echo "# Cpp"
g++ -std=c++17 Multiples_of_3_or_5.cpp -o Multiples_of_3_or_5 -O
./Multiples_of_3_or_5
rm Multiples_of_3_or_5
echo " "

echo "# Rust"
rustc Multiples_of_3_or_5.rs -O
./Multiples_of_3_or_5
rm  Multiples_of_3_or_5
echo " "

echo "# Swift"
swift -O Multiples_of_3_or_5.swift
echo " "

echo "# Dart"
/opt/homebrew/Cellar/dart-beta/2.15.0-268.18.beta/bin/dart run Multiples_of_3_or_5.dart
echo " "


echo "# C#"
cd MultiplesOf3Or5_dotnet
dotnet run
rm Multiples_of_3_or_5.exe
echo " "

echo "C# mono"
cd ..
csc Multiples_of_3_or_5.cs
mono Multiples_of_3_or_5.exe
rm Multiples_of_3_or_5.exe