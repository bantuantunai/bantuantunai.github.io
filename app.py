from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    ic_number = request.form['ic_number']
    phone_number = request.form['phone_number']
    email = request.form['email']
    bank_name = request.form['bank_name']
    account_number = request.form['account_number']

    with open('information.txt', 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"IC Number: {ic_number}\n")
        file.write(f"Phone Number: {phone_number}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Bank Name: {bank_name}\n")
        file.write(f"Account Number: {account_number}\n\n")

    return 'Information submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
