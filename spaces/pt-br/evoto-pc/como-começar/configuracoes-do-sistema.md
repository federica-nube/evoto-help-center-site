---
title: "Configurações do Sistema"
source_url: "https://support.evoto.ai/pt-br/configuracoes-do-sistema/"
source_type: "post"
source_id: "16971"
language: "pt-br"
translation_group: "598"
primary_category: "sem-categoria"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/04/desempenho-300x245.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/sync-1-300x53.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/sync2-271x300.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/sync3-300x245.jpg"
---

wp:tadv/classic-paragraph
As configurações do sistema do Evoto permitem otimizar o desempenho, gerenciar o cache, controlar o comportamento das visualizações e personalizar opções de exportação para se adequar melhor ao seu fluxo de trabalho e hardware.

---

# **Desempenho**

Essas configurações ajudam a melhorar a velocidade de processamento de acordo com as capacidades do seu dispositivo.

![](https://support.evoto.ai/wp-content/uploads/2025/04/desempenho-300x245.jpg)

## **Configurações de Velocidade de Renderização**

O Evoto oferece várias opções para melhorar o desempenho de renderização, especialmente durante edições complexas ou fluxos de trabalho de grande volume. Ajustar essas opções pode acelerar os processos de pré-visualização e exportação, equilibrando o uso de recursos e a qualidade do resultado.

### Velocidade de Visualização

Essas configurações ajudam a acelerar a visualização de efeitos, alocando mais recursos do sistema para o processo de renderização:

- ****Aceleração de Renderização de Efeito de Retrato****: Utiliza mais poder de processamento do computador para acelerar a renderização de efeitos relacionados a retratos durante a visualização.
- ****Aceleração de Renderização de Efeito de Cor****: Utiliza mais poder de processamento para acelerar a renderização de ajustes relacionados à cor durante a visualização.

### Velocidade de Exportação

O Evoto aplica os efeitos uma segunda vez ao exportar imagens para garantir a máxima qualidade. Você pode habilitar a seguinte configuração para acelerar esse processo:

- **Aceleração de Renderização de Efeitos de Retrato (Exportação):**

Aloca mais poder de processamento para a renderização de efeitos de retrato durante a exportação, garantindo desempenho mais rápido.

> Observação: É necessário reiniciar o Evoto após habilitar esta configuração para que ela tenha efeito.

### Otimização de Retratos em Grupo

Para fotos com muitos sujeitos (tipicamente 15 ou mais), o Evoto oferece uma opção para melhorar a velocidade de processamento:

- ****Melhorar Velocidade de Processamento de Efeitos em Retratos em Grupo:****

Acelera a renderização de retratos em grupo grandes. Isso pode reduzir ligeiramente a precisão de certos efeitos, mas aumenta significativamente a velocidade de processamento. Desativar essa função garantirá maior precisão dos efeitos em grupo, porém resultará em tempos de processamento mais longos.

## **Configurações de Uso de Memória**

Otimizar o uso de memória ajuda a manter edição estável e responsiva. Essas opções controlam como o Evoto gerencia a memória durante as fases de visualização e exportação:

Fase de Visualização:

- ****Melhorar Utilização de Memória:****Aumenta a eficiência do uso de memória durante a visualização dos efeitos.

- ****Otimizar Espaço de Memória:****Libera recursos de memória adicionais para melhorar o desempenho da visualização.

Fase de Exportação:

- ****Melhorar Utilização de Memória:****Aumenta a velocidade de exportação melhorando a gestão de memória durante o processo.
- ****Otimizar Espaço de Memória:****Maximiza a memória disponível para garantir exportações estáveis e eficientes.

> Observação: É necessário reiniciar o Evoto para que as configurações de memória tenham efeito.

## **Configurações de Rede**

Duração do Timeout de Solicitação: Altere o tempo que o sistema tentará encontrar uma conexão de internet estável antes de exibir uma mensagem de erro de timeout. O padrão do sistema é 3 minutos (180 segundos).

---

# Exportação

- **Máximo de Exportações Simultâneas**

O Evoto define automaticamente com base no seu sistema. Aumentar esse número pode impactar o desempenho do sistema. Ajuste apenas se necessário.

- **Legenda/Descrição da Imagem**

Escolha se os metadados da imagem exportada devem incluir:

-
  - **Evoto (padrão)**
  - **Informações Originais (da imagem de origem)**

---

# **Cachê**

Gerencie as configurações de cachê do Evoto através de:

- **Windows:** Centro Pessoal → Configurações → Cachê
- **macOS:** Evoto → Preferências ou pressione Command “,”→ Cachê

**Configurações de Cachê incluem:**

- **Expiração do Cachê:** Defina a limpeza automática entre 3–15 dias.
- **Limpar Cachê:** Clique em ****Limpar Cachê****para remover dados armazenados imediatamente.

> Observação: Isso apagará todo o histórico de ajustes manuais, como liquify.

- **Tamanho Máximo do Cachê:** Defina um limite de armazenamento. Quando excedido, o cache será limpo automaticamente.

---

# **Visualização**

As configurações de visualização permitem personalizar como as imagens aparecem durante a edição, sem afetar a qualidade da exportação final.

****Espaço de Cor****

Escolha o espaço de cor da visualização:

- sRGB (padrão, recomendado para web)
- Adobe RGB (para gama de cores mais ampla em displays compatíveis)

****Tamanho da Visualização (px)****

Ajusta a resolução da visualização. O Evoto seleciona um padrão baseado no seu sistema. Isso não afeta a qualidade da imagem exportada.

****Visualização em Tamanho Real em Ajustes de Cor em Tempo Real****

Com essa opção ativada, as visualizações no modo de Ajustes de Cor em Tempo Real serão exibidas em resolução total, independentemente do tamanho definido em Tamanho da Visualização (px).

****Configurações de Miniaturas****

Gerencie como as miniaturas de imagens são exibidas na Galeria.

****Configurações de Carregamento de Efeitos**** **(aplica-se apenas se “********Mostrar Imagens Editadas********” estiver ativado nas********Configurações de Miniaturas********)**

O recurso de ****pré-carregamento do efeito**** permite aplicar o efeito em outras imagens enquanto você sincroniza, economizando tempo de espera. Ao clicar na imagem sincronizada, você verá o resultado final com os efeitos aplicados imediatamente.

> Observação: Em computadores Windows, é necessário ter pelo menos 8GB de memória. Computadores MacBook não possuem essa restrição.

****Configurações de Posição e Zoom de Visualização Sincronizad********a********s****

Quando ativado, o Evoto lembra o nível de zoom e a posição usados pela última vez em cada imagem. Você pode ajustar esse comportamento no popup de Configurações de Visualização se necessário.

---

# **Preferências**

## **Frequência de Pop-up de sincronização**

Por padrão, o Evoto está configurado para mostrar o pop-up de Sincronização de Ajustes apenas uma vez por projeto:

- Na primeira vez que você sincronizar ou copiar/colar ajustes, aparecerá um pop-up onde você poderá escolher quais ajustes aplicar.
- Após isso, sincronizar ou colar aplicará automaticamente as configurações previamente selecionadas, sem exibir o pop-up novamente.

Se preferir ver a caixa de seleção de ajustes sempre que sincronizar ou copiar/colar:

1. Clique no botão ****Configurações****ao lado de ****S********incronizar****, no canto inferior direito da tela.

![](https://support.evoto.ai/wp-content/uploads/2025/04/sync-1-300x53.jpg)

2. Na janela pop-up, clique em ****Configurações de Frequência d********e********Pop-up****, no canto superior direito.

![](https://support.evoto.ai/wp-content/uploads/2025/04/sync2-271x300.jpg)

3. Altere a configuração para ****Acionar Sempre****.

![](https://support.evoto.ai/wp-content/uploads/2025/04/sync3-300x245.jpg)

4. Clique em ****OK****para salvar e fechar.

Com essa configuração ativada, você poderá confirmar ou ajustar quais edições serão aplicadas a cada ação de sincronização.

---

## **Captura Vinculada**

**Conexão Automática à Câmera**

Ative esta opção para conectar automaticamente sua câmera ao Evoto ao usar um cabo tether. Se desativada, você precisará conectar a câmera manualmente toda vez que ela for plugada.

## **Configurações de Alternância de Espaço de Trabalho**

Alternar Automaticamente para Editar

Quando ativado, ao importar imagens em um projeto vazio, o programa abrirá automaticamente o painel Editar.

---

# **Uso do Software**

****Compartilhar Minhas Informações de Uso****

Você pode escolher se deseja compartilhar seus dados de uso com o Evoto. Esses dados estão vinculados à sua conta e são utilizados exclusivamente para personalizar sua experiência e melhorar nossos serviços. Todas as informações compartilhadas são coletadas de forma anônima. Você pode desativar o compartilhamento de dados a qualquer momento neste menu.

****Análise de Conteúdo****

O Evoto pode analisar seu conteúdo utilizando técnicas como aprendizado de máquina (machine learning) e métodos similares para aprimorar nossos produtos e serviços. Toda a análise é realizada de maneira anônima, e você pode optar por não participar a qualquer momento. Observe que, em alguns casos específicos, essa configuração pode não se aplicar. [Saiba mais](https://res.evoto.ai/ui/www/policy/privacy.html)

/wp:tadv/classic-paragraph
