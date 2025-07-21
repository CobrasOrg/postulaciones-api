# postulaciones-api

API REST desarrollada con FastAPI para gestionar las postulaciones de mascotas a solicitudes de donación.

## Características

- FastAPI como framework web
- MongoDB como base de datos
- Estructura modular y escalable
- Configuración de CORS
- Variables de entorno con `python-dotenv`
- Husky para validación de mensajes de commit
- Pre-commit hooks para linting y formateo

## Despliegue

La API está disponible en: 
https://postulaciones-api-production.up.railway.app/docs


## Requisitos

- Python 3.8+
- MongoDB
- Node.js y npm (para Husky)
- pip

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/CobrasOrg/postulaciones-api.git
cd postulaciones-api
```

2. Crear y activar el entorno virtual:

```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instalar dependencias de Python:

```bash
pip install -r requirements.txt
```

4. Instalar dependencias de Node.js (para Husky y hooks):

```bash
npm install
```

5. Configurar variables de entorno:

```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

## Ejecución

```bash
uvicorn main:app --reload
```

La aplicación estará disponible en:

- http://localhost:8000 – Mensaje de bienvenida
- http://localhost:8000/api/v1/base/health – Health check
- http://localhost:8000/docs – Documentación Swagger UI
- http://localhost:8000/redoc – Documentación ReDoc


## Estructura del Proyecto

```
postulaciones-api/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   └── base.py
│   │       └── api.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   └── database.py
│   ├── models/
│   │   └── base.py
│   └── schemas/
│       └── base.py
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── commitlint.config.js
├── main.py
├── package.json
├── README.md
└── requirements.txt
```

## Desarrollo

### Agregar Nuevos Endpoints

1. Crear un nuevo archivo en `app/api/v1/endpoints/`
2. Definir el router y los endpoints
3. Registrar el router en `app/api/v1/api.py`

### Convención de Mensajes de Commit

Los mensajes de commit deben seguir el formato:

```
tipo(alcance): descripción

[cuerpo opcional]

[pie opcional]
```

Tipos permitidos:

- `feat`: Nueva característica
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Cambios de formato (espacios, punto y coma, etc.)
- `refactor`: Refactorización de código
- `test`: Agregar o modificar tests
- `chore`: Cambios en tareas de mantenimiento

## Licencia

MIT
