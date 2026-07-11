from ui.color import azul, reset 
menu_principal = f"""{reset}
HOME
│
├── {azul}[01]{reset} PHISHING.     
├── {azul}[02]{reset} OSINT
├── {azul}[03]{reset} NETWORK
├── {azul}[04]{reset} INSTALL
├── {azul}[05]{reset} MALWARES
├── {azul}[06]{reset} C2
├── {azul}[07]{reset} WEB
├── {azul}[08]{reset} LORKUP
├── {azul}[09]{reset} DOX
└── {azul}[00]{reset} EXIT
"""
menu_phishing = f"""{reset}
HOME
│
├── [01] PHISHING
│   │
│   ├── {azul}[01]{reset} ZPHISHING
│   ├── {azul}[02]{reset} FOTO
│   ├── {azul}[03]{reset} INFO
│   ├── {azul}[04]{reset} NETESCOLA
│   └── {azul}[00]{reset} VOLTAR
│
├── [02] OSINT
├── [03] NETWORK
├── [04] INSTALL
├── [05] MALWARES
├── [06] WEB
├── [07] XSS
├── [08] LOOKUP
├── [09] DOX
└── [00] EXIT
"""
menu_cep = f"""{reset}
HOME
│
├─
├── [02] OSINT
│   ├── [01] IP INFO
│   ├── [02] EMAIL (Holehe)
│   ├── [03] CPF
│   ├── [04] WHOIS
│   ├── [05] GOOGLE DORK
│   ├── [06] NOME
│   ├── [07] USERNAME
│   ├── [08] CNPJ
│   ├── [09] PHONE (API)
│   ├── [10] CEP
│   │   ├── {azul}[01]{reset} VIACEP
│   │   ├── {azul}[02]{reset} BRASILAPI
│   │   ├── {azul}[03]{reset} APICEP
│   │   ├── {azul}[04]{reset} CEP ABERTO
│   │   └── {azul}[00]{reset} VOLTAR
│   ├── [11] DDD / DDI
│   ├── [12] NOME PAI
│   ├── [13] GITHUB
│   ├── [14] INSTAGRAM
│   ├── [15] NOME MÃE
│   ├── [16] DNS
│   ├── [17] DNS
│   ├── [18] CNS
│   ├── [19] REDDIT
│   ├── [20] CEP (API)
│   ├── [21] RG
│   ├── [22] PHONE
│   ├── [23] EMAIL (API)
│   └── [00] VOLTAR
"""
menu_ip = f"""{reset}
HOME
│
├─
├── [02] OSINT
│   ├── [01] IP INFO
│   │   ├── {azul}[01]{reset} IPWHO.IS
│   │   ├── {azul}[02]{reset} IPAPI.CO
│   │   ├── {azul}[03]{reset} IPINFO.IO
│   │   ├── {azul}[04]{reset} FREEIPAPI
│   │   ├── {azul}[05]{reset} IP-API
│   │   ├── {azul}[06]{reset} IPDATA
│   │   ├── {azul}[07]{reset} ABSTRACTAPI
│   │   └── {azul}[00]{reset} VOLTAR
│   ├── [02] EMAIL (Holehe)
│   ├── [03] CPF
│   ├── [04] WHOIS
│   ├── [05] GOOGLE DORK
│   ├── [06] NOME
│   ├── [07] USERNAME
│   ├── [08] CNPJ
│   ├── [09] PHONE (API)
│   ├── [10] CEP
│   ├── [11] DDD / DDI
│   ├── [12] NOME PAI
│   ├── [13] GITHUB
│   ├── [14] INSTAGRAM
│   ├── [15] NOME MÃE
│   ├── [16] DNS
│   ├── [17] DNS
│   ├── [18] CNS
│   ├── [19] REDDIT
│   ├── [20] CEP (API)
│   ├── [21] RG
│   ├── [22] PHONE
│   ├── [23] EMAIL (API)
│   └── [00] VOLTAR
"""
menu_osint = f"""{reset}
HOME
│
├── [01] PHISHING
├── [02] OSINT
│   ├── {azul}[01]{reset} IP INFO
│   ├── {azul}[02]{reset} EMAIL (Holehe)
│   ├── {azul}[03]{reset} CPF
│   ├── {azul}[04]{reset} WHOIS
│   ├── {azul}[05]{reset} GOOGLE DORK
│   ├── {azul}[06]{reset} NOME
│   ├── {azul}[07]{reset} USERNAME
│   ├── {azul}[08]{reset} CNPJ
│   ├── {azul}[09]{reset} PHONE (API)
│   ├── {azul}[10]{reset} CEP
│   ├── {azul}[11]{reset} DDD / DDI
│   ├── {azul}[12]{reset} NOME PAI
│   ├── {azul}[13]{reset} GITHUB
│   ├── {azul}[14]{reset} INSTAGRAM
│   ├── {azul}[15]{reset} NOME MÃE
│   ├── {azul}[16]{reset} DNS
│   ├── {azul}[17]{reset} DNS
│   ├── {azul}[18]{reset} CNS
│   ├── {azul}[19]{reset} REDDIT
│   ├── {azul}[20]{reset} CEP (API)
│   ├── {azul}[21]{reset} RG
│   ├── {azul}[22]{reset} PHONE
│   ├── {azul}[23]{reset} EMAIL (API)
│   └── {azul}[00]{reset} VOLTAR
├── [03] NETWORK
├── [04] INSTALL
├── [05] MALWARES
├── [06] WEB
├── [07] XSS
├── [08] LOOKUP
├── [09] DOX
└── [00] EXIT
"""
menu_network = f"""{reset}
HOME
│
├── [01] PHISHING
├── [02] OSINT
├── [03] NETWORK
│   ├── {azul}[01]{reset} NMAP
│   ├── {azul}[02]{reset} SCAN
│   └── {azul}[00]{reset} VOLTAR
├── [04] INSTALL
├── [05] MALWARES
├── [06] WEB
├── [07] XSS
├── [08] LOOKUP
├── [09] DOX
└── [00] EXIT
"""
menu_web = f"""{reset}
HOME
│
├── [01] PHISHING
├── [02] OSINT
├── [03] NETWORK
├── [04] INSTALL
├── [05] MALWARES
├── [06] WEB
│   ├── {azul}[01]{reset} WEB RECON
│   ├── {azul}[02]{reset} SQL
│   ├── {azul}[03]{reset} XSS
│   ├── {azul}[04]{reset} DIRECTORY ENUMERATION
│   ├── {azul}[05]{reset} SUBDOMAIN ENUMERATION
│   ├── {azul}[06]{reset} SSRF
│   └── {azul}[00]{reset} VOLTAR
├── [07] XSS
├── [08] LOOKUP
├── [09] DOX
└── [00] EXIT
"""

menu_lookup = f"""{reset}
HOME
│
├── [01] PHISHING
├── [02] OSINT
├── [03] NETWORK
├── [04] INSTALL
├── [05] MALWARES
├── [06] WEB
├── [07] XSS
├── [08] LOOKUP
│   ├── {azul}[01]{reset} INSTAGRAM
│   ├── {azul}[02]{reset} XVIDEOS
│   ├── {azul}[03]{reset} INFO_PESSOA
│   ├── {azul}[04]{reset} FACEBOOK
│   ├── {azul}[05]{reset} GMAIL
│   ├── {azul}[06]{reset} REDDIT
│   ├── {azul}[07]{reset} PORNHUB
│   ├── {azul}[08]{reset} GOV
│   ├── {azul}[09]{reset} NETESCOLA
│   ├── {azul}[10]{reset} DISCORD
│   ├── {azul}[11]{reset} DS
│   ├── {azul}[12]{reset} PAINEL POLÍCIA
│   ├── {azul}[13]{reset} NETFLIX
│   ├── {azul}[14]{reset} ROBLOX
│   ├── {azul}[15]{reset} YOUTUBE
│   ├── {azul}[16]{reset} SISREG3
│   ├── {azul}[17]{reset} LINKEDIN
│   ├── {azul}[18]{reset} BRADESCO
│   ├── {azul}[19]{reset} SHESS
│   ├── {azul}[20]{reset} GITHUB
│   ├── {azul}[21]{reset} YOSEE
│   └── {azul}[00]{reset} VOLTAR
├── [09] DOX
└── [00] EXIT
"""

menu_malware = f"""{reset}
HOME
│
├── [01] PHISHING
├── [02] OSINT
├── [03] NETWORK
├── [04] INSTALL
├── [05] MALWARES
│   │
│   ├── {azul}[01]{reset} PYTHON
│   ├── {azul}[02]{reset} BASH
│   ├── {azul}[03]{reset} POWERSHELL
│   └── {azul}[00]{reset} VOLTAR
├── [06] WEB
├── [07] XSS
├── [08] LOOKUP
├── [09] DOX
└── [00] EXIT
"""
