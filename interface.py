import os
import sys

from PyQt6.QtWidgets import QApplication, QFileDialog


class PathSave:
    """Classe para selecionar e validar um diretório."""

    def __init__(self) -> None:
        """Inicializa o aplicativo PyQt."""
        self.app = QApplication(sys.argv)


    def get_root(self) -> str | None:
        """Abre um diálogo para selecionar um diretório.
        
        Retorna:
            str: Caminho do diretório escolhido, ou None se for inválido.
        """

        root = QFileDialog.getExistingDirectory(None, "Selecione um diretório").strip()

        if not root: # Se for vazio, o usuário cancelou
            return None
        
        if not os.path.isdir(root):
            message = f"A raiz informada <{root}> não foi encontrada!"
            border = "*" * (len(message) + 4)
            sys.stderr.write(f"\n{border}\n {message} \n{border}\n")
            return None
        
        return root
    def get_file(self) -> str:
        """Abre um diálogo para selecionar um arquivo

        Retorna:
            str: Caminho do arquivo escolhido, ou None se for inválido
        """
        filter = "Images (*.png, *.jpg, *.jpeg, *.btm, *.gif, *.webp);;Minha extensão (*.ard);;PDF (*.pdf);;Todos os arquivos (*.*)"
        file, filter_selected = QFileDialog.getOpenFileName(None, "Selecione um arquivo", "", filter)

        if not file: # Se for vazio, o usuario cancelou
            return None
        
        if not os.path.isfile(file):
            message = f"O arquivo informado <{file}> não foi encontrado!"
            border = "*" * (len(message) + 4)
            sys.stderr.write(f"\n{border}\n {message} \n{border}\n")
            return None
        return file