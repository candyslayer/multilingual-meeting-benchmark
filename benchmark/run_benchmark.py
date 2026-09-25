import json
import os
from tqdm import tqdm
from datasets import load_dataset
from openai import OpenAI

MODEL = "Qwen3-8B"
BASE_URL = "http://localhost:8000/v1"
MAX_SAMPLES = 10
RESULT = "result"

os.makedirs(RESULT, exist_ok=True)

client = OpenAI(base_url=BASE_URL, api_key="EMPTY")

LANGUAGES = {
    "zh": "中文",
    "en": "English",
    "th": "Thai",
    "vi": "Vietnamese",
    "id": "Indonesian",
    "ms": "Malay"
}


def generate(prompt):
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=800
    )
    return r.choices[0].message.content


def meeting_prompt(text, language):
    return f"""
You are a professional international meeting secretary.

Generate meeting minutes in {LANGUAGES[language]}.

Requirements:
- Preserve decisions and action items.
- Use natural local business expression.
- Do not translate word by word.

Transcript:
{text}

Meeting minutes:
"""


def run_meetingbank():
    ds = load_dataset("huuuyeah/MeetingBank")
    split = "test" if "test" in ds else "train"
    data = ds[split].select(range(min(MAX_SAMPLES, len(ds[split]))))

    all_result = {}

    for lang in LANGUAGES:
        results = []
        for item in tqdm(data, desc=lang):
            output = generate(
                meeting_prompt(item["transcript"], lang)
            )
            results.append({
                "language": lang,
                "source": item["transcript"],
                "prediction": output
            })

        all_result[lang] = results

    with open(
        f"{RESULT}/meeting_predictions.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(all_result, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    run_meetingbank()
