---
title: "Modo Participante & Organização Inteligente por QR Code"
source_url: "https://support.evoto.ai/pt-br/modo-participante-organizacao-inteligente-por-qr-code/"
source_type: "post"
source_id: "25377"
language: "pt-br"
translation_group: "8003"
primary_category: "sem-categoria"
---

O
Modo Participante
resolve o desafio de gerenciamento de fotos em grande volume. Ao carregar uma lista com nomes e e-mails, o sistema gera QR codes exclusivos para cada participante. Isso permite que o
Agrupamento por IA
organize as fotos automaticamente durante a sessão, além de gerar links de galeria e códigos de acesso exclusivos para cada participante, garantindo a privacidade e a segurança dos dados.
---

# Configuração do Projeto & Importação da Lista de Participantes

Para começar, é necessário definir quem será fotografado através da importação de uma lista de participantes.
## **Criação do Projeto**

- Selecione o **Modo Escola** ao criar um projeto.
- O sistema define automaticamente o **Modo Participante** com a **Proteção por Senha** ativada.

- ***Observação:***

-
  - *Caso deseje alterar as configurações de segurança (por exemplo, para **Sem Senha**), isso pode ser feito na aba **Informações Básicas**.*
  - *É possível alternar entre os modos Escola e Clássico no início, porém, uma vez que uma lista de participantes ou foto seja adicionada a um Projeto Escola, não será possível voltar atrás.*

## **Importação de Dados**

- Acesse a aba **Participantes** e faça o upload da sua lista. Utilize o modelo disponível para download no site.
- **Formato:** Compatível com **.csv, .xls, .xlsx** (até 10MB).
- **Requisitos:** Os campos **"Nome"** e **"E-mail"** são obrigatórios.
- **Validação:** O sistema verifica automaticamente duplicatas e erros de formatação (por exemplo, e-mails inválidos).

## **Gerenciamento da Lista**

- É possível pesquisar nomes ou utilizar **"Re-importar"** para adicionar novos participantes à lista.

***Observação:***

- *Não é possível editar os dados dos participantes (como a grafia do nome) diretamente no aplicativo. Para corrigir um erro, é necessário excluir o registro e re-importá-lo.*
- *A exclusão de um participante também resultará na exclusão de todas as fotos associadas a ele.*

---

# **Fluxo de Trabalho com QR Code**

O sistema gera um QR code exclusivo para cada participante, vinculando a sessão fotográfica física à galeria digital.

- **Geração de Códigos:** Selecione os participantes na lista e clique em **Baixar QR Code**. É possível escolher um layout **(1 ou 2 cartões por página)** para impressão.
  - Durante a sessão, escaneie o cartão para indicar ao sistema: **"As próximas fotos pertencem a este aluno."**
  - O cartão contém o **Link exclusivo da Galeria** e o **Código de Acesso** para que os pais ou o aluno façam login posteriormente.

## **Métodos de Captura e Organização**

Existem três formas de organizar as fotos nas pastas dos participantes. Escolha o método que melhor se adapta ao seu fluxo de trabalho no local.

### **Método A: Agrupamento Automático por IA via Dispositivo Móvel**

Este método utiliza a detecção de QR code em tempo real com conexão ao aplicativo móvel.

1. **Fluxo de trabalho:** Fotografe o aluno segurando seu cartão QR primeiro e, em seguida, tire os retratos.
2. **Organização Automática:** A IA detecta o QR code e direciona automaticamente todas as fotos subsequentes para a pasta do respectivo aluno, até que um novo código seja escaneado.
3. **Requisitos:**
  - É necessária uma conexão com a internet.
  - ***Observação:** A foto contendo o QR code também é enviada para a galeria.*

### **Método B: Organização Manual via Dispositivo Móvel (Somente com Conexão)**

Também é possível fotografar sem cartões QR impressos, selecionando os nomes manualmente.

1. **Fluxo de trabalho:** Conecte sua câmera e toque em **Entrar no Modo de Agrupamento Manual** no aplicativo.
2. **Operação:**
  - Toque em um nome na lista de participantes.
  - Inicie a sessão; as fotos serão direcionadas para o aluno selecionado.
  - Toque em **Concluir e Próximo** para alternar automaticamente para a próxima pessoa na lista (ou toque manualmente em outro nome para alternar).
3. **Status:** A lista acompanha o andamento dos participantes como **Não Iniciado, Em Andamento** ou **Concluído.**

### **Método C: Organização por IA via Web (Pós-Sessão)**

Caso prefira organizar as fotos após o evento, é possível processar as imagens em lote no **Portal Web.**

1. **Fluxo de trabalho:** Fotografe com os cartões QR no local. Em seguida, faça o upload de todas as fotos para o módulo **Agrupamento Total por IA** do projeto web.
2. **Operação:** Após o upload, o sistema escaneará os QR codes e moverá as imagens para as pastas corretas automaticamente.

Tratamento de Fotos Não Organizadas:
Caso um QR code esteja desfocado ou o formato da imagem não seja compatível (por exemplo, alguns arquivos RAW), as fotos aparecerão na pasta "
Não Agrupadas
". Basta selecionar as fotos e movê-las manualmente para a pasta correta. Esta funcionalidade está disponível tanto no
Portal Web
quanto no
Aplicativo Móvel
.
---

# **Entrega e Privacidade**

O Modo Participante aplica padrões rigorosos de privacidade para instituições de ensino.

- **Sem Reconhecimento Facial:** Para garantir a conformidade com as normas de privacidade, o recurso **"Encontre-me"** (Reconhecimento Facial) está desativado neste modo.
- **Controle de Acesso:**
  - **Verificação:** Os responsáveis acessam a galeria por meio do link exclusivo ou escaneando o cartão QR. Se a proteção por senha estiver ativada, deverão inserir o **Código de Acesso de 4 dígitos** (ex.: A3K9). **Observação:** Atualmente, não há limite de tentativas para códigos incorretos.
  - **Visualização Privada:** Após a verificação, o usuário visualiza apenas as suas próprias fotos.
- **Envio de E-mails:**
  - Utilize o botão **Compartilhar por E-mail** para enviar os links individuais da galeria a todos os participantes de forma simultânea.
