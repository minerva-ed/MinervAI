# Import necessary packages
import time  # Import time module for time-related tasks
import asyncio

import utilities as util
from agents.GeneralAgent import GeneralAgent  # Import GeneralAgent from agents/GeneralAgent.py
from agents.CustomerAgent import CustomerAgent  # Import GeneralAgent from agents/GeneralAgent.py
from agents.SalesAgent import SalesAgent  # Import GeneralAgent from agents/GeneralAgent.py

# Define a coroutine to simulate a lecture session
async def simulate_sales(sales_material, sales_index, sales_agent, customer_agents):
    sales_agent.upload_sales_profile(f"""Here are some key points and concepts from sales {sales_index + 1} in LateX: {sales_material}""")  # Upload lecture notes

    # Simulate classroom interaction
    sales_content = await sales_agent.give_sales()  # Get the lecture content from the professor
    question_answer_array = []  # Initialize an array to store Q&A pairs

    print(sales_content)
    # Generate questions from all customers concurrently
    coroutines = [customer.generate_questions(sales_content.result) for customer in customer_agents]
    all_questions = await asyncio.gather(*coroutines)  # Gather all questions

    sales_coroutines = []  # Initialize an array for professor's responses

    # Process each question and get responses
    for customer_index, question in enumerate(all_questions):
        print(question.result)
        if question.result == "-1":  # Check if student doesn't want to ask a question
            continue

        should_ask = True  # Flag to determine if the question should be asked
        for index, [old_question, old_answer, associated_customers_list] in enumerate(question_answer_array):
            similarity_threshold = 0.75  # Define a threshold for similarity
            if util.calculate_cosine_similarity(old_question, question.result) > similarity_threshold:
                should_ask = False  # Set flag to false if similar question already asked
                question_answer_array[index][2].append(customer_index)  # Append student index to existing question
                break

        if not should_ask:  # Skip if question should not be asked
            continue

        # Add the professor's response coroutine for the new question
        sales_coroutines.append(sales_agent.answer_question(customer_agents[customer_index], question.result))
        question_answer_array.append([question.result, "PLACEHOLDER", [customer_index]])  # Add new question to the array

    # Gather all responses from the professor
    sales_answers = await asyncio.gather(*sales_coroutines)
    for index in range(len(question_answer_array)):
        question_answer_array[index][1] = sales_answers[index].result  # Update answers in the Q&A array

    # Create a JSON object for the lecture
    qa_map_output = []
    for question, answer, associated_customers_list in question_answer_array:
        q_a_pair = {
            "question": question,
            "answer": answer,
            "associated_customers_list": associated_customers_list
        }
        qa_map_output.append(q_a_pair)  # Append Q&A pairs to the output map

    sales_Json = {
        "sales": sales_content.result,
        "QnA": qa_map_output
    }
    return sales_Json  # Return the sales JSON object

# Define the main function to simulate a classroom
async def simulate_clients(content):
    start_time = time.time()  # Record the start time of the simulation

    # Create instances of Professor and Student Agents
    sales_agent = SalesAgent()  # Instantiate a SalesAgent
    customer_agents = [CustomerAgent("Google","An internet company which builds serach engines. Most of its revenue comes from ads."),
                    #    CustomerAgent("McDonalds","A fast food company which sells burgers. Most of its revenue comes from selling burgers."), 
                    #    CustomerAgent("Walmart","A retail company which sells groceries. Most of its revenue comes from selling groceries."), 
                       CustomerAgent("Sequoia","A venture capital firm which invests in startups. Most of its revenue comes from investing in successful startups.")]
    splitOnSignSales = "----------"  # Define a delimiter for splitting lecture content
    sales = content.split(splitOnSignSales)  # Split the content into individual lectures
    sales_json_list = []  # Initialize a list to store lecture JSON objects

    qna_json_list = []  # Initialize a list to store Q&A JSON objects
    for salesIndex, sales in enumerate(sales):
        sales_json = await simulate_sales(sales, salesIndex, sales_agent, customer_agents)  # Simulate each sales session
        sales_json_list.append(sales_json)  # Append the sales JSON object to the list
        for q_a_pair in sales_json["QnA"]:
            qna_json_list.append(q_a_pair)  # Append each Q&A pair to the list

    general_agent = GeneralAgent()  # Instantiate a GeneralAgent
    summary = await general_agent.generate_summary(qna_json_list)  # Generate a summary of Q&A

    # Construct the final JSON object with lecture content and summary
    
    # student_list = []
    
    # for student in students:
    #     myString = f"""Background {student.educational_background} ; Retention Rate: {student.retention_rate}"""
    #     newString = await general_agent.get_personality(myString)
    #     student_list.append(newString.result)
        
    result_json = {
        "lectures": sales_json_list,
        "summary": summary.result, # Include the summary in the result
        "qna": qna_json_list
    }
    print(result_json)  # Print the result JSON

    end_time = time.time()  # Record the end time of the simulation

    # Calculate and print the elapsed time of the simulation
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    
    return result_json  # Return the result JSON


# Execute the main function if this script is run as the main module
if __name__ == "__main__":
    import asyncio  # Import asyncio for asynchronous execution
    asyncio.run(simulate_clients(util.load("samples/sales/sample.txt")))  # Run the simulate_classroom coroutine