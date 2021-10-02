import armazenamento_de_dados.administrador_de_csv as adm_csv
from modelos.tabela_tarefas import TabelaTarefas


def gera_tarefas():
    # Use a breakpoint in the code line below to debug your script.
    fila_geral = adm_csv.extrai_filas_do_csv()

    tabela_tarefas = TabelaTarefas()
    tarefas_faltantes = tabela_tarefas.pega_tarefas_faltantes()
    while len(tarefas_faltantes) > 0:
        morador = fila_geral.pega_proximo_morador_a_pegar_tarefa()
        tarefa_escolhida = morador.fila_ind.pega_primeira_da_lista_e_poe_no_fim_da_fila(tarefas_faltantes)
        tabela_tarefas.atribuir_tarefa(tarefa_escolhida, morador)

        tarefas_faltantes = tabela_tarefas.pega_tarefas_faltantes()

    tabela_tarefas.mostra_tabela()

    adm_csv.salva_filas_no_csv(fila_geral)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gera_tarefas()
