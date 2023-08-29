from src.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM


class PredictionPipeline:
    def __init__(self):
        pass

    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(r"trained_model\checkpoint-1500")
        model = AutoModelForSeq2SeqLM.from_pretrained(r"trained_model\checkpoint-1500")

        inputs = tokenizer(text, return_tensors="pt").input_ids
        outputs = model.generate(inputs, max_new_tokens=100, do_sample=False)
        summarized_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return summarized_text