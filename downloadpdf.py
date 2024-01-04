import requests
import shutil
import os

def baixar_e_mover_pdf(url_origem, caminho_destino):
    # Baixar o arquivo PDF da URL de origem
    resposta = requests.get(url_origem, stream=True)
    
    if resposta.status_code == 200:
        # Criar o diretório de destino se não existir
        os.makedirs(caminho_destino, exist_ok=True)

        # Caminho do arquivo temporário
        caminho_temporario = os.path.join(caminho_destino, 'arquivo_temporario2.pdf')
        
        # Salvar o conteúdo no arquivo temporário
        with open(caminho_temporario, 'wb') as arquivo_temporario:
            resposta.raw.decode_content = True
            shutil.copyfileobj(resposta.raw, arquivo_temporario)

        print(f"Arquivo PDF baixado com sucesso para {caminho_temporario}")
    else:
        print(f"Falha ao baixar o arquivo PDF da URL de origem. Status code: {resposta.status_code}")

# Exemplo de uso
url_origem_pdf = 'http://cielab.lisnet.com.br/laudos/integra/pdf/?link=282222&zso=2617912'
caminho_destino_pdf = 'C:\pufavofunciona\pdfs'

baixar_e_mover_pdf(url_origem_pdf, caminho_destino_pdf)
