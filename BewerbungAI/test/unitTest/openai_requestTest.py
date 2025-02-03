import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from WebApplication.Text_Preprocessing.openai_request import openAIRequest

class TestOpenAIRequest(unittest.TestCase):

    @patch("WebApplication.Text_Preprocessing.openai_request.openai.ChatCompletion.create")
    def test_openAIRequest(self, mock_openai):
        """Test OpenAI Request function by mocking OpenAI API response."""

        # Mock OpenAI API response
        mock_openai.return_value = {
            "choices": [
                {"message": {"content": "Dear Hiring Manager,\nThis is a test cover letter.\nSincerely, Doe, John"}}
            ]
        }

        # Sample input data
        resume_data = {
            "first_name": "John",
            "last_name": "Doe",
            "address": "123 Test St",
            "zipcode": "12345",
            "city": "Test City",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "date": "2025-02-03"
        }

        application_data = {
            "manager_name": "Jane Smith",
            "company_name": "TechCorp",
            "company_address": "456 Business Rd",
            "company_zip_code": "67890",
            "company_city": "Big City"
        }

        finalJobDescription = {
            "job": {"summary": "This is a job description summary."}
        }

        finalPersonalDescription = {
            "experience": {"summary": "5 years of experience in software development."},
            "education": {"summary": "Bachelor's degree in Computer Science."},
            "skills": {"summary": "Python, Machine Learning, AI."},
            "interests": {"summary": "AI Research, Open Source Contribution."}
        }

        # Call the function
        result = openAIRequest(resume_data, application_data, finalJobDescription, finalPersonalDescription)

        # Check the expected output
        self.assertIn("Dear Hiring Manager", result)
        self.assertIn("Sincerely, Doe, John", result)

if __name__ == "__main__":
    unittest.main()
