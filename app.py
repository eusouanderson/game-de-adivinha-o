from flask import Flask, render_template, request
from random import randint



app = Flask(__name__)

@app.route('/')
def on_start():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    numberale = str(randint(1, 5))
    button_select = str(request.form.get('opcao'))
    print(f'Numero escolhido pela maquina ', numberale)
    print(button_select)
    if button_select == numberale:
        return render_template('win.html') 
    else:
        print('Numero Errado!, Tente de novo!')
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)


