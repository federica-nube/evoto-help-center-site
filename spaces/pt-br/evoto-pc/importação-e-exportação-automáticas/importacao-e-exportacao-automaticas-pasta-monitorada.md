---
title: "Importação e Exportação Automáticas (Pasta Monitorada)"
source_url: "https://support.evoto.ai/pt-br/importacao-e-exportacao-automaticas-pasta-monitorada/"
source_type: "post"
source_id: "16283"
language: "pt-br"
translation_group: "1673"
primary_category: "sem-categoria"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/04/10-278x300.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/11-1-195x300.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/12-3-156x300.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/image-60-300x253.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/13-4-300x206.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/1-5-300x150.jpg"
---

O recurso de **Importação e Exportação Automáticas** otimiza seu fluxo de trabalho monitorando pastas designadas para novas imagens, aplicando automaticamente um predefinição selecionada e exportando os resultados editados. Essa funcionalidade é ideal para o processamento de imagens em grande volume e é especialmente útil quando combinada com a Captura com conexão.

---

#### Visão Geral

As Importação e Exportação Automáticas permitem que:

- Monitore uma ou mais pastas em busca de novas imagens.
- Aplique automaticamente uma predefinição na importação.
- Exporte as imagens editadas para uma pasta de destino separada.
- Personalize a estrutura de arquivos, a frequência de exportação e muito mais.

Esse recurso ajuda a automatizar tarefas repetitivas, permitindo que você se concentre no trabalho criativo enquanto o Evoto cuida do processamento.

---

#### Notas Principais

- Importação e Exportação Automáticas e Captura com Câmera Conectada podem ser usados no mesmo projeto. Eles funcionam de forma independente e não interferem entre si.
- A **Pasta de Captura** (Captura com Câmera Conectada), a **Pasta Monitorada** (Importação Automática) e a **Pasta de Exportação** (Exportação Automática) devem ser separadas. Essas pastas não podem se sobrepor.
- As Importação e Exportação Automáticas funcionam apenas na página do projeto ativo. Se você voltar para o Espaço de Trabalho do Projeto ou alternar para outro projeto, o processo será pausado.
- Enquanto a Exportação Automática estiver ativa, os módulos de edição ficam desativados. Para fazer ajustes, pause ou interrompa a Exportação Automática.

---

#### Como Ativar as Importação e Exportação Automáticas

##### Método 1: Ativar ao criar um novo projeto

Após criar um novo projeto, ative a opção ****Importação e Exportação Automáticas**** para configurar o recurso desde o início.

![](https://support.evoto.ai/wp-content/uploads/2025/04/10-278x300.jpg)

##### Método 2: Ativar na seção de Visualização

Em um projeto aberto, vá até a seção **Visualização** e clique em ícone ****Importação e Exportação Automáticas**** para acessar o módulo.

![](https://support.evoto.ai/wp-content/uploads/2025/04/11-1-195x300.jpg)

> Dica: Recomenda-se configurar este recurso em um novo projeto para evitar a exportação não intencional de imagens existentes.

---

#### Configurações de Importação Automática

##### Pasta Monitorada

- Selecione até 100 pastas para monitorar.
- Habilite a opção ****Incluir subpastas**** para monitorar subpastas ilimitadas de primeiro nível dentro de cada pasta.

![](https://support.evoto.ai/wp-content/uploads/2025/04/12-3-156x300.jpg)

##### Formato de Imagem para Importação

Escolha quais formatos de arquivo serão importados automaticamente:

- JPEG
- RAW
- TIFF
- PNG

(Vários formatos podem ser selecionados.)

##### Predefinições

Escolha uma predefinição para ser aplicada automaticamente na importação. Você pode escolher:

- Minhas predefinições
- Predefinições recomendadas

##### Configurações de Visualização da Imagem

- **Mostrar a última imagem importada (padrão):** seleciona e exibe automaticamente a imagem mais recentemente importada.
- **Manter a seleção atual:** mantém a imagem atual selecionada mesmo quando novas imagens são adicionadas.

##### Iniciar Importação Automática

Clique em ****Iniciar importação automática****para começar a monitorar a pasta. Somente as imagens adicionadas após esse ponto serão importadas; os arquivos existentes serão ignorados.

##### Observação (Importação)

- É possível ter subpastas ilimitadas, mas apenas as subpastas de primeiro nível serão processadas.
- As configurações de importação não podem ser alteradas depois que a importação automática é iniciada.

##### Detecção de Importação Inteligente (Retomar Importação)

A Detecção de Importação Inteligente permite a retomada da Importação Automática, garantindo que nenhuma imagem seja perdida mesmo que o fluxo de trabalho da pasta monitorada seja interrompido.

Quando ativada, o Evoto rastreia quais imagens foram importadas de cada pasta monitorada. Se a Importação Automática for pausada ou interrompida e novas fotos forem adicionadas à pasta durante esse período, essas imagens serão importadas automaticamente na próxima vez que você reiniciar a Importação Automática.

![](https://support.evoto.ai/wp-content/uploads/2025/04/image-60-300x253.png)

**Como Ativar:**

1. Vá para **Configurações > Preferências**.
2. Encontre a seção **Importação e Exportação Automáticas**.
3. Ative a **Detecção de Importação Inteligente**.

**Nota:** Este recurso se aplica apenas a projetos de pasta monitorada que foram configurados anteriormente. Novos projetos começarão do zero, independentemente desta configuração.

---

#### Configurações de Exportação Automática

##### Intervalo de Exportação Automática

Definir frequência de verificação de imagens para exportação.

![](https://support.evoto.ai/wp-content/uploads/2025/04/13-4-300x206.jpg)

- **Intervalo:** de 1 segundos a 1 hora
- **Padrão:** 10 minutos

##### Configurações de Exportação de Imagem

**Configurações de Exportação de Imagem**

A **Exportação Automática** utiliza as mesmas opções de configuração que a exportação manual. Clique em **Iniciar Exportação Automática** para exibir todas as configurações de exportação. Para mais detalhes, consulte [**Configurações completas de exportação**](https://support.evoto.ai/pt-br/importacao-exportacao/#:~:text=Editar%20no%20Evoto.-,Exportar%20Imagens,-O%20Evoto%20oferece).

**Opções disponíveis:**

- **Predefinição de Efeito**
- **Local de Exportação**
- **Nome do Arquivo**
- **Tamanho da Imagem**
- **Configurações do Arquivo**
- **Nitidez de Saída**
- **Configurações de Marca d’Água**

![](https://support.evoto.ai/wp-content/uploads/2025/04/1-5-300x150.jpg)

##### Iniciar Exportação Automática

Clique em ****Iniciar Exportação Automática**** para ativar o processo de exportação.

##### Observação (Exportação)

Qualquer imagem que ainda não tenha sido exportada automaticamente — seja a partir de importação automática ou exportação manual — será exportada assim que for detectada. Isso não consumirá créditos adicionais.

Evite combinar **exportação manual com substituição de arquivos não-RAW** ao usar a Exportação Automática, pois isso pode resultar em exportações duplicadas e consumo créditos não necessários.

Para alterar um predefinição ou editar configurações durante a Exportação Automática:

1. Pause ou pare a Exportação Automática.
2. Atualize a predefinição.
3. Retome a Exportação Automática.

Os arquivos originais permanecem na Pasta Monitorada e não são modificados.

---

#### Monitoramento do Progresso

- ****Barra de progresso de importação:****Exibe em tempo real a atividade de importação. Inclui um botão ****Pausar****.
- ****Barra de progresso de exportação:****Mostra o status da exportação, mas **não pode ser pausada** depois de iniciada.

---

#### Uso com Captura com Câmera Conectada (Tethered Shooting)

A função Importação e Exportação Automáticas funciona perfeitamente com a Captura com câmera conectada, permitindo automação completa do fluxo de trabalho — da captura até a exportação final.

##### Exemplo de Fluxo de Trabalho

1. As imagens são capturadas via Captura com Câmera Conectada.
2. As imagens são importadas para o projeto ativo por meio da Importação Automática.
3. É aplicada uma predefinição selecionada.
4. O resultado final é exportado automaticamente para a pasta de destino.

##### Observação

- As pastas de captura, de importação ou de exportação devem permanecer separadas.
- Ao trabalhar com **RAW + JPEG**, ambas as versões serão importadas. Se a Exportação Automática estiver ativa, isso pode resultar em exportações duplicadas.
