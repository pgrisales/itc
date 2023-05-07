#!/usr/bin/env python3
from __future__ import annotations
from tabulate import tabulate
import re
import numpy as np

class Automata:
  def __init__(self, alphabet, states, init_state, accep_states, Delta):
    self.alfabeto = alphabet 
    self.estados = states 
    self.estadoInicial = init_state
    self.estadosAceptacion = accep_states 
    self.delta = self.transitions_parser(alphabet, states, Delta)
    self.estados_inaccesibles = None

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
    col = {i: idx+1 for idx, i in enumerate(col_names)}
    row = {i: idx for idx, i in enumerate(states)}
    col_names = ['delta'] + col_names 
    data = np.empty((len(row), len(col_names)), dtype=object)
    for i in delta:
      split = re.split(r'[:, >, ;]', i)
      idx_row = int(row.get(split[0]))
      idx_col = int(col.get(split[1]))
      data[idx_row, 0] = split[0]
      data[idx_row, idx_col] = str(split[2:])
      
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
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
    return

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
