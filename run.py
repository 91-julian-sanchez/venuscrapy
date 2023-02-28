import argparse
import subprocess
import time
import logging

# Configurar el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
handler = logging.FileHandler('logs.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Creamos un parser para leer el argumento 'tag' que se pasa al script
parser = argparse.ArgumentParser()
parser.add_argument('--tag', required=True)

# Parseamos los argumentos
args = parser.parse_args()
tag = args.tag

# Generamos un timestamp para usar en el nombre del archivo de output
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"output/extract/chaturbate-{tag}-{timestamp}.csv"

# Comando para correr scrapy y guardar el output en un archivo
scrapy_command = ["scrapy", "crawl", "chaturbate", "-O", output_file, "-a", f"tag={tag}"]
logger.info(f"Ejecutando comando: '{' '.join(scrapy_command)}'")
print(f"Ejecutando comando: {' '.join(scrapy_command)}")
subprocess.run(scrapy_command)

# Comando para correr el script etl.py con los argumentos necesarios
etl_command = ["python", "etl.py", "--tag", tag, "--timestamp", timestamp]
logger.info(f"Ejecutando comando: '{' '.join(etl_command)}'")
print(f"Ejecutando comando: {' '.join(etl_command)}")
subprocess.run(etl_command)