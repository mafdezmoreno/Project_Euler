//https://projecteuler.net/problem=1

/*
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 *
 */

fn main() {
    
    use std::time::Instant;
    let now = Instant::now();

    //Real start of the program
    let a = multiples(10);
    let b = multiples(1000);

    println!("{}",a);
    println!("{}",b);

    //End of the program
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

}

fn multiples(value: u32) -> u32 {
  let mut sum_val:u32 = 0;
  for i in 0..value {
    if i % 3 == 0 {
      sum_val += i;
    } else if i % 5 == 0 {
      sum_val += i;
    }
  }
  sum_val
}
