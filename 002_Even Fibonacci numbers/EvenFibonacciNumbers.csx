using System;
using System.Diagnostics;
using System.Threading;

Stopwatch stopwatch = new Stopwatch();
stopwatch.Start();

    int b = 2;
	int a = 1;
	int c = 3;
	int sum_of_even = 2;
	int i = 3;

	while(true) {
		if (i >= 4000000) {
			break;
		}
		c = a + b;
		a = b;
		b = c;
		i = c;
		if (c%2 == 0) {
			sum_of_even += c;
			Console.Write("{0} ", c);
		}
	}

	Console.WriteLine("\n{0} ", sum_of_even);
  
stopwatch.Stop();
Console.WriteLine("Elapsed Time is {0:0.0000} ms", stopwatch.Elapsed.Milliseconds);



