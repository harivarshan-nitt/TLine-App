from flask import Flask , render_template, request
from models import compute
from flask_weasyprint import HTML, render_pdf
from form_validate import validate

app = Flask(__name__) 

@app.route("/")
def root():
    return render_template("root.html")

@app.route("/models")
def models():
    return render_template("models.html")

@app.route("/shortline",methods = ['POST','GET'])
def shortline():
    errors = []
    if request.method=='GET':
        return render_template("shortline.html",errors = errors)
    else:
        error_bool =  validate(request.form)      
        if  error_bool== False:
            output,plot= compute(request.form)
            return render_template("result.html",output=output,plot=plot)
        else:
            errors.append("PROVIDE VALID INPUT")
            return render_template("shortline.html",errors = errors)

        
@app.route("/mediumline",methods = ['POST','GET'])
def mediumline():
    errors = []
    if request.method=='GET':
        return render_template("mediumline.html",errors = errors)
    else:
        error_bool =  validate(request.form)      
        if  error_bool== False:
            output,plot= compute(request.form)
            return render_template("result.html",output=output,plot=plot)
        else:
            errors.append("PROVIDE VALID INPUT")
            return render_template("mediumline.html",errors = errors)

@app.route("/longline",methods = ['POST','GET'])
def longline():
    errors = []
    if request.method=='GET':
        return render_template("longline.html",errors = errors)
    else:
        error_bool =  validate(request.form)      
        if  error_bool== False:
            output,plot= compute(request.form)
            return render_template("result.html",output=output,plot=plot)
        else:
            errors.append("PROVIDE VALID INPUT")
            return render_template("longline.html",errors = errors)

@app.route("/result",methods = ['POST'])
def result():
    output = request.form
    html = render_template("result_pdf.html",output=output)
    return render_pdf(HTML(string=html))
                
if __name__ == "__main__":
    app.run()

