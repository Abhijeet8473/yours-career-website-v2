from flask import Flask,render_template, jsonify
from database import engine
from sqlalchemy import create_engine, text

# app is the object of python

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Bengaluru',
        'salary' : 'Rs 1,00,000'
    },
    {
        'id' : 2,
        'title' : 'Data Scintist',
        'location' : 'Delhi',
        'salary' : 'Rs 15,00,000'
    },
    {
        'id' : 3,
        'title' : 'Frontend Engineer',
        'location' : 'Remote',
        'salary' : 'Rs 12,00,000'
    },
    {
        'id' : 4,
        'title' : 'Back Engineer',
        'location' : 'San Francisco, USA',
        'salary' : '$ 120,000'
    }
]

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

@app.route("/")
def hello_world():       #define a function
    jobs = load_jobs_from_db()
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Career')

# instead of returning html files we can also return json file (json = javascript object)
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run()
