from alphabet import Alphabet
from automatas import *

def read_file(f_path):
  a_type = []
  alphabet = []
  stackAlphabet = []
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
    if s == '#alphabet' or s == '#tapeAlphabet':
      alphabet = Alphabet(f[i]).alphabet
    if s == '#stackAlphabet':
      stackAlphabet = Alphabet(f[i]).alphabet
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
  elif a_type == 'nfa':
    return AFN(alphabet, states, init_state, accep_states, delta)
  elif a_type == 'dpda':
    print('dpda')
    return AFPD(alphabet, stackAlphabet, states, init_state, accep_states, delta)
  elif a_type == 'pda':
    return AFPN(alphabet, stackAlphabet, states, init_state, accep_states, delta)
  elif a_type == 'msm':
    return AF2P(alphabet, stackAlphabet, states, init_state, accep_states, delta)
  elif a_type == 'tm':
    return TM(alphabet, stackAlphabet, states, init_state, accep_states, delta)
