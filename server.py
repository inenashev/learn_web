from flask import Flask, render_template
from weather import weather_by_city



app = Flask(__name__)



@app.route('/')
def index():
    page_title = 'новости python'
    weather = weather_by_city("Moscow,Russia")
    return render_template("index.html", page_title = page_title, weather=weather)

if __name__=="__main__":
    #weather = weather_by_city("Moscow,Russia")
    #print(weather)
    #print(f"Token is: {token}")
    #app.secret_key = 'super secret key'
    #app.run(debug=True)
    app.run()