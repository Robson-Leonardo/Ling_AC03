import controle



ElevadorEsquerda = controle.Elevador(10, [0, 1, 3, 5])

ElevadorDireita = controle.Elevador(10, [-2, -1, 0, 2 , 4, 5, 6])

Predio1 = controle.Predio(6, -2, [ElevadorDireita, ElevadorEsquerda])


ElevadorDireita.deslocar_para(1)
ElevadorEsquerda.deslocar_para(-1)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")
#print(ElevadorEsquerda)

andar = 5
Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")

andar = 3
Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")

andar = -2

Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")

andar = 3

Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")

andar = 4

Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")

andar = 0

Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")

andar = -1

Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")

andar = 1

Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")

andar = 0

Predio1.chamar(andar)
print("chamou no", andar)


print("Elevador direita está no andar:", ElevadorDireita.get_andar_atual(), "e com ", ElevadorDireita.get_quantidade_pessoas(), "pessoas")
print("Elevador esquerda está no andar:", ElevadorEsquerda.get_andar_atual(), "e com ", ElevadorEsquerda.get_quantidade_pessoas(), "pessoas")
