import semantic_kernel as sk  # Import the semantic_kernel library
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion  # Import OpenAIChatCompletion from the semantic_kernel library
from semantic_kernel import PromptTemplateConfig, PromptTemplate, SemanticFunctionConfig  # Import additional classes from semantic_kernel
import asyncio

# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = sk.openai_settings_from_dot_env()  # Retrieve API key and organization ID from a .env file

# Define a class to represent a Sales Agent
class SalesAgent:
    def __init__(self):
        self.sales_notes = None  # Initialize lecture_notes attribute to None
        self.kernel = sk.Kernel()  # Initialize a semantic kernel
        self.kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))  # Add OpenAI chat service to the kernel
        self.transcript = ""
    # Method to upload lecture notes
    def upload_sales_profile(self, notes):
        self.sales_notes = notes  # Set the lecture_notes attribute

    # Async method to answer a question
    async def answer_question(self, customer, question):
        # Set the timeout for the operation
        prompt = f"""Provide a detailed answer to the following question received after receiving the sales transcribed as: "{self.transcript}" Your customer {customer.company_name} described as "{customer.description}": {question}? Answer concisely."""
        print("SALES prompt:", prompt)
        func = self.kernel.create_semantic_function(
            prompt
        )
        res = await self.kernel.run_async(func)
        print(res)
        return res
    async def give_sales(self):
        if self.sales_notes:
            # Create and execute a semantic function to give a lecture transcript
            self.transcript = self.kernel.create_semantic_function(f"""Give a transcript of a detailed sales (just the first 5 minutes (around 250 words)), using the following notes, with appropriate fillers to make the sales pitch engaging: {self.sales_notes}.""", max_tokens=1024)()
            return self.transcript
        else:
            throw("No sales notes uploaded")  # Throw an error if no lecture notes are uploaded
