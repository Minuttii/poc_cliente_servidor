from servidor.handlers import processar_requisicao

def test_processar_requisicao():
    requisicao = {"action": "soma", "parameters": {"a": 5, "b": 10}}
    resposta = processar_requisicao(requisicao)
    assert resposta["status"] == "success"
    assert resposta["result"] == 15
