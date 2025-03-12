# 1️⃣ Usamos Python 3.12 como imagen base
FROM python:3.12

# 2️⃣ Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# 3️⃣ Copiamos solo el archivo de dependencias
COPY requirements.txt .

# 4️⃣ Copiamos `polaris-core` dentro del contenedor antes de instalar dependencias
COPY polaris_core/ /app/polaris_core/

# 5️⃣ Instalamos `polaris-core` manualmente antes de instalar `requirements.txt`
RUN pip install -e /app/polaris_core/

# 6️⃣ Solo copiamos `tg_clientes` sin instalarlo
COPY tg_clientes /app/tg_clientes

# 7️⃣ Copiamos el archivo de configuración
COPY development.ini /app/development.ini

# 7️⃣ Ahora sí, instalamos el resto de las dependencias
RUN pip install -r requirements.txt



# 8️⃣ Exponemos el puerto 9999
EXPOSE 9999

# 9️⃣ Comando para iniciar la aplicación
CMD ["gearbox", "serve"]

