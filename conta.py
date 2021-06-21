class  Conta:

  def __init__(self, numero, titular, saldo, limite):
    print("Contruindo objeto ... {}".format(self))
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite

  def extrato(self):
    print("Saldo de {} de titular {}".format(self.__saldo, self.__titular))
  
  def deposita(self, valor):
    self.__saldo += valor

  def pode_sacar(self):
    pass

  def saca(self, valor):
    if(valor <= (self.__saldo + self.__limite)):
      self.__saldo -= valor
    else:
      print("O valor {} passou o limite".format(valor))

  def transfere(self, valor, origem, destino):
    self.saca(valor)
    destino.deposita[valor]

  @property
  def saldo(self):
    return self.__saldo
  
  @property
  def titular(self):
    return self.__titular

  @property
  def limite(self):
    return self.__limite

  @limite.setter
  def limite(self, limite):
    self.__limite = limite

  @staticmethod
  def codigo_banco():
    return "001"

  @staticmethod
  def codigos_bancos():
    return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}