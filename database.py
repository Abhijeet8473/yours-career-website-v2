   #it is database toolkit for python
# import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://94g4yfis14y0h9gzwny9:pscale_pw_4TKOJ78P5S15zQEvYNGHIHHYTv7pLQq3Hy8wEIHNoZp@aws.connect.psdb.cloud/yourscareer?charset=utf8mb4"

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
    


    
    
    