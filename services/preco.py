from main import Pedido

async def calcular_preco_total(pedido: Pedido, distancia: float) -> float:
    preco_por_km = 0.5
    preco_por_servico = {
        "consultoria_ambiental": 100.0,
        "instalacao_paineis_solares": 500.0,
        "reciclagem_eletronicos": 50.0,
        "aluguel_bicicletas": 20.0
    }
    preco_base = preco_por_servico.get(pedido.tipo_servico, 10.0)
    return preco_base + (distancia * preco_por_km)