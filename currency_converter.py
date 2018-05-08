from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route("/")
def run_server():
    # TODO: load list of currencies form a txt file
    currencies = ['INR', 'EUR', 'AUD' , 'USD']
    
    return render_template('cc.html', currencies_from = sorted(currencies), currencies_to = sorted(currencies) )
 

@app.route("/result", methods=['GET','POST'])
def convert():
    currencies_from = request.args.get('currency_from')
    currencies_to = request.args.get('currency_to')
    amount = float(request.args.get('amount'))
    currency_rates = {'INR': 66.7681, 'EUR': 1.1969, 'AUD': 0.7538 , 'USD' : 1}
 
    converted_rate = (float(amount) * float(currency_rates[currencies_from])  * float(currency_rates[currencies_to]))

    data = {'amount':amount, 'currency_from': currencies_from, 'currency_to': currencies_to, 'converted_amt': converted_rate}
            
    return render_template('result.html', data=data )
 
if __name__ == "__main__":
    app.run(debug = True)
