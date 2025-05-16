# 🤖 git-sync-bot

**git-sync-bot** é uma ferramenta interativa que automatiza a identificação, listagem e verificação do status de repositórios Git em um diretório específico. Ideal para desenvolvedores que trabalham com múltiplos projetos locais e precisam manter o controle de versões atualizado.

---

## 🛠️ Funcionalidades

- 🔍 Escaneia recursivamente um diretório em busca de repositórios Git (`.git`)
- 📂 Salva os caminhos encontrados em um arquivo persistente (`repositories.ard`)
- ✅ Verifica o status dos repositórios e informa quais estão com alterações pendentes
- 🖱️ Interface gráfica simples via PyQt para selecionar pastas e arquivos

---
### Requisitos

- Python 3.10+
- PyQt6

### Instalação das dependências

```bash
pip install PyQt6
```