from flask import Flask 
import webbrowser
from flask import render_template,url_for
from flask import request
app=Flask(__name__)
def to_strings(dic1,dic2,key,msg):

    if key==1:
        msg=msg+f""" <ul><li><input  type='submit'  class='btn-lg' value={dic1[key]} name={dic1[key]}>"""
        msg=msg+"""<ul>"""
        key_val=dic2[key]
        for i in range(0,len(key_val)):
            x=key_val[i][0]
            y=key_val[i][1]
            if x not in dic2.keys():
                if i==0:
                    child="""True"""
                else:
                    child="""False"""
                msg=msg+f"""<li><input  type='submit'   class='btn-lg' value='-' name='{child}_{dic1[key]}'></li>"""
            else:
                to_strings(dic1,dic2,x,msg)
        msg=msg+"""</ul></li></ul"""
    else:
        msg=msg+f"""<li><input  type='submit'  class='btn-lg' value={dic1[key]} name={dic1[key]}>"""
        msg=msg+"""<ul>"""
        key_val=dic2[key]
        for i in range(0,len(key_val)):
            x=key_val[i][0]
            y=key_val[i][1]
            if x not in dic2.keys():
                if i==0:
                    child="""True"""
                else:
                    child="""False"""
                msg=msg+f"""<li><input  type='submit'   class='btn-lg' value='-' name='{child}_{dic1[key]}'></li>"""
            else:
                to_strings(dic1,dic2,x,msg)
        msg=msg+"""</ul></li></ul"""
    return msg
@app.route("/",methods=["POST","GET"])
def home():
    global mes
    global xx
    global msg
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
        #from backend
        venki_l1={1:'A',2:'-',3:'-'}#1 should be root
        venki_k2={1:[[2,'True'],[3,'False']]}
        mes=to_strings(venki_l1,venki_k2,1,msg)
        mes=mes+"""</form></div></div></div> {% endblock %}"""

        
        f = open('templates/indexx.html','a')
        f.write(mes)
        f.write("\n")
        f.close()
        return render_template("indexx.html")
    else:
        f = open('templates/indexx.html','a')
        mes = """<ul><li><input  type='submit'  class='btn-lg' value='-' name='p'></li></ul></form></div></div></div> {% endblock %}"""
        f.write(mes)
        f.write("\n")
        f.close()
        return render_template("indexx.html")
mes=''
msg=''
xx=0
if __name__=="__main__":

   app.run(debug=True)

   