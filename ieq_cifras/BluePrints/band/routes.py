from . import bp_band
from .forms import NewBandForm

from flask import render_template, request

from flask_login import login_required, current_user

@bp_band.route('/my_bands')
@login_required
def my_bands():
    return render_template('my_bands.html', list_bands= [])

@bp_band.route('/new')
@login_required
def new():
    form_newBand  = NewBandForm()
    if request.method == 'GET': # when accessing the page
        return render_template('login.html', title='New Band', form=form_newBand)
