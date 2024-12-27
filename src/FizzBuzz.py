

class FizzBuzz:
  def GetNumber(self, num:int) -> str:
    if (num % 15) == 0:
      StringNum = "FizzBuzz"
    elif (num % 3) == 0:
      StringNum = "Fizz"
    elif (num % 5) == 0:
      StringNum = "Buzz"
    else:
      StringNum = str(num)

    return StringNum
  
  def PrintFizzBuzz(self):
    for i in range(1,101):
      print(self.GetNumber(i))