/*
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
*/

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>

std::vector<int> original_list(const int * max_value);
void swap(int &a, int &b);
void permutation(std::vector<int> list, int current_pos);
void print_vector(std::vector<int>* vec);

class ExecutionTime{
    
    private:
        std::chrono::steady_clock::time_point start;
        std::chrono::steady_clock::time_point stop;
    public:
        ExecutionTime(){
            start = std::chrono::high_resolution_clock::now();
        }
            
        void stop_time(){
            stop = std::chrono::high_resolution_clock::now();
            auto duration = duration_cast<std::chrono::microseconds>(stop - start).count();
            std::cout << duration/1000<< "ms"<< std::endl;
        }
};

ExecutionTime ET;

void main_program(){

    //int max_value_1 = 2;
    //auto list_1 = original_list(max_value_1);
    //permutation(list_1, 0, max_value_1);
    
    const int max_value_2 = 9;  
    auto list_2 = original_list(&max_value_2);
    permutation(list_2, 0);

}

void permutation(std::vector<int>  list, int current_pos){

    int static permutation_th = 0;
    int static vector_size = list.size();

    if (current_pos == vector_size){
        permutation_th++;
        //print_vector(list);
        if (permutation_th==int(1000000)){
            print_vector(&list);
            std::cout<<": "<<permutation_th<<std::endl;
            ET.stop_time();
            _Exit(1); //To force execution detention
        }
    }
    else{
        for (int i=current_pos; i<=vector_size; i++){
            if (list[i]>list[current_pos]){
                swap(list[i],list[current_pos]);
                permutation(list, current_pos+1);
                continue;
            }
            if (i!=current_pos)
                swap(list[i],list[current_pos]);
            permutation(list, current_pos+1);
            if (i!=current_pos)
                swap(list[current_pos],list[i]);
        }
    }
}

void swap(int &a, int &b){
    int temp =a;
    a = b;
    b = temp;
}

void print_vector(std::vector<int>* vec){

    for (int i=0; i<(vec->capacity()); i++)
        std::cout<<vec->at(i);
    //std::cout<<std::endl;
}

std::vector<int> original_list(const int * max_value){
    
    std::vector<int> numbers;
    for (int i=0; i<=*max_value;i++){
        numbers.push_back(i);
        //std::cout<<i<<" ";
    }
    //std::cout<<std::endl;
    return numbers;
}

int main(){

	//! Start
    main_program();
	//! End
}

