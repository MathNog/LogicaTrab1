# INF1009 - Lógica para Computação - PUC-Rio 
## Trabalho 1 - Gerador de Tableuax para Lógica Proposicional
### Alunos: Henrique Soares e Matheus Nogueira
#### Turma: 3WC

**Informações sobre a implementação do trabalho**
1. Linguagem utilizada: Python3.8
2. Biblioteca utilizada: Tkinter
   - O Tkinter é uma biblioteca padrão de Python para interfaces gráficas. Sendo assim, caso já tenha o Python3.8, não deve ser necessário instalar a biblioteca, pois ela já deve estar instalada. 
   
**Intruções para execução correta do programa**
1. Na branch master, exitem 3 arquivos .py. Para executar o programa, clone ou baixe todos os arquivos, e execute "Executa_Tableaux". Os demais módulos são devidamente importados por ele.
   - _**Observação Importante**_: a fórmula a ser verificada precisa estar fielmente de acordo com a formalização da Lógica Proposicional. O símbolo usado para representar a implicação deve ser ">". Nenhuma abreviação deve ser feita. Por exemplo, toda fórmula deve ter um par de parênteses externos: "a>b" deve ser "(a>b)". "(a>b)>c" deve ser "((a>b)>c)". Letras maiúsculas e minúsculas são aceitas. Se v(a) puder ser V ou F para o contra-exemplo gerado para uma fórmula falsificável, v(a) é omitido da exibição do contra exemplo, como em: ((a>b)>(c>d)), pois, nesse caso, dados v(b) = V, v(c) = V, v(d) = F; o valor verdade de 'a' é indiferente para o valor verdade 'F' da fórmula
 

