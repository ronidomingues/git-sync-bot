import os
import subprocess

from interface import PathSave

class FindRepositories(PathSave):
    """Classe para localizar e armazenar repositórios Git."""

    def __init__(self) -> None:
        """Inicializa a classe e define o diretório raiz."""
        super().__init__()
        self.root = self.get_dir()
    
    def _get_repositories(self) -> list[str]:
        """Obtém uma lista de diretórios contendo repositórios Git.
        Retorna:
            list[str]: Lista de caminhos de repositórios Git encontrados.
        """
        repositories = []
        for root, dirs, _ in os.walk(self.root):
            if ".git" in dirs:
                repositories.append(root)
        return repositories
    
    def _add_new_content(self, content:list[str]) -> list[str]:
        """Filtra novos repositórios que ainda não estão no arquivo.
        Args:
            content (list[str]): Conteúdo atual do arquivo.
        Retorna:
           list[str]: Lista de novos repositórios a serem adicionados.  
        """
        existing_repos = set(content)  # Transforma em set para busca mais rápida
        return [f"{repo}\n" for repo in self._get_repositories() if f"{repo}\n" not in existing_repos]
    
    def save_to_ard(self) -> None:
        """Salva os repositórios encontrados no arquivo 'repositories.ard'."""
        save_dir = "saves/"
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, "repositories.ard")
        try:
            # Inicializa o conteúdo do arquivo como lista vazia
            current_content = []

            # Ler conteúdo atual do arquivo
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file_obj:
                    current_content = file_obj.readlines()
            
            # Obter novos repositórios a serem adicionados
            new_content = self._add_new_content(current_content)

            if not new_content:  # Se não há novos repositórios, sair cedo
                print("Nenhum novo repositório encontrado.")
                return
            
            # Escrever novos repositórios no arquivo
            with open(file_path, "a", encoding="utf-8") as repo_file:
                repo_file.writelines(new_content)

            print(f"{len(new_content)} repositório(s) novo(s) salvo(s) em: {file_path}")

        except OSError as e:
            print(f"Erro ao acessar o arquivo: {e}")
        return None

class GitSync(FindRepositories):
    def __init__(self) -> None:
        super().__init__()

    def sync(self):
        repositories = self._get_repositories()
        for repo in repositories:
            print(f"\n==> Verificando repositório em: {repo}")
            os.chdir(repo)
            status = subprocess.getoutput("git status")
            if 'nothing to commit' in status:
                print(f"Repositório em {repo} já está sincronizado.")
            else:
                print(f"Alterações encontradas:\n {status}")
        pass

if __name__ == "__main__":
    obj = GitSync()
    obj.sync()