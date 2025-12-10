import runpod

# Dieser Handler wird bei jedem Job aufgerufen
def handler(job):
    # Input von RunPod (deine JSON)
    input_data = job.get("input", {})

    # Hier würdest du deine ComfyUI-Logik aufrufen, z.B.:
    # - Workflow an lokalen ComfyUI-Server schicken
    # - oder ein CLI starten und Outputs einsammeln
    # Fürs Erste einfach nur echo:
    return {
        "status": "ok",
        "echo_input": input_data
    }

runpod.serverless.start({
    "handler": handler
})
