from flask import Flask #import the Flask object from the flask package
from flask import render_template#for rendering html page
app=Flask(__name__)#creating your Flask application instance with the name app

@app.route("/")#pass '/' to signify that this function respond to main URL
def home():
    return render_template("index.html",process_list="RCG",table_list="RCG,MI,E2K,PRC",antecedent="NOT_PEC_AND_QTZ_SOURCE_APPN_IDS",consequent="SECONDBIT=_APP_ORGIN_RCG")#connects with html page
if __name__=="__main__":
   app.run()#run the development server.