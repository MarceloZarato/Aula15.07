from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
janela = QWidget ()
janela.setWindowTitle("minha primeira janela")
rotulo = QLabel("Olá Mundo!", parent = janela)

janela.resize (1200,900)

janela.show()

app.exec_()
