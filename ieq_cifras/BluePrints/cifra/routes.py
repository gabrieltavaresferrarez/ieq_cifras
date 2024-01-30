from . import bp_cifra
from flask import render_template

@bp_cifra.route('/view/<int:id_cifra>')
def view(id_cifra):
    return render_template('view.html', id_cifra=id_cifra)

@bp_cifra.route('/upload')
def upload():
    return render_template('upload.html')

# id_cifra ou nome cifra?
# talvez uma formatação doida de : nomeCifra_idCifra
@bp_cifra.route('/edit/<int:id_cifra>')
def edit(id_cifra):
    return render_template('edit.html')