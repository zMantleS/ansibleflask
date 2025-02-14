from flask import *
from flask_mysqldb import MySQL

app = Flask("My ansible AI app", template_folder="/usr/share/nginx/html")
app.config["MYSQL_USER"] = "admint"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "AnsibleApp"
app.config["MYSQL_HOST"] = "192.168.0.30"
app.config["MYSQL_PORT"] = 3306

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")



app.run(host="0.0.0.0", port=5000, debug=True)
