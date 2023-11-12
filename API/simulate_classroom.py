#### RUN THIS TO INSTALL PKGS ########
# python -m pip install semantic-kernel
######################################

# Import necessary packages
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel import PromptTemplateConfig, PromptTemplate, SemanticFunctionConfig
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random


# Prepare OpenAI service using credentials stored in the `.env` file
api_key, org_id = sk.openai_settings_from_dot_env()


# Cosine Similarity Function
def calculate_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]


# Load x lines from a file
def load(filename, lines_to_read = 50):
    lines = []
    with open(filename, 'r') as file:
        for _ in range(lines_to_read):
            line = file.readline()
            if not line:
                break
            lines.append(line.strip())

    return '\n'.join(lines)




# Define prompts
class ProfessorAgent:
    def __init__(self, expertise_area):
        self.expertise_area = expertise_area
        self.lecture_notes = None
        self.kernel = sk.Kernel()
        self.kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo-16k", api_key, org_id))

    def upload_lecture_notes(self, notes):
        self.lecture_notes = notes

    async def answer_question(self, question):
        return self.kernel.create_semantic_function(f"""Provide a detailed answer to the following question in the context of {self.expertise_area} and {self.lecture_notes}: {question}""", temperature=0.8)()

    async def give_lecture(self):
        if self.lecture_notes:
            # Incorporating lecture notes into the lecture generation
            return self.kernel.create_semantic_function(f"""Give a detailed lecture on related to {self.expertise_area}, using the following notes: {self.lecture_notes}.""")()
        else:
            # Default lecture generation without notes
            return self.kernel.create_semantic_function(f"""Give a detailed lecture on {topic} related to {self.expertise_area}.""")()

class StudentAgent:
    def __init__(self, retention_rate, personality_type, educational_background):
        self.retention_rate = retention_rate # 10%, 30%, 70%, 90%
        self.personality_type = personality_type # Introverted, Extroverted
        self.educational_background = educational_background # Liberal Arts, Engineering, Pure Researcher
        
        #initialize kernel
        self.kernel = sk.Kernel()
        self.kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))


    async def generate_questions(self, lecture_content):
        new_lecture_content = ""
        arr = lecture_content.split(".")
        for line in arr:
            r = random.random()
            if r < self.retention_rate:
                new_lecture_content += line + ".\n"
        lecture_content = new_lecture_content

        return self.kernel.create_semantic_function(f"""As a student, you went through the following {lecture_content}: Pretend that you are a student with educational background of {self.educational_background} and personality type of {self.personality_type} . Pretend to be the student described above learning from this lecture, state one clarifying question you have about this lecture, and do not state anything other than the question. If you have a good understading already, you can not asking questions, and respond by saying -1""",max_tokens=120,temperature=0.5)()

    async def discuss_with_peer(self, peer, lecture_content):
        # This function simulates discussion between two students
        pass

# Main simulation function
async def simulate_classroom(content=load("lecture-notes.txt")):

    # Create Professor and Student Agents
    professor = ProfessorAgent("Mathematics")
    students = [StudentAgent(0.5, "extroverted", "really dumb liberal arts students studying anthropology"), 
                StudentAgent(0.8, "introverted", "engineering"),
                StudentAgent(0.95, "extroverted", "research in math"),
                StudentAgent(0.7, "introverted", "physics"),
                StudentAgent(0.2, "introverted", "art history"),
                StudentAgent(0.3, "extroverted", "political science"),
                StudentAgent(0.8, "introverted", "engineering"),
                StudentAgent(0.8, "extroverted", "research in statistics")]
    # Example: Upload lecture notes
    professor.upload_lecture_notes(f"""Here are some key points and concepts about Groups, Rings, and Fields in LateX: { content }""")

    # Simulate classroom interaction
    lecture_content = await professor.give_lecture()
    print(lecture_content)
    final_array = []
    print("Question + Answer pairs: ")
    for student in students:
        question = await student.generate_questions(lecture_content.result)
        if question.result == "-1":
            continue
            
        should_ask = True
        for index, [old_question, old_answer, counter] in enumerate(final_array):
            similarity_threshold = 0.75  # Adjust the threshold as needed
            if calculate_cosine_similarity(old_question, question.result) > similarity_threshold:
                should_ask = False
                final_array[index][2]+=1
                break

        if not should_ask:
            continue

        answer = await professor.answer_question(question.result)
        final_array.append([question.result, answer.result, 1])
        print("Question: ", question.result)
        print("Answer: ", answer.result)
    
    print(len(final_array))
    for index, [question, answer, counter] in enumerate(final_array):
        print(f"""Index: {index}  Counter {counter}""")
    return {"lecture": lecture_content.result, "qa_array": final_array}
    # Log the interaction for analysis
    # save_to_report(final_array)

    # Simulate break time interaction
    # for i in range(len(students)):
    #     for j in range(i + 1, len(students)):
    #         await students[i].discuss_with_peer(students[j], lecture_content)
            # Log the interaction for analysis


# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(simulate_classroom())