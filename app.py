from flask import Flask, render_template, url_for, render_template_string  # type: ignore


app = Flask(__name__, static_url_path='/static', template_folder='templates')


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/serie1_all_kanji")
def serie1_all_kanji():
    return render_template("/1 - Serie/serie1_all_kanji.html")

@app.route("/serie1_grupo1")
def serie1_grupo1():
    return render_template("/1 - Serie/serie1_grupo1.html")

@app.route("/serie1_grupo2")
def serie1_grupo2():
    return render_template("/1 - Serie/serie1_grupo2.html")

@app.route("/serie1_grupo3")
def serie1_grupo3():
    return render_template("/1 - Serie/serie1_grupo3.html")

@app.route("/serie1_grupo4")
def serie1_grupo4():
    return render_template("/1 - Serie/serie1_grupo4.html")

@app.route("/serie1_grupo5")
def serie1_grupo5():
    return render_template("/1 - Serie/serie1_grupo5.html")

@app.route("/serie1_grupo6")
def serie1_grupo6():
    return render_template("/1 - Serie/serie1_grupo6.html")

@app.route("/serie1_grupo7")
def serie1_grupo7():
    return render_template("/1 - Serie/serie1_grupo7.html")

@app.route("/serie1_grupo8")
def serie1_grupo8():
    return render_template("/1 - Serie/serie1_grupo8.html")

@app.route("/serie1_grupo9")
def serie1_grupo9():
    return render_template("/1 - Serie/serie1_grupo9.html")

@app.route("/serie1_grupo10")
def serie1_grupo10():
    return render_template("/1 - Serie/serie1_grupo10.html")


if __name__ == "__main__":
    app.run(debug= True)
