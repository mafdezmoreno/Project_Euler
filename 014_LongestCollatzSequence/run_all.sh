#!/bin/bash

echo "## Dart"
echo " "
dart run LongestCollatzSequence.dart
echo " "

echo "## GO"
echo " "
go run LongestCollatzSequence.go 
echo " "

echo "## Rust"
echo " "
rustc LongestCollatzSequence.rs -O
./LongestCollatzSequence
rm LongestCollatzSequence
echo " "