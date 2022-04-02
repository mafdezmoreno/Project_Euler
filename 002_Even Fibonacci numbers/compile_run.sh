
echo "## Cpp"

g++ -std=c++20 EvenFibonacciNumbers.cpp -o EvenFibonacciNumbers -O
./EvenFibonacciNumbers
rm EvenFibonacciNumbers
echo " "

echo "## Go"

go run EvenFibonacciNumbers.go
echo " "

echo "## Python"

python3 EvenFibonacciNumbers.py
echo " "

echo "## F#"

dotnet fsi EvenFibonacciNumbers.fsx
echo " "


echo "## C#"

cd EvenFibonacciNumbers_C#
dotnet run
cd ..
echo " "

echo "## C#"

dotnet script EvenFibonacciNumbers.csx
echo " "
