import os

from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_name(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([f'{email}', f'{subject}', f'{message}'])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something go wrong'


# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/components")
# def components():
#     return render_template('components.html')
#
# @app.route("/work.html")
# def work():
#     return render_template("work.html")
#
# @app.route("/works.html")
# def works():
#     return render_template("works.html")
#
# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")
#
# @app.route("/thankyou.html")
# def thankyou():
#     return render_template("thankyou.html")

# @app.route('/<username>')
# def hello_world2(username=None):
#     return render_template('index.html', name=username)
#
# @app.route('/<username>/<int:post_id>')
# def show_post(username=None, post_id=None):
#     # show the post with the given id, the id is an integer
#     return render_template('index2.html', name=username, post_id=post_id)
#
# @app.route("/index")
# def inedex_page():
#     return render_template('index.html')