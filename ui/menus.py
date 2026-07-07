from ui.color import azul, reset 
menu_principal = f"""
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
├── [09] DOX
└── [10] EXIT
"""
menu_phishing = f"""
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
└── [10] EXIT
"""
menu_osint = f"""
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
└── [10] EXIT
"""
menu_network = f"""
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
└── [10] EXIT
"""
menu_web = f"""
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
└── [10] EXIT
"""

menu_lookup = f"""
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
└── [10] EXIT
"""

menu_malwares = """
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
└── [10] EXIT
"""
