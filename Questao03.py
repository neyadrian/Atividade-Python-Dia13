altDegrau: float; alt: float; altFinal: float

altDegrau = float(input("Digite a altura de cada degrau: "))
alt = float(input("Digite a altura que você pretende chegar: "))

altFinal = alt / altDegrau

print(f"Você nessecitará subir {altFinal} degraus para chegar na sua meta.")