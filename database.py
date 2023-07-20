   #it is database toolkit for python
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://ptpkl36td6iqijliqg9g:pscale_pw_Cz95RahQnAZqIX45jM2N4vAvgIpPmFGrQPpt8KIF1nA@aws.connect.psdb.cloud/yourscareer?charset=utf8mb4"

engine = create_engine(
    db_connection_string, 
    connect_args={
        "ssl" : {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


    


    
    
    