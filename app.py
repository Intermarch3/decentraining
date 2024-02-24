from flask import Flask, request, redirect, url_for, flash, send_from_directory, render_template
import os

ALLOWED_EXTENSIONS = set(['py', 'csv', 'png', 'jpg', 'jpeg', 'txt', 'json'])
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

app = Flask(__name__, static_folder='assets')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/training', methods=['GET', 'POST'])
def training():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # return redirect to the uploaded file
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('training.html'), 200

@app.route('/', methods=['GET'])
def main():
    return render_template('page.html'), 200