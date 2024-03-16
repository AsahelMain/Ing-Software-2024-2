from flask import Flask, render_template

from alchemyClasses import db
from controllers.PrimerControlador import mi_primer_blueprint
from controllers.ControllerAlumno import alumno_blueprint
from controllers.ControladorUsuario import blueprint_usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://asmc:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
app.register_blueprint(mi_primer_blueprint)
app.register_blueprint(alumno_blueprint)
app.register_blueprint(blueprint_usuario)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
