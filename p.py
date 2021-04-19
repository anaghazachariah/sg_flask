from flask import Flask 
from flask import render_template,url_for
from flask import request
app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
       # HERE WE HAVE TO READ THE NODE NAME WHICH WE CLICKED AND HAVE TO RETURN A NEW TREE
        
        return render_template("index.html",cv={'A':['B','C']})
    else:
        return render_template("index.html",cv={'A':['-','-']})

if __name__=="__main__":
   app.run()