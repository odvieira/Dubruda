# Políticas Públicas de Resposta à Covid-19 no Brasil

Esse é um projeto da [Blavatnik School of Government](www.bsg.ox.ac.uk), da [FGV EBAPE – Escola Brasileira de Administração Pública e de Empresas](https://ebape.fgv.br), e da [Universidade de São Paulo](http://dcp.fflch.usp.br), uma expansão do [Blavatnik School of Government OxCGRT](https://www.bsg.ox.ac.uk/covidtracker).

Mais informações estão disponíveis no site do projeto: [www.bsg.ox.ac.uk/pesquisa-covid19-brasil](http://bsg.ox.ac.uk/pesquisa-covid19-brasil).

---

__Citação sugerida para a base de dados:__ Anna Petherick, Beatriz Kira, Lorena Barberia, Thomas Boby, Rafael Goldszmidt, e Maria Luciano.[ _Brazil’s Covid-19 Government Response Policies_](http://bsg.ox.ac.uk/pesquisa-covid19-brasil), Blavatnik School of Government, 2020.

---

### Base de dados de respostas governamentais à Covid-19 a nível subnacional no Brasil
Com base no [sistema de codificação](https://github.com/OxCGRT/Brazil-covid-policy/blob/master/documentation/codebook_subnational.md) do Oxford COVID-19 Government Response Tracker (OxCGRT), esta base de dados apresenta uma medida sistemática e objetivo da força das políticas de resposta ao Covid-19 que foram implementadas pelo governo federal, pelos governos estaduais, e pelos governos de todas as capitais estaduais e da segunda cidade de cada estado.

Atualmente a base de dados inclui 12 indicadores: C1 a C8, H1 a H3 e H6. Tais indicadores permitem a criação de dois [índices](https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/index_methodology.md) distintos: o índice de rigidez e o índice de contenção e saúde. A base de dados é atualizada continuamente e em tempo real.

Os dados sobre políticas adotadas no nível estadual foram incoporados também ao [repositório principal do OxCGRT](https://github.com/OxCGRT/covid-policy-tracker). O presente repositório contém um banco de dados secundário distinto, que não deve ser interpretado da mesma forma que o banco de dados principal. As diferenças entre os dois são descritas abaixo.

#### Diferenças entre os níveis das medidas

Este repositório contém dados para três níveis de políticas públicas, descritos usando os sufixos "GOV", “WIDE”, e “TOTAL”. As medidas descritas com o sufixo "GOV" referem-se a políticas emitidas apenas em um nível específico de governo e podem ser usadas para comparar as medidas adotadas por diferentes níveis de governo.

As medidas descritas com o sufixo “_WIDE” capturam todas as respostas adotadas por uma determinada jurisdição e seus subcomponentes. Medidas “_WIDE” não incorporam políticas gerais de níveis mais altos de governo que podem substituir as políticas locais, mas capturam medidas adotadas por níveis mais altos se elas forem especificamente direcionadas para aquela jurisdição subnacional. Por exemplo, se um governo nacional ordenar o fechamento de eventos em uma determinada cidade que está passando por um surto. As políticas descritas com o sufixo “TOTAL” descrevem todas as respostas adotadas por uma jurisdição específica, aquelas abaixo dela, e também incluem políticas herdadas de níveis superiores que afetam essa jurisdição. Por exemplo, se um país tiver uma restrição de viagens internacionais que se aplique a todo o país, isso aparecerá como uma política NAT_GOV e será herdada por STATE_TOTAL e CITY_TOTAL, mas não por STATE_WIDE nem CITY_WIDE.

O repositório brasileiro contém oito rótulos descritivos:
- NAT_GOV: Políticas adotadas apenas pelo governo federal brasileiro.
- NAT_TOTAL: Parte do conjunto de dados internacional OxCGRT, descreve o ambiente de resposta geral do país, incluindo políticas definidas pelos governos subnacionais onde tais valores forem mais rigorosos do que a ação nacional.
- STATE_GOV: Políticas adotadas apenas por aquele governo estadual específico.
- STATE_WIDE: Descreve as respostas do governo adotadas por um estado e seus subcomponentes. Não inclui políticas adotadas em um nível superior de governo.
- STATE_TOTAL: Descreve o ambiente de resposta geral que se aplica aos residentes do estado, incluindo políticas definidas pelo governo nacional onde esses valores são mais rigorosos do que a ação em nível estadual.
- CITY_GOV: Políticas adotadas apenas por aquele governo municipal específico.
- CITY_WIDE: Descreve as medidas adotadas por um município e seus subcomponentes. No Brasil, como o município é o nível de federação mais baixo, a política city_policies corresponde às políticas city_gov.
- CITY_TOTAL: Descreve o ambiente de resposta geral que se aplica aos residentes do município, incluindo políticas definidas pelo governo nacional e pelo governo estadual, onde tais valores forem mais rigorosos do que a ação no nível municipal.

#### Intepretação adicional
Flags representando distinções entre medidas focalizadas ou gerais para níveis subnacionais são consistentes com a [documentação da base dados principal](https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md).

O relatório sobre os dados brasileiros descreve a metodologia, protocolos de coleta de dados, e uma descrição detalhadas dos indicadores.

#### Acesso aos dados
A pasta [/data](https://github.com/OxCGRT/Brazil-covid-policy/tree/master/data) neste respositório contém arquivos atualizados periodicamente com os dados subnacionais, que estão disponíveis para a construção de aplicações. Os dados são apresentados no formato "jurisdição-dia", com uma coluna com notas escritas pela nossa equipe de codificadores para cada indicador. Os arquivos são autalizados manualmente em intervalos regulares, e o nome do arquivo pode mudar. Note que alguns dos comentários podem incluir vírgulas e outros caracteres como delimitadores, o que pode afetar análises automatizadas do arquivo CSV.


### Dados de pesquisa sobre as experiências e opiniões em relação às políticas de resposta à Covid-19
Nós também apresentamos os [resultados originais](https://github.com/OxCGRT/Brazil-covid-policy/tree/master/data) de duas rodadas de uma pesquisa conduzida com indivíduos no Brasil. A primeira rodada ocorreu entre os dias 6 e 27 de maio com 1,654 indivíduos em oito capitais estaduais, enquanto a segunda rodada ocorreu entre 27 de julho e 2 de outubro, em nove capitais estaduais.

A pesquisa foi desenhada para identificar até que ponto a realidade nessas oito cidades correspondia à [lista de recommendações](https://apps.who.int/iris/bitstream/handle/10665/331773/WHO-2019-nCoV-Adjusting_PH_measures-2020.1-eng.pdf) da Organização Mundial da Saúde (OMS) quanto às medidas que deveriam ser adotadas para a flexibilização segura das políticas de resposta à Covid-19. Ambas as rodadas foram conduzidas pelo telefone e usaram amostras estratificada por idade, sexo, escolaridade e faixa de renda.


### Índice de Risco de Abertura (RoOI) derivado dos dados subnacionais brasileiros
À medida que a Covid-19 se espalhou pelo Brasil, a rigidez das respostas governamentais adotadas por cidades e estados aumentaram e diminuíram. A base de dados de políticas públicas adotadas por unidades subnacionais brasileiras, combinada com dados de outras fontes, fornece uma visão geral do risco e das respostas de diferentes unidades da federação ao longo do tempo.

O _Índice de Risco de Abertura (RoOI)_ é baseado nas [recomendações](https://apps.who.int/iris/bitstream/handle/10665/331773/WHO-2019-nCoV-Adjusting_PH_measures-2020.1-eng.pdf) publicadas pela OMS sobre as condições que devem ser observadas antes que as respostas à Covid-19 sejam relaxadas. O RoOI visa a informar a tomada de decisão acerca de quando é seguro reabrir a economia ou quando medidas mais restritas devem ser adotadas, à medida que governos buscam calibrar suas respostas.

O cálculo detalhado e a lógica por trás da fórmula estão no [relatório de pesquisa](http://bsg.ox.ac.uk/pesquisa-19-brasil), e a versão atualizada está disponível na [documentação deste repositório](https://github.com/OxCGRT/Brazil-covid-policy/tree/master/documentation).

### Análise de regiões específicas

Relatórios individuais relatando a situação de nove capitais brasileiras (São Paulo/SP, Rio de Janeiro/RS, Porto Alegre/RS, Goiânia/GO, Salvador/BA, Recife/PE, Fortaleza/CE, Manaus/AM e Belém/PA) estão disponíveis na pasta [/policy briefs](https://github.com/OxCGRT/Brazil-covid-policy/tree/master/policy_briefs).


### Agradecimentos
Os autores agradecem seus colegas por comentários e sugestões sobre as perguntas de pesquisa, especialmente Eduardo Andrade, Thomas Hale, Toby Phillips, Clare Leaver e Cesar Zucco. A pesquisa foi financiada pelo Global Challenges Research Fund, [The Alfred Landecker Foundation](https://www.bsg.ox.ac.uk/research/research-programmes/alfred-landecker-programme), e pela [Blavatnik School of Government](www.bsg.ox.ac.uk).

O time de codificadores subnacionais do OxCGRT Brasil é composto por: Aline Tognini, André Houang, Anna Paula Ferrari Matos, Bárbara Prado Simão, Beatriz Franco, Beatriz Kira, Bruna Maria da Silva Ruys, Camila Sacchetto, Carla Vila, Carlos Danquer Amaral, Carolina Martinelli, Carolina Scherer Beidacki,  Celso Antônio Coelho Júnior, Daniel Pereira Cabral, Danielle Stephanie Gomes Treider, Davi Mancebo Fernandes, Davi Romão, Dayane Ferreira, Déborah Palacio do Sacramento, Denilson Soares Gomes Junior, Elisa Codonho Premazzi, Elisangela Oliveira de Freitas, Fabiana da Silva Pereira, Felipe Natil Martins Moreira, Felipe Paiva Pinto, Gabriel de Azevedo Soyer, Guilherme Ramos, Henrique Oliveira da Motta, Hermann Fernandes Pais, Horácio Figueira de Moura Neto, Isabel Seelaender Costa Rosa, Isabela Blumm, João Ferreira Silva, João Gabriel de Paula Resende, João Pires Mattar, José Renato Venâncio Resende, Larissa Cristina Margarido, Laura Boeira, Letícia de Araújo Dias, Letícia Plaza, Liene Baptista, Luiz Eduardo Barbieri Bedendo, Luiz Guilherme Roth Cantarelli, Marcela Mello Zamudio, Maria Leticia Claro de Faria Oliveira, Maria Luciano, Marília Camargo Miyashiro, Marta Koch, Mateus Henrique Müller, Matheus Porto Lucena, Maurício Nardi Valle, Mayra Henrique de Melo, Natalia Brigagão, Natália Colvero Maraschin, Natália de Paula Moreira, Nicole Guedes Barros, Nicole Nanci, Pedro Arcain Riccetto, Pedro Ferreira Baccelli Reis, Pedro Santana Schmalz, Pollyana Lima, Ricardo Miranda Rocha Leitao, Rodrigo Furst, Tamoi Fujii, Teresa Soter Henriques, Thiago William Pereira Barcelos, Vinicius Tadeu Silvério dos Santos, Viviane de Assis Ignacio, e Walter Vinicius Ribeiro Cancelieri.
