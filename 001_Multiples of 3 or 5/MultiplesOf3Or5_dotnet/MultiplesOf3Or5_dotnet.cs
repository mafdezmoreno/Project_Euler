// To create projet:
// dotnet new console --framework net6.0
// To execute:
// dotnet run

using System;
using System.Diagnostics;
using System.Threading;

Stopwatch stopwatch = new Stopwatch();
stopwatch.Start();

void Multiples(int value)
{
    int sum = 0;
    for (int i = 0; i < value; i++){

        if (i%3==0){
            //Console.WriteLine(i);
            sum = sum +i;
        }   
        else if (i%5==0){
            //Console.WriteLine(i);
            sum +=i;
        }
    }
    
    Console.WriteLine("Sum: " + sum);
}


Multiples(10);
Multiples(1000);
stopwatch.Stop();

Console.WriteLine("Elapsed Time is {0:0.0000} ms", stopwatch.Elapsed.Milliseconds);
