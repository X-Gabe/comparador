from flask import Flask, render_template, request
from difflib import SequenceMatcher, HtmlDiff

app = Flask(__name__)

def calcular_similaridade(texto1, texto2):
    """
    Retorna a porcentagem de similaridade entre dois textos
    """
    return SequenceMatcher(None, texto1, texto2).ratio() * 100

# Aqui eu defini a rota 
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        texto1 = request.form["texto1"]
        texto2 = request.form["texto2"]

        # Variavel de similaridade
        similaridade = calcular_similaridade(texto1, texto2)

        # Aqui Gera HTML com as diferenças
        diff = HtmlDiff(wrapcolumn=70)  # wrapcolumn quebra linhas longas
        diff_html = diff.make_table(
            texto1.splitlines(),
            texto2.splitlines(),
            "Texto 1",
            "Texto 2",
            context=True,
            numlines=2
        )

        return render_template(
            "resultado.html", 
            similaridade=round(similaridade, 2), 
            diff_html=diff_html
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
