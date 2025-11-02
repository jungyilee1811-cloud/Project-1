import json 
import os 
import requests 
import time

FILE_NAME="facts.json" 
def load_facts(): 
    if not os.path.exists(FILE_NAME): 
        return [] 
    with open(FILE_NAME, "r", encoding="utf-8") as f: 
        return json.load(f) 
def save_facts(facts):
    with open(FILE_NAME, "w", encoding="utf-8") as f: 
        json.dump(facts, f, indent=4, ensure_ascii=False) 
def add_fact(new_fact, source="uselessfacts.jsph.pl"): 
    facts = load_facts() 
    for fact in facts: 
        if fact["text"] == new_fact: 
            print(" This fact already exists.") 
            return False 
    facts.append({"text": new_fact, "source": source}) 
    save_facts(facts) 
    print("New fact added.") 
    return True 
def get_fact_from_api(): 
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random" 
    response = requests.get(url) 
    if response.status_code == 200: 
        return response.json()["text"]
    return None 
def main_code():
  if __name__ == "__main__":  
      new_fact = get_fact_from_api() 
      if new_fact: 
          add_fact(new_fact) 
      else: 
          print(" Failure to get fact.") 
          print("\n Current database content：") 
  all_facts = load_facts() 
  i = 1
  for fact in all_facts:
      print(str(i) + ". " + fact["text"])
      i = i + 1
while True:
  main_code()
  time.sleep(20)
  
