from flask import (Flask, render_template, request, url_for)
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

app =Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained(r"trained_model\checkpoint-1500")
model = AutoModelForSeq2SeqLM.from_pretrained(r"trained_model\checkpoint-1500")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = str(request.form.get('inputText'))
        inputs = tokenizer(text, return_tensors="pt").input_ids
        outputs = model.generate(inputs, max_new_tokens=100, do_sample=False)
        summarized_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return render_template('index.html', summarized_text=summarized_text)    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)