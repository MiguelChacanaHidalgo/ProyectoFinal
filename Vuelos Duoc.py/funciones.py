asientos = [[0] * 6 for _ in range(7)]

def mostrar_asientos():
    print("Asientos disponibles:")
    for i in range(len(asientos)):
        for c in range(len(asientos[i])):
            if asientos[i][c] == 0:
                print(i * 6 + c + 1, end=" ")
            else:
                print("X", end=" ")
        print()
    print()
