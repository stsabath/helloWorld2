from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Sebestyen Toszegi-Sabath! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def about_css():  # put application's code here
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():

    subject = request.args.get('subject')
    course_number = request.args.get('course_number')

    return render_template(
        "favorite-course.html",
        subject=subject,
        course_number=course_number
    )

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        print('First name entered: ' + request.form.get('first_name'))
        print('Last name entered: ' + request.form.get('last_name'))
        print('Email entered: ' + request.form.get('email'))

        if request.form.get('agree_check'):
            print('Agree to be contacted entered: ' + request.form.get('agree_check'))

        return render_template('contact.html', form_submitted=True)


    else:
        return render_template('contact.html')



    return render_template("contact.html")

if __name__ == '__main__':
    app.run()

