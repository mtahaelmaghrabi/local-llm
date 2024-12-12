
./bin/ollama serve &

pid=$!

sleep 5

echo "Pulling llama3 model ..."
ollama pull llama3.1:8b

wait $pid