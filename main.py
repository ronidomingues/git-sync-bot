import os;
import subprocess;

class VerifyRepo:
    def __get_folder(self:object) -> str:
        path = input("Digite o caminho do diretório alvo da busca: ").strip();
        if not os.path.isdir(path):
            print(f"Diretório '{path}' não encontrado!");
            return "Path not found";
        else:
            return path;
    def __find_repo(self:object) -> list:
        path = self.__get_folder();
        repo_list = [];
        if path != 'Path not found':
            for root, dirs, files in os.walk(path):
                if '.git' in dirs:
                    repo_list.append(root);
        else:
            self.main();
        return repo_list;
    def __git_sync(self:object) -> None:
        repo_list = self.__find_repo();
        for repo in repo_list:
            print(f"\n==> Verificando repositório em: {repo}");
            os.chdir(repo);
            status = subprocess.getoutput("git status");
            if 'nothing to commit' in status:
                print("Repositório já está sincronizado.");
                pass;
            else:
                print(f"Alterações encontradas:\n {status}");
                action = input("Deseja adicionar todas as alterações e comitar? [y/n | yes/no]: ");
                if action in ['y', 'Y', 'yes', 'Yes', 'YES']:
                    os.system("git add .");
                    pass;
                elif action in ['n', 'N', 'no', 'No', 'NO']:
                    manual_adding = input(f"Veja as mudanças para adicionar: \n \t {status} \n\n Digite manualemnte as mudanças que deseja adicionar separadas por um único espaço: \n\t");
                    os.system(f"git add {manual_adding}");
                    pass;
                else:
                    break;
                    pass;
                commit_message = input(f"Digite a mensagem para o commit das mudanças: \n {status} \n");
                if len(commit_message) > 0:
                    os.system(f'git commit -m "fix: {commit_message}"');
                    pass;
                else:
                    os.system('git commit -m "fix: Commit Automático"');
                    print(f"Commit feito com a mensagem padrão: 'fix: Commit Automático'");
                    pass;
                try:
                    push_result = subprocess.run("git push -u origin main", shell=True, check=True, capture_output=True, text=True);
                    print(push_result.stdout);
                    print("Push realizado com sucesso.");
                except subprocess.CalledProcessError as e:
                    print("Erro ao executar git push!");
                    print("Código de retorno:", e.returncode);
                    print("Saída padrão:", e.stdout);
                    print("Saída de erro:", e.stderr);
                pass;
            pass;
        pass;
    def main(self:object) -> None:
        self.__git_sync();
        pass;

if __name__ == "__main__":
    sync_repo = VerifyRepo();
    sync_repo.main();