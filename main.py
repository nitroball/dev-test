from flask import Flask, request, send_from_directory
from api.diffusion import generate_image

app = Flask(__name__)

@app.route('/image', methods=['GET'])
def image_endpoint():
    prompt = request.args.get('prompt')
    image_name = generate_image(prompt)
    return send_from_directory('static/images', image_name)

if __name__ == '__main__':
    app.run(debug=True)