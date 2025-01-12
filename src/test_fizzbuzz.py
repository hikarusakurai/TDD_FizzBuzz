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
# ・5の倍数の場合は"Buzz"に変換する===============> 完了
# ・3と5の両方の倍数の場合は"FizzBuzz"をに変換する=> 完了
#===========================================================#

import unittest 
from FizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
  # 数字を文字列に変換するテスト
  def test_NumToString(self):
    fizzbuzz = FizzBuzz()

    # 3,5の倍数以外の場合
    self.assertEqual("1", fizzbuzz.GetNumber(1))
    self.assertEqual("2", fizzbuzz.GetNumber(2))

    # 3を渡すとFizzを返す
    self.assertEqual("Fizz", fizzbuzz.GetNumber(3))
    # 9を渡すとFizzを返すa
    self.assertEqual("Fizz", fizzbuzz.GetNumber(9))

    # 5を渡すとBuzzを返す
    self.assertEqual("Buzz", fizzbuzz.GetNumber(5))
    # 10を渡すとBuzzを返す
    self.assertEqual("Buzz", fizzbuzz.GetNumber(10))

    # 15を渡すとFizzBuzzを返す
    self.assertEqual("FizzBuzz", fizzbuzz.GetNumber(15))
    self.assertEqual("FizzBuzz", fizzbuzz.GetNumber(60))