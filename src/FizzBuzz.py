

class FizzBuzz:
  def GetNumber(self, num:int) -> str:
    if (num % 3) == 0:
      StringNum = "Fizz"
    else:
      StringNum = str(num)

    return StringNum