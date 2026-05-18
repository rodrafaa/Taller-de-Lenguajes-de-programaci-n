from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Flask"

if __name__ == "__main__":
    app.run(debug=True)

----------------------------------------------------------------------------------

mkdir templates; mkdir static; mkdir static/css
ni index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Hello World Medium</h2>
</body>
</html>
:p!

git commit -m "Subiendo proyecto Flask"

---------------------------------------------------
