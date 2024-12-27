#======課題==================================================#
# FizzBuzzの課題詳細
# 要件:
# 数字を1から100まで順番に出力します。
# ただし、以下のルールに従います：
# 3の倍数の場合は数字の代わりに "Fizz" を出力する。
# 5の倍数の場合は数字の代わりに "Buzz" を出力する。
# 3と5の両方の倍数の場合は数字の代わりに "FizzBuzz" を出力する。
#===========================================================#

#======Todo==================================================#
# ・数字を文字列に変換する =======================> 完了
# ・3の倍数の場合は"Fizz"に変換する===============> 完了
# ・5の倍数の場合は"Buzz"に変換する
# ・3と5の両方の倍数の場合は"FizzBuzz"をに変換する
#===========================================================#

import unittest 
from FizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
  def test_NumToString(self):
    fizzbuzz = FizzBuzz()
    self.assertEqual("1", fizzbuzz.GetNumber(1))
    self.assertEqual("2", fizzbuzz.GetNumber(2))

    self.assertEqual("Fizz", fizzbuzz.GetNumber(3))
    self.assertEqual("Fizz", fizzbuzz.GetNumber(9))

    self.assertEqual("Buzz", fizzbuzz.GetNumber(5))
    self.assertEqual("Buzz", fizzbuzz.GetNumber(10))