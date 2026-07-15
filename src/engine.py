import requests
from typing import Optional

class OllamaClient:
    """Klient do komunikacji z lokalnym API Ollamy."""
    
    def __init__(self, model: str = "llama3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def ask(self, prompt: str) -> Optional[str]:
        """Wysyła zapytanie do modelu i zwraca odpowiedź."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(self.url, json=payload, timeout=30)
            response.raise_for_status()
            return response.json().get("response")
        except requests.exceptions.RequestException as e:
            print(f"Error: Nie można połączyć się z Ollama: {e}")
            return None