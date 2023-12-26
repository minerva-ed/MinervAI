import semantic_kernel as sk  # Import the semantic_kernel library
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion  # Import OpenAIChatCompletion from the semantic_kernel library
from semantic_kernel import PromptTemplateConfig, PromptTemplate, SemanticFunctionConfig  # Import additional classes from semantic_kernel

# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = sk.openai_settings_from_dot_env()  # Retrieve API key and organization ID from a .env file

# Define a class to represent a Professor Agent
class ProfessorAgent:
    def __init__(self):
        self.lecture_notes = None  # Initialize lecture_notes attribute to None
        self.kernel = sk.Kernel()  # Initialize a semantic kernel
        self.kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))  # Add OpenAI chat service to the kernel

    # Method to upload lecture notes
    def upload_lecture_notes(self, notes):
        self.lecture_notes = notes  # Set the lecture_notes attribute

    # Async method to answer a question
    async def answer_question(self, question):
        # Create and execute a semantic function to provide an answer
        return self.kernel.create_semantic_function(f"""Provide a detailed answer to the following question received after the following lecture {self.lecture_notes}: {question}? Answer concisely.""", temperature=0.8)()

    # Async method to give a lecture
    async def give_lecture(self):
        if self.lecture_notes:
            # Create and execute a semantic function to give a lecture transcript
            return self.kernel.create_semantic_function(f"""Give a transcript of a detailed lecture (just the first 5 minutes (around 250 words)), using the following notes in LaTeX, with appropriate fillers to make the lecture engaging: {self.lecture_notes}. MAKE SURE THAT WHEN YOU ARE using math expressions, use $$math$$ notation and not $$math$$.""", max_tokens=1024)()
        else:
            throw("No lecture notes uploaded")  # Throw an error if no lecture notes are uploaded
