
# 🖼️ Automação AWS - Redução de Imagens no S3

Este script Python usa `boto3` e `Pillow` para:

1. Baixar uma imagem de um bucket S3
2. Redimensionar a imagem (ex: largura para 300px)
3. Salvar novamente no S3

---

## ⚙️ Requisitos

- `boto3` (AWS SDK para Python)
- `pillow` (manipulação de imagens)
- Credenciais AWS válidas com acesso ao S3
```bash
pip install boto3 pillow
```

---

## 🚀 Uso

```python
processar_imagem_s3("meu-bucket", "imagens/original.jpg", "imagens/redimensionado.jpg")
```

**Nota:** O exemplo acima é comentado por segurança. Só execute com credenciais válidas e buckets reais.

---

Este exemplo mostra como automatizar tarefas com imagens em nuvem usando Python.
