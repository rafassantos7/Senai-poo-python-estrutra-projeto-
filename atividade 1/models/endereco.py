from models.enums.unidade_federativa import Unidade_Federativa

class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: int, cidade: str, uf: Unidade_Federativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
    def __str__(self) -> str:
        return (
            f"Logradouro: {self.logradouro}\n"
            f"Numero: {self.numero}\n"
            f"Complemento: {self.complemento}\n"
            f"cep: {self.cep}\n"
            f"Cidade: {self.cidade}\n"
            f"Uf: {self.uf.value}"
                )