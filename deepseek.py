import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Access them like this
API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env file!")




def deepseek(cv, jd, api_key = API_KEY):
    
    client = OpenAI(
        api_key = api_key,
        base_url="https://api.deepseek.com"
    )
    
    # Strict instructions to output ONLY the score
    system_prompt = """You are an expert ATS scoring system. Evaluate the match between the CV and the Job Description.
    You must output a JSON object containing exactly one key: "score". 
    The value must be an integer from 0 to 100 representing the similarity percentage.
    Example output: {"score": 82}"""
    
    user_prompt = f"CV Text:\n{cv}\n\nJob Description:\n{jd}"
    
    try:
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={'type': 'json_object'},
            temperature=0.0  # Set to 0 for maximum consistency and less "creativity"
        )
        
        # Parse the JSON and return just the integer
        result = json.loads(response.choices[0].message.content)
        return int(result.get("score", 0))
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
