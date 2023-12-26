# Import necessary packages
import time  # Import time module for time-related tasks
import asyncio

import utilities as util
from agents.GeneralAgent import GeneralAgent  # Import GeneralAgent from agents/GeneralAgent.py
from agents.ProfessorAgent import ProfessorAgent  # Import ProfessorAgent from agents/ProfessorAgent.py
from agents.StudentAgent import StudentAgent  # Import StudentAgent from agents/StudentAgent.py

# Define a coroutine to simulate a lecture session
async def simulate_lecture(lecture, lecture_index, professor, students):
    professor.upload_lecture_notes(f"""Here are some key points and concepts from lecture {lecture_index + 1} in LateX: {lecture}""")  # Upload lecture notes

    # Simulate classroom interaction
    lecture_content = await professor.give_lecture()  # Get the lecture content from the professor
    question_answer_array = []  # Initialize an array to store Q&A pairs

    # Generate questions from all students concurrently
    coroutines = [student.generate_questions(lecture_content.result) for student in students]
    all_questions = await asyncio.gather(*coroutines)  # Gather all questions

    prof_coroutines = []  # Initialize an array for professor's responses

    # Process each question and get responses
    for student_index, question in enumerate(all_questions):
        print(question.result)
        if question.result == "-1":  # Check if student doesn't want to ask a question
            continue

        should_ask = True  # Flag to determine if the question should be asked
        for index, [old_question, old_answer, associated_students_list] in enumerate(question_answer_array):
            similarity_threshold = 0.75  # Define a threshold for similarity
            if util.calculate_cosine_similarity(old_question, question.result) > similarity_threshold:
                should_ask = False  # Set flag to false if similar question already asked
                question_answer_array[index][2].append(student_index)  # Append student index to existing question
                break

        if not should_ask:  # Skip if question should not be asked
            continue

        # Add the professor's response coroutine for the new question
        prof_coroutines.append(professor.answer_question(question.result))
        question_answer_array.append([question.result, "PLACEHOLDER", [student_index]])  # Add new question to the array

    # Gather all responses from the professor
    prof_answers = await asyncio.gather(*prof_coroutines)
    for index in range(len(question_answer_array)):
        question_answer_array[index][1] = prof_answers[index].result  # Update answers in the Q&A array

    # Create a JSON object for the lecture
    qa_map_output = []
    for question, answer, associated_students_list in question_answer_array:
        q_a_pair = {
            "question": question,
            "answer": answer,
            "associated_students_list": associated_students_list
        }
        qa_map_output.append(q_a_pair)  # Append Q&A pairs to the output map

    lecture_Json = {
        "lecture": lecture_content.result,
        "QnA": qa_map_output
    }
    return lecture_Json  # Return the lecture JSON object

# Define the main function to simulate a classroom
async def simulate_classroom(content):
    start_time = time.time()  # Record the start time of the simulation

    # Create instances of Professor and Student Agents
    professor = ProfessorAgent()  # Instantiate a ProfessorAgent
    students = [StudentAgent(0.5, "25%", "really smart liberal arts students studying anthropology"),
                StudentAgent(0.2, "40%", "art history"),
                StudentAgent(0.3, "50%", "political science"),
                StudentAgent(0.8, "80%", "engineering"),
                StudentAgent(0.8, "99%", "research in statistics")]  # Instantiate a list of StudentAgents with varied profiles

    splitOnSignLectures = "----------"  # Define a delimiter for splitting lecture content
    lectures = content.split(splitOnSignLectures)  # Split the content into individual lectures
    lecture_json_list = []  # Initialize a list to store lecture JSON objects

    qna_json_list = []  # Initialize a list to store Q&A JSON objects
    for lectureIndex, lecture in enumerate(lectures):
        lecture_json = await simulate_lecture(lecture, lectureIndex, professor, students)  # Simulate each lecture
        lecture_json_list.append(lecture_json)  # Append the lecture JSON object to the list
        for q_a_pair in lecture_json["QnA"]:
            qna_json_list.append(q_a_pair)  # Append each Q&A pair to the list

    general_agent = GeneralAgent()  # Instantiate a GeneralAgent
    summary = await general_agent.generate_summary(qna_json_list)  # Generate a summary of Q&A

    # Construct the final JSON object with lecture content and summary
    
    student_list = []
    
    for student in students:
        myString = f"""Background {student.educational_background} ; Retention Rate: {student.retention_rate}"""
        newString = await general_agent.get_personality(myString)
        student_list.append(newString.result)
        
    result_json = {
        "lectures": lecture_json_list,
        "summary": summary.result, # Include the summary in the result
        "students": student_list
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
    asyncio.run(simulate_classroom(util.load("samples/sample.txt")))  # Run the simulate_classroom coroutine
