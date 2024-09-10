from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import Unidade_Federativa
from models.endereco import Endereco
import os
os.system("clear")

pessoa1 = Pessoa(777,"breninho","13/08/2003",40028922,"breninhobranquinho@gmail.com", Sexo.MASCULINO, 
                 Endereco("Rua dos Ghosthosos",69,"Perto da rua dos capengas",410000,"Salvador",Unidade_Federativa.BAHIA))

print (pessoa1)