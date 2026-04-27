# Simulação de Threads em Python

Este projeto foi desenvolvido como parte da disciplina de Arquitetura de Computadores e Sistemas Operacionais.

O objetivo é simular a execução de múltiplas threads e observar como o sistema se comporta em diferentes cenários.

## Cenários

- Cenário 1: execução com 3 threads  
- Cenário 2: execução com maior número de threads  
- Cenário 3: threads com diferentes tempos de execução  

## Análise dos cenários

### Cenário 1

Com 3 threads, foi possível observar a execução concorrente básica. As threads iniciam quase ao mesmo tempo, mas finalizam de acordo com seu tempo de execução.

Isso mostra que, mesmo em execução paralela, o tempo de resposta varia conforme a carga de cada thread. O tempo total do programa é influenciado pela thread com maior duração.

### Cenário 2

Com o aumento para 5 threads, houve maior concorrência no sistema. Apesar de mais tarefas serem executadas simultaneamente, também ocorre maior disputa por recursos da CPU.

Isso pode impactar o tempo de resposta e mostra que aumentar o número de threads nem sempre melhora o desempenho, dependendo da capacidade do sistema.

### Cenário 3

Neste cenário, foi possível observar um comportamento semelhante a prioridade por tempo de execução. Threads com menor duração finalizaram mais rapidamente.

Isso mostra que tarefas mais curtas têm menor tempo de resposta, enquanto tarefas mais longas podem sofrer maior tempo de espera, destacando a importância de um bom escalonamento.

## Tecnologias utilizadas

- Python  
- Biblioteca threading  

## Como executar

1. Baixe ou clone este repositório  
2. Execute um dos arquivos no terminal:

python cenario1.py
python cenario2.py
python cenario3.py

## Observação

Este projeto tem caráter acadêmico e foi importante para entender, na prática, conceitos de concorrência e execução de threads.

## Autor

Alexandre Aguilar
