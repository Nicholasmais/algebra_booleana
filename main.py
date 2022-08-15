from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def sel_var():
    return render_template("selecionar_variaveis.html")


@app.route("/editar_algoritmo/<num_var>", methods=["POST","GET"])
def editar(num_var):

        num_var = num_var[8:] #num_var=7. o txt para pegar o número 
        params = []
        types_ = []
        for index in range(int(num_var)):

            params.append([request.form.get(f"var_{index}"), 
                            request.form.get(f"sel_{index}")])
 
        return render_template("criar_regra.html", content=params, num_vars = num_var, types = types_) 
  
if __name__ == "__main__":
    app.run(debug=True)
