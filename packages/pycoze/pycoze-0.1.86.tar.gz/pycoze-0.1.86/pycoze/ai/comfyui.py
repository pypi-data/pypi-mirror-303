from .vram_reserve import reserve_vram_retry, release_vram


class ComfyUI:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        reserve_vram_retry(20)  # 20GB VRAM
        with open(self.file_path, "r") as file:
            return file.read()

    def __exit__(self, exc_type, exc_value, traceback):
        clear_memory()
        return None

    def unload(self):
        clear_memory()
        return None


def clear_memory():
    import requests
    import json

    release_vram()

    url = "http://127.0.0.1:8188/free"
    data = {"unload_models": True, "free_memory": False}
    response = requests.post(
        url, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    return response.status_code, response.text
