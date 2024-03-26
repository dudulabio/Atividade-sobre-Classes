class Plantio:
  def __init__(self, data_plantio, hectares_plantados, talhao, safra):
      self.data_plantio = data_plantio
      self.hectares_plantados = hectares_plantados
      self.talhao = talhao
      self.safra = safra

if __name__ == "__main__":
  talhao1 = Talhao(1, 100)
  cultura1 = Cultura("Milho")
  safra1 = Safra("Safra de Verão", 2024, 2025, cultura1)
  plantio1 = Plantio("2024-03-25", 80, talhao1, safra1)
  print(plantio1)
