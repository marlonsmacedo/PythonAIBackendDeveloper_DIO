from workout_api.contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example='CT Vasco da Gama', max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example='Rua Gen. Almério de Moura 131, Rio de Janeiro, RJ, 20921-060', max_length=75)]
    proprietario: Annotated[str, Field(description="Nome do proprietário do centro de treinamento", example='Pedro Paulo de Oliveira', max_length=50)]