def processar_requisicao(requisicao: dict) -> dict:
    try:
        action = requisicao.get("action")
        parameters = requisicao.get("parameters", {})
        
        if action == "soma":
            resultado = parameters.get("a", 0) + parameters.get("b", 0)
            return {"status": "success", "result": resultado}
        else:
            return {"status": "error", "message": "Ação não suportada"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
