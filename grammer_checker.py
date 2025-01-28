import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

def load_grammer_model():
    """Loads the pre-trained model for grammer correction and hugging face model for tokenizer
    This model loads the T5 model for grammatical error correction
    and retunr Tokenizer , pre trained model , torch_devide"""
    model_name = 'abhinavsarkar/Google-T5-base-Grammatical_Error_Correction-Finetuned-C4-200M-550k'
    torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    return tokenizer,model,torch_device


def correct_grammer(input_text,tokenizer,model,torch_device,num_return_sequences=2):
    batch = tokenizer([input_text], truncation=True, padding='max_length', max_length=64, return_tensors="pt").to(torch_device)
    translated = model.generate(**batch, max_length=64, num_beams=4, num_return_sequences=num_return_sequences, temperature=1.5)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text


