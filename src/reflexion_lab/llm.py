import os
import json
import time
from typing import Any, Dict, List, Optional, Tuple
import tiktoken
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def call_llm(
    system_prompt: str, 
    user_prompt: str, 
    model: str = "gpt-4o-mini",
    response_format: Optional[Dict] = None
) -> Tuple[str, int, float]:
    start_time = time.time()
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    print(f"[LLM] Calling {model} with system prompt: {system_prompt[:50]}...")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        response_format=response_format,
        temperature=0
    )
    content = response.choices[0].message.content
    print(f"[LLM] Received {len(content)} chars")
    latency = (time.time() - start_time) * 1000
    
    # Actual tokens from response
    tokens = response.usage.total_tokens
    
    return content, tokens, latency
