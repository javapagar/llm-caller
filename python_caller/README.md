### Mini-APP

## Configuración entorno y dependencias
Lo primero es generar el entorno virtual de python
```bash
python -m venv .venv
```

Se activa el entorno y se instalan las dependencias:
- Linux Mac
```bash
source .venv/bin/activate && \
pip install .
```
- windows
```
.\.venv\Scripts\activate.bat; pip install .
```
## Ejecución:
el parametro option:
- abstract: modo resumen. Si no se pasa el parámetro esta es la opción por defecto.
- classificate: clasifica tickets por prioridad
- extract: extrae los nombres encontrados en el texto

### Forma de uso
```bash
python mini_app.py --help
```

### Usando un mensaje de texto para extraer nombres
```bash
python mini_app.py -m "La Ingeniería de IA no es un concepto que haya surgido de la noche a la mañana." -o extract
```