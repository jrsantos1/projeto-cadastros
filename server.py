from flask import Flask, render_template, Blueprint

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://@jrsantos/DGR?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'minha_chave_secreta_super_segura'
db = SQLAlchemy(app)
