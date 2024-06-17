from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

DALLE_API_ENDPOINT = 'https://api.openai.com/v1/images/dalle-mini/generate'
API_KEY = 'your_openai_api_key_here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()

    description = data.get('description', '')

    if not description:
        return jsonify({'error': 'Empty description provided.'}), 400

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}',
    }

    payload = {
        'prompt': description,
        'max_tokens': 50,
    }

    try:
        response = requests.post(DALLE_API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()

        generated_image_data = response.json()

        image_url = generated_image_data.get('data', {}).get('image', {}).get('url')

        if image_url:
            return jsonify({'url': image_url})
        else:
            return jsonify({'error': 'Failed to retrieve image URL from response.'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request to DALL-E-mini API failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
