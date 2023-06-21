from processing import read_file

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

  print('')
  print('Autómata M1:')
  print('')
  a = read_file(f1)
  print('')
  print('Autómata M2:')
  print('')
  b = read_file(f2)
  print('')
  print('Autómata M3:')
  print('')
  c = read_file(f3)

  print('')
  print('Autómata M1\':')
  print('')
  AFD.simplificarAFD(a)
  print('')
  print('Autómata M2\':')
  print('')
  AFD.simplificarAFD(b)
  print('')
  print('Autómata M3\':')
  print('')
  AFD.simplificarAFD(c)

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
