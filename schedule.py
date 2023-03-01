import subprocess
import argparse
import time
import logging
import random

# Configurar el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
handler = logging.FileHandler('logs.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

parser = argparse.ArgumentParser()
parser.add_argument('--tag', required=True)
args = parser.parse_args()
tag = args.tag

while True:
    logger.info(f"Ejecutando el comando 'python run.py --tag {tag}'")
    subprocess.run(["python", "run.py", "--tag", tag])
    time.sleep((15 * 60)+(random.randint(1, 3)))