from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient

app = Flask(__name__)

# Initialize the Hugging Face client with your API key
client = InferenceClient(api_key="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")

@app.route('/')
def home():
    return render_template('index.html')  # Renders the frontend page

@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        # Get the question from the frontend
        data = request.get_json()
        user_question = data.get('question')  # Extract question from JSON

        if not user_question:
            return jsonify({"error": "No question provided"}), 400

        # Prepare the message for Hugging Face model
        messages = [{"role": "user", "content": user_question}]

        # Generate response from Hugging Face model
        completion = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1", 
            messages=messages,
            max_tokens=500
        )

        # Return the generated response as JSON
        return jsonify({"response": completion.choices[0].message['content']})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/test_static')
def test_static():
    return app.send_static_file('style.css')

if __name__ == '__main__':
    app.run(debug=True)
