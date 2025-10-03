@echo off
REM Crear entorno virtual
python -m venv venv

REM Activar entorno virtual (usar call para que se mantenga)
call venv\Scripts\activate

REM Instalar dependencias dentro del venv
pip install -r requirements.txt
pip install ipykernel

REM Registrar el kernel
python -m ipykernel install --user --name=taller1-env --display-name "Python (taller1-env)"

echo.
echo =======================================
echo  Entorno virtual y kernel configurados
echo =======================================
pause
