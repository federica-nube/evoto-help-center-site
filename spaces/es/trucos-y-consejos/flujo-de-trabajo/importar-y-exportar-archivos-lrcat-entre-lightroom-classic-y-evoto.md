---
title: "Cómo integrar perfectamente Evoto con Lightroom Classic"
source_url: "https://support.evoto.ai/es/importar-y-exportar-archivos-lrcat-entre-lightroom-classic-y-evoto/"
source_type: "post"
source_id: "11639"
language: "es"
translation_group: "1079"
primary_category: "sin-categoria"
tags:
  - "tips"
---

Para muchos fotógrafos, Lightroom Classic es el software preferido para la gradación de color y la gestión de imágenes. El soporte de Evoto para imágenes individuales y archivos .lrcat (catálogos de Lightroom Classic) te permite usar ambos programas en conjunto, combinando el poder organizativo de Lightroom con las herramientas avanzadas de edición con IA de Evoto. Esta integración te ayuda a elevar tu trabajo sin sacrificar la comodidad. Las dos opciones de flujo de trabajo Puedes integrar Evoto en tu flujo de trabajo de dos formas principales, según tus necesidades.
1. Integración de imagen individual (viaje rápido de ida y vuelta)
Este flujo de trabajo es ideal para enviar rápidamente una sola imagen de Lightroom a Evoto para una edición puntual, como un retoque de retrato, antes de devolverla.
2. Integración completa de catálogo (procesamiento por lotes)
Este flujo de trabajo es para fotógrafos que quieren aprovechar el poder de la IA de Evoto para el procesamiento por lotes o mantener la estructura de su proyecto mientras cambian entre plataformas. Es ideal para un proyecto completo o una colección de imágenes.
---

### Flujo de trabajo 1: Integración de imagen individual

Este es el método más rápido para realizar ediciones con IA en una sola imagen.
1. **Comienza en Lightroom Classic:** Inicia tu proceso seleccionando, organizando o realizando ediciones iniciales en tu imagen en Lightroom.
2. **Enviar a Evoto:** Haz clic derecho en la imagen que deseas editar, luego selecciona **Editar en > Editar en Evoto**.
3. **Editar en Evoto:** La imagen se abrirá en Evoto. Realiza tus ediciones avanzadas (por ejemplo, piel, ojos, cabello, etc.).
4. **Exportar de vuelta a Lightroom:** Cuando estés listo, haz clic en **Exportar** en Evoto y usa la siguiente configuración:
- **Exportar a:** Selecciona la ubicación de la carpeta original de la foto.
- **Archivos existentes:** Elige **Reemplazar** y asegúrate de que la opción **"Reemplazar archivo(s) original(es)"** esté marcada.
5. **Actualizar en Lightroom:** Cuando vuelvas a Lightroom, es posible que necesites hacer clic en el icono de metadatos y seleccionar **Importar configuración desde disco** para actualizar la imagen y reflejar los cambios realizados en Evoto.

---

### Flujo de trabajo 2: Integración completa de catálogo

Este flujo de trabajo está diseñado para fotógrafos que desean mantener la estructura de su proyecto mientras cambian entre plataformas.
#### Paso 1: Prepara tu catálogo en Lightroom

Crea o abre tu archivo .lrcat existente en Lightroom Classic. Este catálogo servirá como base para importar en Evoto.
#### Paso 2: Importa el catálogo en Evoto

Evoto facilita traer un catálogo completo de Lightroom a tu espacio de trabajo.
- **Arrastrar y soltar:** Arrastra y suelta directamente el archivo .lrcat en Evoto.
- **Vía Nuevo Proyecto:** Alternativamente, crea un nuevo proyecto y selecciona el archivo .lrcat desde las opciones de importación.

Una vez importado, puedes elegir qué colecciones específicas o conjuntos filtrados dentro del catálogo importar a Evoto.
- **Opciones de importación:**
- **Importar configuración desde .lrcat:** Marca esta casilla si deseas que los controles deslizantes de color básicos de Lightroom (por ejemplo, Exposición, Temperatura, Tinte) se transfieran a Evoto.
- **Lo que no se transfiere:** Ciertos ajustes de Lightroom no se transferirán a Evoto, ya que dependen de diferentes motores de renderizado. Estos incluyen:
- Corrección de perspectiva
- Desenfoque de lente
- Ajustes locales
- Enmascaramiento avanzado

#### Paso 3: Edita tus imágenes en Evoto

Edita tus imágenes importadas usando el conjunto completo de herramientas de Evoto. Puedes aplicar preajustes, sincronizar ajustes en un lote y usar todas las funciones de IA.
#### Paso 4: Exporta el catálogo desde Evoto

Cuando hayas terminado de editar, puedes exportar tus imágenes y metadatos de vuelta a un catálogo compatible con Lightroom.
- **Para exportar:** Selecciona todas las imágenes que deseas exportar, luego ve a **Exportar > Exportar como archivo .lrcat**.
- **Opciones de exportación:**
- **Carpeta .lrcat original:** Exporta a la carpeta que contiene el archivo .lrcat original y añade una pila en Lightroom.
- **Carpeta específica:** Crea un nuevo archivo .lrcat con las imágenes editadas y los metadatos en una ubicación elegida.
- **Escritorio:** Mismo comportamiento que "Carpeta específica", pero guarda el nuevo archivo .lrcat directamente en tu escritorio.

### Consideraciones clave

- **Soporte de archivos RAW:** Evoto admite la importación de imágenes RAW a través de archivos .lrcat. Sin embargo, **las imágenes RAW no se pueden exportar**; deben convertirse a TIFF o JPG.
- **Reemplazo de archivos no RAW:** Esta opción reemplaza las imágenes originales no RAW (JPG, TIFF, PNG) en Lightroom con las versiones editadas en Evoto. Evoto hace automáticamente una copia de seguridad de los archivos originales para permitir reediciones sin gastar créditos adicionales.
- **Reedición:** Para reeditar una imagen existente, ábrela de nuevo en Evoto y vuelve a exportarla. Para nuevas imágenes añadidas a tu .lrcat original, puedes hacer clic derecho para abrirlas en Evoto, editarlas y exportarlas de vuelta.

Esta guía está diseñada para fotógrafos que desean mantener el control mientras maximizan la velocidad y la calidad.
