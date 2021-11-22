import pickle
from model_files.ml_model import price_prediction
from costum_transformers.transformers import KmPerYear
from flask import Flask, render_template, request, url_for
from forms import CarFeaturesForm
import math
import __main__
__main__.KmPerYear = KmPerYear

#initialize the app
app = Flask("__name__")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/', methods=["POST","GET"])
def predict():
    if request.method == "POST":
        form = CarFeaturesForm()
        features = dict(request.form)

        with open('./model_files/model.bin', 'rb') as f_in:
            model = pickle.load(f_in)

        prediction = math.floor(price_prediction(features, model)[0])
        return render_template('prediction.html', title='Register', form=form, prediction=prediction)
    else:
        form = CarFeaturesForm()
        return render_template('layout.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
