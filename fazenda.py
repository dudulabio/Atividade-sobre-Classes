class Fazenda:
  def __init__(self, nome):
      self.nome = nome
      self.talhoes = []

  def adicionar_talhao(self, talhao):
      self.talhoes.append(talhao)

  def encontrar_talhao_maior_area(self):
      if not self.talhoes:
          return None
      return max(self.talhoes, key=lambda talhao: talhao.area)

  def encontrar_talhao_menor_area(self):
      if not self.talhoes:
          return None
      return min(self.talhoes, key=lambda talhao: talhao.area)

if __name__ == "__main__":
  talhao1 = Talhao(1, 100)
  talhao2 = Talhao(2, 150)
  fazenda1 = Fazenda("Fazenda A")
  fazenda1.adicionar_talhao(talhao1)
  fazenda1.adicionar_talhao(talhao2)
  print("Talhões da fazenda:")
  for talhao in fazenda1.talhoes:
      print(talhao)
