import choral_explanation
import json
import os

TIP_UUID = 'dbc665a4-5364-468c-8bbc-e48790f3907e'
DIR_PATH = f"target/tip"

raw_data = choral_explanation.fetch_question_data(TIP_UUID)

os.makedirs(f"{DIR_PATH}", exist_ok=True)

with open(f"{DIR_PATH}/raw-data.json", 'w', encoding='utf8') as file:
	json.dump(raw_data, file, indent=2, ensure_ascii=False)
	file.write("\n")
