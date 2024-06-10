from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/api/v1/get_days")
def countdown(): 
  now = datetime.now()
  new_year = datetime(2025, 1, 1)
  time_to_new_year = new_year - now
  return "{}".format(time_to_new_year.days, time_to_new_year.seconds//3600,                  (time_to_new_year.seconds//60)%60)

if __name__ == "__main__":
  app.run(host='0.0.0.0')
