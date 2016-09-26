#!/usr/bin/python3

#***
#*  Speed Exercise 2
#*  26 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Instructions:
#*      Make a function that accepts a number and prints that many numbers 
#*      in the fibonacci sequence. Limit the input to <=200.
#***

def fibonacci_sequence(iterations):
    current_value, next_value = 0, 1
    count = 0
    while count < iterations:
        count += 1
        print(current_value)
        current_value, next_value = next_value, current_value + next_value

if __name__ == "__main__":
    input_iterations = int(input("Desired Iterations in Fibonacci Sequence: "))
    if input_iterations <= 200:
        fibonacci_sequence(input_iterations)
    else:
        print("Cannot print more than 200 iterations. Printing only 200 iterations.")
        fibonacci_sequence(200)
