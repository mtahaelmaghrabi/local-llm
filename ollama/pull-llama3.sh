
./bin/ollama serve &

pid=$!

sleep 5

echo "Pulling llama3.3:70b model ..."
ollama pull llama3.3:70b

wait $pid