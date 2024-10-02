from openai import OpenAI

client = OpenAI(api_key="your api_key")


def translate_to_chinese(text):
    # GPT 모델에 전달할 프롬프트 생성
    prompt = f"Translate the following English sentence to Chinese: \"{text}\""

    # OpenAI API 호출
    response = client.chat.completions.create(model="gpt-3.5-turbo",  # GPT-3.5 모델 사용
    messages=[
        {"role": "system", "content": "You are a helpful assistant who translates English to Chinese."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=100,
    temperature=0.5)

    # 번역된 텍스트 추출
    translated_text = response.choices[0].message.content.strip()
    return translated_text

# 예제 실행
if __name__ == "__main__":
    english_sentence = input("Enter an English sentence to translate: ")
    chinese_translation = translate_to_chinese(english_sentence)
    print("Translated to Chinese:", chinese_translation)
