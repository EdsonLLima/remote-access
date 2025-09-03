# Remote Access

### Visão Geral do Projeto

Este projeto, **Remote Access**, tem como objetivo criar uma aplicação de acesso remoto simples e eficaz usando Python.

### Sumário

- [Arquitetura da Aplicação](#arquitetura-da-aplicacao)
- [Passo 1: Estabelecendo a Conexão com Sockets](#passo-1-estabelecendo-a-conexao-com-sockets)
- [Próximos Passos](#próximos-passos)

---

### Arquitetura da Aplicação
A aplicação é dividida em dois componentes principais: um servidor (a ser instalado na máquina remota) e um cliente (a sua máquina de controle). A comunicação é feita via sockets TCP.

### Passo 1: Estabelecendo a Conexão com Sockets
Nesta etapa inicial, a base de comunicação em tempo real foi estabelecida. O código de servidor e cliente foi implementado para permitir a conexão e garantir que a comunicação fundamental esteja funcionando.

### Passo 2: Captura e Streaming de Tela

Nesta etapa, foi adicionada a funcionalidade para o servidor capturar a tela e enviá-la para o cliente em tempo real. A biblioteca Pillow foi utilizada para a captura de imagens, permitindo a visualização da tela remota.

### Passo 3: Controle Remoto de Mouse e Teclado

Nesta etapa, a aplicação foi aprimorada para permitir o controle total da máquina remota. A biblioteca `pyautogui` foi integrada para simular eventos de mouse (movimento e cliques) e teclado, tornando o acesso remoto funcional para interações do usuário.

### Próximos Passos

- [ ] Melhorar a interface do usuário.
- [ ] Implementar a lógica de empacotamento da aplicação.