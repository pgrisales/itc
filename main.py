#!/usr/bin/env python3
from alphabet import Alphabet
from automatas import *

# Read input file
if __name__ == '__main__':
  a_type = []
  alphabet = []
  states = []
  init_state = []
  accep_states = []
  delta = []
  f = open('./input2.txt').read().splitlines()
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
    dfa = AFD(alphabet, states, init_state, accep_states, delta)
    dfa.process('aabb') 
  elif a_type == 'nfa':
    nfa = AFN(alphabet, states, init_state, accep_states, delta)
    nfa.process('aabb') 
  else:
    nfa_lambda = AFNLambda(alphabet, states, init_state, accep_states, delta)
    nfa_lambda.process('aabb') 
