import random

class Alphabet:
  def __init__(self, alphabet):
      self.start = ord(alphabet[0])
      self.end = ord(alphabet[-1])
      self.alphabet = self.gen_alphabet(alphabet)
        
  # TODO handle '$' and first > last
  def gen_alphabet(self, alphabet):
    if len(alphabet) == 1: return alphabet
    return [chr(i) for i in range(self.start, self.end+1)]

  def gen_rand_string(self, n: int):
    string = ''
    for i in range(n):
      string = ''.join([string, self.alphabet[random.randint(0, len(self.alphabet)-1)]])
    return string

  def __str__(self):
    return str(self.alphabet)
