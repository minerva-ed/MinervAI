import semantic_kernel as sk  # Import the semantic_kernel library
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion  # Import OpenAIChatCompletion from the semantic_kernel library
from semantic_kernel import PromptTemplateConfig, PromptTemplate, SemanticFunctionConfig  # Import additional classes from semantic_kernel

import random

# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = sk.openai_settings_from_dot_env()  # Retrieve API key and organization ID from a .env file

# Define a class to represent a Student Agent
class StudentAgent:
    def __init__(self, retention_rate, question_rate, educational_background):
        self.retention_rate = retention_rate  # Set the retention rate (e.g., 0.1, 0.2, 0.8)
        self.question_rate = question_rate  # Set the question rate (e.g., 0.1, 0.2, 0.8)
        self.educational_background = educational_background  # Set the educational background (e.g., Liberal Arts, Engineering, Pure Researcher)
        
        self.kernel = sk.Kernel()  # Initialize a semantic kernel
        self.kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-4-1106-preview", api_key, org_id))  # Add OpenAI chat service to the kernel

    # Async method to generate questions from a lecture content
    async def generate_questions(self, lecture_content):
        new_lecture_content = ""  # Initialize a variable to store processed lecture content
        arr = lecture_content.split(".") 
        # Process lecture content
        for line in arr:
            r = random.random()  # Generate a random number
            if r < self.retention_rate:
                new_lecture_content += line + ".\n"  # Add lines to new content based on retention rate

        lecture_content = new_lecture_content  # Update lecture content

        # Create and execute a semantic function to generate questions
        return self.kernel.create_semantic_function(f"""As a student, you went through the following {lecture_content}: Pretend that you are a student with educational background of {self.educational_background}, and have likelihood to ask question of {self.question_rate}. Pretend to be the student described above learning from this lecture, state one succinct clarifying question you have about this lecture and explain to the professor which part of the lecture your confusion originated from, and do not state anything other than the question. If you do not want to ask a question respond by saying -1""", max_tokens=200, temperature=0.5)()

    # Method stub for discuss_with_peer (not implemented)
    async def discuss_with_peer(self, peer, lecture_content):
        pass  # Placeholder for future implementation
