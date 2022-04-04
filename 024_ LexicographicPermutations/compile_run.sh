
echo "## Cpp"
g++ -std=c++20 LexicographicPermutations.cpp -lpthread -o LexicographicPermutations -O
./LexicographicPermutations
rm LexicographicPermutations
echo " "

echo "## Cpp v2"
g++ -std=c++20 LexicographicPermutations_v2.cpp -lpthread -o LexicographicPermutations_v2 -O
./LexicographicPermutations_v2
rm LexicographicPermutations_v2
echo " "