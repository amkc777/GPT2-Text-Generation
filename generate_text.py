import warnings
# Suppress warnings that may arise from using certain libraries
warnings.filterwarnings("ignore")

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 tokenizer and model
# The tokenizer converts text into a format suitable for the model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# The model generates text based on input tokens. 
# Here, we set pad_token_id to the end-of-sequence token to avoid padding issues.
model = GPT2LMHeadModel.from_pretrained('gpt2', pad_token_id=tokenizer.eos_token_id)

# Define the input sequence (prompt) for text generation
sequence = "What is AI?"

# Tokenize the input sequence and convert it into PyTorch tensors
# return_tensors='pt' indicates that we want the output in PyTorch tensor format
inputs = tokenizer.encode(sequence, return_tensors='pt')

# Generate text using the model
# - inputs: the tokenized input sequence
# - max_length: the maximum length of the generated sequence
# - do_sample: whether to sample from the model or choose the most likely token
# - num_beams: number of beams for beam search (higher values lead to better quality but longer processing time)
# - no_repeat_ngram_size: prevents the model from repeating any n-grams of this size (set to 2 for bi-grams)
# - early_stopping: stop generation when a satisfactory output is produced
outputs = model.generate(
    inputs, 
    max_length=400, 
    do_sample=True, 
    num_beams=5, 
    no_repeat_ngram_size=2, 
    early_stopping=True
)

# Decode the generated token IDs back into a human-readable string
# skip_special_tokens=True removes special tokens like <eos> from the output
text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print the generated output
print(text)
