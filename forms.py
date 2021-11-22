from flask_wtf import FlaskForm
from wtforms.fields import SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

#importing choices for classes
unique_bodys = []
with open("static/unique_body.txt", 'r') as f:
    for line in f:
        clean_line = line.replace("\n", "")
        unique_bodys.append(clean_line)
unique_bodys.sort()

unique_fuels = []
with open("static/unique_fuel.txt", 'r') as f:
    for line in f:
        clean_line = line.replace("\n", "")
        unique_fuels.append(clean_line)
unique_fuels.sort()

unique_makes = []
with open("static/unique_makes.txt", 'r') as f:
    for line in f:
        clean_line = line.replace("\n", "")
        unique_makes.append(clean_line)
unique_makes.sort()

unique_models = []
with open("static/unique_models.txt", 'r') as f:
    for line in f:
        clean_line = line.replace("\n", "")
        unique_models.append(clean_line)
unique_models.sort()

unique_trans = []
with open("static/unique_trans.txt", 'r') as f:
    for line in f:
        clean_line = line.replace("\n", "")
        unique_trans.append(clean_line)
unique_trans.sort()

unique_years = []
with open("static/unique_years.txt", 'r') as f:
    for line in f:
        clean_line = line.replace("\n", "")
        unique_years.append(clean_line)



class CarFeaturesForm(FlaskForm):
    Make = SelectField("Make", choices = unique_makes, validators = [DataRequired()])
    Model = SelectField("Model", choices = unique_models, validators=[DataRequired()])
    Year = SelectField("Year", choices = unique_years, validators=[DataRequired()])
    BodyStyle = SelectField("Body Style", choices = unique_bodys, validators=[DataRequired()])
    Distance = IntegerField("Distance", validators=[DataRequired(), NumberRange(min=0,max=5)])
    Engine = IntegerField("Engine capacity(cm3)", validators=[DataRequired(), NumberRange(min=0,max=5)])
    FuelType = SelectField("Fuel type", choices = unique_fuels, validators=[DataRequired()])
    Transmission = SelectField("Transmission", choices = unique_trans, validators=[DataRequired()])
    submit = SubmitField()