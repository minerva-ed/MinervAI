#### RUN THIS TO INSTALL PKGS ########
# python -m pip install semantic-kernel
######################################
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

# Initialize the kernel
kernel = sk.Kernel()
# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

# Define prompts
class LectureAgent:
    give_lecture = kernel.create_semantic_function("""Give a very concise lecture on {{$INPUT}}""", max_tokens=100)
    ask_question = kernel.create_semantic_function("""Answer the following question given to your lecture: {{$INPUT}}""")
class StudentAgent:    
    generate_questions = kernel.create_semantic_function("""Do you have any questions on the following lecture? Do you not undersand or need more clearity on anything? {{$INPUT}}""")

    load_question_answer = kernel.create_semantic_function("""Read the following question and answer carefully, and make sure you understand: {{$INPUT}}""")





async def main():
    input_doc = ["Groups", "Rings", "Fields"]
    for section in input_doc:
        context = kernel.CreateNewContext(input_doc)
        lecture = LectureAgent.give_lecture(context)
        print(lecture)

        question = StudentAgent.generate_questions(context)
        print(question)

        answer = LectureAgent.ask_question(question)
        print(answer)

        loaded = StudentAgent.load_question_answer((question, answer))
        print(loaded)





# Run the main function
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())