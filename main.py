#!/usr/bin/env python3
from alphabet import Alphabet
from automatas import *

def read_file(f_path):
  a_type = []
  alphabet = []
  states = []
  init_state = []
  accep_states = []
  delta = []
  f = open(f_path).read().splitlines()
  a_type = f[0][2:] 
  for i in range(0, len(f)):
    if f[i][0] == '#':
      s = f[i]
      continue
    if s == '#alphabet':
      alphabet = Alphabet(f[i]).alphabet
    elif s == '#states':
      states.append(f[i])
    elif s == '#initial':
      init_state = f[i]
    elif s == '#accepting':
      accep_states.append(f[i])
    elif s == '#transitions':
      delta.append(f[i])

  if a_type == 'dfa':
    return AFD(alphabet, states, init_state, accep_states, delta)
    #dfa.process('aabb') 
  elif a_type == 'nfa':
    return AFN(alphabet, states, init_state, accep_states, delta)
    #nfa.process('aabb') 
    #nfa.draw()
  else:
    return AFNLambda(alphabet, states, init_state, accep_states, delta)
    #nfa_lambda.process('aabb') 
def test_producto_cartesiano():
  f1 = 'cartesiano1.txt'
  f2 = 'cartesiano2.txt'
  a = read_file(f1)
  b = read_file(f2)
  c = a.producto_cartesiano(b)

  return

# Read input file
if __name__ == '__main__':
  f1 = './input2.txt'
  f2 = './input2.txt'
  test_producto_cartesiano()
