from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from src.entity import ModelTrainerConfig
import torch
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_tf = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_ckpt
        ).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=self.config.model_ckpt)

        # loading data
        dataset_BBC_pt = load_from_disk(self.config.data_path)

        training_args = Seq2SeqTrainingArguments(
            output_dir="self.config.root_dir",
            evaluation_strategy="epoch",
            # learning_rate=2e-3,
            per_device_train_batch_size=20,
            weight_decay=0.01,
            save_total_limit=3,
            num_train_epochs=1,
            # predict_with_generate=True,
        )

        trainer = Seq2SeqTrainer(
            model=model_tf,
            args=training_args,
            train_dataset=dataset_BBC_pt["train"],
            eval_dataset=dataset_BBC_pt["validation"],
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
        )

        trainer.train()

        ## Save model
        model_tf.save_pretrained(
            os.path.join(self.config.root_dir, "SummarizerModel")
        )
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
