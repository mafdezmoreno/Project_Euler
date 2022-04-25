#include <iostream>
#include <chrono>
#include <vector>


void run();
long double division(long double numerator,long double denominator);
bool value_in_array(int value, std::vector<int>);

void run(int limit){

    int max_count = 0;
    int value_of_max_count = 0;
    for (int d = 2; d <= limit; d++){
        std::vector<int> remainders;
        int resto = 1;
        int count = 0;
        //std::cout<< d << "; " << 1./d << ": ";
        while (count<(d-1)){
            resto = (resto*10)%d;
            //std::cout<< resto << " ";
            if (resto==0)
                break;
            if (value_in_array(resto, remainders))
                break;
            remainders.push_back(resto);
            count++;
        }
        if (count>max_count){
            max_count = count;
            value_of_max_count = d;
        }        
    }
    std::cout<<max_count<<std::endl; 
    std::cout<<value_of_max_count<<std::endl; 
}

bool value_in_array(int value, std::vector<int> list){

    for (int i = 0; i<list.size(); i++){
        if (value == list[i]){
            return true;
        }
    }
    return false;
}

long double division(long double numerator,long double denominator){

    return numerator/denominator;
}

int main(){

    using namespace std::chrono;

    auto start = high_resolution_clock::now();
    //! Start

    run(1001);

    //! Final of the program
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
  
    std::cout << duration.count()/1000 << "ms"<< std::endl;

    return 0;
}