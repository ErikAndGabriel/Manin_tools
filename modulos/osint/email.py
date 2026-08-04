import os 
from ui.banner import banner_execucao1 
from core.clear import clear
def Email(email):
  try:
    clear()
    print(banner_execucao1)
    os.system(f"holehe {email}")
  except Exception as e:
    return f"erro: {e}"
