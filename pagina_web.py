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

*HTML*

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GameStore</title>

    <link rel="stylesheet" href="{{url_for('static', filename='css/output-style.css')}}">

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">

    <style>
        body{
            font-family: 'Orbitron', sans-serif;
        }

        .neon-text{
            text-shadow:
                0 0 5px #00ffae,
                0 0 10px #00ffae,
                0 0 20px #00ffae,
                0 0 40px #00ffae;
        }

        .card-glow:hover{
            box-shadow:
                0 0 10px #00ffae,
                0 0 20px #00ffae;
        }
    </style>
</head>

<body class="bg-zinc-950 text-white min-h-screen">

    <!-- Navbar -->
    <nav class="bg-zinc-950 border-b border-emerald-500 p-5 flex justify-between items-center">

        <h1 class="text-4xl font-black text-emerald-400 neon-text">
            GameStore
        </h1>

        <ul class="flex gap-8 text-lg font-bold">
            <li class="hover:text-emerald-400 transition cursor-pointer">
                Inicio
            </li>

            <li class="hover:text-emerald-400 transition cursor-pointer">
                Juegos
            </li>

            <li class="hover:text-emerald-400 transition cursor-pointer">
                Ofertas
            </li>

            <li class="hover:text-emerald-400 transition cursor-pointer">
                Contacto
            </li>
        </ul>
    </nav>

    <!-- Hero -->
    <section class="text-center py-20 px-6">

        <h2 class="text-6xl font-black mb-6 neon-text text-emerald-400">
            ENTER THE GAME
        </h2>

        <p class="text-zinc-400 text-2xl max-w-3xl mx-auto leading-relaxed">
            Descubre videojuegos épicos, aventuras futuristas y las mejores ofertas gamer del momento.
        </p>

    </section>

    <!-- Cards -->
    <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 p-10">

        <!-- Card 1 -->
        <div class="bg-zinc-900 rounded-3xl overflow-hidden border border-zinc-800 hover:scale-105 transition duration-300 card-glow">

            <img
                src="{{ url_for('static', filename='images/cyberpunk.jpg') }}"
                class="w-full h-72 object-cover"
            >

            <div class="p-6">

                <h3 class="text-3xl font-black text-emerald-400 mb-3">
                    Cyber Nexus
                </h3>

                <p class="text-zinc-400 mb-6">
                    Explora una ciudad cyberpunk llena de acción, tecnología y enemigos futuristas.
                </p>

                <button class="bg-emerald-500 hover:bg-emerald-400 text-black font-black px-6 py-3 rounded-xl transition">
                    Comprar
                </button>

            </div>
        </div>

        <!-- Card 2 -->
        <div class="bg-zinc-900 rounded-3xl overflow-hidden border border-zinc-800 hover:scale-105 transition duration-300 card-glow">

            <img
                src="https://images.unsplash.com/photo-1511512578047-dfb367046420?q=80&w=1400&auto=format&fit=crop"
                class="w-full h-72 object-cover"
            >

            <div class="p-6">

                <h3 class="text-3xl font-black text-cyan-400 mb-3">
                    Battle Arena X
                </h3>

                <p class="text-zinc-400 mb-6">
                    Compite online con jugadores de todo el mundo en combates extremos.
                </p>

                <button class="bg-cyan-400 hover:bg-cyan-300 text-black font-black px-6 py-3 rounded-xl transition">
                    Comprar
                </button>

            </div>
        </div>

        <!-- Card 3 -->
        <div class="bg-zinc-900 rounded-3xl overflow-hidden border border-zinc-800 hover:scale-105 transition duration-300 card-glow">

            <img
                src="{{ url_for('static', filename='images/carros.jpg') }}"
                class="w-full h-72 object-cover"
            >

            <div class="p-6">

                <h3 class="text-3xl font-black text-pink-500 mb-3">
                    Velocity Drift
                </h3>

                <p class="text-zinc-400 mb-6">
                    Vive carreras callejeras neon a máxima velocidad en ciudades futuristas.
                </p>

                <button class="bg-pink-500 hover:bg-pink-400 text-black font-black px-6 py-3 rounded-xl transition">
                    Comprar
                </button>

            </div>
        </div>

    </section>

</body>
</html>

