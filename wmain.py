from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QGridLayout, QFormLayout
from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit
import process

def gui():
    app = QApplication([])
    window = QWidget()
    layout = QGridLayout()

    leftLayout = QVBoxLayout()

    formLayout = QFormLayout()
    endpointBox = QLineEdit("https://<url>.openai.azure.com/openai/deployments/gpt-4o-mini")
    formLayout.addRow("Endpoint", endpointBox)
    keyBox = QLineEdit()
    formLayout.addRow("Key", keyBox)
    modelBox = QLineEdit("gpt-4o-mini")
    formLayout.addRow("Model", modelBox)
    leftLayout.addLayout(formLayout)

    leftLayout.addWidget(QLabel("Input"))
    inputBox = QPlainTextEdit()
    inputBox.setMinimumHeight(80)
    leftLayout.addWidget(inputBox)

    generateButton = QPushButton("Generate")
    leftLayout.addWidget(generateButton)
    layout.addLayout(leftLayout, 0, 0)

    arrowLabel = QLabel("->")
    layout.addWidget(arrowLabel, 0, 1)

    rightLayout = QVBoxLayout()
    rightLayout.addWidget(QLabel("Output"))
    outputBox = QPlainTextEdit()
    outputBox.setReadOnly(True)
    outputBox.setMinimumHeight(80)
    rightLayout.addWidget(outputBox)
    layout.addLayout(rightLayout, 0, 2)

    def generate():
        inputText = inputBox.toPlainText()
        endpoint = endpointBox.text()
        key = keyBox.text()
        model = modelBox.text()
        outputBox.setPlainText("Generating...")
        outputText = process.split_text(inputText, endpoint, key, model)
        outputBox.setPlainText(outputText)
    
    generateButton.clicked.connect(generate)
    window.setLayout(layout)
    window.setWindowTitle("Point Breaker")
    window.show()

    app.exec()