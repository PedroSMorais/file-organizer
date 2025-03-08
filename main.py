import os
import shutil

# Definir os tipos de arquivos e suas pastas correspondentes
FILE_TYPES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "Vídeos": [".mp4", ".mkv", ".flv", ".mov"],
    "Arquivos_Compactados": [".zip", ".rar", ".tar", ".gz"],
    "Outros": []  # Para arquivos que não se encaixam em nenhuma categoria
}

def criar_pastas(diretorio):
    """Cria as pastas para cada tipo de arquivo."""
    for pasta in FILE_TYPES:
        caminho_pasta = os.path.join(diretorio, pasta)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

def mover_arquivos(diretorio):
    """Move os arquivos para as pastas correspondentes."""
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            extensao = os.path.splitext(arquivo)[1].lower()
            movido = False
            for pasta, extensoes in FILE_TYPES.items():
                if extensao in extensoes:
                    shutil.move(caminho_arquivo, os.path.join(diretorio, pasta, arquivo))
                    movido = True
                    break
            if not movido:
                shutil.move(caminho_arquivo, os.path.join(diretorio, "Outros", arquivo))

def organizar_arquivos(diretorio):
    """Organiza os arquivos no diretório especificado."""
    criar_pastas(diretorio)
    mover_arquivos(diretorio)
    print(f"Arquivos em '{diretorio}' organizados com sucesso!")

if __name__ == "__main__":
    diretorio = input("Digite o caminho da pasta que deseja organizar: ")
    if os.path.isdir(diretorio):
        organizar_arquivos(diretorio)
    else:
        print("Caminho inválido. Por favor, insira um diretório válido.")