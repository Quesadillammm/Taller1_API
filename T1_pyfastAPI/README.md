🎓 Trainee API — T1_pyfastAPIAPI REST diseñada para la gestión de aprendices (trainees), desarrollada con FastAPI 🐍 y MongoDB Atlas 🍃. Cuenta con un CRUD completo, validación de datos integrada y despliegue continuo en Render ☁️.🌐 Enlaces del Proyecto (Producción)🚀 Servicio en Render: https://t1-pyfastapii.onrender.com📚 Documentación Swagger UI: https://t1-pyfastapii.onrender.com/docs📖 Documentación ReDoc: https://t1-pyfastapii.onrender.com/redoc⏳ Nota: Al estar alojado en el plan gratuito de Render, el servidor entra en estado de suspensión tras unos minutos de inactividad. La primera petición puede tardar unos segundos mientras se inicializa el servicio.✨ Características⚡ Operaciones CRUD: Creación, lectura, actualización y eliminación de registros de aprendices.✅ Validación de Datos: Validación de esquemas y correos electrónicos mediante Pydantic v2.🍃 Persistencia en la Nube: Conexión a base de datos MongoDB Atlas mediante pymongo.📑 Documentación Automática: Generación de interfaces interactivas Swagger UI y ReDoc.🧩 Arquitectura Modular: Organización del código dividida en modelos, controladores y vistas.🛠️ Tecnologías UtilizadasCategoríaTecnología / HerramientaLenguajePython 3.11+Framework WebFastAPI, UvicornBase de DatosMongoDB Atlas, PyMongoValidaciónPydantic v2, email-validatorDespliegueRenderControl de VersionesGit / GitHub📂 Estructura del ProyectoT1_pyfastAPI/
├── 📁 data/
├── 📁 src/
│   ├── 📁 models/
│   │   ├── database.py      # Conexión a la base de datos MongoDB Atlas
│   │   └── model.py         # Modelos y esquemas de Pydantic
│   ├── 📁 templates/
│   │   └── controllers.py   # Lógica de negocio y handlers del CRUD
│   └── 📁 views/
│       ├── main.py          # Punto de entrada de la app FastAPI y endpoints
│       └── view.py          # Configuración de URLs base
├── 📁 test/
│   └── test_main.py         # Pruebas de verificación de conexión
├── 📄 requirements.txt      # Dependencias del proyecto
├── 📄 structure.sh          # Script bash para generación de la estructura
└── 📄 README.md             # Documentación principal del proyecto
⚙️ Requisitos PreviosPara ejecutar la API en un entorno de desarrollo local, se requiere:Python 3.11+ instalado en el sistema.Un cluster configurado en MongoDB Atlas con permisos de acceso a la red (IP activa).Git para el manejo de versiones.📥 Instalación y Ejecución Local# 1. Clonar el repositorio
git clone https://github.com/Quesadillammm/Taller1_API.git
cd Taller1_API

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # En Linux / macOS
# venv\Scripts\activate          # En Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Iniciar el servidor localmente
uvicorn src.views.main:app --reload
👤 AutorAndrés Camilo Córdoba Ramírez