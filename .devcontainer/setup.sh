#!/bin/bash

# Instalacja Ollamy
curl -fsSL https://ollama.com/install.sh | sh

# Uruchomienie Ollamy w tle i pobranie modelu
ollama serve > ollama.log 2>&1 &
sleep 5
ollama pull llama3
echo "Ollama jest gotowa!"