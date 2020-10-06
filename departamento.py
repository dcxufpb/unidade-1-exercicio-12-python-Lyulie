# coding: utf-8

class Coordenador:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def validar_campos_obrigatorios(self):
        if not self.nome:
            raise Exception("O nome do coordenador é obrigatório.")
        if not self.cpf:
            raise Exception("O CPF do coordenador é obrigatório.")
    
    def dados_coordenador(self):
        
        self.validar_campos_obrigatorios()

        _idade = self.idade and (f"\nIdade: {self.idade}") or ""
        _cpf = "CPF: " + self.cpf
        return \
f"""
Coordenação:
{self.nome}{_idade}
{_cpf}"""


class Departamento:

    def __init__(self, nome, sigla, localizacao, coordenador):
        self.nome = nome
        self.sigla = sigla
        self.localizacao = localizacao
        self.coordenador = coordenador

    def validar_campos_obrigatorios(self):
        if not self.nome:
            raise Exception("O nome do departamento é obrigatório.")
        if not self.localizacao:
            raise Exception("A localização do departamento é obrigatória.")

    def dados_departamento(self):
        
        self.validar_campos_obrigatorios()

        _nome = self.sigla and self.nome + ", " or self.nome
        _sigla = self.sigla and self.sigla or ""
        _localizacao = "Localização: " + self.localizacao
    
        return \
f"""{_nome}{_sigla}
{_localizacao}
{self.coordenador.dados_coordenador()}"""