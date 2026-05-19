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

node -v
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
npm -v
npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output-style.css --watch

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{url_for('static', filename='css/output-style.css')}}">
    <title>Document</title>
</head>
<body>
    <h2 class='text-4xl text-center font-mono py-5 font-black text-emerald-600'>Hello World Medium</h2>
</body>
</html>
:p!

-------------------------------------------------------

