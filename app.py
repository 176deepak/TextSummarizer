from flask import (Flask, render_template, request)
from src.pipeline.prediction_pipeline import PredictionPipeline


app =Flask(__name__)

pred_obj = PredictionPipeline()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    
        text = str(request.form.get('inputText'))
        text = "summarize: " + text
        summarized_text = pred_obj.predict(text)
    
        return render_template('index.html', input_data=text, summarized_text=summarized_text)    
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)