import openai
client = openai.OpenAI(
    api_key="sk-HGL4d86c43a35160e401c9220683f5337679672ba1bc2Qh3",
    base_url="https://api.gptsapi.net/v1" 
)

def chat():
    messages = [{"role": "system", "content": "你是一个有帮助的中文助手。"}]
    print("欢迎使用 ChatGPT（终端版）！输入 exit 退出。\n")

    while True:
        user_input = input("你：")
        if user_input.strip().lower() == "exit":
            print("再见！")
            break

        messages.append({"role": "user", "content": user_input})

        print("助手：", end="", flush=True)

        try:
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                stream=True
            )

            full_reply = ""
            for chunk in stream:
                delta = chunk.choices[0].delta
                if delta.content:
                    print(delta.content, end="", flush=True)
                    full_reply += delta.content

            print()
            messages.append({"role": "assistant", "content": full_reply})

        except Exception as e:
            print(f"\n[错误]：{e}")

if __name__ == "__main__":
    chat()
