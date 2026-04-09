---
title: "Como Personalizar a Qualidade de Exportação de Imagens no Evoto"
source_url: "https://support.evoto.ai/pt-br/como-personalizar-a-qualidade-de-exportacao-de-imagens-no-evoto/"
source_type: "post"
source_id: "24341"
language: "pt-br"
translation_group: "1751"
primary_category: "sem-categoria"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2026/01/2-3-300x284.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2026/01/3-2-300x105.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2026/01/4-238x300.jpg"
---

O Evoto fornece opções flexíveis para personalizar a qualidade das imagens exportadas, garantindo que você obtenha sempre o resultado desejado. Esta guia ajudará você a otimizar a qualidade da imagem e o tamanho do arquivo ajustando cuidadosamente as configurações disponíveis.

Para mais informações, consulte nossa página completa sobre [Importação & Exportação](../../evoto-pc/como-começar/importacao-exportacao.md).

---

#### Escolher o Formato de Arquivo Ideal

O Evoto oferece suporte a múltiplos formatos de imagem, cada um adequado a diferentes necessidades.

- **Formato Original:**Esta opção exporta a imagem no formato original do arquivo. Se você tiver feito edições em um arquivo RAW, ele será exportado como JPEG. Caso a imagem contenha um canal alfa (como fundo transparente), ela será exportada como PNG.
- **JPG (8-bit):**Formato ideal quando o tamanho do arquivo é uma prioridade, como para uso na web, redes sociais e compartilhamento online. O JPG utiliza compressão, o que reduz o tamanho do arquivo, mas pode resultar em perda de alguns detalhes da imagem.
- **TIFF (8-bit / 16-bit):**A melhor opção para imagens de alta qualidade e sem perdas. O TIFF é um formato profissional que preserva todos os dados da imagem ao evitar compressão, sendo ideal para edições posteriores, impressão profissional e arquivamento.

#### Controlar Qualidade e Tamanho de Arquivo

A configuração de qualidade no Evoto está disponível ao exportar imagens no formato JPG e permite equilibrar a qualidade da imagem com o tamanho do arquivo.

![](https://support.evoto.ai/wp-content/uploads/2026/01/2-3-300x284.jpg)

- **Configurações da qualidade baseadas em porcentagem:** O Evoto utiliza um slider baseado em porcentagem para oferecer controle preciso da qualidade. Você pode escolher entre níveis predefinidos:
- Baixo, Médio, Alto ou Máximo
- Como alternativa, é possível ajustar manualmente o slider para definir uma porcentagem específica.
- **Observação:** Mesmo que você defina uma porcentagem muito baixa, o Evoto exportará a imagem com qualidade mínima de 20%, garantindo que o arquivo permaneça utilizável.
- **Limitar o tamanho do arquivo:** O Evoto permite definir um tamanho específico para o arquivo (por exemplo, "500 KB"). O algoritmo de exportação irá então comprimir a imagem para se aproximar o máximo possível do tamanho especificado.
- **Observação:** O tamanho final do arquivo pode não corresponder exatamente ao valor definido, devido à natureza da compressão de imagens. O algoritmo fará o possível para atender à sua solicitação sem comprometer a qualidade da imagem.

---

#### Ajustar o Nitidez de Saída (Output Sharpening)

O Evoto inclui configurações personalizadas de nitidez de saída (Output Sharpening) para otimizar suas imagens de acordo com o uso final, seja para exibição em tela ou impressão.

![](https://support.evoto.ai/wp-content/uploads/2026/01/3-2-300x105.jpg)

---

#### Ajustar a Resolução e as Dimensões

Ao cortar ou redimensionar uma imagem, é fundamental prestar atenção às configurações de resolução para manter a clareza.

- **Resolução para Corte:** Ao usar a configuração de corte L × A × Resolução (W × H × Resolution), você pode otimizar a nitidez da imagem exportada aumentando o valor de px/in (pixels por polegada). Por padrão, este valor geralmente é 300, mas você pode aumentá-lo até 30.000 para garantir uma alta densidade de pixel durante o corte, o que é especialmente importante para trabalhos com qualidade de impressão.

![](https://support.evoto.ai/wp-content/uploads/2026/01/4-238x300.jpg)

- **Outras Opções de Redimensionamento:**Para redimensionar imagens, você também pode utilizar outros tipos de escala, como Porcentagem, Largura & Altura (Width & Height) ou Lado Longo / Lado Curto (Long Edge / Short Edge), para definir as dimensões finais da imagem exportada.
