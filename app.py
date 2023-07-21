from flask import Flask,render_template, jsonify, request
from database import load_jobs_from_db, load_jobs_form_db, add_application_to_db


# app is the object of python
# pass : ixyfhswoksyqcuvq


app = Flask(__name__)

@app.route("/")
def hello_world():       #define a function
    jobs = load_jobs_from_db()
    return render_template('home.html',
                           jobs=jobs,
                           company_name='Career')


@app.route("/job/<id>")
def show_job(id):
    job =load_jobs_form_db(id)

    if not job:
        return "Not Found", 404
    
    return render_template('job_page.html',
                          job = job)

# instead of returning html files we can also return json file (json = javascript object)
@app.route("/job/<id>/apply", methods=['post'])
def apply_to_jobs(id):
    data = request.form
    job = load_jobs_form_db(id)
    # return jsonify(job['title'])
    # store the data in db
    # display an aknowledgement
    if job:
        add_application_to_db(id, data)
        # send_confirmation_email(data, job['title'], data['email'])  # Send the confirmation email
        return render_template('application_submit.html', job=job, application=data)
    else:
        # Handle the case when the job with the given id does not exist
        # For example, you can redirect to an error page or display an error message
        return render_template('job_not_found.html')

# application = load_jobs_form_db('email')
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = '578'  # Use the appropriate port for your mail server
# app.config['MAIL_USERNAME'] = 'codewithme21@gmail,com'
# app.config['MAIL_PASSWORD'] = 'Abhijeet@2002'
# # app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)

# def send_confirmation_email(application_data, job_title, recipient_email):
#     subject = "Job Application Confirmation - " + job_title
#     body = f"Dear {application_data['full_name']},\n\nThank you for applying to the job '{job_title}'. We have received your application.\n\nBest regards,\nThe Career Team"

#     msg = Message(subject, recipients=[recipient_email], body=body)
#     mail.send(msg)




if __name__ == "__main__":
    app.run()
