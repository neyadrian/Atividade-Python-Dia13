pesoSaco: float; gramas: float; pesoTotal: float

pesoSaco = float(input("Digite o peso do saco de ração: "))
gramas = float(input("Digite a quantidade de ração colocada para cada gato: "))

pesoTotal = pesoSaco - (gramas*2)/5

print(f"Restará {pesoTotal} KG depois de 5 dias.")