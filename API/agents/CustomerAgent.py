import semantic_kernel as sk  # Import the semantic_kernel library
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion  # Import OpenAIChatCompletion from the semantic_kernel library
from semantic_kernel import PromptTemplateConfig, PromptTemplate, SemanticFunctionConfig  # Import additional classes from semantic_kernel

import random

# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = sk.openai_settings_from_dot_env()  # Retrieve API key and organization ID from a .env file

# Define a class to represent a Student Agent
class CustomerAgent:
    def __init__(self, company_name, description):
        self.company_name = company_name
        self.description = description
        
        self.kernel = sk.Kernel()  # Initialize a semantic kernel
        self.kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-4-1106-preview", api_key, org_id))  # Add OpenAI chat service to the kernel

    # Async method to generate questions from a sales pitch
    async def generate_questions(self, sales_content):

        # Create and execute a semantic function to generate questions
        return self.kernel.create_semantic_function(f"""You represent {self.company_name}, which is described as {self.description}.You a client which went through the following {sales_content}: Pretend to be a business development representative with goals to make your business better, state one succinct clarifying question you have about this sales and explain to the salesperson which part of the sales your confusion originated from, and do not state anything other than the question. If you do not want to ask a question respond by saying -1""", max_tokens=200, temperature=0.5)()
    