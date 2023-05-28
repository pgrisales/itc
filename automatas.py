#!/usr/bin/env python3
from __future__ import annotations
from tabulate import tabulate
import re
import numpy as np
from graphviz import Digraph


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
        # path = ' -> '.join(temp[::-1])
        temp = temp[::-1]
        if abort:
            temp.append('Abortado')
        else:
            if temp[-1][0] in self.a.accepting_states:
                temp.append('Aceptacion')
            else:
                temp.append('No aceptacion')
        # temp = ' -> '.join([', '.join(i) for i in temp])
        print(temp)
        # return path

    def __str__(self):
        return str(self.name)


class Automata:
    def __init__(self, alphabet, states, init_state, accepting_states, Delta):
        self.alfabeto = alphabet
        self.estados = states
        self.init_state = init_state
        self.accepting_states = accepting_states
        self.row = {}
        self.col = {}
        self.delta, self.graph = self.transitions_parser(alphabet, states, Delta)
        self.estados_inaccesibles = None

    def view(self):
      self.graph.view()

    def transitions_parser(self, alphabet, states, delta):
      f = Digraph('finite_state_machine', filename='fsm.gv')
      f.attr(rankdir='LR', size='8,5')

      f.attr('node', shape='circle')
      f.node(self.init_state)

      f.attr('node', shape='doublecircle')
      print(self.accepting_states)
      for i in self.accepting_states:
        f.node(i)

      col_names =  [i for i in alphabet] + ['$']
      self.col = {i: idx+1 for idx, i in enumerate(col_names)}
      self.row = {i: idx for idx, i in enumerate(states)}
      col_names = ['delta'] + col_names 
      data = np.empty((len(self.row), len(col_names)), dtype=object)

      f.attr('node', shape='circle')

      for i in delta:
        split = re.split(r'[:, >, ;]', i)
        idx_row = int(self.row.get(split[0]))
        idx_col = int(self.col.get(split[1]))
        for i in split[2:]:
          f.edge(split[0], i, label=col_names[idx_col])

        data[idx_row, 0] = split[0]
        data[idx_row, idx_col] = split[2:]
      print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
      return data, f

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


class AFD(Automata):
    def __init__(self, alfabeto, estados, estadoInicial, accepting_states, Delta):
        self.estados_limbo = None
        Automata.__init__(self, alfabeto, estados, estadoInicial, accepting_states, Delta)

    def verificarCorregirCompletitudAFD(self):
        return

    def hallarEstadosLimbo(self):
        return

    def __str__(self):
        return 'AFD'

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
    def __init__(self, alfabeto, estados, estadoInicial, accepting_states, Delta):
        Automata.__init__(self, alfabeto, estados, estadoInicial, accepting_states, Delta)

    #  def __init__(self, nombreArchivo):
    #    return

    def __str__(self):
        return 'AFN'

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

    def procesarListaCadenasConversion(self, listaCadenas, nombreArchivo, imprimirPantalla):
        return
class AFNLambda(Automata):
  def __init__(self, alfabeto, estados, estadoInicial, accepting_states, Delta):
    AFN.__init__(self, alfabeto, estados, estadoInicial, accepting_states, Delta)
  def __str__(self):
    return  'AFN-Lambda'

    def __str__(self):
        return 'AFN-Lambda'
