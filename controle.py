# Atividade Contínua 3
# Robson Leonardo Lino 1901595
# Victor Hugo Tarriga Gomes 1901395


class Elevador:

    def __init__(self, capacidade, andares):
        aux = False

        for andar in andares:
            if andar == 0:
                aux = True

        if aux == False:
            andares.append(0)

        self.__capacidade = capacidade #Quantidade maxima de pessoas
        self.__andar_atual = 0
        self.__quantidade_pessoas = 0 #Quantidade de pessoas atual
        self.__atendidos = andares            

    def entrar(self):
        if not self.__quantidade_pessoas == self.__capacidade:
            self.__quantidade_pessoas += 1

    def sair(self):
        if not self.__quantidade_pessoas == 0:
            self.__quantidade_pessoas -= 1 

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
        
    def deslocar_para(self, andar):
        if andar in self.__atendidos:
            self.__andar_atual = andar
        
    def getAtendidos(self):
        return self.__atendidos
        

    def printelevador(self):
        print("Capacidade maxima {0}, andares atendidos {1}, está no andar {2} com {3} pessoas.".format(self.__capacidade,
                                                                                                        self.__atendidos,
                                                                                                        self.__andar_atual,
                                                                                                        self.__quantidade_pessoas))
        

class Predio:

    def __init__(self, andar_alto, andar_baixo, elevadores):
        andaresAtendidos = []
        if elevadores != [] and type(elevadores) == list:
            for andarAtual in range(andar_baixo, andar_alto+1):
                for ElevadorAtual in elevadores:
                    if andarAtual in ElevadorAtual.getAtendidos():
                        andaresAtendidos.append(andarAtual)
            for andarAtual2 in range(andar_baixo, andar_alto+1):
                if not andarAtual2 in andaresAtendidos:
                    raise ValueError
        else:
            raise ValueError
        
        self.__elevadores = elevadores
        self.__andar_alto = andar_alto
        self.__andar_baixo = andar_baixo
        
            

    def chamar(self, andar):
        return ""


    def __embarque(self, indice_elevador):
        return ""

    def __desembarque(self, indice_elevador):
        return ""

    def printPredio(self):
        print("Andar alto {0}, andar baixo {1}, com os elevadores {2}".format(self.__andar_alto, 
                                                                              self.__andar_baixo, 
                                                                              self.__elevadores))
        for x in self.__elevadores:
            x.printelevador()