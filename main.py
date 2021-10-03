from enum import Enum
import pandas as pd


class Tarefa(Enum):
    COCO = ('Cocô', 1)
    PANOS = ('Panos', 1)
    LIXO = ('Lixo', 1)
    LOUCA = ('Louça', 2)


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


class Morador:
    def __init__(self, nome, fila_tarefas=None):
        self.nome = nome
        self.fila_ind = FilaIndividual(fila_tarefas)

    def __str__(self):
        return self.nome


class TabelaTarefas:
    def __init__(self):
        self.tabela = {tarefa: [] for tarefa in Tarefa}

    def pega_tarefas_faltantes(self):
        return [tarefa for tarefa in self.tabela if len(self.tabela[tarefa]) < tarefa.value[1]]

    def atribuir_tarefa(self, tarefa: Tarefa, morador: Morador):
        self.tabela[tarefa].append(morador)

    def mostra_tabela(self):
        for tarefa, moradores in self.tabela.items():
            print(f"{tarefa.value[0]}: {','.join(map(str, moradores))}")


def extrai_filas_do_csv():
    info_filas = pd.read_csv('filas.csv')
    fila_geral = []
    for info_fila in info_filas.iterrows():
        dados_morador = info_fila[1].values
        morador = Morador(
            dados_morador[0],
            [Tarefa[nome_tarefa] for nome_tarefa in dados_morador[1:]]
        )
        fila_geral.append(morador)
    return FilaMoradores(fila_geral)


def salva_filas_no_csv(fila_geral: FilaMoradores):
    """
    Referência: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    """
    n_tipos_de_tarefas = len(Tarefa)
    dict_info = {'Nome': []}
    for n in reversed(range(n_tipos_de_tarefas)):
        dict_info['Tarefa de prioridade ' + str(n)] = []

    for morador in fila_geral:
        dict_info['Nome'].append(morador.nome)
        for n in range(n_tipos_de_tarefas):
            dict_info['Tarefa de prioridade ' + str(n)].append(morador.fila_ind[-(n+1)].name)

    df = pd.DataFrame(dict_info)
    df.to_csv('filas.csv', index=False)


def gera_tarefas():
    # Use a breakpoint in the code line below to debug your script.
    fila_geral = extrai_filas_do_csv()

    tabela_tarefas = TabelaTarefas()
    tarefas_faltantes = tabela_tarefas.pega_tarefas_faltantes()
    while len(tarefas_faltantes) > 0:
        morador = fila_geral.pega_proximo_morador_a_pegar_tarefa()
        tarefa_escolhida = morador.fila_ind.pega_primeira_da_lista_e_poe_no_fim_da_fila(tarefas_faltantes)
        tabela_tarefas.atribuir_tarefa(tarefa_escolhida, morador)

        tarefas_faltantes = tabela_tarefas.pega_tarefas_faltantes()

    tabela_tarefas.mostra_tabela()

    salva_filas_no_csv(fila_geral)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gera_tarefas()
