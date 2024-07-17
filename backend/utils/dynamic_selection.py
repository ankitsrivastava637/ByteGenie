from difflib import SequenceMatcher
from utils.few_shot_examples import few_shot_examples

def select_few_shot_examples(query):
    def similarity(a, b):
        return SequenceMatcher(None, a, b).ratio()
    
    selected_examples = sorted(few_shot_examples, key=lambda x: similarity(query, x["input"]), reverse=True)
    return selected_examples[:3]  # Select top 3 most similar examples
