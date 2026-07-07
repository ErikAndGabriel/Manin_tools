from config.APIS.api_ip import APIS_IP
from core.config import Timeout, Headers
import json 
import requests 

class Ip:
  def __init__(self, ip, arquivo):
    self.ip = ip
    self.arq = arquivo
    self.timeout = Timeout("api")
    self.headers = Headers("aleatorio")
    
  def IpBusca(self):
    url = APIS_IP["ipwois"]["url"].format(self.ip)
    resposta = requests.get(
      url, 
      timeout=self.timeout,
      headers=self.headers
    )
    
    if resposta.status_code == 200:
      data = resposta.json()
      print(f"""
      api em uso.......: {APIS["api_ip"]}
      ip...............: {data["ip"]}
      sucesso..........: {data["success"]}
      tipo.............: {data["type"]}
      continente.......: {data["continent"]}
      codigo continente: {data["continent_code"]}
      região...........: {data["region"]}
      codigo região....: {data["region_code"]}
      cidade...........: {data["city"]}
      coordenadas......: {data["latitude"]}, {data["longitude"]}
      is eu............: {data["is_eu"]}
      postal...........: {data["postal"]}
      calling_code.....: {data["calling_code"]}
      capital..........: {data["capital"]}
      borders..........: {data["borders"]}
      img..............: {data["flag"]["img"]}
      emoje............: {data["flag"]["emoje"]}
      emoji_unicode....: {data["flag"]["emoji_unicode"]}
      asn..............: {data["connection"]["asn"]}
      org..............: {data["connection"]["org"]}
      isp..............: {data["connection"]["isp"]}
      domínio..........: {data["connection"]["domain"]}
      id...............: {data["timezone"]["id"]}
      addr.............: {data["timezone"]["addr"]}
      is dst...........: {data["timezone"]["is_dst"]}
      offset...........: {data["timezone"]["offset"]}
      utc..............: {data["timezone"]["utc"]}
      """)
      return True
    else:
      return "erro de conexão"
