from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def survey():
    return render_template_string(open("survey.html").read())

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    print("Survey Response Received:")
    for key, value in data.items():
        print(f"{key}: {value}")
    
    return "Thank you for submitting the survey!"

if __name__ == '__main__':
    app.run(debug=True)
