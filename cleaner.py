# utils.py
import re
import os

def clean_description(text):
    if not text: return ""
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[•▪►✓*]+', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')