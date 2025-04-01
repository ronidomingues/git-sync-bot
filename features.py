import os
import subprocess
import datetime

class FindRepositories:
    def __init__(self:object) -> None:
        self.root = self.__get_root()
        self.repositories = self.__get_repositories()
        print(self.root, self.repositories, sep="\n")
        pass
    def __get_root(self:object) -> str:
        root = input("Digite o caminho do diretório alvo da busca por repositórios: ").strip()
        if not os.path.isdir(root):
            message = f"A raíz informada <{root}> não foi encontrada!"
            border = "*"*(len(message) + 20)
            print(f"{border}\n{message.center(len(border))}\n{border}")
            self.__init__()
        else:
            return root
    def __get_repositories(self:object) -> list[str]:
        repositories = []
        for root, dirs, files in os.walk(self.root):
            if ".git" in dirs:
                repositories.append(root)
        return repositories
    def __add_new_content(self:object, content:list[str]) -> list[str]:
        new_content = []
        for path in self.repositories:
            if path not in content:
                path = path+"\n"
                new_content.append(path)
        return new_content
    def save_listed_repositories(self:object) -> None:
        path = "saves/"
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            message = f"O diretório <{path}> já existe!"
            border = "*"*(len(message) + 20)
            print(f"{border}\n{message.center(len(border))}\n{border}")
        file = path + "repositories.ard"
        with open(file, "a+") as repositories:
            repositories.seek(0) #Voltando o cursor para o inicio do arquivo para que ele leia o arquivo inteiro
            current_content = repositories.readlines()
            # Vai para o final do arquivo para adicionar novo conteúdo
            repositories.seek(0, 2)  # Move o cursor para o final do arquivo
            new_content = self.__add_new_content(current_content)
            for content in new_content:
                repositories.write(content) # Adicionando o novo conteúdo ao final do arquivo


obj = FindRepositories()
obj.save_listed_repositories()