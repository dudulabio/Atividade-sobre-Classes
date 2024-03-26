class Talhao:
  def __init__(self, numero, area):
      self.numero = numero
      self.area = area

  def __str__(self):
      return f"Talhão: {self.numero}, Área: {self.area} hectares"

if __name__ == "__main__":
  talhao1 = Talhao(1, 100)
  print(talhao1)
