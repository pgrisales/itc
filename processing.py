#!/usr/bin/env python3
from alphabet import Alphabet
from automatas import *
import tabulate
import re
import numpy as np

class Procesamiento:
  def __init__(self):
    return

  def string_process_AFD(cadena, esAceptada, listaEstadoSimboloDeProcesamiento):
    return
  # Estas tres últimas deben incluir el estado y el simbolo de cada paso
  def string_process_AFN(cadena, esAceptada, procesamientosAbortados, procesamientosAceptacion, procesamientosRechazados):
    return
  # Estas tres últimas deben incluir el estado y el simbolo de cada paso
  def string_process_AFNLambda(cadena, esAceptada, procesamientosAbortados, procesamientosAceptacion, procesamientosRechazados): 
    return

def transitions_parser(alphabet, states, delta):
  col_names = ['delta'] + ['$'] + [i for i in alphabet]
  col = {i: idx for idx, i in enumerate(col_names)}
  row = {i: idx for idx, i in enumerate(states)}
  data = [[i] for i in row]
  print(type(data[0]))
  data = [i.append([]) for j in range(len(col)-1) for i in data]
  print('data',data)
  row_idx = 0
#  delta = [re.split(r'[:, >, ;]', i) for i in delta]
  #print(delta)
  print(col)
  for i in delta:
    split = re.split(r'[:, >, ;]', i)
    idx_row = row.get(split[0])
    idx_col = col.get(split[1])
    print('#####')
    print('spli: ', split)
    print(split)
    data[idx_row][idx_col] = [split[2:]]
#    print(split)
#    print(row.get(split[0]))
#    print(col.get(split[1]))
#    print(split[2:])

#  print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

# Read input file
if __name__ == '__main__':
  a_type = []
  alphabet = []
  states = []
  init_state = []
  accep_states = []
  delta = []
  f = open('./input.txt').read().splitlines()
  a_type = f[0][2:] 
  for i in range(0, len(f)):
    if f[i][0] == '#':
      s = f[i]
      continue
    if s == '#alphabet':
      alphabet = Alphabet(f[i])
    elif s == '#states':
      states.append(f[i])
    elif s == '#initial':
      init_state = f[i]
    elif s == '#accepting':
      accep_states.append(f[i])
    elif s == '#transitions':
      delta.append(f[i])

  delta = transitions_parser(alphabet.alphabet, states, delta)
#  print('type: ', a_type)
#  print('alphabet', alphabet)
#  print('states: ', states)
#  print('init state: ', init_state)
#  print('accep_states: ', accep_states)
#  print('delta ', delta)

  if a_type == 'dfa':
    dfa = AFD(alphabet, states, init_state, accep_states, delta)
  elif a_type == 'nfa':
    nfa = AFN(alphabet, states, init_state, accep_states, delta)
  else:
    nfa_lambda = AFNLambda(alphabet, states, init_state, accep_states, delta)
    

