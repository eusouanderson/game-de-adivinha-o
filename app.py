from flask import Flask, render_template, request
from random import randint



app = Flask(__name__)
num_tent = 0

@app.route('/')
def on_start():
    global num_tent
    num_tent = 0
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global num_tent
    numberale = str(randint(1, 5))
    button_select = str(request.form.get('opcao'))
    num_tent += 1    
    print(f'Numero escolhido pela maquina ', numberale)
    print(button_select)
    if button_select == numberale:
        return render_template('win.html', tent= num_tent) 
    else:
        erro = 'Numero Errado!, Tente de novo!'
        maq = f'Numero escolhido pela maquina foi {numberale}'
        tent = f'Tentativas: {num_tent}'
        return render_template('index.html', erro=erro, maq = maq, tent=tent)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


