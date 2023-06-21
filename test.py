from processing import read_file
from automatas import *

def test_AFD():
  input_file = './inputs/input.txt'
  a = read_file(input_file)
  a.process('abab')
  a.view()

def test_AFN():
  input_file = './inputs/afpn.txt'
  a = read_file(input_file)
  a.process('abab')
  a.view()

def test_AFNLambda():
  input_file = './inputs/afpn.txt'
  a = read_file(input_file)
  a.process('abab')
  a.view()

def test_AFNtoAFD():
  return
def test_AFNLambdaToAFN():
  return
def test_Complemento():
  return

def test_Simplificacion():
  f1 = './inputs/simplificar1.txt'
  f2 = './inputs/simplificar2.txt'
  f3 = './inputs/simplificar3.txt'
  
  print('\nSimplificación AFD:\n\nAutómata M1:\n')
  a = read_file(f1)
  print('Estado inicial: ' + str(a.init_state))
  print('Estados de aceptación: ' + str(a.accepting_states) + '\n')

  print('\nAutómata M2:\n')
  b = read_file(f2)
  print('Estado inicial: ' + str(b.init_state))
  print('Estados de aceptación: ' + str(b.accepting_states) + '\n')

  print('\nAutómata M3:\n')
  c = read_file(f3)
  print('Estado inicial: ' + str(c.init_state))
  print('Estados de aceptación: ' + str(c.accepting_states) + '\n')

  print('\nAutómata M1\':\n')
  A = AFD.simplificarAFD(a)
  print('Estado inicial: ' + str(A.init_state))
  print('Estados de aceptación: ' + str(A.accepting_states) + '\n')
  print('\nAutómata M2\':\n')
  B = AFD.simplificarAFD(b)
  print('Estado inicial: ' + str(B.init_state))
  print('Estados de aceptación: ' + str(B.accepting_states) + '\n')
  print('\nAutómata M3\':\n')
  C = AFD.simplificarAFD(c)
  print('Estado inicial: ' + str(C.init_state))
  print('Estados de aceptación: ' + str(C.accepting_states) + '\n')

def test_producto_cartesiano():
    f1 = './inputs/cartesiano1.txt'
    f2 = './inputs/cartesiano2.txt'
    a = read_file(f1)
    b = read_file(f2)
    c = AFD.hallarProductoCartesianoY(a, b)

# Taller 3
def test_AFPN():
  input_file = './inputs/afpn.txt'
  a = read_file(input_file)
  a.process('abab')
  a.process_detail('abab')
  a.procesarListaCadenas(['abab', 'aaaa'])
  a.exportar()
  a.view()

def test_AFPD():
  input_file = './inputs/afpd.txt'
  a = read_file(input_file)
  a.process('aabb')
  a.process_detail('aabb')
  a.procesarListaCadenas(['aabb', 'aaaa'])
  a.exportar()
  a.view()

def test_AF2P():
  input_file = './inputs/af2p.txt'
  a = read_file(input_file)
  a.process('aabbcc')
  a.process_detail('aabbcc')
  a.procesarListaCadenas(['aabbcc', 'aaaa'])
  a.exportar()
  a.view()
