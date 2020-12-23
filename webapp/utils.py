import re 
import os
from pathlib import Path
from webapp import app


def utility():
    work_path = Path("/Users/tashitsering/Desktop/W4OCR/webapp/static/files/file.txt")
    work_text = work_path.read_text(encoding="utf-8")
    result = work_text.splitlines()
    return result
        
        
    
    
