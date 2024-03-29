from . import bp_band
from .forms import NewBandForm

# from ieq_cifras.Extensions.database import database
from ieq_cifras.models import User, Band, BandMember
from ieq_cifras.Extensions.database import database

from flask import render_template, request, redirect, url_for, abort

from flask_login import login_required, current_user

'''This is the view of the band'''
@bp_band.route('/<id_band>')
def home(id_band):
    band = Band.query.get(id_band)
    if not band:
        return abort(404)
    if current_user not in band.users:
        return abort(401)
    return render_template('bandHome.html', band=band)
    # return f'{band.name}| {band.users}'


@bp_band.route('/my_bands')
@login_required
def my_bands():
    list_bandMembers = BandMember.query.filter_by(id_user = current_user.id, is_del=False).all()
    list_bandIDs = [bandMember.id for bandMember in list_bandMembers]
    list_bands = database.session.query(Band).filter(Band.id.in_(list_bandIDs)).all()
    list_bands = current_user.bands
    return render_template('my_bands.html', list_bands= list_bands)

@bp_band.route('/new', methods=['GET', 'POST'])
@login_required
def new(): 
    form_newBand  = NewBandForm()
    if request.method == 'GET': # when accessing the page
        return render_template('new.html', title='New Band', form=form_newBand)
    elif request.method == 'POST':
        if form_newBand.validate_on_submit():
            new_band = Band(name=form_newBand.name.data, id_manager=current_user.id)
            database.session.add(new_band)
            database.session.commit()
            new_bandMember = BandMember(id_user = current_user.id, id_band=new_band.id)
            database.session.add(new_bandMember)
            database.session.commit()
            return redirect(url_for('band.my_bands'))
        else:
            return render_template('new.html', title='New Band', form=form_newBand)

@bp_band.route('/<id_band>/invite')
@login_required
def invite(id_band):
    band = Band.query.get(id_band)
    if current_user.id != band.id_manager:
        return abort(401)
    
    
    return render_template('invite.html', band=band)

@bp_band.route('/<id_band>/enter/<access_key>', methods=[ 'GET', 'POST'])
@login_required
def enter(id_band, access_key):
    band = Band.query.get(id_band)
    if band.access_key != access_key: # verify if key is correct
        return 'chave inválida'
    elif current_user in band.users: # verify if user is already in band
        return 'você ja está nessa banda'
    
    if request.method == 'GET':
        return render_template('enter.html', band=band)
    elif request.method == 'POST':
        bandMember = BandMember(id_user = current_user.id, id_band = band.id)
        database.session.add(bandMember)
        database.session.commit()
        return redirect(url_for('band.home', id_band = id_band))
