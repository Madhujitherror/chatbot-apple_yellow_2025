# porject config
import google.generativeai as genai
genai.configure(api_key="AIzaSyBp1x0nQUQmyZ1DYwNkIolbY_HHqKl_pak")
apple = genai.GenerativeModel("gemini-2.5-flash")
chat = apple.start_chat(history=[])
print("HI !! I'm Apple the Chatbot")
while True:
    user_input=input("User: ")
    if user_input.lower() == "bye":
        break

    response = chat.send_message(user_input)
    print("Apple  : ",response.text)
