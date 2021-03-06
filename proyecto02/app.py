"""
    Tomado de https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
"""

from config import enlace
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = enlace
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Matricula(db.Model):

    __tablename__ = 'matriculas'

    id = db.Column(db.Integer, primary_key=True)
    nombrePropietario = db.Column(db.String(200))
    placa = db.Column(db.String(200))
    # este atributo no puede ser nulo
    anio = db.Column(db.String(200), nullable=False)
    costo = db.Column(db.Float(100.0))


def __repr__(self):
    return "Matricula: nombre Propietario = %s placa = %s anio = %s costo = %d" % (
        self.nombrePropietario,
        self.placa,
        self.anio,
        self.costo)

# vista


@app.route('/')
def index():
    matriculas = Matricula.query.all()
    return render_template('index.html', matriculas=matriculas)


@app.route('/<int:Matricula_id>/')
def Matricula(matricula_id):
    matricula = Matricula.query.get_or_404(matricula_id)
    return render_template('matricula.html', matricula=matricula)


@app.route('/add/matricula/', methods=('GET', 'POST'))
def crear():
    if request.method == 'POST':
        nombrePropietario = request.form['nombrePropietario']
        placa = request.form['placa']
        anio = request.form['anio']
        costo = request.form['costo']
        vehiculo = Matricula(nombrePropietario=nombrePropietario,
                           placa=placa,
                           anio=anio,
                           costo=costo,
                           )
        db.session.add(vehiculo)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('crear.html')


@app.route('/editar/matricula/<int:matricula_id>/', methods=('GET', 'POST'))
def editar(matricula_id):
    matricula = Matricula.query.get_or_404(matricula_id)

    if request.method == 'POST':
        nombrePropietario = request.form['nombrePropietario']
        placa = request.form['placa']
        anio = request.form['anio']
        costo = request.form['costo']

        Matricula.nombrePropietario = nombrePropietario
        Matricula.placa = placa
        Matricula.placa = placa
        db.session.add(Matricula)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('editar.html', Matricula=Matricula)
