FIIZ BUZZ function

```python

def fizz_buzz(number):
  if number<3:
    return "Invalid"
  if (number%3==0 and number%5==0):
    return "FizzBuzz"
  elif number % 3==0:
    return "Fizz"
  elif number % 5==0:
    return "Buzz"
  else:
    return number
  
  ```
    
 This is a simple function that takes a number as an input.The number should be dvisible by 3,5 or both .In each case,it returns the strings "Fizz","Buzz" and "FizzBuzz" if the number is divisible by 3,5 or both respectively.
 

