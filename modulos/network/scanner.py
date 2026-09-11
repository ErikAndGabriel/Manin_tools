import socket
import time
from config.portas import servicos

SERVICOS = servicos
class Scanner:
    def __init__(self, timeout=0.5):
        self.timeout = timeout

    def resolver(self, alvo):
        try:
            return socket.gethostbyname(alvo)
        except socket.gaierror:
            return None

    def verificar_porta(self, host, porta):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)

        inicio = time.perf_counter()

        try:
            resultado = sock.connect_ex((host, porta))
            tempo = (time.perf_counter() - inicio) * 1000

            if resultado == 0:
                return {
                    "porta": porta,
                    "estado": "open",
                    "servico": SERVICOS.get(porta, "desconhecido"),
                    "tempo_ms": round(tempo, 2)
                }

            return {
                "porta": porta,
                "estado": "closed",
                "servico": SERVICOS.get(porta, "desconhecido"),
                "tempo_ms": round(tempo, 2)
            }

        except socket.timeout:
            return {
                "porta": porta,
                "estado": "timeout",
                "servico": SERVICOS.get(porta, "desconhecido"),
                "tempo_ms": None
            }

        except OSError:
            return {
                "porta": porta,
                "estado": "error",
                "servico": SERVICOS.get(porta, "desconhecido"),
                "tempo_ms": None
            }

        finally:
            sock.close()

    def scan(self, alvo, porta_inicial=1, porta_final=1024):
        ip = self.resolver(alvo)

        if not ip:
            return {
                "alvo": alvo,
                "ip": None,
                "erro": "Não foi possível resolver o alvo.",
                "portas": []
            }

        resultados = []

        for porta in range(porta_inicial, porta_final + 1):
            resultado = self.verificar_porta(ip, porta)

            if resultado["estado"] == "open":
                resultados.append(resultado)

        return {
            "alvo": alvo,
            "ip": ip,
            "erro": None,
            "portas": resultados
          }
