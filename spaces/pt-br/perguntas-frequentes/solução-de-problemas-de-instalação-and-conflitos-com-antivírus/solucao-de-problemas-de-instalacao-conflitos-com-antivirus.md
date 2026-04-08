---
title: "Solução de Problemas de Instalação & Conflitos com Antivírus"
source_url: "https://support.evoto.ai/pt-br/solucao-de-problemas-de-instalacao-conflitos-com-antivirus/"
source_type: "post"
source_id: "23886"
language: "pt-br"
translation_group: "6278"
primary_category: "sem-categoria"
---

Este guia aborda problemas comuns em que o Evoto pode ser bloqueado pelo sistema operacional ou por softwares antivírus, fornecendo instruções para garantir uma instalação e operação sem problemas.

---

### Como corrigir o erro “O Evoto não pode ser aberto porque não foi baixado da App Store” no Mac?

Esse erro ocorre quando o **Gatekeeper do macOS**, um recurso de segurança, impede a abertura de aplicativos que não foram baixados da App Store ou de desenvolvedores identificados.

**Como resolver:**

1. Clique em **OK** na janela de diálogo que exibe a mensagem de erro.
2. Abra **Ajustes do Sistema** (macOS Ventura 13 ou posterior) ou **Preferências do Sistema** (macOS Monterey 12 ou anterior).
3. Acesse **Privacidade e Segurança** (ou **Segurança e Privacidade** em versões mais antigas do macOS).
4. Vá até a aba **Geral**.
5. Clique no ícone de cadeado no canto inferior esquerdo e autentique-se com uma conta de administrador do Mac.
6. Localize a seção **“Permitir aplicativos baixados de:”** e selecione **“App Store e desenvolvedores identificados”**.
7. Alternativamente, se você acabou de ver a mensagem de erro do Evoto, pode aparecer um botão **“Abrir Mesmo Assim”** ao lado do nome do Evoto na aba **Geral**. Clique nele para permitir a abertura pontualmente.
8. Feche os Ajustes/Preferências do Sistema.
9. Retorne ao aplicativo Evoto e abra-o novamente. Ele deverá iniciar normalmente.

---

### Como permitir o Evoto no antivírus do Windows?

Programas antivírus e anti-malware podem, ocasionalmente, bloquear processos relacionados ao Evoto, impedindo seu funcionamento adequado. Ao criar uma exceção (whitelist), você garante que o Evoto funcione sem interferências.

**Importante:**Os passos podem variar levemente conforme a versão do antivírus. Recomendamos excluir **toda a pasta de instalação do Evoto** (por exemplo, `C:\Program Files\Evoto` ou `C:\Program Files (x86)\Evoto`) para evitar conflitos.

**Windows Defender**

1. Abra **Segurança do Windows** (pela área de notificação ou pelo menu Iniciar).
2. Selecione **Proteção contra vírus e ameaças**.
3. Clique em **Configurações de proteção contra vírus e ameaças**.
4. Role até **Exclusões** e clique em **Adicionar ou remover exclusões**.
5. Clique em **Adicionar uma exclusão** e selecione **Pasta**.
6. Selecione a pasta de instalação do Evoto (ex.: `C:\Program Files\Evoto`).
7. Clique em **Selecionar pasta** para confirmar.

Para mais detalhes, consulte: [*Add an exclusion to Windows Security*](https://www.google.com/search?q=https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-ad47-27b9-e67324b2ce26)

**McAfee**

1. Abra o software de segurança McAfee.
2. Vá para **Segurança do PC** → **Firewall**.
3. Procure por **Conexões de Internet para Programas** ou **Permissões de Programas**.
4. **Se o Evoto estiver listado:**

-
- Selecione o Evoto e clique em **Editar**.
- Em **Acesso**, selecione **Entrada e Saída** (**Incoming and Outgoing**) e altere o tipo de **Padrão** para **Abrir para todos os dispositivos**.
- Clique em **Salvar**.

5.**Se o Evoto não estiver listado:**

-
- Clique em **Adicionar**.
- Clique em **Procurar** e localize o arquivo `Evoto.exe` (Evoto executable file).
- Selecione-o e clique em **Abrir**.
- Configure **Entrada e Saída (Incoming and outgoing)**como **Abrir para todos os dispositivos**.
- Clique em **Salvar**.

Para mais detalhes, consulte: [*How to exclude files from virus scans on Windows - McAfee*](https://www.google.com/search?q=https://www.mcafee.com/support/%3FarticleId%3DTS100813%26page%3Dshell%26shellPage%3Ddevice-security/firewall/firewall-rules)

**Avast**

1. Abra a interface do Avast.
2. Vá para **Configurações**.
3. Selecione **Geral** → **Exclusões**.
4. Na aba **Caminhos de Arquivos**, clique em **Procurar**.
5. Selecione a pasta de instalação do Evoto.
6. Recomenda-se excluir a pasta inteira.
7. Confirme as alterações e certifique-se de que a proteção em tempo real esteja ativada.

Para mais detalhes, consulte: [*Avast Antivirus scan exclusions*](https://support.avast.com/en-us/article/Antivirus-scan-exclusions/).

**ESET**

1. Abra o ESET Smart Security ou ESET NOD32 Antivirus.
2. Pressione **F5** para abrir as **Configurações Avançadas**.
3. Expanda **Antivírus e antispyware** → **Exclusões**.
4. Clique em **Adicionar**.
5. Selecione a pasta de instalação do Evoto.
6. Clique em **OK** para confirmar.

Para mais detalhes, consulte: [*Exclude an application by name from scanning in ESET Windows home products*](https://www.google.com/search?q=https://support.eset.com/en/kb2779-exclude-an-application-by-name-from-scanning-in-eset-windows-home-products).

**Avira**

1. Clique com o botão direito no ícone do Avira e desative temporariamente a proteção em tempo real.
2. Instale ou execute o Evoto.
3. Reative a proteção em tempo real.
4. Abra o Avira e vá para **Proteção** → **Proteção em tempo real**.
5. Acesse **Exceções** ou **Exclusões**.
6. Adicione a pasta do Evoto ou o arquivo `Evoto.exe`.
7. Confirme as alterações.

Para mais detalhes, consulte no site oficial de Avira.

**Bitdefender**

1. Abra o Bitdefender.
2. Clique em **Proteção**.
3. Acesse **Configurações** do módulo Antivírus.
4. Vá para a aba **Exclusões**.
5. Clique em **Adicionar**.
6. Selecione a pasta de instalação do Evoto ou o arquivo `Evoto.exe` que pretende excluir.
7. Confirme e garanta que a proteção em tempo real esteja ativada.

Para mais detalhes, consulte: [*How to exclude files and folders from Bitdefender Antivirus scan*](https://www.google.com/search?q=https://www.bitdefender.com/consumer/support/article/19875/).

**Malwarebytes**

1. Abra o Malwarebytes.
2. Vá para **Configurações**.
3. Selecione **Lista de Permissões** (Allow List).
4. Clique em **Adicionar arquivo** ou **Adicionar pasta**.
5. Selecione o arquivo ou a pasta do Evoto.
6. Confirme a exclusão.

Para mais detalhes, consulte: [*Manage the Allow List in Malwarebytes for Windows v4*](https://www.google.com/search?q=https://support.malwarebytes.com/hc/en-us/articles/360038479534-Manage-the-Allow-List-in-Malwarebytes-for-Windows-v4).
