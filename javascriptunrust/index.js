// First we need a counter, which will be i
// Then we need to loop it to increase by an increment of 1 starting at 1 till 20.
// Then we need to see if its divisible by 3 or 5 or both
// If divisible by 3, print "fizz", 
// if divisible by 5 print "buzz", 
// if divisible by both 3 and 5 print fizzbuzz
// otherwise print the number.

for (let i = 1; i <= 20; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}