import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './videos/'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/example")
def example():
    return "<h1>Only and Example</h1>"


@app.route("/upload", methods=['POST'])
def uploadVideo(filename):
    if filename not in request.files:
        flash("No file part")
        return redirect(request.url)
    file = request.files[filename]
    if file.filename == '':
        flash('No selected file')
        return;
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return;

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello_world()
