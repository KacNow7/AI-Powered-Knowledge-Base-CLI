import argparse
import sys
from engine import OllamaClient

def main():
    parser = argparse.ArgumentParser(
        description="Ollama Local Assistant - Proste narzędzie AI dla Twojego terminala."
    )
    parser.add_argument(
        "prompt", 
        type=str, 
        help="Treść pytania, które chcesz zadać modelowi AI."
    )
    
    args = parser.parse_args()
    client = OllamaClient()

    print(f"--- Pytanie: {args.prompt} ---")
    print("AI myśli...")
    
    answer = client.ask(args.prompt)
    
    if answer:
        print(f"\nOdpowiedź:\n{answer}")
    else:
        print("\nNie udało się uzyskać odpowiedzi. Sprawdź, czy Ollama działa.")
        sys.exit(1)

if __name__ == "__main__":
    main()