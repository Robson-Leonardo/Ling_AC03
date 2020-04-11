#  Atividade Contínua 3
# Robson Leonardo Lino 1901595
# Victor Hugo Tarriga Gomes 1901395


class Elevador:

    def __init__(self, capacidade, andares):
        if 0 not in andares:
            andares.append(0)
    
        self.__capacidade = capacidade
        self.__andar_atual = 0
        self.__quantidade_pessoas = 0
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
                break

    def descer(self):
        invertida = self.__atendidos
        invertida.sort(reverse=True)
        for andar in invertida:
            if andar < self.__andar_atual:
                self.__andar_atual = andar
                break

    def deslocar_para(self, andar):
        if andar in self.__atendidos:
            self.__andar_atual = andar

    def get_atendidos(self):
        return self.__atendidos

    def get_andar_atual(self):
        return self.__andar_atual

    def get_quantidade_pessoas(self):
        return self.__quantidade_pessoas


class Predio:

    def __init__(self, andar_alto, andar_baixo, elevadores):
        andares_atendidos = []
        # Condição para entrar somente uma lista e que não seja vazia
        if elevadores != [] and type(elevadores) == list:
            # Percorre todos os andares do Prédio
            for andar_atual in range(andar_baixo, andar_alto+1):
                # Pega o elevador
                for atual in elevadores:
                    # Identifica se o andar que está no
                    # for é atendidos por algum elevador
                    if andar_atual in atual.get_atendidos():
                        # Monta uma lista de andares atendidos
                        andares_atendidos.append(andar_atual)
                # Percorre todos os andares do Prédio
            for andar_atual2 in range(andar_baixo, andar_alto+1):
                # Identifica se o andar da vez está dentro da lista de
                # andares atendidos pelo os elevadores
                if andar_atual2 not in andares_atendidos:
                    raise ValueError("Andar {0},\
                                     não foi atendido.".format(andar_atual2))

            # Começo da logica para identificar se tem algum elevador que
            #  possui um andar inexistente no prédio
            for andar_atual in range(andar_baixo, andar_alto+1):
                # Pega o elevador
                for atual in elevadores:
                    # Percorre a lista de andares atendidos do elevador
                    for andar_atendido in atual.get_atendidos():
                        if (andar_atendido not in
                                range(andar_baixo, andar_alto+1)):
                            # Monta uma lista de andares atendidos
                            raise ValueError("Andar {0} que é atendido por um\
                                             elevador porém é inexistente\
                                             no prédio".format(andar_atendido))
        else:
            raise ValueError("Lista vazia ou não é uma lista")

        self.__elevadores = elevadores
        self.__andar_alto = andar_alto
        self.__andar_baixo = andar_baixo

    def chamar(self, andar):
        # Verifica se o andar chamado é um andar valido pelo
        if andar in range(self.__andar_baixo, self.__andar_alto+1):
            # Cria uma lista de o elevador candidato a ser chamado
            mais_proximo = [None, 999, None, 0]
            # Cria uma lista que contém todos os elevadores que
            # atendem o andar chamado
            elev_atendem = []
            # Percorre todos os elevadores do Prédio
            for atual in self.__elevadores:
                # Verifica que o andar chamado é atendido pelo o Prédio
                if andar in atual.get_atendidos():
                    # Identifica se o elevador vai descer ou subir
                    if atual.get_andar_atual() < andar:
                        # Adiciona o elevador na lista de
                        # elevadores que atentem,
                        # colocando o objeto na primeira
                        # posição, a quanitadade de andares que precisa se
                        # deslocar, se vai subir ou descer e a
                        # quantidade de pessoas dentro do elevador
                        elev_atendem.append([atual,
                                             andar - atual.get_andar_atual(),
                                             "Subir",
                                             atual.get_quantidade_pessoas()])
                    else:
                        elev_atendem.append([atual,
                                             atual.get_andar_atual() - andar,
                                             "Descer",
                                             atual.get_quantidade_pessoas()])
            # Percorre a lista de elevadores que atendem o andar chamado.
            for elevador_da_vez in elev_atendem:
                # Verifica se a quantidade de andares que precisa
                # andar do elevador candidato é maior do que a quantidade
                # de andares que precisa andar do elevador da vez no for
                if mais_proximo[1] > elevador_da_vez[1]:
                    # se for menor atualiza a lista de candidato
                    mais_proximo = [elevador_da_vez[0],
                                    elevador_da_vez[1],
                                    elevador_da_vez[2],
                                    elevador_da_vez[3]]
                # Se não for menor, verifica se ele vai descer
                elif mais_proximo[1] == elevador_da_vez[1]:
                    # Verifica se o elevador da vez vai descer, e ja aproveita
                    # e verificar se candidato não vai descer
                    if (elevador_da_vez[2] == "Descer" and not
                            mais_proximo[2] == "Descer"):
                        # Se o elevador da vez for descer e o
                        # candidato for subir, atualiza a lista do candidato
                        mais_proximo = [elevador_da_vez[0],
                                        elevador_da_vez[1],
                                        elevador_da_vez[2],
                                        elevador_da_vez[3]]
                    # Se ambos forem descer, verifica a quantidade de
                    # pessoas do candidato e do elevador atual
                    elif (mais_proximo[1] == elevador_da_vez[1] and
                            elevador_da_vez[2] == mais_proximo[2]):
                        if mais_proximo[3] > elevador_da_vez[3]:
                            mais_proximo = [elevador_da_vez[0],
                                            elevador_da_vez[1],
                                            elevador_da_vez[2],
                                            elevador_da_vez[3]]

                # Se todos os if falarem, ou seja, empatou a porra toda,
                # pega o primeiro elevador da lista de elevadore que atendem
                else:
                    mais_proximo = elev_atendem[0]

            # Move o elevador escolhido para o andar que chamou
            mais_proximo[0].deslocar_para(andar)

            if andar > 0:
                self.__embarque(mais_proximo[0])
            elif andar <= 0:
                self.__desembarque(mais_proximo[0])
        else:
            raise ValueError("Andar chamado não existe.")

    def __embarque(self, indice_elevador):
        indice_elevador.entrar()

    def __desembarque(self, indice_elevador):
        for a in range(0, indice_elevador.get_quantidade_pessoas() + 1):
            indice_elevador.sair()
