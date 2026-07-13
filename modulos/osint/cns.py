"""
      atenção esse módulo foi fornecido por
      @akalinpapo
      ass: erik
      
"""

import hashlib
import re
import random
import warnings
import tempfile
import os
from datetime import datetime
import requests
from colorama import init, Fore, Style

try:
    init(autoreset=True)
except:
    pass

warnings.filterwarnings('ignore')

class SisregConsulta:
    
    def __init__(self, documento):
        self.credenciais = [
            {'user': 'henrique.nevessol', 'senha': hashlib.sha256('Medicina2'.upper().encode()).hexdigest()},
            {'user': 'alberto_gomes', 'senha': hashlib.sha256('agb251090'.upper().encode()).hexdigest()},
        ]
        self.session = requests.Session()
        self.session.verify = False
        self._logado = False
        self.documento = re.sub(r'\D', '', str(documento))
        self.dados = None
        self.cookie_file = None
        self._consultar()
    
    def _clean(self, text):
        if not text:
            return ''
        return ' '.join(re.sub(r'\s+', ' ', text).strip().split())

    def _extract_table(self, html, label):
        start = html.find(label)
        if start == -1:
            return None
        table_start = html.lower().find('<table', start)
        if table_start == -1:
            return None
        table_end = html.lower().find('</table>', table_start)
        if table_end == -1:
            return None
        table_end += len('</table>')
        return html[table_start:table_end]

    def _login(self):
        if self._logado:
            return True
            
        self.cookie_file = tempfile.NamedTemporaryFile(delete=False, prefix='sisreg_')
        self.cookie_file.close()
        
        url = "https://sisregiii.saude.gov.br/"
        
        for tentativa in range(30):
            cred = random.choice(self.credenciais)
            usuario = cred['user']
            senha = cred['senha']
            
            post = {
                'usuario': usuario,
                'senha': '',
                'senha_256': senha,
                'etapa': 'ACESSO',
                'logout': ''
            }
            
            headers = {
                'Host': 'sisregiii.saude.gov.br',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Origin': 'https://sisregiii.saude.gov.br',
                'Sec-GPC': '1',
                'Connection': 'keep-alive',
                'Referer': 'https://sisregiii.saude.gov.br/',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Priority': 'u=0, i'
            }
            
            try:
                response = self.session.post(url, data=post, headers=headers, timeout=30)
                
                if self.cookie_file:
                    with open(self.cookie_file.name, 'w') as f:
                        for cookie in self.session.cookies:
                            f.write(f"{cookie.domain}\tTRUE\t{cookie.path}\t{cookie.secure}\t{cookie.expires}\t{cookie.name}\t{cookie.value}\n")
                
                if '<p>Sair</p>' in response.text:
                    self._logado = True
                    return True
            except Exception as e:
                continue
                
        return False

    def _consultar(self):
        if len(self.documento) != 15:
            self.dados = {'error': 'input invalido'}
            return

        if not self._login():
            self.dados = {'error': True, 'message': 'error na credencial'}
            
        url = 'https://sisregiii.saude.gov.br/cgi-bin/cadweb50?standalone=1'
        post = {
            'nu_cns': self.documento,
            'nome_paciente': '',
            'nome_mae': '',
            'dt_nascimento': '',
            'uf_nasc': '',
            'mun_nasc': '',
            'uf_res': '',
            'mun_res': '',
            'sexo': '',
            'etapa': 'DETALHAR',
            'url': '',
            'standalone': '1'
        }
        
        headers = {
            'Host': 'sisregiii.saude.gov.br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Origin': 'https://sisregiii.saude.gov.br',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://sisregiii.saude.gov.br/cgi-bin/cadweb50?standalone=1',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=4'
        }
        
        try:
            if self.cookie_file and os.path.exists(self.cookie_file.name):
                with open(self.cookie_file.name, 'r') as f:
                    for line in f:
                        parts = line.strip().split('\t')
                        if len(parts) >= 7:
                            self.session.cookies.set(parts[5], parts[6])
            
            response = self.session.post(url, data=post, headers=headers, timeout=30)
            html = response.text
            
            import html as html_parser
            html = html_parser.unescape(html)
            
            if 'Dados Pessoais:' not in html:
                self.dados = {'error': True, 'message': 'não foi encontrado ninguem com esse CNS'}
                return
                
            self.dados = self._parse_dados(html)
            self._mostrar_formatado()
            
        except Exception as e:
            self.dados = {'error': True, 'message': f'Erro na consulta: {str(e)}'}
        finally:
            if self.cookie_file and os.path.exists(self.cookie_file.name):
                try:
                    os.unlink(self.cookie_file.name)
                except:
                    pass

    def _parse_dados(self, html):
        fields = {}
        
        pattern = re.compile(
            r'<tr[^>]*>\s*<td[^>]*>\s*<b>\s*([^<:]+):\s*</b>\s*</td>\s*<td[^>]*>\s*<b>\s*([^<:]+):\s*</b>\s*</td>\s*</tr>\s*'
            r'<tr[^>]*>\s*<td[^>]*>\s*([^<]*?)\s*</td>\s*<td[^>]*>\s*([^<]*?)\s*</td>\s*</tr>',
            re.IGNORECASE | re.DOTALL
        )
        
        matches = pattern.findall(html)
        for m in matches:
            fields[self._clean(m[0])] = self._clean(m[2])
            fields[self._clean(m[1])] = self._clean(m[3])
        
        data = {}
        data['nome'] = fields.get('Nome', '')
        data['cpf'] = self._extrair_cpf(html)
        data['cns'] = self._extrair_cns(html)
        data['nome_mae'] = fields.get('Nome da Mãe', '')
        data['nome_pai'] = fields.get('Nome do Pai', '')
        data['sexo'] = fields.get('Sexo', '')
        data['raca'] = fields.get('Raça', '')
        data['nacionalidade'] = fields.get('Nacionalidade', '')
        data['municipio_nascimento'] = fields.get('Município de Nascimento', '')
        data['tipo_logradouro'] = fields.get('Tipo Logradouro', '')
        data['data_nascimento'] = fields.get('Data de Nascimento', '')
        data['logradouro'] = fields.get('Logradouro', '')
        data['complemento'] = fields.get('Complemento', '')
        data['numero'] = fields.get('Número', '')
        data['bairro'] = fields.get('Bairro', '')
        data['cep'] = fields.get('CEP', '')
        data['pais_residencia'] = fields.get('País de Residência', '')
        data['municipio_residencia'] = fields.get('Município de Residência', '')
        
        documentos = self._extrair_documentos(html)
        obito = self._extrair_obito(html)
        contatos = self._extrair_contatos(html)
        
        return {
            'base': data,
            'obito': obito,
            'contatos': contatos,
            'documentos': documentos
        }

    def _extrair_cpf(self, html):
        match = re.search(r'\b(\d{3}\.?\d{3}\.?\d{3}-?\d{2})\b', html)
        return self._clean(match.group(1) if match else '')

    def _extrair_cns(self, html):
        match = re.search(
            r'CNS:\s*</b>\s*</td>\s*</tr>\s*<tr[^>]*>\s*<td[^>]*>\s*<font[^>]*>\s*<B>\s*([^<]*?)\s*</B>\s*</font>',
            html, re.IGNORECASE
        )
        return self._clean(match.group(1) if match else '')

    def _extrair_documentos(self, html):
        documentos = {}
        
        if 'Num. RG' in html:
            pattern = re.compile(
                r'<TR>\s*'
                r'<TD[^>]*>\s*([^<]+?)\s*</TD>\s*'
                r'<TD[^>]*>\s*([^<]+?)\s*</TD>\s*'
                r'<TD[^>]*>\s*([^<]+?)\s*</TD>\s*'
                r'<TD[^>]*>\s*([^<]+?)\s*</TD>\s*'
                r'</TR>\s*<TR>\s*'
                r'<TD[^>]*>\s*([^<]*?)\s*</TD>\s*'
                r'<TD[^>]*>\s*([^<]*?)\s*</TD>\s*'
                r'<TD[^>]*>\s*([^<]*?)\s*</TD>\s*'
                r'<TD[^>]*>\s*([^<]*?)\s*</TD>\s*'
                r'</TR>',
                re.IGNORECASE
            )
            m = pattern.search(html)
            if m:
                rg = {
                    self._clean(m.group(1)): self._clean(m.group(5)),
                    self._clean(m.group(2)): self._clean(m.group(6)),
                    self._clean(m.group(3)): self._clean(m.group(7)),
                    self._clean(m.group(4)): self._clean(m.group(8))
                }
                documentos['rg'] = rg

        if 'Certidão de Nascimento' in html:
            pattern = re.compile(
                r'<tr>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'</tr>\s*<tr>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'<td[^>]*>\s*([^<]*?)\s*</td>\s*'
                r'</tr>',
                re.IGNORECASE
            )
            m = pattern.search(html)
            if m:
                cartorio = {
                    self._clean(m.group(1)): self._clean(m.group(6)),
                    self._clean(m.group(2)): self._clean(m.group(7)),
                    self._clean(m.group(3)): self._clean(m.group(8)),
                    self._clean(m.group(4)): self._clean(m.group(9)),
                    self._clean(m.group(5)): self._clean(m.group(10))
                }
                documentos['certidao_nascimento'] = cartorio

        return documentos if documentos else 'sem documentos'

    def _extrair_obito(self, html):
        obito = None
        
        start = html.find('Detalhes do Óbito:')
        if start != -1:
            next_section = html.find('td_titulo_tabela', start + len('Detalhes do Óbito:'))
            html_obito = html[start:next_section] if next_section != -1 else html[start:]
            
            obito = {'tem_obito': True}
            
            pattern = re.compile(
                r'<tr[^>]*>\s*<td[^>]*>\s*<b>\s*([^<:]+):\s*</b>\s*</td>\s*<td[^>]*>\s*<b>\s*([^<:]+):\s*</b>\s*</td>\s*</tr>\s*'
                r'<tr[^>]*>\s*<td[^>]*>\s*([^<]*?)\s*</td>\s*<td[^>]*>\s*([^<]*?)\s*</td>\s*</tr>',
                re.IGNORECASE
            )
            
            matches = pattern.findall(html_obito)
            for m in matches:
                obito[self._clean(m[0])] = self._clean(m[2])
                obito[self._clean(m[1])] = self._clean(m[3])
            
            motivo_match = re.search(
                r'<td[^>]*>\s*<b>\s*Motivo:\s*</b>\s*</td>\s*</tr>\s*<tr[^>]*>\s*<td[^>]*>\s*([^<]*?)\s*</td>',
                html_obito, re.IGNORECASE
            )
            if motivo_match:
                obito['Motivo'] = self._clean(motivo_match.group(1))
        
        if obito is None:
            obito = {'tem_obito': False}
        
        return obito

    def _extrair_contatos(self, html):
        emails = None
        telefones = None
        
        html_emails = self._extract_table(html, 'E-mail(s):')
        if html_emails is not None:
            pattern = re.compile(
                r'<TR[^>]*>\s*'
                r'<TD\s+align=\'center\'>\s*([^<]*?)\s*</TD>\s*'
                r'<TD\s+align=\'center\'>\s*([^<]*?)\s*</TD>\s*'
                r'<TD\s+align=\'center\'>\s*(?:<FONT[^>]*>)?\s*([^<]*?)\s*(?:</FONT>)?\s*</TD>\s*'
                r'</TR>',
                re.IGNORECASE
            )
            matches = pattern.findall(html_emails)
            if matches:
                emails = []
                for m in matches:
                    emails.append({
                        'tipo': self._clean(m[0]),
                        'email': self._clean(m[1]),
                        'validado': self._clean(m[2]) if len(m) > 2 else 'N/A'
                    })
        
        html_telefones = self._extract_table(html, 'Telefone(s):')
        if html_telefones is not None:
            pattern = re.compile(
                r'<TR[^>]*>\s*'
                r'<TD\s+align=\'center\'>\s*([^<]*?)\s*</TD>\s*'
                r'<TD\s+align=\'center\'>\s*([^<]*?)\s*</TD>\s*'
                r'<TD\s+align=\'center\'>\s*([^<]*?)\s*</TD>\s*'
                r'</TR>',
                re.IGNORECASE
            )
            matches = pattern.findall(html_telefones)
            if matches:
                telefones = []
                for m in matches:
                    telefones.append({
                        'tipo': self._clean(m[0]),
                        'ddd': self._clean(re.sub(r'[()]', '', m[1])),
                        'numero': self._clean(m[2])
                    })
        
        return {
            'emails': emails if emails is not None else 'sem email',
            'telefones': telefones if telefones is not None else 'sem telefone'
        }

    def _mostrar_formatado(self):
        if not self.dados or 'error' in self.dados:
            print(f"{Fore.RED}ERRO: {self.dados.get('message', 'Erro desconhecido')}")
            return
        
        dados = self.dados
        base = dados.get('base', {})
        obito = dados.get('obito', {'tem_obito': False})
        contatos = dados.get('contatos', {'emails': 'sem email', 'telefones': 'sem telefone'})
        documentos = dados.get('documentos', 'sem documentos')
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.WHITE}SISTEMA DE REGULAÇÃO - SISREG")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        print(f"{Fore.WHITE}DADOS PESSOAIS")
        print(f"{Fore.CYAN}{'-'*40}")
        
        campos_base = [
            ('NOME', base.get('nome', '')),
            ('CPF', base.get('cpf', '')),
            ('CNS', base.get('cns', '')),
            ('DATA NASCIMENTO', base.get('data_nascimento', '')),
            ('SEXO', base.get('sexo', '')),
            ('RACA', base.get('raca', '')),
            ('NACIONALIDADE', base.get('nacionalidade', '')),
            ('MUNICIPIO NASCIMENTO', base.get('municipio_nascimento', '')),
            ('NOME DA MAE', base.get('nome_mae', '')),
            ('NOME DO PAI', base.get('nome_pai', '')),
        ]
        
        for label, valor in campos_base:
            display = valor if valor else 'N/A'
            print(f"{Fore.WHITE}{label:22} : {Fore.CYAN}{display}")
        
        print(f"\n{Fore.WHITE}ENDERECO")
        print(f"{Fore.CYAN}{'-'*40}")
        
        campos_endereco = [
            ('TIPO LOGRADOURO', base.get('tipo_logradouro', '')),
            ('LOGRADOURO', base.get('logradouro', '')),
            ('NUMERO', base.get('numero', '')),
            ('COMPLEMENTO', base.get('complemento', '')),
            ('BAIRRO', base.get('bairro', '')),
            ('CEP', base.get('cep', '')),
            ('MUNICIPIO RESIDENCIA', base.get('municipio_residencia', '')),
            ('PAIS RESIDENCIA', base.get('pais_residencia', '')),
        ]
        
        for label, valor in campos_endereco:
            display = valor if valor else 'N/A'
            print(f"{Fore.WHITE}{label:22} : {Fore.CYAN}{display}")
        
        emails = contatos.get('emails', 'sem email')
        if emails != 'sem email' and emails:
            print(f"\n{Fore.WHITE}EMAILS")
            print(f"{Fore.CYAN}{'-'*40}")
            for email in emails:
                print(f"{Fore.WHITE}TIPO{' '*19} : {Fore.CYAN}{email.get('tipo', 'N/A')}")
                print(f"{Fore.WHITE}EMAIL{' '*18} : {Fore.CYAN}{email.get('email', 'N/A')}")
                print(f"{Fore.WHITE}VALIDADO{' '*15} : {Fore.CYAN}{email.get('validado', 'N/A')}")
        else:
            print(f"\n{Fore.WHITE}EMAILS")
            print(f"{Fore.CYAN}{'-'*40}")
            print(f"{Fore.WHITE}SITUACAO{' '*15} : {Fore.CYAN}SEM EMAILS CADASTRADOS")
        
        telefones = contatos.get('telefones', 'sem telefone')
        if telefones != 'sem telefone' and telefones:
            print(f"\n{Fore.WHITE}TELEFONES")
            print(f"{Fore.CYAN}{'-'*40}")
            for tel in telefones:
                print(f"{Fore.WHITE}TIPO{' '*19} : {Fore.CYAN}{tel.get('tipo', 'N/A')}")
                print(f"{Fore.WHITE}DDD{' '*20} : {Fore.CYAN}{tel.get('ddd', 'N/A')}")
                print(f"{Fore.WHITE}NUMERO{' '*17} : {Fore.CYAN}{tel.get('numero', 'N/A')}")
        else:
            print(f"\n{Fore.WHITE}TELEFONES")
            print(f"{Fore.CYAN}{'-'*40}")
            print(f"{Fore.WHITE}SITUACAO{' '*15} : {Fore.CYAN}SEM TELEFONES CADASTRADOS")
        
        if documentos != 'sem documentos':
            print(f"\n{Fore.WHITE}DOCUMENTOS")
            print(f"{Fore.CYAN}{'-'*40}")
            
            if 'rg' in documentos:
                print(f"{Fore.WHITE}RG")
                for key, value in documentos['rg'].items():
                    display = value if value else 'N/A'
                    print(f"{Fore.WHITE}{key:22} : {Fore.CYAN}{display}")
                print(f"{Fore.CYAN}{'-'*40}")
            
            if 'certidao_nascimento' in documentos:
                print(f"{Fore.WHITE}CERTIDAO DE NASCIMENTO")
                for key, value in documentos['certidao_nascimento'].items():
                    display = value if value else 'N/A'
                    print(f"{Fore.WHITE}{key:22} : {Fore.CYAN}{display}")
                print(f"{Fore.CYAN}{'-'*40}")
        else:
            print(f"\n{Fore.WHITE}DOCUMENTOS")
            print(f"{Fore.CYAN}{'-'*40}")
            print(f"{Fore.WHITE}SITUACAO{' '*15} : {Fore.CYAN}SEM DOCUMENTOS CADASTRADOS")
        
        print(f"\n{Fore.WHITE}OBITO")
        print(f"{Fore.CYAN}{'-'*40}")
        
        if obito.get('tem_obito', False):
            print(f"{Fore.WHITE}SITUACAO{' '*15} : {Fore.RED}REGISTRO DE OBITO ENCONTRADO")
            for key, value in obito.items():
                if key != 'tem_obito' and value:
                    print(f"{Fore.WHITE}{key.upper():22} : {Fore.CYAN}{value}")
        else:
            print(f"{Fore.WHITE}SITUACAO{' '*15} : {Fore.GREEN}SEM REGISTRO DE OBITO")
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.WHITE}CONSULTA REALIZADA EM: {Fore.CYAN}{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"{Fore.CYAN}{'='*60}\n")

    def __str__(self):
        if not self.dados or 'error' in self.dados:
            return f"ERRO: {self.dados.get('message', 'Erro desconhecido')}"
        base = self.dados.get('base', {})
        nome = base.get('nome', 'N/A')
        cns = base.get('cns', 'N/A')
        return f"{nome} | CNS: {cns}"

    def get_dados(self):
        return self.dados
