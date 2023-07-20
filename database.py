   #it is database toolkit for python
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://b8hzsy719wb6vqh4pzy6:pscale_pw_wNE7APtD1oCL0RdMXegJEdxJuHpl5qqEWPA48b1pnA0@aws.connect.psdb.cloud/yourscareer?charset=utf8mb4"

engine = create_engine(
    db_connection_string, 
    connect_args={
        "ssl" : {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))

#     jobs = []
#     for row in result.all():
#         jobs.append(row._asdict())
#     print(jobs)
    


    
    
    