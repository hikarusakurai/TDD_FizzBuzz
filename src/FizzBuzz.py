

class FizzBuzz:
  def GetNumber(self, num:int) -> str:
    if (num % 3) == 0:
      StringNum = "Fizz"
    elif (num % 5) == 0:
      StringNum = "Buzz"
    else:
      StringNum = str(num)

    return StringNum