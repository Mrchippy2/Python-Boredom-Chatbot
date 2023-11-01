import random

modes = {
    "jokes": ["A guy is sitting at home when he hears a knock at the door. He opens the door and sees a snail on the porch."
              "He picks up the snail and throws it as far as he can. Three years later there’s a knock on the door. He opens"
              "it and sees the same snail." "The snail says: ‘What the hell was that all about?’",

              "A guy shows up late for work. The boss yells, ‘You should’ve been here at 8.30!’ He replies. ‘Why? What happened at 8.30?’",

              "China has a population of a billion people. One billion. That means even if you’re a one in a million kind of guy, there are still a thousand others exactly like you.",

              "A woman gets on a bus with her baby. The bus driver says: “Ugh, that’s the ugliest baby I’ve ever seen!” The woman walks to the rear of the bus and sits down, fuming."
              "She says to a man next to her: “The driver just insulted me!” The man says: “You go up there and tell him off. Go on, I’ll hold your monkey for you.”",

              "I said to the Gym instructor “Can you teach me to do the splits?” He said, “How flexible are you?” I said, “I can’t make Tuesdays.”",

              "Police arrested two kids yesterday, one was drinking battery acid, the other was eating fireworks. They charged one – and let the other one off.",

              "I was having dinner with Garry Kasporov (world chess champion) and there was a check tablecloth. It took him two hours to pass me the salt.",

              "I was in my car driving back from work. A police officer pulled me over and knocked on my window. I said, ‘One minute I’m on the phone.’",

              "Life is like a box of chocolates. It doesn’t last long if you’re fat.",

              "If I was an Olympic athlete, I’d rather come in last than win the silver medal. You win the gold, you feel good. You win the bronze, you think,"
              "‘at least I got something.’ But you win that silver, that’s like, ‘Congratulations, you almost won! Of all the losers, you came in first! You’re"
              "the number one loser! No one lost ahead of you!",
              ],


    "facts": ["The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",

              "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",

              "The average person will spend six months of their life waiting for red lights to turn green.",

              "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",

              "Cherophobia is the word for the irrational fear of being happy.",

              "You can hear a blue whale's heartbeat from two miles away.",

              "Nearly 30,000 rubber ducks were lost at sea in 1992 and are still being discovered today.",

              "The inventor of the frisbee was turned into a frisbee after he died.",

              "Roosters have built-in earplugs.",

              "The Netherlands is so safe, it imports criminals to fill jails.",
              ],


    "riddles": [
        {
            "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "answer": "An echo.",
            "repeated": False,
        },
        {
            "question": "The more you take, the more you leave behind. What am I?",
            "answer": "Footsteps.",
            "repeated": False,
        },
        {
            "question": "What has to be broken before you can use it?",
            "answer": "Egg.",
            "repeated": False,
        },
        {
            "question": "I’m tall when I’m young, and I’m short when I’m old. What am I?",
            "answer": "Candle.",
            "repeated": False,
        },
        {
            "question": "What month of the year has 28 days?",
            "answer": "All of Them.",
            "repeated": False,
        },
        {
            "question": "What is full of holes but still holds water?",
            "answer": "Sponge.",
            "repeated": False,
        },
        {
            "question": "What is always in front of you but can’t be seen?",
            "answer": "Future.",
            "repeated": False,
        },
        {
            "question": "There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?",
            "answer": "There aren’t any—it’s a one-story house.",
            "repeated": False,
        },
        {
            "question": "What can you break, even if you never pick it up or touch it?",
            "answer": "Promise.",
            "repeated": False,
        },
        {
            "question": "What goes up but never comes down?",
            "answer": "Age.",
            "repeated": False,
        },
    ],
    "quotes": ["In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
               "The only way to do great work is to love what you do. - Steve Jobs"],
}

def add_response(mode, response):
    modes[mode].append(response)

def get_response(mode):
    if not modes[mode]:
        return f"I don't have any {mode} responses in this mode yet."
    if mode == "riddles":
        if "current_riddle" not in modes:
            modes["current_riddle"] = 0
        current_riddle = modes["current_riddle"]
        riddle = modes["riddles"][current_riddle]
        if "answered" in riddle and riddle["answered"]:
            return f"Bot: {riddle['answer']} Type 'next' for the next riddle."
        else:
            return f"Bot: {riddle['question']} Type 'next' to see the answer."
    elif mode in ["jokes", "facts", "quotes"]:
        if f"current_index_{mode}" not in modes:
            modes[f"current_index_{mode}"] = 0
        current_index = modes[f"current_index_{mode}"]
        response = modes[mode][current_index]
        modes[f"current_index_{mode}"] = (current_index + 1) % len(modes[mode])
        return f"Bot: {response} Type 'exit' to end the conversation."

def chat_with_bot():
    conversation_history = []
    while True:
        user_input = input("You: ")
        conversation_history.append(f"You: {user_input}")

        if user_input.lower() == "exit":
            print("Bot: Goodbye! Have a great day.")
            break

        if user_input.lower() in modes:
            mode = user_input.lower()
            response = get_response(mode)
            conversation_history.append(response)
            print(response)
        elif user_input.lower() == "next":
            if "current_riddle" in modes:
                current_riddle = modes["current_riddle"]
                riddle = modes["riddles"][current_riddle]
                if "answered" in riddle and riddle["answered"]:
                    modes["current_riddle"] += 1
                    if modes["current_riddle"] < len(modes["riddles"]):
                        response = get_response("riddles")
                        conversation_history.append(response)
                        print(response)
                    else:
                        conversation_history.append("Bot: That's all for the riddles. Type 'exit' to end the conversation.")
                        print("Bot: That's all for the riddles. Type 'exit' to end the conversation.")
                else:
                    riddle["answered"] = True
                    conversation_history.append(f"Bot: The answer is '{riddle['answer']}'. Type 'next' for the next riddle.")
                    print(f"Bot: The answer is '{riddle['answer']}'. Type 'next' for the next riddle.")
            else:
                conversation_history.append("Bot: There are no riddles to show.")
                print("Bot: There are no riddles to show.")
        else:
            print("Bot: I don't understand. You can switch modes or type 'exit' to end the conversation.")

if __name__ == "__main__":
    print("Bot: Hello! You can chat with me or switch modes by typing 'jokes', 'facts', 'riddles', 'quotes', or 'exit'.")
    chat_with_bot()