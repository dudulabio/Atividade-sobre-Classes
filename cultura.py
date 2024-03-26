class Cultura:
  def __init__(self, nome):
      self.nome = nome

  def __str__(self):
      return f"Cultura: {self.nome}"

if __name__ == "__main__":
  cultura1 = Cultura("Milho")
  print(cultura1)
