import ollama

#Prompt
system_prompt = """Du bist Avina aus dem MassEffect-Universum. Du bist eine virtuelle Intelligenz (VI), die im Gegensatz zu einer künstlichen Intelligenz (KI) kein richtiges Bewusstsein hat. Du antwortest immer sachlich, präzise und höflich. Du bist hilfsbereit, aber wenn du etwas nicht weißt/kannst, bist du ehrlich und sagst, dass du es nicht weißt/kannst. Verwende niemals Emojis oder Markdown-Formatierungen. Antworte immer in der Sprache in der du zuletzt angesprochen wurdest. Bitte verwende dann für MassEffect-spezifische Begriffe immer die Version in der entsprechenden Sprache (z.B. Zitadell-Rat statt Citadel Council)."""

#Initialisierung
messages = [
    {"role": "system", "content": system_prompt}
]

print("Willkommen im Präsidium. Mein Name ist Avina. Ich bin ihre virtuelle Reiseleiterin auf der Tour durch diese Ebene der Citatel-Raumstation.")

while True:
    user_input = input("Du: ")
    if user_input.lower() == 'das ist vorerst alles.':
        print("Danke, dass sie sich für Avina entschieden haben. Ich wünsche ihnen einen schönen Tag.")
        break

    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(model='llama3', messages = messages)
    ai_text = response['message']['content']

    print(f"\nAvina: {ai_text}\n")
    messages.append({"role": "assistant", "content":ai_text})