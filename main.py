from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.pedido import Pedido
from services.geolocalizacao import calcular_distancia
from services.pagamento import processar_pagamento
from services.preco import calcular_preco_total

app = FastAPI()

# Modelo para o cálculo de frete
class FreteInput(BaseModel):
    cep_cliente: str
    cep_prestador: str

# Simulação de banco de dados
pedidos = []

@app.post("/pedidos/")
async def criar_pedido(pedido: Pedido):
    # Calcula distância e preço total
    distancia = await calcular_distancia(pedido.cep_cliente, pedido.cep_prestador)
    pedido.valor_base = await calcular_preco_total(pedido, distancia)
    
    # Processa pagamento
    pagamento = await processar_pagamento(pedido)
    
    # Adiciona pedido com número de rastreamento
    pedido_id = len(pedidos)
    pedidos.append(pedido)
    return {"pedido": pedido, "numero_rastreamento": f"TRK{pedido_id:06d}", "pagamento": pagamento}

@app.get("/pedidos/{pedido_id}")
async def obter_pedido(pedido_id: int):
    if pedido_id >= len(pedidos):
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedidos[pedido_id]

@app.post("/calcular-frete/")
async def calcular_frete(frete_input: FreteInput):
    distancia = await calcular_distancia(frete_input.cep_cliente, frete_input.cep_prestador)
    frete = distancia * 0.5  # R$0,50 por km
    return {"frete": frete, "distancia_km": distancia}