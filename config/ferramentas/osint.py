from controllers.outros_osint.osint_ip import painel_ip
from controllers.outros_osint.osint_cep import painel_cep 
from controllers.outros_osint.osint_cpf import painel_cpf
from controllers.outros_osint.osint_email import painel_email
from controllers.outros_osint.osint_whois import painel_whois
from controllers.outros_osint.osint_telegram import painel_telegram

ferramentas = {
  "1": painel_ip,
  "2": painel_email,
  "3": painel_cpf,
  "4": painel_whois,
  "5": painel_telegram,
  "10": painel_cep
}
