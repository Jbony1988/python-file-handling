from flask import Flask, render_template, request, redirect, url_for
import os
import shutil

app = Flask(__name__)

# Define file categories and their extensions
CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the uploads folder if it doesn't exist

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('files')  # Get the list of uploaded files
        if not files or all(file.filename == '' for file in files):
            return render_template('index.html', error="No files uploaded.")
        
        # Save files to the upload folder
        for file in files:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        
        organize_files(UPLOAD_FOLDER)  # Organize files in the upload folder
        return redirect(url_for('result'))
    
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in CATEGORIES.items():
                if file_extension in extensions:
                    category_path = os.path.join(directory, category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    moved = True
                    break
            if not moved:
                others_path = os.path.join(directory, 'Others')
                if not os.path.exists(others_path):
                    os.makedirs(others_path)
                shutil.move(file_path, os.path.join(others_path, filename))

if __name__ == '__main__':
    app.run(debug=True)
