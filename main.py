from flask import Flask, request, render_template
import requests
app = Flask(__name__)
# List of states for Drop down button
STATES = ["Maharashtra", "Delhi", "Tamil Nadu", "Rajasthan", "Madhya Pradesh", "Uttar Pradesh", "Gujarat", "Telangana", "Andhra Pradesh", "Kerala", "Jammu and Kashmir", "Karnataka", "Haryana", "West Bengal", "Punjab", "Bihar", "Odisha", "Uttarakhand", "Chhattisgarh",
          "Himachal Pradesh", "Assam", "Jharkhand", "Chandigarh", "Ladakh", "Andaman and Nicobar Islands", "Goa", "Puducherry", "Manipur", "Tripura", "Mizoram", "Arunachal Pradesh", "Dadra and Nagar Haveli", "Nagaland", "Meghalaya", "Daman and Diu", "Lakshadweep", "Sikkim"]

# Route to index.html
@app.route("/")
def index():
    return render_template('index.html', data=STATES)

# Route to get the data from the API
@app.route("/covid_data/<state>", methods=['GET'])
def getCovidData(state):
    if request.method == 'GET':
        response = requests.get('https://api.covid19india.org/data.json')
        data = response.json()['statewise']
        for _state in data:
            if _state['state'] == state:
                # return _state['staIte'], _state['lastupdatedtime'], _state['active'], _state['confirmed'], _state['deaths'], _state['recovered']
                return _state


if __name__ == "__main__":
    app.run(host="0.0.0.0")
