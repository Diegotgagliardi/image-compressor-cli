import os
from PIL import Image
from tkinter import Tk, filedialog

def comprimir_imagem(caminho_entrada, caminho_saida, qualidade=75, max_largura=1920, max_altura=1080):
    try:
        imagem = Image.open(caminho_entrada)
        imagem_exif = imagem.info.get('exif')
        formato_original = imagem.format

        imagem.thumbnail((max_largura, max_altura))

        if imagem.mode in ("RGBA", "P"):
            imagem = imagem.convert("RGB")

        parametros = {
            'format': formato_original,
            'quality': qualidade,
            'optimize': True
        }

        if imagem_exif and formato_original.upper() == "JPEG":
            parametros['exif'] = imagem_exif

        imagem.save(caminho_saida, **parametros)

        tamanho_original = os.path.getsize(caminho_entrada) / 1024
        tamanho_novo = os.path.getsize(caminho_saida) / 1024

        print(f"[✔] {os.path.basename(caminho_entrada)}")
        print(f"   Original: {tamanho_original:.2f} KB -> Comprimida: {tamanho_novo:.2f} KB\n")

    except Exception as e:
        print(f"[X] Erro em '{caminho_entrada}': {e}")


def selecionar_pasta():
    root = Tk()
    root.withdraw()  # Oculta a janela principal
    pasta = filedialog.askdirectory(title="Selecione a pasta com as imagens")
    return pasta


def comprimir_em_lote(pasta_entrada, qualidade=75):
    if not pasta_entrada:
        print("Nenhuma pasta foi selecionada.")
        return

    pasta_saida = os.path.join(pasta_entrada, "comprimidas")
    os.makedirs(pasta_saida, exist_ok=True)

    print(f"\n📁 Pasta selecionada: {pasta_entrada}")

    arquivos = os.listdir(pasta_entrada)
    print(f"📝 Arquivos encontrados: {arquivos}")

    formatos_suportados = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".tif", ".gif")

    for arquivo in arquivos:
        if arquivo.lower().endswith(formatos_suportados):
            print(f"➡️ Processando: {arquivo}")
            caminho_entrada = os.path.join(pasta_entrada, arquivo)
            caminho_saida = os.path.join(pasta_saida, arquivo)
            comprimir_imagem(caminho_entrada, caminho_saida, qualidade)


# === Executa o script ===
if __name__ == "__main__":
    pasta_escolhida = selecionar_pasta()
    qualidade = 75  # entre 60 e 85 para equilibrar qualidade x tamanho

    comprimir_em_lote(pasta_escolhida, qualidade)