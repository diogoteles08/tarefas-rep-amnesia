import pandas as pd

from modelos.morador import Morador
from modelos.tabela_tarefas import Tarefa
from modelos.filas import FilaMoradores


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
    df = pd.DataFrame({'Nome': [morador.nome for morador in fila_geral],
                       'Tarefa1': [morador.fila_ind[0].name for morador in fila_geral],
                       'Tarefa2': [morador.fila_ind[1].name for morador in fila_geral],
                       'Tarefa3': [morador.fila_ind[2].name for morador in fila_geral],
                       'Tarefa4': [morador.fila_ind[3].name for morador in fila_geral]})
    df.to_csv('filas.csv', index=False)


