from transformers import pipeline

def call_api(prompt:str, options, context):
    pipe = pipeline("text-generation", model="google/gemma-3-270m-it")
    messages = [
        {"role": "user", "content": 
        prompt},
    ]
    output = pipe(messages)
    generated_text = output[0]['generated_text'][1]['content']
    return {
        "output": f"{generated_text}"
    }

