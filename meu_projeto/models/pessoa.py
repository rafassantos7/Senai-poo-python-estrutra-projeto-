from models.endereco import Endereco
from models.enums.sexo import Sexo

class Pessoa:
    def __init__(self,nome: str, idade: int, sexo: Sexo, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSexo : {self.sexo.value}\nEndereco:\n{self.endereco}"
