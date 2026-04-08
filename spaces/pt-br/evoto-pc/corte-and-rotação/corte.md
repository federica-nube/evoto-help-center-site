---
title: "Corte"
source_url: "https://support.evoto.ai/pt-br/corte/"
source_type: "post"
source_id: "16247"
language: "pt-br"
translation_group: "625"
primary_category: "sem-categoria"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/04/corte1-182x300.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/corte2-300x104.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/corte3-205x300.jpg"
---

O Evoto oferece vários métodos de corte para atender a diferentes necessidades, incluindo proporção fixa, tamanho livre e dimensões personalizadas. Após ajustar o corte, clique em ****OK**** no canto inferior direito para aplicar o resultado.

#### Tipos de Corte

![](https://support.evoto.ai/wp-content/uploads/2025/04/corte1-182x300.jpg)

- **Original**

Recorta a imagem com base nas dimensões originais importadas para o Evoto.

- **Conforme Capturado**

Utiliza as dimensões registradas pela câmera no momento da captura.

- **Proporção Fixa**

Insira uma proporção fixa de largura e altura para recortar manualmente a imagem mantendo as proporções especificadas.

> Observação: Supor ta Localização de Rosto por IA e pode ser salvo como predefinição, desde que não haja mais de um rosto na imagem e que o rosto não esteja girado em mais de 75 graus.

- **Livre**

Permite recorte livre arrastando diretamente a moldura de corte na tela. A proporção e as dimensões podem ser ajustadas livremente.

- **Foto de ID**

Projetado para retratos profissionais e fotos de identificação. Com padrão de 300 PPI, garante saída de impressão de alta qualidade.

> Observação: É melhor usar quando a unidade de corte estiver configurada em cm ou inches.

- **L × A × Resolução**

Define largura, altura e resolução exatas para um recorte de precisão.

- **Minha Predefinição de Corte**

Personalize e salve seus parâmetros de corte preferidos. Clique em ****Criar Predefinição de Corte**** para salvar as configurações e utilizá-las no futuro. A seleção de Minha Predefinição de Corte aparecerá depois de você Criar Predefinição de Corte.

![](https://support.evoto.ai/wp-content/uploads/2025/04/corte2-300x104.jpg)

---

#### Localização por IA

![](https://support.evoto.ai/wp-content/uploads/2025/04/corte3-205x300.jpg)

Localização por IA pode ser ativada nos seguintes tipos de corte:

Proporção fixa, 1:1, 4:5, 5:7, 2:3, 16:9, 1,91:1, 2:1, 3:1, 4:3, L × A × Resolução, Foto de Identidade.

Quando ativado, o recurso**Localização por IA** seleciona de forma inteligente os sujeitos completos e ajusta a porcentagem de distância em relação aos limites do corte, incluindo:

- Posicionamento do corte com base na localização do sujeito
- Posicionamento do corte com base na localização do rosto

**Alinhamento automático de pessoa**

O recurso Alinhamento automático de pessoa no módulo de Localização por IA (apenas para fotos de uma única pessoa):

- Alinhamento vertical usando o eixo central do sujeito
- Alinhamento horizontal usando a linha de base dos olhos

##### Opções de Área de Localização

- **Cabeça**: inclui rosto e cabelo
- **Cabeça + Topo**: inclui rosto, cabelo e qualquer acessório na cabeça
- **Rosto**: foca estritamente no rosto

##### Sliders de Ajuste

- **Margem superior:** Ajusta o espaço entre o topo da cabeça e a borda superior da foto.
- **Tamanho da cabeça:** Controla o quão grande a cabeça aparece na imagem final.
- **Posição horizontal de rosto:** Define onde o rosto aparece horizontalmente na imagem:
- 50 = rosto centralizado
- 25 = rosto deslocado para a esquerda
- 75 = rosto deslocado para a direita

> Observação: Ao usar o corte L × A × Resolução, é possível definir uma resolução personalizada. O corte de Foto de I D tem padrão de 300 PPI. Outros tipos de corte usarão a resolução original da imagem.

---

#### Dimensões da Imagem e Casos de Borda

O recurso Localização de Rosto por IA é desativado quando:

- A imagem contém mais de uma pessoa
- O rosto do sujeito está inclinado em mais de 75 graus

Quando os sliders de recorte ultrapassam os valores permitidos, eles retornam automaticamente para o intervalo válido mais próximo.

**Sincronizar Configurações**

Ao sincronizar configurações de recorte da Imagem A para a Imagem B:

- Se a Imagem B não tiver rosto detectável ou contiver múltiplos rostos, o recorte não será sincronizado.
- Se os valores sincronizados excederem o intervalo suportado na Imagem B, eles serão ajustados para o limite permitido mais próximo.
