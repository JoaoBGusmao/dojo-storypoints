## Resumo
Dado um projeto quebrado em demandas e estimado em story points, devemos calcular qual
a data do final do projeto.
*Por segurança, adicione uma gordurinha de 1 dia nos dias necessário*

## Saída do programa:
A saída deve representar a data final do projeto, partindo de hoje.

## Classe Person (representa 1 funcionário)

```
class Person(object):
	def __init__(self, name, storyPointsDay):
		self.name = name
		self.storyPointsDay = storyPointsDay

	def getName(self):
		return self.name

	def getStoryPointsDay(self):
		return self.storyPointsDay
```

## Exemplo de entrada e saída
### Entrada:
Lista de funcionários e seus storypoints:
Nome: João
Storypoints/dia: 8

Nome: Vinna
Storypoints/dia: 8

Nome: Jonathan
Storypoints/dia: 13

Story point das demandas:
8, 3, 5, 13, 2, 2, 1, 5, 13, 20

### Saída
2018-04-07 (com gordurinha)