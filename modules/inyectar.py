import os
import subprocess
from datetime import datetime, timedelta

start_date = datetime(2025, 4, 16)
total_days = 365
commits_per_day = 78

print(f">>> Iniciando inyeccion de {total_days * commits_per_day} commits...")

for day in range(total_days + 1):
    current_date = start_date + timedelta(days=day)
    date_str = current_date.strftime('%Y-%m-%dT12:00:00')
    
    # Configuramos la fecha para este bloque de commits
    os.environ['GIT_AUTHOR_DATE'] = date_str
    os.environ['GIT_COMMITTER_DATE'] = date_str
    
    # Ejecutamos los 78 commits del dia en un solo proceso de shell para ir rapido
    cmd = f'for /L %j in (1,1,78) do git commit -m "Data entry %j - {date_str}" --allow-empty --quiet'
    subprocess.run(cmd, shell=True, env=os.environ)
    
    if day % 10 == 0:
        print(f">>> Progreso: Dia {day}/365 ({date_str})")

print(">>> PROCESO FINALIZADO.")
