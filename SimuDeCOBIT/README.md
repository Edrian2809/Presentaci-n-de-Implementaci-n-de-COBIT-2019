# 🟢 DHM COMMAND CENTER v4.0 — "The Audience Edition"

> **Sistema de Defensa Final: COBIT 2019 & CMMI v3.0**
> *Universidad Nacional de Ingeniería (UNI) — Ingeniería de Software III*

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![COBIT 2019](https://img.shields.io/badge/Framework-COBIT%202019-00F0FF?style=for-the-badge)
![CMMI v3.0](https://img.shields.io/badge/Model-CMMI%20v3.0-00FF66?style=for-the-badge)

## 📖 Descripción General

El **DHM Command Center** es una aplicación interactiva desarrollada en Streamlit que transforma una defensa académica tradicional en una experiencia visual e inmersiva. 

El sistema simula la implementación de un marco de **Gobierno de I&T basado en COBIT 2019** y un **modelo de madurez CMMI v3.0 Nivel 2** para la empresa ficticia **Distribuidora Huevos Méndez (DHM)**. A través de un diseño *Cyberpunk Hacker*, la aplicación justifica financieramente (ROI), técnicamente (11 Factores de Diseño) y operativamente (Plan de 24 semanas) la transformación digital de la empresa.

## 🚀 Características Principales (Historia en 5 Actos)

La navegación está estructurada como una narrativa secuencial para el jurado:

*   **🎬 PITCH Inicial:** Landing page con KPIs de impacto, resumen ejecutivo y llamado a la acción.
*   **ACTO I — El Problema:** Diagnóstico visual (AS-IS) usando un Radar Chart para comparar la capacidad actual vs. la meta Nivel 2.
*   **ACTO II — El Diagnóstico:** 
    *   **11 Flip Cards:** Tarjetas 3D interactivas que muestran los Factores de Diseño (DF1-DF11), sus referencias y justificaciones.
    *   **Mapa de Calor P×I:** Matriz interactiva 5x5 con los 19 riesgos oficiales de COBIT. Los 5 riesgos críticos brillan intensamente, mientras que los de menor impacto están atenuados.
*   **ACTO III — La Solución:** Roadmap visual Q1-Q4, simulador de asignación presupuestal interactivo con *sliders* y un Radar Chart dinámico.
*   **ACTO IV — El Impacto:** Business Case demostrable.
    *   **Waterfall Chart:** Cascada financiera que demuestra la inversión vs. los beneficios.
    *   **Evolución del ROI:** Gráfico de línea que comprueba el *Break-even* en el Mes 4.
    *   **Medidores de Madurez:** Gráfico de brechas (Gap Chart) por dominio (EDM, APO, BAI, DSS, MEA).
*   **ACTO V — La Evidencia:** Simulador de cierre de brechas CMMI (B1-B10), Timeline cronológico de evidencias auditables (con hashes) y **Bibliografía completa en formato APA 7ª Edición**.

## 🛠️ Stack Tecnológico

*   **Backend/Lógica:** Python 3.9+
*   **Frontend/UI:** Streamlit (Layout wide)
*   **Visualización de Datos:** ApexCharts.js (inyectado vía HTML/JS)
*   **Estilos y Animaciones:** CSS3 puro (Efectos neón, Flip Cards 3D, Scanlines, Glows)
*   **Inyección de Componentes:** `streamlit.components.v1`

## ⚙️ Requisitos e Instalación

Sigue estos pasos para ejecutar la aplicación en tu entorno local:

1. **Clonar el repositorio** o descargar los archivos.
2. **Asegurarte de tener Python instalado** (versión 3.9 o superior).
3. **Instalar las dependencias necesarias** (se recomienda usar un entorno virtual):
   ```bash
   pip install streamlit pandas
   ```
4. **Verificar la carpeta de documentación:** Asegúrate de tener la carpeta `extraido/` (o los archivos referenciados) en el mismo directorio, aunque la app usa los datos *hardcodeados* extraídos de ellos.

## 🏃‍♂️ Ejecución

Para iniciar el servidor de Streamlit, abre tu terminal en la carpeta del proyecto y ejecuta:

```bash
streamlit run dhm_governance_suite.py
```

La aplicación se abrirá automáticamente en tu navegador (usualmente en `http://localhost:8501`).

## 📂 Estructura del Proyecto

```text
📦 DHM-Command-Center
 ┣ 📜 dhm_governance_suite.py  # Código fuente principal (UI, lógica y estilos)
 ┣ 📜 README.md                # Este archivo
 ┗ 📂 extraido/                # Carpeta con los documentos fuente (Opcional para la ejecución)
    ┣ 📜 DocumentoFinalCobit2019.docx
    ┣ 📜 CasoNegocioPrograma.docx
    ┣ 📜 PlanConsolidadoPrograma.docx
    ┗ 📜 TablaBrechasPrograma.docx
```

## 👥 Autores y Créditos

*   **Anngelly Aleska Mejia Mendoza** (Carnet: 2022-07951)
*   **Edrian Gabriel Espinoza Herrera** (Carnet: 2022-07861)
*   **Eliza Sougey Aguirre Gonzales** (Carnet: 2022-07781)

**Asignatura:** Ingeniería de Software III  
**Tutor:** Msc. Roberto Carlos Alfaro Arriola  
**Grupo:** 5T2-COM-S  
**Fecha:** 05 de Noviembre del 2026  
**Institución:** Universidad Nacional de Ingeniería (UNI) - Managua, Nicaragua.

---
*"La tecnología no define la estrategia, pero sin gobierno, la estrategia no se sostiene."*
```


### ¿Por qué solo estas dos?
1.  **`streamlit`**: Es el motor principal de la aplicación (interfaz, componentes, sesiones). Requerimos la versión 1.30 o superior porque el código usa `st.toggle` y `st.html`, que son funciones más recientes.
2.  **`pandas`**: Aunque en la versión final no se explota al máximo, el código tiene la línea `import pandas as pd`. Si no está en el archivo, la app lanzará un `ModuleNotFoundError` al iniciar.
3.  *Nota:* Las demás librerías que usas (`json`, `datetime`, `math`) ya vienen instaladas por defecto en Python (Standard Library). Y `streamlit.components.v1` ya viene dentro del paquete de Streamlit.

### 🚀 ¿Cómo instalarlo?
Si estás subiendo esto a un repositorio de GitHub para desplegarlo en **Streamlit Community Cloud**, la plataforma leerá este archivo automáticamente.

Si lo estás corriendo en tu computadora, solo abre tu terminal en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```