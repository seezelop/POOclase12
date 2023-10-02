class Automovil:
  ruedas = 4

  def __init__(self, color, marca, aceleracion):
    self.color = color
    self.marca = marca
    self.aceleracion = aceleracion
    self.velocidad = 0


coche1 = Automovil("celeste", "Fiat", 210)

print(coche1.ruedas)

print(f'el coche tiene una aceleracion de {coche1.aceleracion}')

coche1.aceleracion = 30
print(f'el coche tiene una aceleracion de {coche1.aceleracion}')
