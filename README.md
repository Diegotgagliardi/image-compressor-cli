# 🗜️ Image Compressor CLI

Este é um script em Python para compressão de imagens em massa com seletor de pastas via interface gráfica. Ele reduz o tamanho dos arquivos mantendo a qualidade visual e preservando o formato original da imagem (JPEG, PNG, WebP, TIFF, etc).

Ideal para fotógrafos, designers, equipes de marketing ou qualquer pessoa que precise otimizar imagens rapidamente antes de enviar para a web ou armazenamento em nuvem.

---

## ✨ Funcionalidades

- Compressão automática de todas as imagens de uma pasta
- Mantém o formato original (JPEG, PNG, WebP, etc)
- Preserva proporções e qualidade visual
- Suporte a `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff`, `.gif`
- Interface de seleção de pasta com Tkinter
- Geração automática da pasta `comprimidas` com os arquivos otimizados

---

## ▶️ Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/image-compressor-cli.git
   cd image-compressor-cli

2. Instale o Pillow (caso ainda não tenha):
pip install pillow

3. Execute o script:
python compressor_em_massa.py

4. Uma janela será aberta para você escolher a pasta com imagens.

5. As imagens comprimidas serão salvas na subpasta comprimidas.
