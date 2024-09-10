from models.endereco import Endereco
from models.enums.sexo import Sexo

class Pessoa:
    def __init__(self, id: int, nome: str, dataNascimento: str, telefone: int, email: str, sexo: Sexo, endereco: Endereco ) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"ID: {self.id}\n"
            f"Nome: {self.nome}\n"
            f"Data de Nascimento: {self.dataNascimento}\n"
            f"Telefone: {self.telefone}\n"
            f"Email: {self.email}\n"
            f"Sexo: {self.sexo.value}\n"
            f"{self.endereco}\n")