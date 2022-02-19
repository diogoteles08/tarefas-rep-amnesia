# Gerador de tarefas da República Amnésia

Na república amnésia, os moradores como um coletivo são responsáveis por realizar algumas atividades ao longos dos dias
para manter o ambiente mais agradável e manter uma boa convivência. Chamamos de "tarefas da rep" algumas atividades 
específicas, como guardar a louça do escorredor, tirar o lixo e limpar o cocô da nossa cachorra, pois elas têm que ser
feitas constantemente. Para não sobrecarregar nenhum morador, fazemos uma rotatividade de modo que cada semana moradores
específicos fiquem responsáveis por uma dessas tarefas. Essa rotatividade era sempre feita manualmente, e este programa
vêm com o objetivo de automatizar a geração dessas tarefas.

## Pseudo-algoritmo
A ideia principal da divisão de tarefas, é que haja uma rotação adequada entre os moradores que realizam tarefas a cada
semana. Por exemplo, se o Theo pegou uma tarefa essa semana, queremos que ele fique o máximo de semanas possível sem
precisar pegar outras tarefas.

Além disso, também queremos que cada morador leve o maior tempo possível para precisar realizar uma mesma tarefa
novamente. Por exemplo, se essa semana o Theo pegou a tarefa de LIXO, queremos que ele pegue outras tarefas antes de
pegar novamente a tarefa de LIXO.

Para conseguir suprir esses requisitos, foram criados os seguintes conceitos a seguir.

### Fila geral de moradores
Essa fila serve para rotacionar os moradores que recebem tarefas ao longo das semanas. É ela que determina quais
moradores devem pegar tarefas em dada semana. Por exemplo, imagine que precisamos de 2 pessoas para realizar tarefas numa
dada semana, e a fila geral é:

* Theo
* Sussu
* Catuba
* Trix

Nesse caso o Theo e a Sussu deverão pegar tarefas, e a fila passará a ser:

* Catuba
* Trix
* Theo
* Sussu

### Lista de tarefas
Há uma lista de todas as tarefas a serem desempenhadas na república amnésia, que também indica quantas pessoas ao mesmo
tempo são necessárias para desempenhar. Por exemplo, há a tarefa de levar o lixo da cozinha para fora de casa, que 
precisa apenas de uma pessoa por semana, enquanto há a tarefa de secar e guardar a louça do escorredor, que demanda bem
mais trabalho, portanto precisa de duas pessoas por semana.

Atualmente essa lista de tarefas está manualmente inserida no código. Uma possível melhoria futura seria salvá-la em um
armazenamento externo.

### Fila de prioridades de tarefa por morador
Cada morador tem uma fila de prioridades, que indicaria qual tarefa ele preferencialmente deveria pegar da próxima vez.
Sempre que uma tarefa é realizada por um morador, ela vai para o final da fila desse morador, assim levará mais tempo
para ele ter que desempenhar a mesma tarefa.

Por exemplo, supondo que tenhamos as tarefas LIXO, COCÔ e LOUÇA. A fila do Theo atualmente é esta:

Prioridade 2 | Prioridade 1 | Prioridade 0
:----------: | :----------: | :----------: 
| LIXO | COCÔ | LOUÇA |

Se ele precisar pegar uma tarefa nessa semana, e nenhuma tarefa ainda foi pega, ele deverá pegar a tarefa LIXO, e então
sua fila passará a ser:

Prioridade 2 | Prioridade 1 | Prioridade 0
:----------: | :----------: | :----------: 
| COCÔ | LOUÇA | LIXO |

## Tecnologias utilizadas
A ideia inicial deste programa é ser o mais simples, compreensível e mantível possível, para que futuros moradores da
república consigam adaptar o código para futuras necessidades que venham a surgir.

### Linguagem de programação
Nesse cenário, foi escolhido fazer o programa utilizando Python, pois é uma linguagem relativamente fácil, amplamente
utilizada, e também utilizada na Unicamp nas matérias de programação básica.

### Armazenamento
Como o programa não exige nenhum armazenamento de dados complexo ou elaborado, ele foi programado para salvar os dados
em um arquivo .csv.

## Contribuidores <3
Esse programa foi idealizado e inicialmente implementado pelo morador Pousada (Diogo Teles Sant Anna), 016 da Computação
Unicamp e morador da Amnésia entre 2019 e 2021.

### Lista de Contribuidores:
* Diogo Teles Sant Anna (Pousada)
* Saia Jeans