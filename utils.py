def validar_lista_tarefas(response):
    """
    Valida que a resposta HTTP:
    - É uma lista (array JSON)
    - Contém pelo menos uma tarefa com a chave 'completed'
    """
    dados = response.json()

    assert isinstance(dados, list), (
        f"Esperava uma lista, mas recebeu: {type(dados).__name__}"
    )

    assert any("completed" in tarefa for tarefa in dados), (
        "Nenhuma tarefa na lista contém a chave 'completed'"
    )
