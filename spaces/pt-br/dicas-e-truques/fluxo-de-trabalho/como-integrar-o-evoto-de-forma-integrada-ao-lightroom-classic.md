---
title: "Como integrar o Evoto de forma integrada ao Lightroom Classic"
source_url: "https://support.evoto.ai/pt-br/como-integrar-o-evoto-de-forma-integrada-ao-lightroom-classic/"
source_type: "post"
source_id: "23913"
language: "pt-br"
translation_group: "1079"
primary_category: "sem-categoria"
migration_flags:
  - "possible_shortcode"
---

Para muitos fotógrafos, o Lightroom Classic é o software de referência para correção de cores e gerenciamento de imagens. O suporte do Evoto tanto para imagens individuais quanto para arquivos .lrcat (catálogos do Lightroom Classic) permite que você utilize os dois programas de forma integrada, combinando o poderoso sistema de organização do Lightroom com as ferramentas avançadas de edição por IA do Evoto. Essa integração ajuda você a elevar a qualidade do seu trabalho sem abrir mão da praticidade.

[embed]https://youtu.be/KKUupdgn1rg[/embed]

**Duas opções de fluxo de trabalho**

Você pode integrar o Evoto ao seu fluxo de trabalho de duas formas principais, dependendo das suas necessidades.

**1. Integração de imagem individual (ida e volta rápida)** Esse fluxo de trabalho é ideal para enviar rapidamente uma única imagem do Lightroom para o Evoto para uma edição pontual, como o retoque de um retrato, e depois retorná-la ao Lightroom.

**2. Integração de catálogo completo (processamento em lote)** Esse fluxo de trabalho é indicado para fotógrafos que desejam aproveitar o poder da IA do Evoto para processamento em lote ou manter a estrutura do projeto ao alternar entre as plataformas. É a melhor opção para trabalhar um projeto inteiro ou uma coleção de imagens.

---

### Fluxo de trabalho 1: Integração de imagem individual

Este é o método mais rápido para realizar edições com IA em uma única imagem.

1. **Comece no Lightroom Classic:** Inicie o processo selecionando, organizando ou fazendo ajustes iniciais na imagem no Lightroom.
2. **Enviar para o Evoto:** Clique com o botão direito na imagem que deseja editar e selecione **Editar em > Editar no Evoto**.
3. **Editar no Evoto:** A imagem será aberta no Evoto. Realize as edições avançadas desejadas (por exemplo, pele, olhos, cabelo etc.).
4. **Exportar de volta para o Lightroom:** Quando finalizar, clique em **Exportar** no Evoto e utilize as seguintes configurações:

-
- **Exportar para:** selecione o local da pasta original da foto.
- **Arquivos existentes:** escolha **Substituir** e certifique-se de que a opção **Substituir arquivo(s) original(is)** esteja marcada.

5. **Atualizar no Lightroom:** Ao retornar ao Lightroom, pode ser necessário clicar no ícone de metadados e selecionar **Importar configurações do disco** para atualizar a imagem e refletir as alterações feitas no Evoto.

---

### Fluxo de trabalho 2: Integração de catálogo completo

Este fluxo de trabalho é indicado para fotógrafos que desejam manter a estrutura do projeto ao alternar entre plataformas.

#### Passo 1: Preparar seu catálogo no Lightroom

Crie ou abra seu arquivo .lrcat existente no Lightroom Classic. Esse catálogo servirá como base para a importação no Evoto.

#### Passo 2: Importar o catálogo para o Evoto

O Evoto facilita a importação de um catálogo completo do Lightroom para o seu espaço de trabalho.

- **Arrastar e soltar:** Arraste diretamente o arquivo .lrcat para o Evoto.
- **Via Novo Projeto:** Como alternativa, crie um novo projeto e selecione o arquivo .lrcat nas opções de importação.

Após a importação, você pode escolher coleções específicas ou conjuntos filtrados dentro do catálogo para importar no Evoto.

**Opções de importação:**

- **Importar configurações do .lrcat:** Marque esta opção se quiser que os controles básicos de cor do Lightroom (por exemplo, Exposição, Temperatura, Matiz) sejam aplicados no Evoto.
- **O que não é transferido:**Alguns ajustes do Lightroom não podem ser transferidos para o Evoto, pois dependem de motores de renderização diferentes. Isso inclui:
- Correção de perspectiva
- Desfoque de lente
- Ajustes locais
- Máscaras avançadas

#### Passo 3: Editar suas imagens no Evoto

Edite as imagens importadas utilizando todas as ferramentas do Evoto. É possível aplicar predefinições, sincronizar ajustes em lote e usar todos os recursos de IA.

#### Passo 4: Exportar o catálogo do Evoto

Após finalizar a edição, exporte suas imagens e metadados de volta para um catálogo compatível com o Lightroom.

- **Como exportar:**Selecione todas as imagens que deseja exportar e vá em **Exportar > Exportar como arquivo .lrcat**.
- **Opções de exportação:**
- **Pasta do .lrcat original:** Exporta para a pasta que contém o arquivo .lrcat original e adiciona um stack no Lightroom.
- **Pasta específica:** Cria um novo arquivo .lrcat com as imagens editadas e metadados em uma pasta escolhida.
- **Desktop:** Comportamento igual à “Pasta específica”, mas salva o novo arquivo .lrcat diretamente para seu desktop.

---

### Considerações importantes

- **Suporte a arquivos RAW:** O Evoto suporta a importação de imagens RAW via arquivos .lrcat. No entanto, imagens RAW não podem ser exportadas diretamente; elas devem ser convertidas para TIFF ou JPG.
- **Substituição de arquivos não-RAW:** Essa opção substitui as imagens não-RAW originais (JPG, TIFF, PNG) no Lightroom pelas versões editadas no Evoto. O Evoto faz backup automático dos arquivos originais para permitir re-edições sem consumir créditos adicionais.
- **Re-edição:** Para re-editar uma imagem existente, abra-a novamente no Evoto e exporte-a novamente. Para novas imagens adicionadas ao seu .lrcat original, clique com o botão direito para abri-las no Evoto, edite e exporte de volta.

Este guia foi desenvolvido para fotógrafos que desejam manter controle total sobre seus projetos, maximizando velocidade e qualidade das edições.
