   #it is database toolkit for python
# import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://zsaid0qcqgth099orlgm:pscale_pw_aWBPCCBvF8YqPaZ5tZupmMJeDTXERwmalj4RpxnQikw@aws.connect.psdb.cloud/yourscareer?charset=utf8mb4"

engine = create_engine(
    db_connection_string, 
    connect_args={
        "ssl" : {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs
# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))

#     jobs = []
#     for row in result.all():
#         jobs.append(row._asdict())
#     print(jobs)

def load_jobs_form_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE id = :val")
        result = conn.execute(query.bindparams(val=id))
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            row_dict = rows[0]._asdict()  # Add parentheses to call the method
            return row_dict
        
 
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO application(job_id, full_name, email, linkedin_url, education, work_Experience, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :work_Experience, :resume_url)")

        conn.execute(query, {
            "job_id": job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "linkedin_url": data['linkedin_url'],
            "education": data['education'],
            "work_Experience": data['work_Experience'],
            "resume_url": data['resume_url']
        })

