from pydantic import Field, PositiveFloat
from typing import Annotated
from workout_api.contrib.schemas import BaseSchema
class AteltaBase(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Atleta", example='João', max_length=50)]
    cpf: Annotated[str, Field(description="CPF do Atleta", example='1234567890', max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", example=75.5)]
    altura: Annotated[PositiveFloat, Field(description="Peso do Atleta", example=1.70)]
    sexo: Annotated[str, Field(description="Sexo do Atleta", example='M', max_length=1)]