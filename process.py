import tiktoken
import openai

econding = "o200k_base"
tk = tiktoken.get_encoding(econding)
default_prompt = "Without altering the original text, restructure it by dividing it into paragraphs of 100 to 300 words each. Ensure that each paragraph clusters semantically related sentences to enhance coherence and readability."
def count_tokens(text):
    return len(tk.encode(text))

def first_split(text, split_token = 2000):
    lines = text.split("\n")
    lines = [line.strip() for line in lines if line.strip() != ""]
    counts = [count_tokens(line) for line in lines]
    groups = []
    if lines:
        current = lines[0]
        total = counts[0]
        for i in range(1, len(lines)):
            if total + counts[i] < split_token:
                current += f"\n{lines[i]}"
                total += counts[i]
            else:
                groups.append(current)
                current = lines[i]
                total = counts[i]
        groups.append(current)
    return groups

def get_client(endpoint, key):
    if "openai.azure.com" in endpoint:
        return openai.AzureOpenAI(base_url=endpoint, api_key=key, api_version="2024-10-21")
    else:
        return openai.Client(api_key=key)

def split_by_model(text, endpoint, key, model = "gpt-4o-mini"):
    client = get_client(endpoint, key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": default_prompt
            },
            {
                "role": "user",
                "content": text
            }],
        max_tokens= 4000)
    return response.choices[0].message.content

def split_text(text, endpoint, key, model = "gpt-4o-mini", split_token = 2000):
    groups = first_split(text, split_token)
    result = []
    for group in groups:
        result.append(split_by_model(group, endpoint, key, model))
    return "\n".join(result)