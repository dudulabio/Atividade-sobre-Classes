class Trator:
  def __init__(self, marca, modelo, cor, potencia):
      self.marca = marca
      self.modelo = modelo
      self.cor= cor
      self.potencia = potencia

  def __str__(self):
      return f"Trator:{self.marca}{self.modelo},Ano:{self.cor},Potência:{self.potencia}"

if __name__ == "__main__":
  trator1 = Trator('John Deere','Trator de Arado', 'Vermelho', '9000')
  print(trator1)
