"""EL centro de salud famisalud aplica vacunas a los bebes menores de un año y la dosis aplicar depende de peso y la edad del bebe segun la siguiente formula:



realice un programa en python que le permita a la enfermera determinar con facilidad la dosis de la vacuna que debe aplicar a un bebe."""


peso=float(input("ingresa el peso del bebe:"))



edad=float(input("ingrese edad del bebe:"))

dosisvacuna=(peso +10) /(edad *10) *8

print("la dosisvacuna a aplicar es:",dosisvacuna)