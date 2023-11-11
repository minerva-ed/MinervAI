#### RUN THIS TO INSTALL PKGS ########
# python -m pip install semantic-kernel
######################################

# Import necessary packages
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel import PromptTemplateConfig, PromptTemplate, SemanticFunctionConfig


# Initialize the kernel
kernel = sk.Kernel()
# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))



# Define prompts
class ProfessorAgent:
    def __init__(self, expertise_area):
        self.expertise_area = expertise_area
        self.lecture_notes = None

    def upload_lecture_notes(self, notes):
        self.lecture_notes = notes

    async def answer_question(self, question):
        return kernel.create_semantic_function(f"""Provide a detailed answer to the following question in the context of {self.expertise_area}: {question}""")()

    async def give_lecture(self, topic):
        if self.lecture_notes:
            # Incorporating lecture notes into the lecture generation
            return kernel.create_semantic_function(f"""Give a detailed lecture on {topic} related to {self.expertise_area}, using the following notes: {self.lecture_notes}.""", max_tokens=200)()
        else:
            # Default lecture generation without notes
            return kernel.create_semantic_function(f"""Give a detailed lecture on {topic} related to {self.expertise_area}.""", max_tokens=150)()

class StudentAgent:
    def __init__(self, knowledge_level, personality_type):
        self.knowledge_level = knowledge_level
        self.personality_type = personality_type

    async def generate_questions(self, lecture_content):
        return kernel.create_semantic_function(f"""Given your knowledge level of {self.knowledge_level} and personality type {self.personality_type}, state one question you have about this lecture: {lecture_content}:""")()

    async def discuss_with_peer(self, peer, lecture_content):
        # This function simulates discussion between two students
        pass

# Main simulation function
async def simulate_classroom():

    # Create Professor and Student Agents
    professor = ProfessorAgent("Mathematics")
    students = [StudentAgent("partial", "introverted"), StudentAgent("partial", "extroverted")]

    # Example: Upload lecture notes
    professor.upload_lecture_notes("Here are some key points and concepts about Groups, Rings, and Fields...")

    # Simulate classroom interaction
    lecture_topic = "Groups, Rings, Fields"
    lecture_content = await professor.give_lecture(lecture_topic)
    print(lecture_content)
    for student in students:
        print("Looking at student:", student)
        question = await student.generate_questions(lecture_content)
        print("Question:", question)
        answer = await professor.answer_question(question)
        print("Answer:", answer)
        # Log the interaction for analysis

    # Simulate break time interaction
    # for i in range(len(students)):
    #     for j in range(i + 1, len(students)):
    #         await students[i].discuss_with_peer(students[j], lecture_content)
            # Log the interaction for analysis

# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(simulate_classroom())