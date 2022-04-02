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


fn main() {

	use std::time::Instant;
    let now = Instant::now();

	//let result = get_largest_sequence(1000000);
	get_largest_sequence(1000000);
	//println!("{}", result);
	// ! End of the program
	let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
}

fn get_largest_sequence(max_value:u64){//} -> u64 {

	let mut largest_seq_generator:u64 = 0; //start number of Collatz list
	let mut len_collatz: u64 = 0;
	//let mut seq_Collatz:Vec<u64>;

	let mut i = max_value;
	while i > 0 {
		let temp = sequence(i);
		let temp_len = (temp.len()) as u64;
		if temp_len > len_collatz {
			//seq_Collatz = temp;
			len_collatz = temp_len;
			largest_seq_generator = i;
		}
		i-=1;
	}

	println!("{}",largest_seq_generator);
	//return largest_seq_generator;
}

fn collatz_list_generator()->Vec<u64> {
	
	let mut collatz_list: Vec<u64> = vec![1];
	let mut i = 1;
	while i<=1000000{
		i = i * 2;
		collatz_list.push(i);
		
	}
	return collatz_list;
}

fn sequence(start: u64) -> Vec<u64> {

	let mut next: u64 = start as u64;
	let mut sequence = vec![start];
	let mut collatz_list = collatz_list_generator();

	loop{
		if next <= 1 {
			break
		}
		let (exist, index) = contains_element(collatz_list.as_slice(), next);
		if exist {
			collatz_list.reverse();
			sequence.extend(&collatz_list[..index]);
			return sequence;

		} else {
			if next%2 == 0 {
				next = if_even(next)
			} else {
				next = if_odd(next)
			}
		}

		sequence.push(next)
	}
	if next == 1 {
		return sequence
	}
	return vec![0]
}

fn contains_element(input: &[u64], element:u64) -> (bool, usize) {

	for (index, item) in input.iter().enumerate() {
		if *item == element {
			return (true, index);
		}
	}
	return (false, 0);
}

fn if_even(n:u64) ->u64 {
	
	return n / 2;
}

fn if_odd(n:u64)->u64 {
	
	return 3*n + 1;
}
