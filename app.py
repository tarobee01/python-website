from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id': '1',
  'title': 'data analyst',
  'location': 'japan mie prefecture',
  'salary': '1500yen',
},
{
  'id': '2',
  'title': 'data engineer',
  'location': 'japan mie prefecture',
  'salary': '1500yen',
},
{
  'id': '3',
  'title': 'programing engineer',
  'location': 'japan mie prefecture',
  'salary': '1500yen',
}
]

@app.route("/")
def first_website():
  return render_template('home.html', jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
