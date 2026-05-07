from app.graph import graph

def run():
    print("Smart study assistant")

    while True:

        question = input("Enter your question (or 'exit' to quit): ")

        if question.lower() == "exit":
            break

        # Here you would typically process the question and get an answer
        # For now, we'll just print the question
        print(f"You asked: {question}")

        result = graph.invoke({
            "question": question,
            "question_type": "",
            "answer": ""})

        print('\n')
        print(f"Question type which you have asked: {result['question_type']}")

        print('\n')

        print(f"Answer: {result['answer']}")

if __name__ == "__main__":
    run()