import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from capote_ai.pdf_to_text import extract_text_and_tables_from_pdf
from capote_ai.grammar_check import grammer_score, init_openai
from dotenv import load_dotenv

# Loading env file for future env variable retrieval
load_dotenv() 
# File for question generation/regeneration:
FILE_PATH = 'Sample_PDF/pdf_3.pdf'

# Initialising the OpenAI client
init_openai(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_org_key=os.getenv("OPENAI_ORG_KEY"),
    openai_proj_key=os.getenv("OPENAI_PROJ_KEY")
)

# Open the PDF file in binary mode
with open(FILE_PATH, 'rb') as file_obj:
    # Call the extract_text_and_tables_from_pdf function with the file object
    assignment_content = extract_text_and_tables_from_pdf(file_obj)

success, result = grammer_score(assignment_content)

if success:
    print(result)
else:
    print("Error:", result)