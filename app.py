from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Pasadena, California',
    'salary': '$100,000'
  },
  {
    'id': 2,
  'title': 'Data Scientist',
  'location': 'Pasadena, California',
  'salary': '$150,000'
  },
  {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  },
  {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Fransisco, California',
  'salary': '$175,000'
  }
  



]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='JPL')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)