class Safra:
  def __init__(self, nome, ano_inicio, ano_fim, cultura):
      self.nome = nome
      self.ano_inicio = ano_inicio
      self.ano_fim = ano_fim
      self.cultura = cultura

  def __str__(self):
      return f"Safra: {self.nome}, Ano de Início: {self.ano_inicio}, Ano de Fim: {self.ano_fim}, Cultura: {self.cultura}"

if __name__ == "__main__":
  cultura1 = Cultura("Milho")
  safra1 = Safra("Safra de Verão", 2024, 2025, cultura1)
  print(safra1)
