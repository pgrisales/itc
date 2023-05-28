#!/usr/bin/env python3
from __future__ import annotations
from tabulate import tabulate
import re
import numpy as np
import graphviz

class Node:
  def __init__(self, name, automata=None, childs=None, parent=None):
    self.name = name
    self.a = automata
    self.parent = parent
    self.childs = self.set_childs(self.name)

  def set_childs(self, name):
    state = name[0]
    s = name[1]
    if s:
      idx_row = self.a.row.get(state)
      idx_col = self.a.col.get(s[0])
      res = self.a.delta[idx_row, idx_col]
      s = s[1:]
      if res:
        res = [[i, s] for i in res]
        for idx, i in enumerate(res):
          n_node = Node(i, automata=self.a, parent=self)
      else:
        self.back_trace(True)
    else:
      self.back_trace()

  def back_trace(self, abort=False):
    temp = []
    t = self
    while t.parent:
      temp.append(t.name)
      t = t.parent
    temp.append(t.name)
    #path = ' -> '.join(temp[::-1])
    temp = temp[::-1]
    if abort:
      temp.append('Abortado')
    else:
      if temp[-1][0] in self.a.estadosAceptacion:
        temp.append('Aceptacion')
      else: 
        temp.append('No aceptacion')
    #temp = ' -> '.join([', '.join(i) for i in temp])
    print(temp)
    #return path

  def __str__(self):
    return str(self.name)

class Automata:
  def __init__(self, alphabet, states, init_state, accep_states, Delta):
    self.alfabeto = alphabet 
    self.estados = states 
    self.init_state = init_state
    self.estadosAceptacion = accep_states 
    self.row = {}
    self.col = {}
    self.delta = self.transitions_parser(alphabet, states, Delta)
    self.estados_inaccesibles = None
  
  def childs(self, temp):
    return 

  def process(self, s):
    root = Node([self.init_state, s], self)

  def exportar(self, archivo):
    return 
  def procesarCadena(self, cadena):
    return False
  def procesarCadenaConDetalles(self, cadena):
    return False 
  def procesarListaCadenas(self, listaCadenas, nombreArchivo, imprimirPantalla):
    return 
  def hallarEstadosInaccesibles(self):
    return 

  def transitions_parser(self, alphabet, states, delta):
    col_names =  [i for i in alphabet] + ['$']
    self.col = {i: idx+1 for idx, i in enumerate(col_names)}
    self.row = {i: idx for idx, i in enumerate(states)}
    col_names = ['delta'] + col_names 
    data = np.empty((len(self.row), len(col_names)), dtype=object)
    for i in delta:
      split = re.split(r'[:, >, ;]', i)
      idx_row = int(self.row.get(split[0]))
      idx_col = int(self.col.get(split[1]))
      data[idx_row, 0] = split[0]
      data[idx_row, idx_col] = split[2:]
      
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

    # DEBUG
    print('')
    print('data:')
    print(data)
    print('')
    print('states:')
    print(states)
    print('')

    return data

class AFD(Automata):
  def __init__(self, alfabeto, estados, estadoInicial, estadosAceptacion, Delta):
    self.estados_limbo = None
    Automata.__init__(self, alfabeto, estados, estadoInicial, estadosAceptacion, Delta)

#  def __init__(self, nombreArchivo):
#    return

  def verificarCorregirCompletitudAFD(self):
    return
  def hallarEstadosLimbo(self):
    return
  def __str__(self):
    return  'AFD'
  def imprimirAFDSimplificado(self):
    return
  def hallarComplemento(self, afdInput: AFD):
    return 
  def hallarProductoCartesianoY(self, afd1: AFD, afd2: AFD):
    return
  def hallarProductoCartesianoO(self, afd1: AFD, afd2: AFD):
    return
  def hallarProductoCartesianoDiferenciaSimetrica(self, afd1: AFD, afd2: AFD):
    return
  def hallarProductoCartesiano(self, afd1: AFD, afd2: AFD, operacion: str):
    return 
  
  def simplificarAFD(self, afdInput: AFD):
    # Componentes de M prima
    states = []
    init_state = 0
    accep_states = []
    delta = []
    # Tabla triangular
    table = np.full((len(afdInput.estados), len(afdInput.estados)), 'E', dtype=str)

    # La diagonal son los números de estado
    for i in range(len(table)):
      table[i][i] = i

    # Primera iteración
    for i in range(1, len(table)):
      for j in range(i):
        if ((afdInput.delta[i][0] in afdInput.estadosAceptacion) and (afdInput.delta[j][0] not in afdInput.estadosAceptacion) or (afdInput.delta[i][0] not in afdInput.estadosAceptacion) and (afdInput.delta[j][0] in afdInput.estadosAceptacion)):
          table[i][j] = '1'

    # DEBUG, imprimimos la tabla
    print('')
    print (table)
    print('')
    
    # Iteración en la que vamos
    iter_number = 1

    # Variable de control para finalizar algoritmo
    marked_this_iter = True

    # Iteraciones siguientes
    while(marked_this_iter):
      iter_number += 1
      marked_this_iter = False

      for i in range(1, len(table)):
        for j in range(i):
          # Si la celda no ha sido marcada previamente
          if (table[i][j] == 'E'):
            # Para cada símbolo del alfabeto
            for k in range(len(afdInput.alfabeto)):

              # DEBUG
              print('Evaluating s' + str(i) + ' and s' + str(j) + ', they go to s' + afdInput.delta[i][k+1][0][1:] + ' and s' + afdInput.delta[j][k+1][0][1:])

              # Verificamos si debemos marcar la celda
              s1 = int(afdInput.delta[i][k+1][0][1:])
              s2 = int(afdInput.delta[j][k+1][0][1:])
              if (s1 == 0 or s2 == len(afdInput.estados)):
                if (table[s2][s1] != 'E'):
                  # Marcamos la celda escribiendo la iteración actual
                  table[i][j] = str(iter_number)
                  # Debemos hacer al menos una iteración más
                  marked_this_iter = True
                  break
              else:
                if ((s1 != s2) and table[s1][s2] != 'E'):
                  # Marcamos la celda escribiendo la iteración actual
                  table[i][j] = str(iter_number)
                  # Debemos hacer al menos una iteración más
                  marked_this_iter = True
                  break

      # DEBUG, imprimimos la tabla al final de cada iteración
      print('')
      print (table)
      print('')

    # Calculamos los estados de M' y las clases de equivalencia
    accounted_for = np.full(len(afdInput.estados), False, dtype=bool)
    new_state = 0
    equivalence = {}
    # Para cada columna (estado) de la tabla triangular
    for j in range(len(table)):
      # Si este estado no pertenece ya a una clase de equivalencia
      if (not accounted_for[j]):
        # Añadir estado nuevo
        accounted_for[j] = True
        states.append('s' + str(new_state))
        # Armar la clase de equivalencia a la que pertenecerá
        equivalence['s' + str(new_state)] = {j}
        # Para cada relación con otros estados
        for i in range(j + 1, len(table)):
          # Si hay un estado i equivalente a j
          if (table[i][j] == 'E'):
            # Añadirlo a la misma clase de equivalencia
            equivalence['s' + str(new_state)].add(i)
            # Marcar estado i como usado
            accounted_for[i] = True
        # Potencial siguiente estado de M'
        new_state += 1
    
    # Estado inicial
    for i in equivalence:
      if (int(afdInput.init_state[1:]) in equivalence[i]):
        init_state = i
        break

    # Estados de aceptación
    # Para cada estado i de M'
    for i in equivalence:
      # Para cada estado j de M que forma parte del estado i de M'
      for j in equivalence[i]:
        # Si algun estado j es de aceptación, i es de aceptación
        if (('s' + str(j)) in afdInput.estadosAceptacion):
          accep_states.append(i)
          break

    # Delta
    # Para cada estado i de M'
    for i in equivalence:
      # Con un estado j de M cualquiera perteneciente a i
      for j in equivalence[i]:
        origin_state = j
        break

      # DEBUG
      # print("Checking " + i + ", chosen origin state is s" + str(origin_state))

      # Para cada símbolo del alfabeto
      for k in range(len(afdInput.alfabeto)):
        target_state = int(afdInput.delta[origin_state][k+1][0][1:])

        # DEBUG
        # print("Checking simbol " + afdInput.alfabeto[k] + ", target state is " + str(target_state))

        # Hallar la transición d'(i,k)
        for j in equivalence:
          if (target_state in equivalence[j]):
            delta.append(i + ':' + afdInput.alfabeto[k] + '>' + j)
            break

    # DEBUG
    print('Equivalence classes:')
    print(equivalence)
    print('')
    print('Final states:')
    print(states)
    print('')
    print('Initial state:')
    print(init_state)
    print('')
    print('Acceptance states:')
    print(accep_states)
    print('')
    print('Final Delta:')
    print(delta)
    print('')

    return AFD(afdInput.alfabeto, states, init_state, accep_states, delta)

class AFN(Automata):
  def __init__(self, alfabeto, estados, estadoInicial, estadosAceptacion, Delta):
    Automata.__init__(self, alfabeto, estados, estadoInicial, estadosAceptacion, Delta)

#  def __init__(self, nombreArchivo):
#    return

  def __str__(self):
    return  'AFN'
  def imprimirAFNSimplificado(self):
    return
  def AFNtoAFD(self, afn: AFN):
    return
  def computarTodosLosProcesamientos(self, cadena, nombreArchivo):
    return
  def procesarCadenaConversion(self, cadena):
    return False
  def procesarCadenaConDetallesConversion(self, cadena):
    return False
  def procesarListaCadenasConversion(self, listaCadenas,nombreArchivo, imprimirPantalla):
    return

class AFNLambda(Automata):
  def __init__(self, alfabeto, estados, estadoInicial, estadosAceptacion, Delta):
    AFN.__init__(self, alfabeto, estados, estadoInicial, estadosAceptacion, Delta)
  def __str__(self):
    return  'AFN-Lambda'
