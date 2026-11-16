FACTORES = {
    "DF1": {
        "nombre": "Estrategia de la Empresa",
        "categoria": "Gobernanza",
        "clase": "Liderazgo en Costos (5/5) / Estabilidad (4/5)",
        "impacto": "+30 APO06 / +30 EDM04",
        "ref": "Miles & Snow (1978); ISACA (2018a, p.21)",
        "herramienta": "Tipologías Estratégicas de Miles & Snow",
        "detalle": "DHM opera con márgenes reducidos en distribución perecedera. Prioriza eficiencia extrema y control de gastos (APO06, EDM04). Innovación libre atenuada (-30 en APO02/APO03).",
        "icon": "📊",
        "prioridad": "ALTA",
        "verificado": True
    },
    "DF2": {
        "nombre": "Metas Empresariales (BSC)",
        "categoria": "Gobernanza",
        "clase": "EG01, EG05, EG08, EG13",
        "impacto": "+35 APO04 (Máx Factor)",
        "ref": "Kaplan & Norton (1996); ISACA (2018a, pp.22-24)",
        "herramienta": "Balanced Scorecard (BSC)",
        "detalle": "Seleccionadas 4 metas del BSC: Financiera (EG01 peso 5), Cliente (EG05 peso 4), Procesos (EG08 peso 4), Innovación (EG13 peso 5). Cascada activa APO04 (+35) y BAI03 (+30).",
        "icon": "🎯",
        "prioridad": "ALTA",
        "verificado": True
    },
    "DF3": {
        "nombre": "Perfil de Riesgo",
        "categoria": "Gestión",
        "clase": "5 Cat. Críticas (2 Muy Alto / 3 Alto)",
        "impacto": "+85 APO13 (Máximo Global)",
        "ref": "Guía ISACA Riesgos (ISACA 2009, 2020); Santoso & Putri (2023)",
        "herramienta": "Guía ISACA de Gestión de Riesgos (Risk IT)",
        "detalle": "Concentración operativa en PC única con PostgreSQL sin firewall ni backup automático. SPOF crítico: Infraestructura (20/25) y Ataques lógicos (20/25). Desencadena APO13 (+85), BAI06 (+70), DSS02 (+60).",
        "icon": "🚨",
        "prioridad": "CRÍTICA",
        "verificado": True
    },
    "DF4": {
        "nombre": "Problemas de I&T (Dolencias)",
        "categoria": "Gestión",
        "clase": "Dolencias J(3), I(3), L(2)",
        "impacto": "+10 BAI01 / +10 BAI09",
        "ref": "Catálogo 20 Dolencias COBIT (ISACA 2018a); UNI (2026)",
        "herramienta": "Lista de Chequeo de Dolencias COBIT",
        "detalle": "J: Proyectos que fallan por falta de plan formal (Brecha B1). I: Sobrecarga del único Líder Técnico (D2). L: Modelo operativo poco claro. Activa BAI01 para gestión de programas e hitos CMMI.",
        "icon": "🧩",
        "prioridad": "ALTA",
        "verificado": True
    },
    "DF5": {
        "nombre": "Panorama de Amenazas",
        "categoria": "Gestión",
        "clase": "Híbrido 75% High / 25% Normal",
        "impacto": "+65 APO13 / +65 EDM03",
        "ref": "CTI Ciclo F3EAD (Brown & Roberts, 2017); ISACA (2018c, DF5)",
        "herramienta": "Inteligencia de Amenazas (CTI)",
        "detalle": "Entorno externo normal pero exposición interna severa (sin firewall perimetral, BYOD sin control en 20 vendedores). Amenazas de baja sofisticación causarían daño devastador.",
        "icon": "⚔️",
        "prioridad": "CRÍTICA",
        "verificado": True
    },
    "DF6": {
        "nombre": "Requerimientos Cumplimiento",
        "categoria": "Gestión",
        "clase": "High 25% · Normal 75% · Low 0%",
        "impacto": "+25 MEA03",
        "ref": "COBIT 2019 Design Toolkit v1.0, DF6; DF6.docx (UNI, 2026)",
        "herramienta": "Matriz de Obligaciones de Cumplimiento",
        "detalle": "Obligaciones sanitarias BPM, fiscales (DGII/IVA) y de licencias. MEA03.01 y MEA03.04 al Nivel 2 para cumplimiento proactivo del riesgo R2 (16/25).",
        "icon": "📜",
        "prioridad": "ALTA",
        "verificado": True
    },
    "DF7": {
        "nombre": "Rol de TI en la Empresa",
        "categoria": "Gobernanza",
        "clase": "Support=1 · Factory=3 · Turnaround=2 · Strategic=5",
        "impacto": "+30 EDM01",
        "ref": "COBIT 2019 Design Toolkit v1.0, DF7; McFarlan (1984); DF7.docx (UNI, 2026)",
        "herramienta": "Matriz Estratégica de McFarlan",
        "detalle": "Perfil híbrido Fábrica (3) + Estratégico (5). EDM01 maximiza por dependencia crítica del software propio. El CDC actúa como consejo de gobierno de I&T, cerrando B8.",
        "icon": "⚙️",
        "prioridad": "ALTA",
        "verificado": True
    },
    "DF8": {
        "nombre": "Modelo de Abastecimiento (Sourcing)",
        "categoria": "Gestión",
        "clase": "Outsourcing 30% · Cloud 50% · Insourced 20%",
        "impacto": "+15 EDM03",
        "ref": "COBIT 2019 Design Toolkit v1.0, DF8; DF8.docx (UNI, 2026)",
        "herramienta": "Matriz de Decisión de Sourcing (Toolkit)",
        "detalle": "Híbrido con dominancia Cloud. Terceros sin SLAs formales (Brecha B9). EDM03.01, .02 y .03 al Nivel 2 con el CDC como comité de riesgos.",
        "icon": "🏢",
        "prioridad": "ALTA",
        "verificado": True
    },
    "DF9": {
        "nombre": "Métodos de Implementación",
        "categoria": "Gestión",
        "clase": "50% Ágil / 10% DevOps / 40% Trad.",
        "impacto": "+65 BAI03 / +60 BAI02 / +60 BAI06",
        "ref": "CMMI Development V3.0 (2023); Agile Fluency Model",
        "herramienta": "Modelos de Ciclo de Vida (CMMI / Agile Fluency)",
        "detalle": "Evolución en ciclos cortos con cambios gerenciales frecuentes (50% ágil), despliegues incrementales con Git (10% DevOps) y disciplina documental CMMI Nivel 2 (40% tradicional).",
        "icon": "🔧",
        "prioridad": "ALTA",
        "verificado": True
    },
    "DF10": {
        "nombre": "Adopción de Tecnología",
        "categoria": "Comportamiento",
        "clase": "75% First Mover / 15% Follower / 10% Slow",
        "impacto": "+75 APO07 (Máx Factor) / +55 APO08",
        "ref": "Rogers (1995, 4ª ed. Difusión de Innovaciones); ISACA (2018a)",
        "herramienta": "Curva de Adopción de Rogers",
        "detalle": "Sistema central propio en Django/Clean Architecture convierte a DHM en First Mover sectorial. Detona APO07 (+75%) para retener talento técnico y mitigar el riesgo de fuga de know-how.",
        "icon": "🚀",
        "prioridad": "ALTA",
        "verificado": True
    },
    "DF11": {
        "nombre": "Tamaño de la Empresa",
        "categoria": "Comportamiento",
        "clase": "38.0 FTE (Microempresa / SME)",
        "impacto": "Simplificación Integral I&T",
        "ref": "Conteo Oficial FTE; Guía Pymes COBIT (ISACA 2018a, p.28)",
        "herramienta": "", # Excluido por petición
        "detalle": "38 empleados a tiempo completo (<50 FTE). Aplica directrices de simplificación: comités corporativos unificados en el CDC, roles cruzados y políticas ligeras pero auditables.",
        "icon": "👥",
        "prioridad": "MEDIA",
        "verificado": True
    }
}
