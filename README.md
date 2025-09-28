# DuoTasks

DuoTasks es una aplicación web para la gestión de tareas colaborativas, desarrollada con Flask y Supabase.

## Características
- Registro e inicio de sesión de usuarios
- Gestión de tareas personales y compartidas
- Interfaz moderna con HTML, CSS y Jinja2
- Integración con Supabase para autenticación y almacenamiento

## Estructura del proyecto
```
app/
  __init__.py
  routes.py
  supabase_client.py
  routes/
    auth.py
    home.py
    tasks.py
  static/
    css/
      style.css
  templates/
    base.html
    index.html
    login.html
    navbar.html
    register.html
run.py
requirements.txt
```

## Instalación
1. Clona el repositorio:
   ```
   git clone https://github.com/Manriv31/DuoTasks.git
   ```
2. Crea y activa un entorno virtual:
   ```
   python -m venv venv-duoTasks
   venv-duoTasks\Scripts\activate
   ```
3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso
1. Configura tus credenciales de Supabase en las variables de entorno.
2. Ejecuta la aplicación:
   ```
   python run.py
   ```
3. Accede a `http://localhost:5000` en tu navegador.

## Dependencias principales
- Flask
- Supabase-py
- Jinja2
- python-dotenv

## Licencia
Este proyecto está bajo la licencia MIT.
