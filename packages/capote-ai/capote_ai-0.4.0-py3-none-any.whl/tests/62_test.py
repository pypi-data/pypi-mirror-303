import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import capote_ai.pdf_to_text as pdf_to_text
import capote_ai.rubric_gen as rubric_gen
from dotenv import load_dotenv

load_dotenv()

# Initialising the OpenAI client
rubric_gen.init_openai(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_org_key=os.getenv("OPENAI_ORG_KEY"),
    openai_proj_key=os.getenv("OPENAI_PROJ_KEY")
)

# Read Marking Guide
# FILE_PATH = 'Sample_PDF/Sample_Marking_Guide.pdf'
FILE_PATH = 'Sample_PDF/Sample_MarkingGuide.pdf'

with open(FILE_PATH, 'rb') as file_obj:
    guide_content = pdf_to_text.extract_text_and_tables_from_pdf(file_obj)

rubric_input = {
  "marking_guide": guide_content,
  "ulos": [
    "ULO1: Understand core object-oriented concepts.",
    "ULO2: Apply design patterns to improve software structure.",
    "ULO3: Implement modular, scalable systems using OOP principles."
  ]
}

test_rubric_gen = rubric_gen.convert_rubric(rubric_input)

print(test_rubric_gen)