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
        with open("templates/indexx.html", "r") as f:
            lines = f.readlines()
        f.close()
        with open("templates/indexx.html", "w") as f:
            for line in lines:
                if line.strip("\n") != mes:
                    f.write(line)
        f.close()
        f = open('templates/indexx.html','a')           
        x=(request.form)
        for i in x:
            button_clicked=i
        print(button_clicked)#NODE WHICH WE CLICKED



        #sample from backend
        venki_l1={1:'A',2:'-',3:'-'}
        venki_k2={1:[[2,'True'],[3,'False']]}

        #string to be generated from venkitesh's code for sample backend
        mes = """<ul><li><input  type='submit'  class='btn-lg' value='A' name='A'><ul><li><input  type='submit'   class='btn-lg' value='-' name='TRUE_A'></li><li><input  type='submit'  class='btn-lg' value='-' name='FALSE_A'></li></ul></li></ul>"""

        mes=mes+"""</form></div></div></div> {% endblock %}"""
        f.write(mes)
        f.write("\n")
        f.close()
        return render_template("indexx.html")
    else:
        f = open('templates/indexx.html','a')
        mes = """<ul><li><input type='submit' class='btn-lg' value='-' name='parent' ></li></ul></form></div></div></div> {% endblock %}"""
        f.write(mes)
        f.write("\n")
        f.close()
        return render_template("indexx.html")
mes=''
xx=0
if __name__=="__main__":

   app.run(debug=True)

   



