from sqlassistant import ask_question
print("SQL Assistant Ready (type 'exit' to quit)\n")

while True:
    question = input("You: ")
    if question.lower().strip() == "exit":
        print("Goodbye!")
        break

    answer = ask_question(question)
    print("Answer:", answer)