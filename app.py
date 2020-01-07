from flask import Flask
from flask import request
from PIL import Image
import base64
from io import BytesIO
import os
from flask import jsonify
from utils import get_np_array_from_file,de_noise,de_blur
app = Flask(__name__)

UPLOAD_FOLDER = os.path.join("images")
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def hello():
    return "Hello, World!"
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method =='POST':
        image = request.files['image']
        np_img = get_np_array_from_file(image)
        # image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
        np_img_denoise = de_noise(de_blur(np_img))
        denoiseImage = Image.fromarray(np_img_denoise)
        # denoise_path = os.path.join(app.config["UPLOAD_FOLDER"], "denoise_"+image.filename)
        # denoiseImage.save(denoise_path)
        buffered = BytesIO()
        denoiseImage.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        # img_str = base64.b64encode(buffered.getvalue()).decode()
        return jsonify(data = img_str)
    return "Flask inside Docker!!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
