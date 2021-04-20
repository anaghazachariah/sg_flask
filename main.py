from flask import Flask 
from flask import render_template,url_for
from flask import request
app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        x=(request.form)
        for i in x:
            button_clicked=i#NODE WHICH WE CLICKED
        print(button_clicked)
        return render_template("index.html",cv={'A':['B','C'],'D':['BA','CA']})
    else:
        return render_template("index.html",cv={'A':['-','-']})

if __name__=="__main__":
   app.run()