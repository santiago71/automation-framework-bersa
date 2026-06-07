# Automation Testing Framework - Banco Entre Ríos

## Descripción

Framework de automatización de pruebas funcionales desarrollado en Python utilizando Selenium WebDriver y Pytest.

El proyecto fue diseñado siguiendo el patrón **Page Object Model (POM)** con el objetivo de garantizar escalabilidad, mantenibilidad y reutilización del código.

Actualmente automatiza el proceso de autenticación de usuarios en la plataforma web de Banco Entre Ríos, validando escenarios de login exitoso y login fallido mediante pruebas basadas en datos externos.

---

## Objetivos del Proyecto

* Automatizar pruebas funcionales de aplicaciones web.
* Implementar buenas prácticas de automatización QA.
* Aplicar el patrón de diseño Page Object Model (POM).
* Utilizar Data Driven Testing mediante archivos CSV.
* Generar evidencias automáticas de ejecución.
* Generar reportes HTML con resultados detallados.

---

## Tecnologías Utilizadas

* Python 3
* Selenium WebDriver
* Pytest
* Pytest HTML
* Google Chrome
* ChromeDriver
* Visual Studio Code
* Git
* GitHub

---

## Arquitectura del Framework

El framework está organizado siguiendo el patrón **Page Object Model (POM)**, separando la lógica de negocio de la interacción con los elementos de la interfaz.

```text
project/
│
├── page/
│   ├── base_page.py
│   └── login_page.py
│
├── test/
│   └── test_login.py
│
├── data/
│   └── login.csv
│
├── utils/
│   ├── assertions.py
│   └── data_reader.py
│
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Funcionalidades Implementadas

* Page Object Model (POM)
* Data Driven Testing utilizando CSV
* Fixtures reutilizables con Pytest
* Esperas explícitas mediante WebDriverWait
* Capturas automáticas de evidencia
* Reportes HTML automáticos
* Parametrización de pruebas con Pytest
* Reutilización de componentes mediante herencia

---

## Casos de Prueba Automatizados

### Login Exitoso

Valida que un usuario con credenciales válidas pueda acceder correctamente al sistema.

### Login Fallido

Valida que el sistema responda correctamente ante credenciales inválidas o usuarios bloqueados.

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/santiago71/automation-framework-bersa.git
```

Ingresar al directorio del proyecto:

```bash
cd automation-framework-bersa
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución de Pruebas

Ejecutar todas las pruebas:

```bash
pytest -v
```

Ejecutar únicamente las pruebas de login:

```bash
pytest -v test/test_login.py
```

---

## Generación de Reportes

El framework genera automáticamente:

* Reporte HTML de ejecución.
* Capturas de pantalla de cada escenario ejecutado.
* Evidencias visuales integradas en el reporte.

Ejemplo de ejecución:

```bash
pytest --html=reporte.html --self-contained-html
```

---

## Buenas Prácticas Aplicadas

* Separación de responsabilidades.
* Reutilización de código mediante herencia.
* Centralización de acciones comunes en BasePage.
* Uso de locators centralizados.
* Datos de prueba externos.
* Automatización mantenible y escalable.

---

## Mejoras Futuras

* Integración continua con GitHub Actions.
* Ejecución Headless para CI/CD.
* Soporte para múltiples navegadores.
* Configuración por ambientes (QA, UAT, PROD).
* Logging centralizado.
* Integración con Allure Reports.

---

## Autor

**Santiago Sanchez**

Proyecto desarrollado con fines de aprendizaje, práctica y consolidación de conocimientos en QA Automation utilizando Selenium y Pytest.
