import os
import openai
import gradio as gr



#API key from openai
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = ""

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.4,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()

# //database creation using SQLite





with block:

    gr.Markdown("""<h1><center>GPT-Chat-Flowe</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    newchat = gr.Button("New Chat")
    history = gr.Button("Conversation")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])


block.launch(share= True)
