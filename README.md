# SERVIDOR TEMPORÁRIO HTTP SIMPLES COM REGISTRO DE LOGS
<p align="justify">
   
Este projeto implementa um servidor HTTP simples utilizando os módulos `http.server` e `socketserver` do Python. 
Ele serve arquivos de um diretório específico e registra todas as requisições recebidas tanto no terminal quanto em um arquivo de log.

## Aplicação

Um servidor HTTP simples, como este, pode ser muito útil em várias situações na área de infraestrutura. 
Aqui estão algumas aplicações práticas:

**1. Servir Arquivos Estáticos** \
   Compartilhamento de Arquivos: \
   Permite a transferência rápida de arquivos em uma rede local sem a necessidade de configurar um servidor mais complexo.
   Distribuição de Documentos: \ 
   Para equipes que precisam acessar documentos ou recursos, um servidor HTTP pode ser uma maneira rápida de disponibilizá-los.

**2. Teste de Aplicações Web** \
   Ambiente de Desenvolvimento Local: \ 
   Permite testar rapidamente aplicações web em desenvolvimento sem a complexidade de configurar um servidor completo como Apache ou Nginx.
   Verificação de Recursos Estáticos: \
   Verifique se os arquivos HTML, CSS ou JavaScript estão acessíveis e funcionando corretamente.

**3. Prototipagem Rápida** \
   Demonstrações: \
   Ideal para criar protótipos rápidos de aplicações web ou serviços que podem ser demonstrados a partes interessadas sem um grande investimento de tempo.
   Ambientes de Teste para APIs: \
   Você pode usar o servidor para simular respostas de APIs durante o desenvolvimento de clientes ou serviços.

**4. Transferência de Dados Temporários** \
Upload de Arquivos: Em um ambiente controlado, um servidor simples pode ser usado para enviar arquivos temporariamente sem a necessidade de soluções complexas.
Backup de Dados: Rápido e fácil para criar backups de arquivos em uma rede local.

**5. Monitoramento e Diagnóstico** \
Logs de Atividade: Útil para monitorar e registrar atividades de rede, permitindo diagnósticos de problemas em tempo real.
Testes de Conectividade: Ajuda a verificar se um servidor ou serviço pode ser acessado corretamente.

**6. Documentação e Recursos** \
Wiki ou Documentação Interna: Um servidor simples pode ser utilizado para hospedar uma documentação interna leve ou uma wiki.
Dashboards de Status: Pode servir páginas HTML simples que exibem o status de serviços ou outros recursos.

**7. Experimentos e Aprendizado** \
Prática de DevOps: Ideal para iniciantes em DevOps que desejam entender como funciona a configuração de servidores e o manuseio de requisições HTTP.
Desenvolvimento de Habilidades: Excelente oportunidade para aprender sobre redes e servidores de forma prática.

**Considerações Finais** \
Embora um servidor HTTP simples seja muito prático, ele não deve ser usado para aplicações em produção que exigem segurança robusta, gerenciamento de tráfego ou escalabilidade. Para essas situações, servidores web mais avançados (como Nginx ou Apache) são recomendados.

## Funcionalidades

- Serve arquivos estáticos do diretório `/files` (ou de qualquer outro diretório que você especificar).
- Registra todas as requisições HTTP no terminal e em um arquivo de log (`/files/weblog`).
- Permite o uso de **Cross-Origin Resource Sharing (CORS)** adicionando o cabeçalho `Access-Control-Allow-Origin: *` em todas as respostas.
- Log em arquivo e terminal: A função `log_message` faz dois registros: um no arquivo `weblog` usando o **módulo logging**, e outro diretamente no `terminal com print()`. 
Isso garante que as ações das requisições sejam visíveis no terminal e gravadas no log.
- Arquivo de log: O arquivo de log será salvo no caminho `/files/weblog`. Se o diretório `/files` não existir, você pode precisar criá-lo.
Agora, ao rodar o script, você verá as requisições HTTP no terminal, enquanto todas as mensagens também serão registradas no arquivo weblog.

## Requisitos

- Python 3.x
- Permissão de escrita no diretório `/files` (ou no diretório que você especificar para servir os arquivos).

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/<seu-usuario>/<nome-do-repositorio>.git
   cd <nome-do-repositorio>
2. Certifique-se de que o diretório /files exista e contenha os arquivos que você deseja servir. Caso o diretório não exista, crie-o:

   ```bash
   mkdir /files
    ```
3. Inicialize o servidor:

   ```bash
   python3 http-simple-server.py
   ```
O servidor irá iniciar na porta 8000 por padrão. Você pode acessá-lo em http://localhost:8000.

Logs
Terminal: Todas as requisições recebidas são exibidas em tempo real no terminal.
Arquivo: As requisições também são gravadas no arquivo de log localizado em /files/weblog.
Personalização
Para alterar o diretório de onde os arquivos são servidos, modifique a linha os.chdir('/files') no script para o caminho desejado.
Para mudar a porta padrão, altere o valor da variável PORT no script.
Encerrando o Servidor
Para parar o servidor, pressione Ctrl+C no terminal.

### Instruções adicionais:
- Substitua `"<seu-usuario>"` e `"<nome-do-repositorio>"` pelos seus dados do GitHub.
- Certifique-se de criar um arquivo de licença, se aplicável.

</p>
