FROM jenkins/jenkins:lts

USER root

# Instalar Python, pip y venv
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Crear entorno virtual en /opt/venv
RUN python3 -m venv /opt/venv

# Activar entorno virtual e instalar pandas y requests
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install pandas requests

# Agregar entorno virtual al PATH del sistema
ENV PATH="/opt/venv/bin:$PATH"

USER jenkins
