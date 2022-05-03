/*
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
*/

// Solution based on:
// https://www.educative.io/edpresso/coin-change-problem-2-finding-the-number-of-ways-to-make-a-sum

#include<iostream>
#include <vector>
#include <chrono>


int find_possible_ways(std::vector<int> coins, int sum);

int main(){
    using namespace std::chrono;
    auto start = high_resolution_clock::now();
    //! START
    
    std::vector<int> coins = {2, 1};     // Array of available coins
    int sum = 5;            // The sum to be made
    std::cout<< "The possible ways "<< sum << " can be made is: " <<std::endl;
    std::cout<< find_possible_ways(coins, sum) <<std::endl;

    std::vector<int> coins2 = {200, 100, 50, 20, 10, 5, 2, 1};     // Array of available coins
    int sum2 = 200;            // The sum to be made
    std::cout<< "The possible ways "<< sum2 << " can be made is: " <<std::endl;
    std::cout<< find_possible_ways(coins2, sum2) <<std::endl;

    //! END
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    std::cout << duration.count() << "us"<< std::endl;
    return 0;
}
int find_possible_ways(std::vector<int> coins, int sum){
    
    int size = coins.size();

    // Declaring a 2-D array
    // for storing solutions to subproblems:
    std::vector<std::vector<int>> sol(size+1, std::vector<int> (sum+1, 0));
  
    // Initializing first column of array to 1
    // because a sum of 0 can be made
    // in one possible way: {0}
    for (int i = 0; i<=size; i++)
        sol[i][0] = 1;
    

    //Solution
    for (int i=1; i<=size; i++){
        for (int j=1; j<=sum; j++){
            if (coins[i - 1] > j)  // Cannot pick the highest coin:
                sol[i][j] = sol[i - 1][j];
            else  // Pick the highest coin:
                sol[i][j] = sol[i - 1][j] + sol[i][j - coins[i - 1]];
        }
    }
    
    return sol[size][sum];
}