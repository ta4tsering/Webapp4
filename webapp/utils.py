import re 
import os
from pathlib import Path
from webapp import app


def utility():
    work_path = Path(os.path.join(app.config["FILES_UPLOAD"]))
    work_text = work_path.read_text(encoding="utf-8")
    result = []
    pg_text = ""
    work_keys = re.split(f"\n", work_text)
    for i, work_key in enumerate(work_keys[1:],1):
        if i % 2 == 0:
            pg_text += work_key
        else:
            pg_text += work_key
            result.append(pg_text)
            pg_text = ""
    return print(result)
        
        
    
    
