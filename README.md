# Clima_con_Kivy

El siguiente repositorio, contiene una aplicación para android hecha con python 3.0+
Kivy:
  Es un framework que nos ayuda a realizar dichas tareas, dividiendo la lógica y el diseño.
  Kivy tiene una cierta apariencia en cuanto a la estructura de html o css, haciendo que nosotros seamos más ordenados a la hora de programar


# Lo que necesitas...

Una vez desarrollado tu proyecto, necesitas convertir o compilar todo a un archivo "APK" el cual será el resultado final que podrás instalar en tu dispositivo móvil.
Para ello necesitas abrir "GOOGLE COLAB" el cual nos servirá de compilador.
Una vez en esa plataforma tendrás que cargar los archivos ".PY" y ".KV" para que inicie la conversión.
Luego tendras que escribir en cada linea ejecutable el siguiente codigo.

!pip install buildozer

!pip install cython==0.29.19

!apt install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev
    
!apt install -y \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good
    
!apt install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6

!apt install libffi-dev

!pip install kivy

!apt install ldd

!buildozer init

!buildozer -v android debug


# Recomendaciones
Ya que "GOOGLE COLAB" es un servicio en linea, cualquier interrupción en la red,hará que nos arroje un error, asi que asegurate de contar con una buena red.
Tambíen estas instrucciones las puedes realizar desde un S.O. con LINUX

