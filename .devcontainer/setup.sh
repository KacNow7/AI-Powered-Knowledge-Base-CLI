#!/bin/bash
# Instalacja zależności
sudo apt-get update && sudo apt-get install -y zstd

# Instalacja Ollamy
curl -fsSL https://ollama.com/install.sh | sh

# Uruchomienie w tle
ollama serve > ollama.log 2>&1 &
sleep 10

# Pobranie modelu
ollama pull llama3