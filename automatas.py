#!/usr/bin/env python3
from __future__ import annotations

class Automata:
  def __init__(self, alfabeto, estados, estadoInicial, estadosAceptacion,Delta):
    self.alfabeto = alfabeto
    self.estados = estados
    self.estadoInicial = estadoInicial
    self.estadosAceptacion = estadosAceptacion
    self.delta = Delta
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
