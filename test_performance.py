import asyncio
import time
import pytest
import httpx
import pytest_asyncio

from api_pagamentos import app


# Marca todos os testes do arquivo como assíncronos
pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize("num_requisicoes", [5, 20, 50])
async def test_pagamentos_simultaneos(num_requisicoes: int):
    """
    Testa o endpoint /processar disparando múltiplas requisições
    simultâneas via asyncio.gather e valida:
      - Todos os status code são 200
      - O tempo total é menor que 3.5 segundos (mesmo com 50 req.)
    """
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:

        async def fazer_requisicao():
            return await client.get("/processar")

        inicio = time.perf_counter()

        respostas = await asyncio.gather(
            *[fazer_requisicao() for _ in range(num_requisicoes)]
        )

        duracao = time.perf_counter() - inicio

    # Valida que todas as respostas têm status 200
    status_codes = [r.status_code for r in respostas]
    assert all(sc == 200 for sc in status_codes), (
        f"Respostas com erro encontradas: {status_codes}"
    )

    # Valida que o tempo total foi menor que 3.5 segundos
    assert duracao < 3.5, (
        f"Tempo total ({duracao:.2f}s) excedeu o limite de 3.5s "
        f"para {num_requisicoes} requisições simultâneas"
    )

    print(
        f"\n✅ {num_requisicoes} requisições simultâneas concluídas "
        f"em {duracao:.2f}s"
    )
