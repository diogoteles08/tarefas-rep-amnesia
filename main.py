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


class FilaIndividual(Fila):
    def __init__(self, valor_inicial=None):
        if valor_inicial is None:
            valor_inicial = list(Tarefa)
        super().__init__(valor_inicial)


class Morador:
    def __init__(self, nome, fila_tarefas=None):
        self.nome = nome
        self.fila_ind = FilaIndividual(fila_tarefas)

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
    return fila_geral

def gera_tarefas():
    # Use a breakpoint in the code line below to debug your script.
    fila_geral = extrai_filas_do_csv()
    print(f'Hi,')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gera_tarefas();