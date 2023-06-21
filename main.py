#!/usr/bin/env python3
from processing import read_file

#if __name__ == '__main__':
#  input_file = './input.txt'
#  automata = read_file(input_file)
#  #automata.view()

def test_AF2P():
  input_file = './inputs/af2p.txt'
  return read_file(input_file)

def test_AFPN():
  input_file = './inputs/afpn.txt'
  a = read_file(input_file)
  a.process('abab')
  a.view()

def test_AFPD():
  input_file = './inputs/afpd.txt'
  a = read_file(input_file)
  a.process('aabb')
  a.view()

# Read input file
if __name__ == '__main__':
  #test_AFPD()
  test_AFPN()
  #probarSimplificacion()

