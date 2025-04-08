FROM ollama/ollama

# Run the AI model when container starts
CMD ["ollama", "run", "tinyllama"]
