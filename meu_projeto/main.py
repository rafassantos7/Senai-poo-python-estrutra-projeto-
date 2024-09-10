import os
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco

os.system("clear")

pessoa1 = Pessoa("rafael",23,Sexo.MASCULINO, Endereco("Rua dos TIs", 13))

print(pessoa1)