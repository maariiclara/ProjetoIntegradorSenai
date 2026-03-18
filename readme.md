## -------- REQUISITOS FUNCIONAIS DO SISTEMA --------
- RF01 - Cadastrar os alunos com seu nome e suas notas
- RF02 - Verificar se pelo menos o aluno tem 2 notas
- RF03 - Verificar se as notas são válidas (tem que ser maior igual a 0 e menor igual a 10)
- RF04 - Calcular a média de cada aluno
- RF05 - Ter uma lista de todos os alunos com suas médias
- RF06 - Identificar alunos em recuperação
- RF07 - Identificar o aluno com melhor desempenho
- RF08 - Gerar um relatório final em arquivo txt


## -------- REQUISITOS NÃO FUNCIONAIS DO SISTEMA --------
- RNF01 - O sistema deve ser modular, dividido entre: main.py e processamento.py
- RNF02 - O sistema deve tratar possíveis erros de informações
- RNF03 - O sistema deve ter uma execução rápida
- RNF04 - O sistema deve ter um bom desempenho ao analisar os dados
- RNF05 - O sistema deve ter uma interface simples e fácil de usar na prática
- RNF06 - O código do sistema deve ser bem organizado


## -------- REGRAS DE NEGÓCIO DO SISTEMA --------
RN01 - A estrutura dos dados tem que ser formados por lista e tuplas: [(“Nome”, [notas])]  
RN02 - A lista de notas não pode estar vazia e nem ter números negativos  
RN03 - Alunos com média menor que 7.0 estão em recuperação  
RN04 - Aluno com a maior média é considerado o Top Student