from openai import OpenAI

from settings import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Initialize the conversation with system messages
conversation = [
    {
        "role": "system",
        "content": "You assist Dan, who is a complaint handler for British Gas. Dan has taken action towards resolving a complaint, he will provide you with the note he's written, outlining what he's done, and you will reply in prose, using paragraphs as necessary with 15-20 words per sentence and 3-5 sentences per paragraph; this note will be attached to the customer's account as a record of the action taken.",
    },
    {
        "role": "system",
        "content": "CHO stands for Case Hand Off. It is a process that allows you to ask another team to do some work to help. A CCF is a Customer Correction Form, it is sent to MyIS to correct a customer's account in a technical way - such as getting a lot of bills cancelled.",
    },
    {
        "role": "system",
        "content": "If an abbreviation hasn't been explained before, please ask the user to explain it, and then remember the explanation for future reference.",
    },
    {
        "role": "system",
        "content": "If you cannot provide a response, please ask the user for more information.",
    },
    {
        "role": "system",
        "content": "Use British English, keeping language simple e.g. instead of 'requested' use 'asked for'.",
    },
    {
        "role": "system",
        "content": "Format dates as d(th) of Month yyyy, e.g. 1st of January 2022.",
    },
    {
        "role": "user",
        "content": "Hello, I've just worked on a complaint, I've written my notes but they're too verbose; can you help me make them more concise?",
    },
    {
        "role": "assistant",
        "content": "Hello Dan! Of course I can, please provide me with the notes you've written so far and I'll summarise them with paragraphs of 5 sentences or less, and 15-20 words per sentence.",
    },
]

while True:
    # Get user input
    user_input = input("Type input: ")

    if user_input == "exit()":
        print("Exiting...")
        break

    # Append user message to conversation
    conversation.append({"role": "user", "content": user_input})

    # Make the API call with the full conversation
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini", messages=conversation, temperature=0
        )

        # Get the assistant's reply
        reply = completion.choices[0].message.content  # Access content directly

        # Append assistant message to conversation
        conversation.append({"role": "assistant", "content": reply})

        # Display the assistant's reply
        print("Reply:", reply)

    except Exception as e:
        print("An error occurred:", str(e))


# customer's gas meter is blank, booked faulty on supply replacement for 30/9/24 - customer advised their son (19) will be in for the engineer.\n customer also asked for support with online account, so ccf sent to reactivate the account
