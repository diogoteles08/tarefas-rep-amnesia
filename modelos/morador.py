from filas import FilaIndividual


class Morador:
    def __init__(self, nome, fila_tarefas=None):
        self.nome = nome
        self.fila_ind = FilaIndividual(fila_tarefas)

    def __str__(self):
        return self.nome

