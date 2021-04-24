from flask import Flask 
import webbrowser
from flask import render_template,url_for
from flask import request
app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    global mes
    global xx
    if request.method=="POST":
        x=(request.form)
        for i in x:
            button_clicked=i#NODE WHICH WE CLICKED
        print(button_clicked)
        with open("templates/indexx.html", "r") as f:
            lines = f.readlines()
        f.close()
        with open("templates/indexx.html", "w") as f:
            for line in lines:
                if line.strip("\n") != mes:
                    f.write(line)
        f.close()
        f = open('templates/indexx.html','a')
        mes = """<ul><li><input  type='submit'  class='btn-lg' value='A' name='p'><ul><li><input  type='submit'   class='btn-lg' value='B' name='TRUEE_C'></li><li><input  type='submit'  class='btn-lg' value='C' name='FALSEE_C'></li></ul></li></ul></form></div></div></div> {% endblock %}"""
        f.write(mes)
        f.write("\n")
        f.close()
        return render_template("indexx.html")
    else:
        f = open('templates/indexx.html','a')
        mes = """<ul><li><input  type='submit'  class='btn-lg' value='A' name='p'><ul><li><input  type='submit'   class='btn-lg' value='-' name='TRUE_c'></li><li><input  type='submit'  class='btn-lg' value='-' name='FALSE_c'></li></ul></li></ul></form></div></div></div> {% endblock %}"""
        f.write(mes)
        f.write("\n")
        f.close()
        return render_template("indexx.html")
mes=''
xx=0
if __name__=="__main__":

   app.run(debug=True)

   



