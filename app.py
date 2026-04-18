from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')


        if len(name) < 3:
            f'Ism 3 harfdan katta bolishi kerak'

        if '@' not in email:
            f'Emailda @ belgisi bolishi kerak'

        if len(password) < 6:
            f'Parol  6 ta belgidan iborat bolishi kerak'

        else:
            return render_template('result.html', name=name, email=email, password=password)


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
