<h1> Boas-vindas ao repositório do Job Insights! </h1>
 
 <h4>Sobre o projeto:</h4>
 <p>
 Neste projeto tive que implementar análises a partir de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). Também escrevi alguns testes implementação de uma análise de dados.<br>
Os dados foram extraídos do site Glassdoor e obtidos através do Kaggle, uma plataforma disponiblizando conjuntos de dados para cientistas de dados.<br><br>

🚵 Habilidades a serem trabalhadas:<br><br>

Utilizar o terminal interativo do Python.<br>
Utilizar estruturas condicionais e de repetição.<br>
Utilizar funções built-in do Python.<br>
Utilizar tratamento de exceções.<br>
Realizar a manipulação de arquivos.<br>
Escrever funções.<br>
Escrever testes com Pytest.<br>
Escrever seus próprios módulos e importá-los em outros códigos.<br>


 </p>
 
 <h3> Requisitos do Projeto: </h3>
 
 <p> 
  1. Implemente a função read<br><br>

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. Esta função será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.<br><br>

A função deve receber um path (uma string com o caminho para um arquivo).<br>
A função deve abrir o arquivo e ler seus conteúdos.<br>
A função deve tratar o arquivo como CSV.<br>
A função deve retornar uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.<br>


   <br><br>
2.  Implemente a função get_unique_job_types<br><br>

Agora que temos como carregar os dados, podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.<br><br>

A função deve receber o path do arquivo csv com os dados.<br>
A função deve invocar a função jobs.read com o path recebido para obter os dados.<br>
A função deve retornar uma lista de valores únicos presentes na coluna job_type.<br><br>

3.  Implemente a função get_unique_industries<br><br>

Da mesma forma, agora iremos identificar quais indústrias estão representadas nesse conjunto de dados.<br><br>

A função deve obter os dados da mesma forma que o requisito 2.<br>
A função deve retornar uma lista de valores únicos presentes na coluna industry.<br>
A função desconsidera valores vazios<br><br>

4. Implemente a função get_max_salary<br><br>

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.<br><br>

A função deve obter os dados da mesma forma que o requisito 2.<br>
A função deve ignorar os valores ausentes.<br>
A função deve retornar um valor inteiro com o maior salário presente na coluna max_salary.
<br><br>

5.Implemente a função get_min_salary<br><br>

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o menor valor de todas as faixas.<br><br>

A função deve obter os dados da mesma forma que o requisito 2.<br>
A função deve ignorar os valores ausentes.<br>
A função deve retornar um valor inteiro com o menor salário presente na coluna min_salary.<br><br>

6. Implemente a função filter_by_job_type<br><br>

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar esse filtro.<br><br>

A função deve receber uma lista de dicionários jobs como primeiro parâmetro.<br>
A função deve receber uma string job_type como segundo parâmetro.<br>
A função deve retornar uma lista com todos os empregos onde a coluna job_type corresponde ao parâmetro job_type.
<br><br>

7.  Implemente a função filter_by_industry<br><br>

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria. Vamos precisar implementar esse filtro também.<br><br>

A função deve receber uma lista de dicionários jobs como primeiro parâmetro.<br>
A função deve receber uma string industry como segundo parâmetro.<br>
A função deve retornar uma lista de dicionários com todos os empregos onde a coluna industry corresponde ao parâmetro industry.
<br><br>

8. Implemente a função matches_salary_range<br><br>

O aplicativo vai precisar filtrar os empregos por salário também. Como uma função auxiliar, implemente matches_salary_range para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.<br><br>

A função deve receber um dicionário job como primeiro parâmetro, com as chaves min_salary e max_salary, que podem ser números ou strings que representem números.<br>
A função deve receber um número ou string que represente o número salary como segundo parâmetro.<br>
A função deve lançar um erro ValueError nos seguintes casos:<br>
alguma das chaves min_salary ou max_salary estão ausentes no dicionário;<br>
alguma das chaves min_salary ou max_salary tem valores não-numéricos;<br>
o valor de min_salary é maior que o valor de max_salary;<br>
o parâmetro salary tem valores não numéricos;<br>
A função deve retornar True se o salário procurado estiver dentro da faixa salarial ou False se não estiver.<br><br>

9. Implemente a função filter_by_salary_range<br><br>

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a função auxiliar implementada no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.<br><br>

A função deve receber uma lista de dicionários jobs como primeiro parâmetro.<br>
A função deve receber um número ou string salary como segundo parâmetro.<br>
A função deve ignorar os empregos com valores inválidos para min_salary ou max_salary.<br>
Observação: strings que representem números são valores válidos para min_salary ou max_salary.<br>
A função deve retornar uma lista com todos os empregos onde o salário salary estiver entre os valores da coluna min_salary e max_salary.
<br><br>

10.- Implemente um teste para a função count_ocurrences<br><br>

A empresa cliente contratou um relatório que informa a quantidade de ocorrências das palavra Python e Javascript nos dados e, para isso, temos uma implementação pronta em src/pre_built/counter.py. Durante o desenvolvimento, sofremos com alguns bugs, que já foram resolvidos. Para termos certeza e confiança da nossa entrega, no entanto, e não corrermos riscos, precisaremos de testes automatizados que garantam isso!<br><br>

O nome deste teste deve ser test_counter, e ele deve garantir que atenda estas especificações:<br><br>

Chamar a função count_ocurrences passando dois parâmetros:<br>
path uma string com o caminho do arquivo (data/jobs.csv);<br>
word uma string com a palavra a ser contabilizada.<br>
Garantir que a função retorna corretamente a quantidade de ocorrências da palavra solicitada<br>
A contagem de palavras deve ser case insentitive, ou seja, não diferenciar letras maiúsculas de minúsculas<br><br>

11. Implemente um teste para a função read_brazilian_file<br><br>

A empresa cliente analisa relatórios em inglês, porém agora ela quer expandir seus negócios aqui para o Brasil e deseja analisar relatórios em português também. No entanto, as chaves do dict que usamos pra organizar os dados devem continuar em inglês. Ou seja: para gerar o relatório, deveremos ler as chaves em português e traduzi-las para inglês para povoar os nossos dados.<br><br>

Nossa equipe já implementou essa função, a read_brazilian_file, na qual adotamos a estratégia de chamar o método original read, que implementamos no requisito 1, e depois traduzimos as chaves para o inglês. Agora precisamos criar testes para ter certeza que esta tudo certo!<br><br>

O nome deste teste deve ser test_brazilian_jobs, e ele deve garantir que atenda as seguintes especificações:<br><br>

Chamar a função read_brazilian_file e ela deve receber um parâmetro:<br>
path que é uma string com o caminho do arquivo csv em português (tests/mocks/brazilians_jobs.csv);<br>
Retorna uma lista de dicionários com as chaves em inglês<br><br>

12.  Implemente um teste para a função sort_by<br><br>

Por fim, espera-se que a pessoa usuária possa escolher um critério de ordenação para exibir os empregos. Já temos uma implementação para essa ordenação em src/pre_built/sorting.py, mas queremos ter certeza de que ela funciona e, principalmente, que não deixará de funcionar conforme vamos implementando novos recursos. Precisamos então escrever um teste!<br><br>

Esse teste deve se chamar test_sort_by_criteria e garantir que a função funciona segundo esta especificação:<br><br>

A função sort_by recebe dois parâmetros:<br>
jobs uma lista de dicionários com os detalhes de cada emprego;<br>
criteria uma string com uma chave para ser usada como critério de ordenação.<br>
O parâmetro criteria deve ter um destes valores: min_salary, max_salary, date_posted<br>
A ordenação para min_salary deve ser crescente, mas para max_salary ou date_posted devem ser decrescentes.<br>
Os empregos que não apresentarem um valor válido no campo escolhido para ordenação devem aparecer no final da lista.
<br><br>

 
