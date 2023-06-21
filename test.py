class Prueba:
  def __init__(self):
    return
  def probarAFD():
    return
  def probarAFN():
    return
  def probarAFNLambda():
    return
  def main():
    return
  def probarAFNtoAFD():
    return
  def probarAFNLambdaToAFN():
    return
  def probarComplemento():
    return
  def probarProductoCartesiano():
    return
  def probarSimplificacion():
    return
class Validacion:
  def __init__(self):
    return
  def validarAFNtoAFD(listaDeAFNs):
    return
  def validarAFNLambdaToAFN(listaDeAFNLambdas):
    return

def test_procces_string():
  return

def test_producto_cartesiano():
    f1 = './cartesiano1.txt'
    f2 = './cartesiano2.txt'
    a = read_file(f1)
    b = read_file(f2)
    c = AFD.hallarProductoCartesianoY(a, b)

def probarSimplificacion():
  f1 = './simplificar1.txt'
  f2 = './simplificar2.txt'
  f3 = './simplificar3.txt'

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