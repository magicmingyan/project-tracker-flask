"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, flash, redirect

import hackbright

app = Flask(__name__)
app.secret_key = "HI!"


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                            first = first,
                            last = last,
                            github = github)

    return html

@app.route("/student-search")
def get_studnt_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['GET', 'POST'])
def student_add():
    """ Adds a student."""


    github = request.form.get('github')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    hackbright.make_new_student(first_name, last_name, github)
    flash("Added student to form")

    # html = render_template("add_student_dataset.html")
    #                         # first_name = first_name,
    #                         # last_name= last_name,
    #                         # github = github)

    # return html
    return render_template("add_student_dataset.html")
    #return redirect("/student")

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
