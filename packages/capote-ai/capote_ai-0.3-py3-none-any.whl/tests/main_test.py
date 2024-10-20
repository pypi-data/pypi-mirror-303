import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

## Test client for testing package based question generation module:
import capote_ai.viva_questions as viva_questions
import capote_ai.pdf_to_text as pdf_to_text
from dotenv import load_dotenv

# Loading env file for future env variable retrieval
load_dotenv() 

# File for question generation/regeneration:
FILE_PATH = 'Sample_PDF/comp3010.pdf'

# Initialising the OpenAI client
viva_questions.init_openai(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_org_key=os.getenv("OPENAI_ORG_KEY"),
    openai_proj_key=os.getenv("OPENAI_PROJ_KEY")
)

# Open the PDF file in binary mode
with open(FILE_PATH, 'rb') as file_obj:
    # Call the extract_text_and_tables_from_pdf function with the file object
    assignment_content = pdf_to_text.extract_text_and_tables_from_pdf(file_obj)
    # assignment_content, tables_by_page = pdf_to_text.extract_text_and_tables_from_pdf(file_obj)
    # print(assignment_content)

# Preparing input data
# expected no.of questions input definition for reference:
question_types = {
    'Factual recall': 'no_of_questions_factual_recall',
    'Conceptual understanding': 'no_of_questions_conceptual_understanding',
    'Analysis and evaluation': 'no_of_questions_analysis_evaluation',
    'Application and problem-solving': 'no_of_questions_application_problem_solving',
    'Open-ended': 'no_of_questions_open_ended'
}

input_data = {
    'assignment_title': "Impact of Agile Methodologies on Software Development",
    'unit_name': "Introduction to Software Engineering",
    'no_of_questions_factual_recall': 3,
    'no_of_questions_analysis_evaluation': 2,
    'no_of_questions_open_ended':1,
    'no_of_questions_application_problem_solving': 8,
    'question_challenging_level': "Medium",
    'student_year_level': "Third Year",
    'assignment_content':assignment_content,
}

##Double check regarding question difficulty, student year level
regen_input_data = {
    'assignment_title': "Impact of Agile Methodologies on Software Development",
    'unit_name': "Introduction to Software Engineering",
    'question_reason': [
        {"question_1": "Can you explain the core principles of Agile methodologies as described in your assignment?", 
         "reason": "Too vague",
         "question_type": "Factual recall"},
        {"question_2": "Considering the trends in software development, how do you foresee the role of Agile methodologies evolving in the next five years?", 
         "reason": "Not aligned with assignment content",
         "question_type": "Open-ended"}
    ],
    'assignment_content':assignment_content,
}

# Generating viva questions
success, result = viva_questions.generate_viva_questions(input_data)
# success, result = viva_questions.regenerate_questions(regen_input_data)

if success:
    print(result)
else:
    print("Error:", result)