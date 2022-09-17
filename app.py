
from flask import Flask,render_template,request,session,redirect,url_for

app = Flask(__name__)
app.secret_key='marcos'


@app.route('/',methods=['GET','POST'])
def index():
    nombre= request.form.get('nombre')
    contra=request.form.get('contraseña')
    session['nombre']=nombre
    if nombre=='marcos':
        return redirect(url_for('perfil'))
    return render_template('index.html')

@app.route('/perfil',methods=['GET'])
def perfil():
    if 'nombre' in session:
        return render_template('perfil.html') 
    return "Acesso denegado"

if __name__=='__main__':
    app.run(debug=True)