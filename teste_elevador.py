import controle

ElevadorEsquerda = controle.Elevador(10, [0, 1, 3, 5, 6])

ElevadorDireita = controle.Elevador(10, [-2, -1, 0, 1, 2, 3, 4, 5])

Elevador1 = controle.Elevador(10, [-4, -2, 0, 2, 4, 6, 8, 10, 12])
Elevador2 = controle.Elevador(10,[-3, -1, 0, 1, 3, 5, 7, 9, 11, 13, 15])
elevador3 = controle.Elevador(10, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14])

Predio1 = controle.Predio(15, -4, [Elevador1, Elevador2, elevador3])


Elevador1.deslocar_para(10)
Elevador2.deslocar_para(-3)
elevador3.deslocar_para(4)

Elevador1.entrar()
Elevador2.entrar()
Elevador2.entrar()
elevador3.entrar()
elevador3.entrar()
elevador3.entrar()

print("Elevador1 está no andar:", Elevador1.get_andar_atual(), "e com ", Elevador1.get_quantidade_pessoas(), "pessoas")
print("Elevador2 está no andar:", Elevador2.get_andar_atual(), "e com ", Elevador2.get_quantidade_pessoas(), "pessoas")
print("Elevador3 está no andar:", elevador3.get_andar_atual(), "e com ", elevador3.get_quantidade_pessoas(), "pessoas")

Predio1.chamar(11)
print("CHAMOU")

print("Elevador1 está no andar:", Elevador1.get_andar_atual(), "e com ", Elevador1.get_quantidade_pessoas(), "pessoas")
print("Elevador2 está no andar:", Elevador2.get_andar_atual(), "e com ", Elevador2.get_quantidade_pessoas(), "pessoas")
print("Elevador3 está no andar:", elevador3.get_andar_atual(), "e com ", elevador3.get_quantidade_pessoas(), "pessoas")
