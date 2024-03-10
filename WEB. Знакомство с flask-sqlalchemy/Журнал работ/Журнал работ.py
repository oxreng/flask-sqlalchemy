from data.db_session import global_init, create_session
from data.jobs import Jobs
from flask import Flask, render_template

global_init('db/company.sqlite')
app = Flask(__name__)


@app.route('/')
def main_route():
    db_sess = create_session()
    get_data = db_sess.query(Jobs).all()
    return render_template(template_name_or_list='content.html', get_data=get_data, title="Журнал работ")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
