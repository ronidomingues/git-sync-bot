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