   #it is database toolkit for python
# import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://d5fi33vnr19jzm91wntp:pscale_pw_2vbD904IUP8XgvxjtkFVMCXUnjxLdA61byXy8WJip1v@aws.connect.psdb.cloud/yourscareer?charset=utf8mb4"

engine = create_engine(
    db_connection_string, 
    connect_args={
        "ssl" : {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))

#     jobs = []
#     for row in result.all():
#         jobs.append(row._asdict())
#     print(jobs)
    


    
    
    