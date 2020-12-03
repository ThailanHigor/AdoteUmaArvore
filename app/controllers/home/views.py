from . import home
from flask import render_template, url_for, redirect, request,jsonify
from email_validator import validate_email, EmailNotValidError
from flask_mail import Message, Mail

from app import mail

@home.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")

@home.route('/news/cadastrar', methods=["POST"])
def cadastrar_news():
    email =  request.form['email']
    try:
        valid = validate_email(email)
        print(valid.email)
        msg = Message("Novo cadastro Newsletter", sender="Newsletter", recipients=["thailan-higor@hotmail.com", "andrepraz@gmail.com", "liviavid@gmail.com", "pauloedu.carvalho@outlook.com","juliatorres203@gmail.com"])
        msg.html = f"<b>Novo email cadastrado na newsletter:</b> {email}"
        mail.send(msg)
        return jsonify({'status':True})

    except EmailNotValidError:
        return jsonify({'status':False})

@home.route('/contato/cadastrar', methods=["POST"])
def cadastrar_contato():
    nome =  request.form['nome']
    email =  request.form['email']
    assunto =  request.form['assunto']
    mensagem =  request.form['mensagem']

    if nome and email and assunto and mensagem:
        msg = Message("Novo contato cadastrado", sender="Contato", recipients=["thailan-higor@hotmail.com", "andrepraz@gmail.com", "liviavid@gmail.com", "pauloedu.carvalho@outlook.com","juliatorres203@gmail.com"])
        msg.html = f"<b>Novo email cadastrado no contato:</b><br> {nome}<br>{email}<br>{assunto}<br>{mensagem}"
        mail.send(msg)
        return jsonify({'status':True})
    
    return jsonify({'status':False})



