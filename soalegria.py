try:
    with open("happy.txt", "w") as arquivo:
        arquivo.write("Só alegria hahaha")
        arquivo.close()
        print("Tudo na vida tem vantagens e desvantagens")
except:
        print("Algo deu errado")


