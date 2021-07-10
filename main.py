# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from PIL import Image

import os
import inference

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask(__name__)
    Bootstrap(app)

    """
    Routes
    """


    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            uploaded_file = request.files['file']
            if uploaded_file.filename != '':
                image_path = os.path.join('static', uploaded_file.filename)
                uploaded_file.save(image_path)
                class_name = inference.get_prediction(image_path)
                print('CLASS NAME=', class_name)
                result = {
                    'class_name': class_name,
                    'image_path': image_path,
                }
                return render_template('show.html', result=result)
        return render_template('index.html')


    if __name__ == '__main__':
        app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

