# 🚀 Prueba Técnica en TurboGears  

Este repositorio contiene mi implementación de la prueba técnica en **TurboGears** para [Polarissi](https://www.polarissi.com) 
Durante el desarrollo, logré avanzar en varias funcionalidades clave, 
pero también encontré algunas dificultades que documenté en el **Pull Request**.  

📌 **Estado actual:**  
✅ Pull Request enviado y en espera de revisión.  
🔗 **Ver el Pull Request aquí:** [PullRequest](https://github.com/pablotech80/tg_clientes/pull/1#issue-2905690787)  

---

## 📌 Resumen del Desarrollo  

### ✅ **Lo que se ha implementado con éxito**  
- Configuración inicial del entorno con TurboGears y PostgreSQL.  
- Creación del modelo de base de datos con SQLAlchemy, incluyendo la tabla de clientes.  
- Configuración de Jinja2 para el renderizado de plantillas.  
- Implementación de rutas básicas para el CRUD de clientes.  
- Creación de la plantilla `login.html` para la autenticación.  
- Se configuró un usuario administrador (`admin/admin`).  

### ❌ **Dificultades encontradas y pendientes**  
- No logré completar la autenticación de usuarios correctamente (problema con el sistema de sesiones).  
- No pude hacer funcionar correctamente la parte de edición y eliminación de clientes.  
- Configuración de permisos y restricciones para que solo usuarios autenticados accedan al CRUD.  
- No pude probar la aplicación completamente debido a errores que no logré solucionar.  

---

## 💡 **Alternativa en Flask**  
Dado que tenía más experiencia con Flask, desarrollé una versión funcional con este framework. 
Esta versión puede consultarse en mi repositorio:  

🔗 [**Repositorio PolarisApp Flask**](https://github.com/pablotech80/Polarisapp-Flask.git)  

---

## 🔍 **Cómo Ejecutar el Proyecto**  
Si deseas probar el código, sigue estos pasos:  

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/pablotech80/tg_clientes.git
   cd tg_clientes
   ```
2. **Crear y activar un entorno virtual**
    ```bash
   python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```

3. **Instalar las dependencias**  
   ```bash
   pip install -r requirements.txt

   ```
4. **Configurar la base de datos (PostgreSQL)**

- Restaurar el backup .sql provisto
- Configurar sqlalchemy.url en development.ini


5. **Ejecutar la aplicación**
    ```bash 
    gearbox serve --port 9999
    ```
- Accede a la aplicación en http://localhost:9999/

## 📩 Contacto y Feedback

Aprecio cualquier feedback que puedan brindarme para mejorar la implementación.

📌 Pull Request en revisión: PullRequest

GitHub: [**pablotech80**](https://github.com/pablotech80)

Atentamente,
Pablo Techera 
