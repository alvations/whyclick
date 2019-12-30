
import time

from flask import Flask, jsonify, request, render_template, flash

from wtforms import Form, TextField, HiddenField, validators
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms import widgets
from wtforms.fields.core import StringField
from wtforms import SelectMultipleField

from whyclick import whyq

class PasswordField(StringField):
    """
    Original source:
    https://github.com/wtforms/wtforms/blob/2.0.2/wtforms/fields/simple.py#L35-L42

    A StringField, except renders an ``<input type="password">``.
    Also, whatever value is accepted by this field is not rendered back
    to the browser like normal fields.
    """
    widget = widgets.PasswordInput(hide_value=False)

class MultiCheckboxField(SelectMultipleField):
    """
    Originally from https://gist.github.com/doobeh/4668212
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

application = Flask(__name__)
application.config.from_object(__name__)
application.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


DIETS = [
    ('vegetarian', 'Vegetarian'),
    ('halal', 'Halal'),
    ('healthy', 'Healthy')
]

class ReusableForm(Form):
    username = TextField('Username:')
    password = PasswordField('Password:')
    dietary = MultiCheckboxField('Dietary Preferences:', choices=DIETS)

@application.route('/demo', methods=['GET', 'POST'])
def demo():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        request_form = request.form
        query = {'username': request_form['username'],
                 'password': request_form['password'],
                 }
        if form.validate():
            # Parse the dietary preferences.
            kwargs = {d:True for d in request_form.getlist('dietary')}
            # Login to WhyQ
            driver = whyq.login(query['username'], query['password'], headless=False)
            # Randomly order.
            days = driver.find_elements_by_xpath("//div[@class='owl-item active']")
            for element_day in days:
                element_day.click()
                driver, element_day, msg = whyq.randomly_order_one_day(driver, element_day, **kwargs)
                ##print(msg)
                if msg:
                    flash(msg)
                time.sleep(3)

    return render_template('demo.html', form=form)


if __name__ == '__main__':
    application.run(port=5000, host='0.0.0.0')
