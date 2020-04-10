# Atividade Contínua 3
# Robson Leonardo Lino 1901595
# Victor Hugo Tarriga Gomes 1901395


class Elevador:

    def __init__(self, capacidade, atendidos):
        aux = False

        for andar in atendidos:
            if andar == 0:
                aux = True

        if aux == False:
            atendidos.append(0)

        self.__capacidade = capacidade
        self.__andar_atual = 0
        self.__quantidade_pessoas = 0
        self.__atendidos = atendidos            

    def subir(self):
        crescente = self.__atendidos
        crescente.sort()
        for andar in crescente:
            if andar > self.__andar_atual:
                self.__andar_atual = andar
                print("Elevador subiu para o andar", self.__andar_atual)
                break
    
    def descer(self):
        invertida = self.__atendidos
        invertida.sort(reverse=True)
        for andar in invertida:
            if andar < self.__andar_atual:
                self.__andar_atual = andar
                print("Elevador desceu para o andar", self.__andar_atual)
                break
        

    def printelevador(self):
        print("Capacidade maxima {0}, andares atendidos {1}, está no andar {2} com {3} pessoas.".format(self.__capacidade,
                                                                                                        self.__atendidos,
                                                                                                        self.__andar_atual,
                                                                                                        self.__quantidade_pessoas))
        

