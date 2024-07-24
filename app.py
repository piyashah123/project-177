from flask import render_template


templates = [
    {
        "input":5,
        "category":"sports",
        "word":"chess"
    },
    {
        "input":5,
        "category" :"Eurpoean country name",
        "word" : "france"
    },

]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status" :"success",
        "word" : random.choice(templates)

    })