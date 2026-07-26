import os 

def Email(email):
  try:
    os.system(f"holehe {email}")
  except Exception as e:
    return f"erro: {e}"
