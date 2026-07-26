from controllers.outros_osint.osint_ip import painel_ip
from controllers.outros_osint.osint_cep import painel_cep 
from controllers.outros_osint.osint_cpf import painel_cpf
from controllers.outros_osint.osint_email import painel_email

ferramentas = {
  "1": painel_ip,
  "2": painel_email,
  "3": painel_cpf,
  "10": painel_cep
}
