/*
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Gived in LargeSum_input.txt:
  -> 100 numbers
  -> 50 digits each
*/

import 'dart:io';

main() async {
  final stopwatch = Stopwatch()..start();
  //! Start of the program

  //var file = File('013_LargeSum/LargeSum_input.txt');
  var file = File('LargeSum_input.txt');
  List<String> lines;
  String sum = '';

  if (await file.exists()) {
    // Read file
    var contents = await file.readAsStringSync();
    //print(contents);
    //String fileContent = utf8.decode(file.bytes);
    lines = contents.split('\n');

    /*
    for (var i = 0; i < 2; i++) {
      print(lines[i]);
    }
    for (var i = (lines.length - 1); i >= 98; i--) {
      print(lines[i]);
    }*/

    //var test_add = add_numbers(lines[0], lines[1]);
    //print(test_add);
    // 83484225211392112511446123117807668296927154000788

    sum = lines[0];
    //print(sum);
    for (int i = 1; i < lines.length - 1; i++) {
      sum = add_numbers(sum, lines[i]);
      //print(lines[i]);
    }
  } else {
    print("File not found");
  }

  //var test_add = add_numbers('2345', '567');
  //print(test_add);

  print("All sum digits: ");
  print(sum);

  print("Last ten digits");
  for (int i = sum.length - 10; i < sum.length; i++) {
    stdout.write(sum[i]);
  }
  print('');

  print("First ten digits");
  for (int i = 0; i < 10; i++) {
    stdout.write(sum[i]);
  }
  print('');

  //! Final of the program
  print('');
  print('Executed in ${stopwatch.elapsed.inMilliseconds} ms');
  return 0;
}

String add_numbers(String str_long, String str_short) {
  String result = "";

  int n_long = str_long.length;
  int n_short = str_short.length;
  int n_diff = n_long - n_short;

  int carry = 0;
  for (int i = n_long - 1; i >= n_diff; i--) {
    //School sum
    int sum = int.parse(str_long[i]) + int.parse(str_short[i - n_diff]) + carry;
    result = (sum % 10).toString() + result;
    //Carry for next step
    carry = sum ~/ 10;
  }

  // Rest of the digits of the larger number
  for (int i = n_diff - 1; i >= 0; i--) {
    int sum = int.parse(str_long[i]) + carry;
    result = (sum % 10).toString() + result; //str.push_back(sum % 10 + '0');
    carry = sum ~/ 10;
  }

  // Add remaining carry
  if (carry > 0) {
    result = carry.toString() + result;
  }
  return result;
}
