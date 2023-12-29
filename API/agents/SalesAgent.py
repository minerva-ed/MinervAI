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
        self.kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-4-1106-preview", api_key, org_id))  # Add OpenAI chat service to the kernel
        self.transcript = ""
    # Method to upload lecture notes
    def upload_sales_profile(self, notes):
        self.sales_notes = notes  # Set the lecture_notes attribute

    # Async method to answer a question
    async def answer_question(self, customers, questions):
        # Set the timeout for the operation
        prompt = f"""Provide a detailed answer to the following questions from your customers.

        {".".join([f'''{num + 1}. {customer.company_name} described as "{customer.description}": {questions[num]}''' for num, customer in enumerate(customers)])}
        
        Answer concisely, making use of the sales description document provided below. \n {self.sales_notes}. If you deem additional information might be benefitial, still provide the answer but use [[placeholder]] to indicate that there is required information that is not provided in the notes. Otherwise, indicate which section of the sales_notes you use for each sentence of your answer like [[section #]]. MAKE SURE TO DO THIS, as a lack of reference to the section will be invalid.
        
        Furthermore, return your response formatted as an array, answering each questions ["answer1", "answer2", ...] in valid JSON starting with '[' and ending with ']'."""
        print("SALES prompt:", prompt)
        semantic_function = self.kernel.create_semantic_function(
            prompt, max_tokens=1024
        )
        result = await self.kernel.run_async(
            semantic_function)
        result = result.result.strip('```\njson\n').strip('```') # removes quotes and character "json" from openai json response
        return result
    async def give_sales(self):
        if self.sales_notes:
            # Create and execute a semantic function to give a lecture transcript
            sk = self.kernel.create_semantic_function(f"""Give a transcript of a detailed sales (just the first 5 minutes (around 250 words)), using the following notes, with appropriate fillers to make the sales pitch engaging: {self.sales_notes}.""", max_tokens=1024)
            result = await self.kernel.run_async(
                sk
            )
            self.transcript = result
            return result
        else:
            throw("No sales notes uploaded")  # Throw an error if no lecture notes are uploaded
