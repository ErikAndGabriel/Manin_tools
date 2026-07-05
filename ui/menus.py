from ui.color import azul, reset 
menu_principal = f"""
 ___[01] PHISHING.   [02] OSINT _____
|___[03] NETWORK     [04] INSTALL ___|
|___[05] MALWARES.   [06] WEB _______|
|___[07] XSS.        [08] LORKUP ____|
|___[09] DOX.        [10] EXIT ______|
|                                    |
|____________________________________|
                  |
                  |
"""
menu_phishing = f"""
{azul}[1] {reset}ZPHISHING.  {azul}[2] {reset}FOTO
{azul}[3] {reset}INFO.       {azul}[4] {reset}NETESCOLA
{azul}[5] {reset}AUDIO.      {azul}[6] {reset}EXIT
"""

menu_osint = f"""
{azul}[01] {reset}IP INFO   {azul}[02] {reset}EMAIL(Holehe)   {azul}[03] {reset}CPF
{azul}[04] {reset}WHOIS     {azul}[05] {reset}GOOGLEDORK      {azul}[06] {reset}NOME
{azul}[07] {reset}USERNAME  {azul}[08] {reset}CNPJ            {azul}[09] {reset}PHONE(API)
{azul}[10] {reset}CEP.      {azul}[11] {reset}DDD/DDI         {azul}[12] {reset}NOME PAI
{azul}[13] {reset}GITHUB.   {azul}[14] {reset}INSTAGRAM       {azul}[15] {reset}NOME MÃE
{azul}[16] {reset}DNS       {azul}[17] {reset}DNS             {azul}[18] {reset}CNS
{azul}[19] {reset}REDDIT.   {azul}[20] {reset}CEP(API)        {azul}[21] {reset}RG
{azul}[22] {reset}PHONE     {azul}[23] {reset}EMAIL(API)      {azul}[00] {reset}EXIT
"""

network = f"""
{azul}[01] {reset}NMAP
{azul}[02] {reset}SCAN
{azul}[00] {reset}EXIT
"""

web = f"""
[1] WEB RECON [4] DIRECTORY ENUMERATION
[2] SQL.      [5] SUB DOMAIS ENUMERATION
[3] XSS.      [6] SSRF
[0] EXIT
"""
menu_lorkup = f"""
[01] INSTAGRAM [02] XVIDEOS [03] INFO_PESSOA
[04] FACEBOOK  [05] GMAIL.  [06] REDDIT
[07] PORNHUB.  [08] GOV.    [09] NETESCOLA
[10] DISCORD.  [11] DS.     [12] PAINEL POLICIA
[13] NETFLIX.  [14] ROBLOX. [15] YOUTUBE 
[16] SISREG3.  [17] LINKEDI [18] BRADESCO 
[19] SHESS.    [20] GITHUB  [21] YOSEE
               [00] EXIT"""

menu_malwares = f"""
                |
     ___________|__________
     |          |         |
[1] python [2] bash [3] powershell
     |          |         |
     |__________|_________|
                |
"""
