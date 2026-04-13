# 🚜 AgroMarket - E-commerce Sustentable (Full Stack)

Una plataforma de comercio electrónico diseñada específicamente para el sector agrícola. 
Este proyecto conecta productores de insumos sustentables y orgánicos con agricultores,
 a través de una interfaz rápida, moderna y responsiva.

## 🌟 Sobre el Proyecto

AgroMarket nace con el propósito de modernizar el acceso a productos agrícolas mediante una arquitectura 
**Full Stack Desacoplada**. 

A diferencia de las aplicaciones monolíticas tradicionales, este proyecto separa completamente la lógica de negocios y la base de datos (Backend) de la interfaz de usuario (Frontend), comunicándolos exclusivamente a través de una API REST. Esto permite que el sistema sea altamente escalable y esté preparado para futuras integraciones (como una app móvil).

## 🚀 Características Principales

* **Catálogo Dinámico:** Los productos se renderizan en tiempo real consumiendo la API mediante JavaScript (`fetch`).
* **Etiquetado Inteligente:** Sistema visual para destacar automáticamente los productos con certificación orgánica 🌱.
* **Gestión de Medios:** Soporte completo para subida y visualización de imágenes de productos configurado en el backend.
* **Panel de Administración:** Gestión completa de inventario, categorías y productos a través del Admin nativo de Django.
* **Diseño Responsivo:** Interfaz construida con Tailwind CSS, optimizada para dispositivos móviles y escritorio.

## 🛠️ Stack Tecnológico

**Backend (API)**
* Python 🐍
* Django & Django REST Framework (DRF)
* PostgreSQL (Base de datos relacional)
* Pillow (Procesamiento de imágenes)
* django-cors-headers (Gestión de seguridad y accesos)

**Frontend (Cliente)**
* HTML5 & Vanilla JavaScript
* Tailwind CSS (Vía CDN con configuración personalizada)

## ⚙️ Arquitectura
El proyecto consta de dos partes independientes:
1. **API (Django):** Se encarga de la base de datos, la seguridad y de servir los datos en formato JSON.
2. **Cliente (HTML/JS):** Se encarga del diseño, la experiencia de usuario y de solicitar los datos al servidor.

## 💻 Instalación y Uso Local

Para correr este proyecto en tu máquina local, sigue estos pasos:

### 1. Levantar el Backend (API)
```bash
# Clonar el repositorio
git clone https://github.com/danielaportoa/agromarket.git

# Entrar a la carpeta del backend
cd backend_agromarket

# Crear y activar entorno virtual (Mac/Linux)
python3 -m venv venv
source venv/bin/activate
# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones a la base de datos PostgreSQL
python3 manage.py migrate

# Iniciar el servidor
python3 manage.py runserver