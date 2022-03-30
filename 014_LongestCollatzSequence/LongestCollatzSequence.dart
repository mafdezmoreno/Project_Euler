/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

void main() {
  final stopwatch = Stopwatch()..start();
  //! Real start of the program
  /*
  List<int> seq = sequence(13);
  print("Lenght: ${seq.length} \nSequence: ${seq}\n");
  var CollatzList = CollatzList_Generator();
  print(CollatzList);
  print(CollatzList.contains(500));
  print(CollatzList.indexOf(512));
  */
  get_largest_sequence(1000000);
  //! Final of the program
  print('Executed in ${stopwatch.elapsed.inMilliseconds / 1000} s');
}

List<int> get_largest_sequence(int max_value) {
  int largest_seq_generator = 0; //start number of Collarz list
  int len_Collatz = 0; //leght of list
  List<int> seq_Collatz = []; //Collarz list of the numbers

  for (int i = max_value; i > 0; i--) {
    List<int> temp = sequence(i); //Collarz list of the number
    int temp_len = temp.length;
    if (temp_len > len_Collatz) {
      seq_Collatz.clear();
      seq_Collatz = temp;
      len_Collatz = temp_len;
      largest_seq_generator = i;
    }
  }
  //print("Length: ${len_Collatz}, Generator: ${largest_seq_generator}");
  //print(seq_Collatz);
  print(largest_seq_generator);
  return seq_Collatz;
}

List<int> CollatzList_Generator() {
  List<int> CollatzList = [];
  for (int i = 1; i <= 1000000; i = i * 2) {
    CollatzList.add(i);
  }
  //return new List.from(CollatzList.reversed);
  return CollatzList;
}

List<int> sequence(int start) {
  int next = start;
  List<int> sequence = [start];
  List<int> CollatzList = CollatzList_Generator();
  while (true) {
    if (next <= 1) {
      break;
    }

    if (CollatzList.contains(next)) {
      //print("Sequencia añadida");
      return sequence +
          (new List.from(
              (CollatzList.sublist(0, CollatzList.indexOf(next))).reversed));
    } else {
      if (next % 2 == 0) {
        next = if_even(next);
      } else {
        next = if_odd(next);
      }
    }

    sequence.add(next);
  }
  if (next == 1) {
    return sequence;
  }
  return [0];
}

int if_even(int n) {
  return n ~/ 2;
}

int if_odd(int n) {
  return 3 * n + 1;
}
