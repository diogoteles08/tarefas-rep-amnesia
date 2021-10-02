from enum import Enum

from modelos.morador import Morador


class Tarefa(Enum):
    COCO = ('Cocô', 1)
    PANOS = ('Panos', 1)
    LIXO = ('Lixo', 1)
    LOUCA = ('Louça', 2)


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