from pydantic import BaseModel
from typing import Optional

class Pedido(BaseModel):
    cliente_id: int
    servico_id: int
    cep_cliente: str
    cep_prestador: str
    tipo_servico: str
    valor_base: float
    moeda: str = "BRL"