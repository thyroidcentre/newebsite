from flask import Flask, render_template
from constants import Constants
app = Flask(__name__)

@app.context_processor
def inject_constants():
    return dict(constants=Constants)
    
@app.route('/')
def home():
    return render_template('index.html')  
@app.route('/about-us/')
def about():
    return render_template('about.html') 
@app.route('/services/')
def services():
    return render_template('service.html') 
@app.route('/contact-us/')
def contact():
    return render_template('contact.html') 
@app.route('/services/4-scarless-thyroidectomy/')
def scarless_thyroidectomy():
    return render_template('scarless_thyroidectomy.html') 
@app.route('/services/goiter/')
def goiter():
    return render_template('goiter.html') 
@app.route('/services/graves/')
def graves():
    return render_template('graves.html') 
@app.route('/services/hyperparathyroidism/')
def hyperparathyroidism():
    return render_template('hyperparathyroidism.html') 
@app.route('/services/microwave-and-radiofrequency-ablation/')
def microwave_and_radiofrequency_ablation():
    return render_template('microwave_and_radiofrequency_ablation.html') 
@app.route('/services/thyroid-cancer/')
def thyroid_cancer():
    return render_template('thyroid_cancer.html') 
@app.route('/services/thyroid-surgery/')
def thyroid_surgery():
    return render_template('thyroid_surgery.html') 
@app.route('/services/toxic-nodule/')
def toxic_nodule():
    return render_template('toxic_nodule.html')
@app.route('/doctor/siddhartha-chakravarthy/')
def siddhartha_chakravarthy():
    return render_template('doctor1.html') 
@app.route('/doctor/samantha-satyakumar/')
def samantha_satyakumar():
    return render_template('doctor2.html')  
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)  
