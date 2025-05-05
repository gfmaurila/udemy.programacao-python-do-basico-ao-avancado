
# Script: Reduzindo o tamanho de imagens no AWS S3 (simulado)
# Requer: boto3, pillow

import boto3
from PIL import Image
import io

def redimensionar_imagem(imagem_bytes, nova_largura=300):
    imagem = Image.open(io.BytesIO(imagem_bytes))
    proporcao = nova_largura / float(imagem.size[0])
    nova_altura = int((float(imagem.size[1]) * float(proporcao)))
    imagem_redimensionada = imagem.resize((nova_largura, nova_altura))
    
    buffer = io.BytesIO()
    imagem_redimensionada.save(buffer, format='JPEG')
    buffer.seek(0)
    return buffer

def processar_imagem_s3(bucket, chave_origem, chave_destino):
    s3 = boto3.client('s3')
    print("Baixando imagem de:", chave_origem)

    obj = s3.get_object(Bucket=bucket, Key=chave_origem)
    imagem_bytes = obj['Body'].read()

    imagem_red = redimensionar_imagem(imagem_bytes)

    print("Enviando imagem redimensionada para:", chave_destino)
    s3.put_object(Bucket=bucket, Key=chave_destino, Body=imagem_red, ContentType='image/jpeg')
    print("Processo concluído.")

# Simulação:
# processar_imagem_s3("meu-bucket", "imagens/original.jpg", "imagens/redimensionado.jpg")
