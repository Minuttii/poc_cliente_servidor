# poc_cliente_servidor
Aplicacao POC em Python

A Prova de Conceito implementada tem como objetivo demonstrar o uso da arquitetura Cliente-Servidor para comunicação simples entre dois componentes utilizando Sockets em Python.

A estrutura do código é composta por três diretórios principais: cliente, servidor e tests, além dos arquivos de configuração pyproject.toml e setup.py.

cliente/cliente.py: Contém a classe Cliente, responsável por enviar as requisições para o servidor.
servidor/servidor.py: Contém a classe Servidor, que é responsável por escutar e processar as requisições do cliente.
servidor/handlers.py: Contém a função processar_requisicao que implementa a lógica de processamento das requisições recebidas.
tests/test_servidor.py: Contém os testes unitários para garantir o correto funcionamento do servidor.
Configuração de Projeto: Arquivos como pyproject.toml e setup.py ajudam a organizar as dependências e o ambiente de desenvolvimento.

Padrões de projeto:

Command (Processamento de requisições):
O servidor processa as requisições dos clientes com base no tipo de comando (por exemplo, soma). 
Cada comando pode ser considerado uma instância de um Command, onde a ação solicitada pelo cliente é executada em uma função específica (processar_requisicao).
Princípios de SOLID
A implementação segue os princípios de SOLID, que ajudam a garantir que o código seja escalável, fácil de manter e de estender:

Single Responsibility Principle (SRP):

Cada classe e função tem uma única responsabilidade. A classe Cliente é responsável apenas por enviar requisições, enquanto a classe Servidor lida com a escuta de conexões e o processamento das requisições. A função processar_requisicao é responsável exclusivamente pela lógica de processamento das requisições.
Open/Closed Principle (OCP):

O código está aberto para extensão, mas fechado para modificação. Por exemplo, se quisermos adicionar novos tipos de comandos para o servidor (como subtração, multiplicação), podemos adicionar novas funções sem modificar as classes existentes. Isso pode ser feito facilmente através da adição de novos módulos ou classes que tratem de novos comandos.
Liskov Substitution Principle (LSP):

Embora o padrão LSP não tenha sido explicitamente necessário para esta PoC (já que não há herança envolvida), a implementação está estruturada de maneira que, caso desejássemos adicionar herança (por exemplo, para diferentes tipos de clientes ou servidores), isso poderia ser feito sem quebrar o comportamento do sistema.

Dependency Inversion Principle (DIP):

A dependência do servidor de um cliente é injetada por meio de parâmetros de configuração, como o host e port. Isso permite que o servidor e o cliente sejam desacoplados, permitindo a troca de implementação de um ou outro facilmente sem afetar o sistema.

Princípios de Clean Code

A implementação segue também os princípios de Clean Code, que garantem que o código seja legível, compreensível e fácil de manter:

Nomes Significativos:

Os nomes das classes, funções e variáveis são claros e indicam diretamente seu propósito. Por exemplo, Cliente é a classe que representa o cliente que se comunica com o servidor, e processar_requisicao descreve exatamente o que a função faz.
Funções Pequenas e Coesas:

As funções são pequenas e focadas em uma única responsabilidade. A função enviar_requisicao na classe Cliente é responsável apenas por enviar os dados ao servidor e retornar a resposta, sem fazer outras operações. Da mesma forma, processar_requisicao realiza apenas o processamento da requisição.

Tratamento de Erros:

O código lida com erros de forma apropriada. No caso da função processar_requisicao, se houver um erro durante o processamento da requisição, ele é capturado e uma mensagem de erro é retornada, mantendo a comunicação segura e sem falhas inesperadas.
