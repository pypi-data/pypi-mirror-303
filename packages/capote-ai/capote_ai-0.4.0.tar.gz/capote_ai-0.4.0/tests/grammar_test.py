import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from capote_ai.pdf_to_text import extract_text_and_tables_from_pdf
from capote_ai.grammar_check import grammar_score, init_openai, struc_check, spell_check
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv() 

# Path to the sample PDF file
FILE_PATH = 'Sample_PDF/pdf_3.pdf'

# Initialize the OpenAI client
init_openai(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_org_key=os.getenv("OPENAI_ORG_KEY"),
    openai_proj_key=os.getenv("OPENAI_PROJ_KEY")
)

# Open the PDF file in binary mode
with open(FILE_PATH, 'rb') as file_obj:
    # Extract text and tables from the PDF file
    assignment_content = extract_text_and_tables_from_pdf(file_obj)

# Test the grammar_score function
print("\n=== Testing grammar_score function ===")
success, result = grammar_score(assignment_content)
if success:
    print(result)
else:
    print("Error in grammar_score:", result)

# Test the struc_check function
print("\n=== Testing struc_check function ===")
success, result = struc_check(assignment_content)
if success:
    print(result)
else:
    print("Error in struc_check:", result)

# Test the spell_check function
print("\n=== Testing spell_check function ===")
success, result = spell_check(assignment_content)
if success:
    print(result)
else:
    print("Error in spell_check:", result)