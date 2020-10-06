
import pytest

from departamento import Departamento, Coordenador

def verifica_campo_obrigatorio_objeto(mensagem_esperada, departamento):
    with pytest.raises(Exception) as excinfo:
        departamento.dados_departamento()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO = \
"""Departamento 1, Sigla 1
Localização: 11.1111111, 11.1111111

Coordenação:
Coordenador 1
Idade: 11
CPF: 111.111.111-11"""

TEXTO_ESPERADO_SEM_SIGLA = \
"""Departamento 1
Localização: 11.1111111, 11.1111111

Coordenação:
Coordenador 1
Idade: 11
CPF: 111.111.111-11"""

TEXTO_ESPERADO_SEM_IDADE = \
"""Departamento 1, Sigla 1
Localização: 11.1111111, 11.1111111

Coordenação:
Coordenador 1
CPF: 111.111.111-11"""

TEXTO_ESPERADO_SEM_SIGLA_SEM_IDADE = \
"""Departamento 1
Localização: 11.1111111, 11.1111111

Coordenação:
Coordenador 1
CPF: 111.111.111-11"""

NOME_DEPARTAMENTO = "Departamento 1"
SIGLA = "Sigla 1"
LOCALIZACAO = "11.1111111, 11.1111111"
NOME_COORDENADOR = "Coordenador 1"
IDADE = 11
CPF = "111.111.111-11"

## Aplicaçóes para classe Coordenador

coordenador_completo = Coordenador(
    NOME_COORDENADOR,
    IDADE,
    CPF
)
#
coordenador_nome_nulo = Coordenador(
    None,
    IDADE,
    CPF
)
#
coordenador_nome_vazio = Coordenador(
    "",
    IDADE,
    CPF
)
#
coordenador_cpf_nulo = Coordenador(
    NOME_COORDENADOR,
    IDADE,
    None
)
#
coordenador_cpf_vazio = Coordenador(
    NOME_COORDENADOR,
    IDADE,
    ""
)
#
coordenador_idade_nula = Coordenador(
    NOME_COORDENADOR,
    None,
    CPF
)
#
coordenador_idade_vazia = Coordenador(
    NOME_COORDENADOR,
    "",
    CPF
)

##

DEPARTAMENTO_COMPLETO = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    LOCALIZACAO,
    coordenador_completo
)

## Campos Opcionais
## @Coordenador idade
## @Departamento sigla

SIGLA_NULA = Departamento(
    NOME_DEPARTAMENTO,
    None,
    LOCALIZACAO,
    coordenador_completo
)

SIGLA_VAZIA = Departamento(
    NOME_DEPARTAMENTO,
    "",
    LOCALIZACAO,
    coordenador_completo
)

##

IDADE_NULA = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    LOCALIZACAO,
    coordenador_idade_nula
)

IDADE_VAZIA = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    LOCALIZACAO,
    coordenador_idade_vazia
)

##

SIGLA_E_IDADE_VAZIAS = Departamento(
    NOME_DEPARTAMENTO,
    None,
    LOCALIZACAO,
    coordenador_idade_vazia
)

## Campos Obrigatórios
## @Coordenador nome, cpf
## @Departamento nome, localizacao

MENSAGEM_NOME_DEPARTAMENTO_OBRIGATORIO = "O nome do departamento é obrigatório."

MENSAGEM_LOCALIZACAO_OBRIGATORIA = "A localização do departamento é obrigatória."

MENSAGEM_NOME_COORDENADOR_OBRIGATORIO = "O nome do coordenador é obrigatório."

MENSAGEM_CPF_OBRIGATORIO = "O CPF do coordenador é obrigatório."

##

NOME_DEPARTAMENTO_NULO = Departamento(
    None,
    SIGLA,
    LOCALIZACAO,
    coordenador_completo
)

NOME_DEPARTAMENTO_VAZIO = Departamento(
    "",
    SIGLA,
    LOCALIZACAO,
    coordenador_completo
)

##

LOCALIZACAO_NULA = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    None,
    coordenador_completo
)

LOCALIZACAO_VAZIA = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    "",
    coordenador_completo
)

##

NOME_COORDENADOR_NULO = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    LOCALIZACAO,
    coordenador_nome_nulo
)

NOME_COORDENADOR_VAZIO = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    LOCALIZACAO,
    coordenador_nome_vazio
)

##

CPF_NULO = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    LOCALIZACAO,
    coordenador_cpf_nulo
)

CPF_VAZIO = Departamento(
    NOME_DEPARTAMENTO,
    SIGLA,
    LOCALIZACAO,
    coordenador_cpf_vazio
)

## @Testes

def test_departamento_completo():
    assert (DEPARTAMENTO_COMPLETO.dados_departamento() == TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO)

##

def test_sigla_nula():
    assert (SIGLA_NULA.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA)

def test_sigla_vazia():
    assert (SIGLA_VAZIA.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA)

##

def test_idade_nula():
    assert (IDADE_NULA.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE)

def test_idade_vazia():
    assert (IDADE_VAZIA.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE)

##

def test_sigla_e_idade_vazias():
    assert (SIGLA_E_IDADE_VAZIAS.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA_SEM_IDADE)

##

def test_valida_nome_departamento():
    verifica_campo_obrigatorio_objeto(
        MENSAGEM_NOME_DEPARTAMENTO_OBRIGATORIO, 
        NOME_DEPARTAMENTO_NULO
    )
    verifica_campo_obrigatorio_objeto(
        MENSAGEM_NOME_DEPARTAMENTO_OBRIGATORIO, 
        NOME_DEPARTAMENTO_VAZIO
    )

##
    
def test_valida_localizacao():
    verifica_campo_obrigatorio_objeto(
        MENSAGEM_LOCALIZACAO_OBRIGATORIA, 
        LOCALIZACAO_NULA
    )
    verifica_campo_obrigatorio_objeto(
        MENSAGEM_LOCALIZACAO_OBRIGATORIA, 
        LOCALIZACAO_VAZIA
    )

##

def test_valida_nome_coordenador():
    verifica_campo_obrigatorio_objeto(
        MENSAGEM_NOME_COORDENADOR_OBRIGATORIO, 
        NOME_COORDENADOR_NULO
    )
    verifica_campo_obrigatorio_objeto(
        MENSAGEM_NOME_COORDENADOR_OBRIGATORIO, 
        NOME_COORDENADOR_VAZIO
    )

##

def test_valida_cpf():
    verifica_campo_obrigatorio_objeto(
        MENSAGEM_CPF_OBRIGATORIO, 
        CPF_NULO
    )
    verifica_campo_obrigatorio_objeto(
        MENSAGEM_CPF_OBRIGATORIO, 
        CPF_VAZIO
    )