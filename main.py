import ollama

try:
    ollama.ps()
except:
    raise Exception(
        "Ollama is not running. Make sure to start the Ollama server before running this script by running `ollama serve` in the terminal."
    )

messages = [
    {
        "role": "system",
        "content": "You are a gamemaster in a fantasy world for a text-based RPG.",
    },
    {
        "role": "assistant",
        "content": "You are in a tavern. A group of adventurers are sitting at a table, drinking ale and talking loudly. What do you do?",
    },
]


def chat(message):
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )

    stream = ollama.chat(model="llama3.2:1b", messages=messages, stream=True)
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)


print(messages[1]["content"])

while True:
    command = input("\n> ")
    if command == "exit":
        break
    chat(command)
