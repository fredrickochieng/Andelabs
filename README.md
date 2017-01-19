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
 
 
 Data Type function
 
 ```python
 def data_type(n):
	if n == None:
		return 'no value'
	elif type(n) == str:
		rturn len(n)
	elif type(n) == bool:
		return n
	elif type(n) == int:
		if n < 100:
			return "less than 100"
		elif n == 100:
			return 'equal to 100'
		else:
			return "more than 100"
	elif type(n) == list:
		if len(n) < 3:
			return None
		else:
			return n[2]
  ```
  
  The data_type function takes any type of data.It then checks if the data type is a string ,integer or boolean.For instance ,the function checks if the data type is a string and returns the length of that string i.e `elif type(n) == str:
		return len(n)` as shown in the code above .It returns various outputs for other data types e.g integer,booleans and list.For a list it returns the value of index 2 if the the length of the list is greater than 2 and none if the legth of the list is less than 3
		
		
		CAR CLASS
		
You are to create a Car class that can be used to instantiate various vehicles.

It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.

CODE

```python
class Car(object):
  speed = 0

  def __init__(self, name='General', model='GM', vehicle_type=None):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type


    if self.name in ['Porshe', 'Koenigsegg']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.vehicle_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4


  def is_saloon(self):
    if self.vehicle_type is not 'trailer':
        self.vehicle_type == 'saloon'
        return True
    return False

  def drive(self, moving_speed):
    if moving_speed == 3:
      self.speed = 1000
    elif moving_speed == 7:
      self.speed = 77

return self
```



