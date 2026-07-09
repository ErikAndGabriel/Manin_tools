from controllers.osint import painel_osint
from controllers.phishing import painel_phishing
from controllers.web import painel_web
from controllers.network import painel_network
from controllers.malware import painel_malware
from controllers.loorkup import painel_lorkup
from controllers.dox import painel_dox
from controllers.c2 import painel_c2
from controllers.install import painel_install
opcoes = {
  
  "1": painel_phishing,
  "2": painel_osint,
  "3": painel_network,
  "4": painel_install,
  "5": painel_malwares,
  "6": painel_c2,
  "7": painel_web,
  "8": painel_lorkup,
  "9": painel_dox
}
  
