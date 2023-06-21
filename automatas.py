#!/usr/bin/env python3
from __future__ import annotations
from tabulate import tabulate
import re
import numpy as np
from graphviz import Digraph


class Node:
    def __init__(self, name, pila=[], automata=None, childs=None, parent=None):
        self.name = name
        self.a = automata
        self.pila = pila
        self.parent = parent
        self.childs = self.set_childs(self.name)

    def set_childs(self, name):
        state = name[0].split(',')
        if len(state) > 1:
            state, accion_pila, pila = state[0], state[1], self.pila
        else:
            state, pila = name[0], self.pila
        s = name[1]
        if s:
            idx_row = self.a.row.get(state)
            idx_col = self.a.col.get(s[0])
            res = self.a.delta[idx_row, idx_col]
            result = res[0].split(',')
            stack1 = True
            stack2 = True
            if isinstance(self.a, AFPD) or isinstance(self.a, AFPN):
                accion = str(result[1]).split('|')
                if len(pila) > 0 and pila[-1] == accion[0]:
                    if accion[1] != '$':
                        pila.append(accion[1])
                    else:
                        pila.pop(-1)
                elif accion[0] == '$':
                    if accion[1] != '$':
                        pila.append(accion[1])
                else:
                    stack1 = False

            s = s[1:]
            if result[0] and stack1:
                res = [[i, s, pila] for i in res]
                for idx, i in enumerate(res):
                    # print('pila hpta: ', state, s, pila)
                    n_node = Node(i, pila, automata=self.a, parent=self)
            else:
                self.back_trace(True)
        else:
            self.back_trace()

    def back_trace(self, abort=False):
        temp = []
        t = self
        while t.parent:
            if isinstance(self.a, AFPD) or isinstance(self.a, AFPN):
                salida = t.name  # + t.pila
                temp.append(salida)
            else:
                temp.append(t.name)
            t = t.parent
        temp.append(t.name)
        # path = ' -> '.join(temp[::-1])
        temp = temp[::-1]
        if abort:
            temp.append('Abortado')
        else:
            final_state = str(temp[-1][0]).split(',')[0]
            if final_state in self.a.accepting_states:
                if isinstance(self.a, AFPD):
                    if len(t.pila) == 0:
                        temp.append('Aceptacion')
                else:
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
        self.delta, self.graph = self.transitions_parser(
            alphabet, states, Delta)
        self.estados_inaccesibles = None

    def view(self):
        self.graph.view()

    def transitions_parser(self, alphabet, states, delta):
        f = Digraph('finite_state_machine', filename='fsm.gv')
        f.attr(rankdir='LR', size='8,5')

        f.attr('node', shape='circle')
        if self.init_state in self.accepting_states:
            f.attr('node', shape='doublecircle')
        f.node(self.init_state)

        f.attr('node', shape='doublecircle')
        for i in self.accepting_states:
            f.node(i)

        col_names = [i for i in alphabet] + ['$']
        self.col = {i: idx+1 for idx, i in enumerate(col_names)}
        self.row = {i: idx for idx, i in enumerate(states)}
        col_names = ['delta'] + col_names
        data = np.empty((len(self.row), len(col_names)), dtype=object)

        f.attr('node', shape='circle')

        for i in delta:
            split = re.split(r'[: > ;]', i)
            print(split)
            idx_row = int(self.row.get(split[0]))
            idx_col = int(self.col.get(split[1]))
            for i in split[2:]:
                temp = i.split(',')
                label = col_names[idx_col] + str(temp[1:])
                f.edge(split[0], temp[0], label=label)

            data[idx_row, 0] = split[0]
            data[idx_row, idx_col] = split[2:]
        print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
        return data, f

    def process(self, s):
        root = Node([self.init_state, s], [], self)

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


class AFPD(Automata):
    def __init__(self, alfabeto, alfabetPila, estados, estadoInicial, accepting_states, Delta):
        self.estados_limbo = None
        self.pila = []
        Automata.__init__(self, alfabeto, estados,
                          estadoInicial, accepting_states, Delta)


class AFPN(Automata):
    def __init__(self, alfabeto, alfabetPila, estados, estadoInicial, accepting_states, Delta):
        self.estados_limbo = None
        self.pila = []
        Automata.__init__(self, alfabeto, estados,
                          estadoInicial, accepting_states, Delta)


class AFD(Automata):
    def __init__(self, alfabeto, estados, estadoInicial, accepting_states, Delta):
        self.estados_limbo = None
        Automata.__init__(self, alfabeto, estados,
                          estadoInicial, accepting_states, Delta)

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

    @classmethod
    def hallarProductoCartesianoY(self, afd1: AFD, afd2: AFD):
        return self.hallarProductoCartesiano(afd1, afd2, "interseccion")

    @classmethod
    def hallarProductoCartesianoO(self, afd1: AFD, afd2: AFD):
        return self.hallarProductoCartesiano(afd1, afd2, "union")

    @classmethod
    def hallarProductoCartesianoDiferenciaSimetrica(self, afd1: AFD, afd2: AFD):
        return self.hallarProductoCartesiano(afd1, afd2, "diferencia simetrica")

    @classmethod
    def hallarProductoCartesiano(self, afd1: AFD, afd2: AFD, operacion: str):
        nuevosEstados = []
        llegada = []
        nuevoestadoInicial = ""
        nuevoDelta = []
        nuevosEstadosAceptacion = []
        nuevoalfabeto = afd1.alfabeto
        parejas = []
        delta1 = afd1.delta
        delta2 = afd2.delta
        for i in afd1.estados:
            for j in afd2.estados:
                parejas.append(i)
                parejas.append(j)
                nuevosEstados.append(parejas)
                parejas = []
        nuevoestadoInicial = str(nuevosEstados[0][0])+str(nuevosEstados[0][1])
        for i in nuevosEstados:
            for j in range(len(nuevoalfabeto)):
                for k in delta1:
                    if k[0] == i[0]:
                        llegada.append(k[j+1][0])
                for k in delta2:
                    if k[0] == i[1]:
                        llegada.append(k[j+1][0])
                delta = str(i[0]) + str(i[1]) + ":"+nuevoalfabeto[j] + \
                    ">"+str(llegada[0])+str(llegada[1])
                delta = str(delta)
                nuevoDelta.append(delta)
                llegada = []
                delta = ""
        if operacion == "interseccion":
            nuevosEstadosAceptacion = set(
                afd1.accepting_states) & set(afd2.accepting_states)
        elif operacion == "union":
            nuevosEstadosAceptacion = set(
                afd1.accepting_states) | set(afd2.accepting_states)
        elif operacion == "diferencia":
            nuevosEstadosAceptacion = set(
                afd1.accepting_states) - set(afd2.accepting_states)
        else:
            nuevosEstadosAceptacion = set(
                afd1.accepting_states) ^ set(afd2.accepting_states)
        for i in range(len(nuevosEstados)):
            nuevosEstados[i] = str(nuevosEstados[i][0]) + \
                str(nuevosEstados[i][1])
        return AFD(nuevoalfabeto, nuevosEstados, nuevoestadoInicial, nuevosEstadosAceptacion, nuevoDelta)

    def simplificarAFD(afdInput):
        # Componentes de M prima
        states = []
        init_state = 0
        accep_states = []
        delta = []
        # Tabla triangular
        table = np.full((len(afdInput.estados), len(
            afdInput.estados)), 'E', dtype=str)

        # La diagonal son los números de estado
        for i in range(len(table)):
            table[i][i] = i

        # Primera iteración
        for i in range(1, len(table)):
            for j in range(i):
                if ((afdInput.delta[i][0] in afdInput.accepting_states) and (afdInput.delta[j][0] not in afdInput.accepting_states) or (afdInput.delta[i][0] not in afdInput.accepting_states) and (afdInput.delta[j][0] in afdInput.accepting_states)):
                    table[i][j] = '1'

        # DEBUG, imprimimos la tabla
        '''
        print('')
        print (table)
        print('')
        '''

        # Iteración en la que vamos
        iter_number = 1

        # Variable de control para finalizar algoritmo
        marked_this_iter = True

        # Iteraciones siguientes
        while (marked_this_iter):
            iter_number += 1
            marked_this_iter = False

            for i in range(1, len(table)):
                for j in range(i):
                    # Si la celda no ha sido marcada previamente
                    if (table[i][j] == 'E'):
                        # Para cada símbolo del alfabeto
                        for k in range(len(afdInput.alfabeto)):

                            # DEBUG, estado de la evaluación de cada casilla
                            # print('Evaluating s' + str(i) + ' and s' + str(j) + ', they go to s' + afdInput.delta[i][k+1][0][1:] + ' and s' + afdInput.delta[j][k+1][0][1:])

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
            '''
            print('')
            print (table)
            print('')
            '''

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
                if (('s' + str(j)) in afdInput.accepting_states):
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

        # DEBUG, imprimir los elementos finales de M'
        '''
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
        '''

        return AFD(afdInput.alfabeto, states, init_state, accep_states, delta)


class AFN(Automata):
    def __init__(self, alfabeto, estados, estadoInicial, accepting_states, Delta):
        Automata.__init__(self, alfabeto, estados,
                          estadoInicial, accepting_states, Delta)

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
        AFN.__init__(self, alfabeto, estados,
                     estadoInicial, accepting_states, Delta)

    def __str__(self):
        return 'AFN-Lambda'

        def __str__(self):
            return 'AFN-Lambda'
