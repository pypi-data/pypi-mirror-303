import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import capote_ai.rubric_gen as rubric_gen
from dotenv import load_dotenv

load_dotenv()

# Initialising the OpenAI client
rubric_gen.init_openai(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_org_key=os.getenv("OPENAI_ORG_KEY"),
    openai_proj_key=os.getenv("OPENAI_PROJ_KEY")
)
# Define input dictionary for the rubric generation
updated_input = {
  "staff_email": "ta2@example.com",
  "assessment_description": "This assessment evaluates the understanding of object-oriented programming concepts and the ability to design and implement software systems using these concepts.",
  "criteria": [
    {
      "criterion": "Encapsulation and Abstraction",
      "keywords": ["encapsulation", "abstraction"],
      "competencies": ["understanding of encapsulation techniques"],
      "skills": ["design modular systems"],
      "knowledge": ["data hiding", "object-oriented principles"]
    },
    {
      "criterion": "Inheritance and Polymorphism",
      "keywords": ["inheritance", "polymorphism"],
      "competencies": ["apply inheritance effectively"],
      "skills": ["extend class hierarchies"],
      "knowledge": ["polymorphic behavior", "object hierarchy design"]
    },
    {
      "criterion": "Design Patterns",
      "keywords": ["factory", "singleton", "observer"],
      "competencies": ["understanding design patterns"],
      "skills": ["apply design patterns to system architecture"],
      "knowledge": ["creational patterns", "structural patterns"]
    }
  ],
  "ulos": [
    "ULO1: Understand core object-oriented concepts.",
    "ULO2: Apply design patterns to improve software structure.",
    "ULO3: Implement modular, scalable systems using OOP principles."
  ]
}
test_rubric_gen = rubric_gen.generate_rubric(updated_input)

print(test_rubric_gen)