from flask import Flask , render_template, request
from models import short_line,medium_line,long_line
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__) 

@app.route("/")
def root():
    return render_template("root.html")

@app.route("/models")
def models():
    return render_template("models.html")

@app.route("/shortline",methods = ['POST','GET'])
def shortline():
    if request.method=='GET':
        return render_template("shortline.html")
    else:
        output = short_line(request.form)
        return render_template("result.html",output=output)
        
@app.route("/mediumline",methods = ['POST','GET'])
def mediumline():
    if request.method=='GET':
        return render_template("mediumline.html")
    else:
        output = medium_line(request.form)
        return render_template("result.html",output=output)

@app.route("/longline",methods = ['POST','GET'])
def longline():
    if request.method=='GET':
        return render_template("longline.html")
    else:
        output = long_line(request.form)
        return render_template("result.html",output=output)

    
@app.route("/result",methods = ['POST'])
def result():
    output = request.form
    html = render_template("result_pdf.html",output=output)
    return render_pdf(HTML(string=html))
            
                
if __name__ == "__main__":
    #app.run(host='0.0.0.0',port=2000)
    app.run(debug='true')

