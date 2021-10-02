from tabela_tarefas import Tarefa


class Fila:
    def __init__(self, valor_inicial=None):
        if valor_inicial is None:
            valor_inicial = []
        elif type(valor_inicial) is not list:
            raise Exception('Fila inicializada com valor que nao eh lista')
        self.valor = valor_inicial

    def rotacionar(self):
        if len(self.valor) > 1:
            self.valor = self.valor[1:] + self.valor[0]

    def __iter__(self):
        return iter(self.valor)

    def __getitem__(self, index):
        return self.valor[index]


class FilaMoradores(Fila):
    def __init__(self, valor_inicial=None):
        super().__init__(valor_inicial)

    def pega_proximo_morador_a_pegar_tarefa(self):
        """
        Seleciona o morador na primeira posição da fila, coloca no final da fila, e retorna o morador.
        :return: Morador
        """
        morador = self.valor.pop(0)
        self.valor.append(morador)
        return morador


class FilaIndividual(Fila):
    def __init__(self, valor_inicial=None):
        if valor_inicial is None:
            valor_inicial = list(Tarefa)
        super().__init__(valor_inicial)

    def pega_primeira_da_lista_e_poe_no_fim_da_fila(self, lista):
        for i in range(len(Tarefa)):
            if self.valor[i] in lista:
                indice_tarefa_escolhida = i
                tarefa_escolhida = self.valor[i]
                break
        self.valor.pop(indice_tarefa_escolhida)
        self.valor.append(tarefa_escolhida)
        return tarefa_escolhida


