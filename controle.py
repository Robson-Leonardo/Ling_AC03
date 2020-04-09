# Atividade Contínua 3
# Robson Leonardo Lino 1901595
# Victor Hugo Tarriga Gomes 1901395


class Elevador:

    def __init__(self, capacidade, atendidos):
        aux = False
        try:
            for andar in atendidos:
                if andar == 0:
                    aux = True
        except:
            raise Exception("Elevador precisa atender o andar zero e mais e outro andar no minimo")

        if aux == False:
            raise Exception("Elevador não atende andar 0")
        else:
            self.__capacidade = capacidade
            self.__andar_atual = 0
            self.__quantidade_pessoas = 0
            atendidos = list(atendidos)
            atendidos.sort()
            atendidos = tuple(atendidos)
            self.__atendidos = atendidos

    def subir(self):
        for andar in self.__atendidos:
            if andar > self.__andar_atual:
                self.__andar_atual = andar
                break

    def printelevador(self):
        print("Capacidade maxima {0}, andares atendidos {1}, está no andar {2} com {3} pessoas.".format(self.__capacidade,
                                                                                                        self.__atendidos,
                                                                                                        self.__andar_atual,
                                                                                                        self.__quantidade_pessoas))
        

