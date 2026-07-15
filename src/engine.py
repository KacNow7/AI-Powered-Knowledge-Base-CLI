import requests
from typing import Optional

class OllamaClient:
    def __init__(self, model: str = "phi3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def ask(self, prompt: str) -> Optional[str]:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {"num_ctx": 2048}
        }
        
        try:
            response = requests.post(self.url, json=payload, timeout=None)
            response.raise_for_status()
            return response.json().get("response")
        except requests.exceptions.Timeout:
            print("Błąd: Serwer nie odpowiedział w wyznaczonym czasie (timeout).")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Błąd połączenia: {e}")
            return None