---
title: "Importación y Exportación Automática"
source_url: "https://support.evoto.ai/es/auto-import-and-export-es/"
source_type: "post"
source_id: "3144"
language: "es"
translation_group: "1673"
primary_category: "sin-categoria"
tags:
  - "pc-es"
migration_flags:
  - "image"
source_assets:
  - "https://res.evoto.ai/community/post/5kdVcApFuZw.png"
  - "https://res.evoto.ai/community/post/5kdVewi4YeE.png"
  - "https://res.evoto.ai/community/post/5kgtFYTuDUU.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-06-27-at-15.18.29-300x275.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-06-27-at-15.21.07-300x123.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/image-60-300x253.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/1-4-300x256.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/2-300x151.png"
---

La función de Importación y Exportación Automática de Evoto optimiza tu flujo de trabajo al monitorear carpetas designadas en busca de nuevas imágenes, aplicar automáticamente un ajuste preestablecido seleccionado y exportar los resultados editados. Esta funcionalidad es ideal para el procesamiento de imágenes de alto volumen y es especialmente útil cuando se combina con Captura Conectada.
### Descripción General

La Importación y Exportación Automática te permite:

- Monitorear una o más carpetas en busca de nuevas imágenes.
- Aplicar automáticamente un ajuste preestablecido al importar.
- Exportar imágenes editadas a una carpeta de destino separada.
- Personalizar la estructura de archivos, la frecuencia de exportación y más.

Esta función ayuda a automatizar tareas repetitivas, permitiéndote concentrarte en el trabajo creativo mientras Evoto se encarga del procesamiento.

> Notas La Importación y Exportación Automática y la Captura Conectada pueden usarse en el mismo proyecto. Funcionan de forma independiente y no interferirán entre sí. La Carpeta de Captura (Captura Conectada), la Carpeta Vigilada (Importación Automática) y la Carpeta de Exportación (Exportación Automática) deben estar separadas. Estas carpetas no pueden superponerse. La Importación y Exportación Automática solo funciona en la página del proyecto activo. Si regresas al Espacio de Trabajo del Proyecto o cambias de proyecto, el proceso se pausará. Mientras la Exportación Automática está activa, los módulos de edición están deshabilitados. Para realizar ajustes, pausa o detén la Exportación Automática.

---

### Cómo habilitar la Importación y Exportación Automática

#### Método 1: Habilitar al crear un nuevo proyecto

Después de crear un nuevo proyecto, habilita la opción de Importación y Exportación Automática para configurar la función desde el principio.

![image.png](https://res.evoto.ai/community/post/5kdVcApFuZw.png)

#### Método 2: Habilitar en la sección de Vista Previa

En un proyecto abierto, ve a la Sección de Vista Previa y haz clic en el ícono de Importación y Exportación Automática para acceder al módulo.
![image.png](https://res.evoto.ai/community/post/5kdVewi4YeE.png)

Consejo: Se recomienda configurar esto en un proyecto nuevo para evitar exportar imágenes existentes sin querer.
---

### Configuración de Importación Automática

#### Carpeta Vigilada

![image.png](https://res.evoto.ai/community/post/5kgtFYTuDUU.png)

- Selecciona hasta 100 carpetas para que Evoto las monitoree.
- Habilita Incluir Subcarpetas para monitorear subcarpetas ilimitadas de primer nivel dentro de cada carpeta.

#### Tipo de Imagen de Importación

Elige qué tipos de archivo importar automáticamente:

- JPEG
- RAW
- TIFF
- PNG

(Se pueden seleccionar múltiples formatos.)

#### Preajustes

Elige un preajuste que se aplicará automáticamente al importar. Puedes usar:

- Mis Preajustes
- Preajustes Recomendados

![](https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-06-27-at-15.18.29-300x275.png)

#### Configuración de Imagen de Vista Previa

- **Mostrar Última Imagen Importada** (predeterminado): Selecciona y muestra automáticamente la imagen importada más recientemente.
- **Mantener Selección Actual**: Mantiene la imagen actual seleccionada incluso cuando se agregan nuevas imágenes.

![](https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-06-27-at-15.21.07-300x123.png)

#### Iniciar Importación Automática

Haz clic en Iniciar Importación Automática para comenzar a monitorear la carpeta. Por defecto, solo se importarán las imágenes agregadas después de este punto; los archivos existentes se ignoran.

> Notas Puedes tener subcarpetas ilimitadas, pero solo se procesarán las subcarpetas de primer nivel. La configuración de importación no se puede cambiar después de que se inicie la Importación Automática.

##### Detección de Importación Inteligente (Reanudar Importación)

La Detección de Importación Inteligente permite reanudar la Importación Automática, asegurando que no se pierdan imágenes incluso si el flujo de trabajo de la carpeta caliente se interrumpe. Cuando está habilitada, Evoto rastrea qué imágenes se han importado de cada carpeta vigilada. Si la Importación Automática se pausa o detiene y se agregan nuevas fotos a la carpeta durante este tiempo, estas imágenes se importarán automáticamente la próxima vez que reinicies la Importación Automática.
![](https://support.evoto.ai/wp-content/uploads/2025/04/image-60-300x253.png)

Cómo Habilitar:
1. Ve a **Configuración > Preferencias**.
2. Encuentra la sección **Importación y Exportación Automática**.
3. Activa **Detección de Importación Inteligente**.

> Nota: Esta función solo se aplica a proyectos de carpeta caliente que se han configurado previamente. Los proyectos nuevos comenzarán desde cero independientemente de esta configuración.

---

### Configuración de Exportación Automática

#### Intervalo de Exportación Automática

Establece con qué frecuencia Evoto verifica si hay imágenes exportables:

- Rango: 1 segundos a 1 hora
- Predeterminado: 10 minutos

![](https://support.evoto.ai/wp-content/uploads/2025/04/1-4-300x256.jpg)

#### Configuración de Exportación de Imágenes

La Exportación Automática utiliza las mismas opciones de configuración que la exportación manual. Haz clic en Iniciar Exportación Automática para mostrar la configuración completa de exportación. Consulta más detalles en la [Configuración de Exportación](https://support.evoto.ai/how-to-use-import-export/#:~:text=Exporting%20Images,-Evoto%20provides%20comprehensive).

- Preajuste de Efectos
- Ubicación de Exportación
- Nombre de Archivo
- Tamaño de Imagen
- Configuración de Archivo
- Nitidez de Salida
- Configuración de Marca de Agua

![](https://support.evoto.ai/wp-content/uploads/2025/04/2-300x151.png)

#### Iniciar Exportación Automática

Haz clic en Iniciar Exportación Automática para activar la exportación automatizada.

> Notas Cualquier imagen que no se haya exportado automáticamente anteriormente, ya sea de importación automática o exportación manual, se exportará una vez detectada. Esto no consumirá créditos adicionales. Evita combinar la exportación manual con el reemplazo de archivos que no sean RAW al usar la Exportación Automática, ya que esto puede resultar en exportaciones duplicadas y uso innecesario de créditos. Para cambiar un ajuste preestablecido o editar la configuración durante la Exportación Automática: Pausa o detén la Exportación Automática. Actualiza el ajuste preestablecido. Reanuda la Exportación Automática. Los archivos originales permanecen en la Carpeta Vigilada y no se modifican.

---

### Monitoreo del Progreso

- **Barra de Progreso de Importación:** Muestra la actividad de importación en tiempo real. Incluye un botón de Pausa.
- **Barra de Progreso de Exportación:** Muestra el estado de exportación pero no se puede pausar una vez iniciada.

---

### Uso con Captura Conectada

La Importación y Exportación Automática funciona perfectamente con la Captura Conectada, permitiendo una automatización completa desde la captura hasta la exportación final.
#### Flujo de trabajo de ejemplo

1. Las imágenes se capturan mediante Captura Conectada.
2. Las imágenes se importan al proyecto activo a través de la Importación Automática.
3. Se aplica un ajuste preestablecido seleccionado.
4. El resultado final se exporta automáticamente a la carpeta de destino.

> Notas No uses la misma carpeta para captura, importación o exportación. Las tres deben permanecer separadas. Cuando uses RAW + JPEG, ambas versiones se importarán. Si la Exportación Automática está activa, esto puede resultar en exportaciones duplicadas.
