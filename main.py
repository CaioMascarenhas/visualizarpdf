from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/pdfs/<pdf_name>')
def display_pdf(pdf_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, 'pdfs', f'{pdf_name}.pdf')
    return render_template('index.html', pdf_name=pdf_name)

@app.route('/get_pdf/<pdf_name>')
def get_pdf(pdf_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, 'pdfs', f'{pdf_name}.pdf')
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
