from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Define a route for generating responses using the Ollama model
@app.route('/api/generate', methods=['POST'])
def generate():
    user_input = request.json.get('input', '')
    if not user_input:
        return jsonify({'error': 'Input text is required'}), 400
    
    # Run Ollama with the input text (make sure to modify this with your actual Ollama command)
    try:
        # Assuming you are calling Ollama via subprocess
        result = subprocess.run(['ollama', 'run', 'gemma:2b', '--input', user_input],
                                capture_output=True, text=True, check=True)
        response_text = result.stdout.strip()
        
        return jsonify({'response': response_text})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Error while generating response from model', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
