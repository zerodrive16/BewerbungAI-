import sys
import os
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from WebApplication.Text_Preprocessing.spacy_summarizer import *

class TestTextSummarization(unittest.IsolatedAsyncioTestCase):

    async def test_textSummarizationJobDescription_short_text(self):

        text = "This is a short job description."
        result = await textSummarizationJobDescription(text)
        self.assertEqual(result, text)

    @patch("WebApplication.Text_Preprocessing.spacy_summarizer.summarizer")
    async def test_textSummarizationJobDescription_long_text(self, mock_summarizer):

        text = " ".join(["word"] * 100)  # text with 100 words
        mock_summarizer.return_value = [{"summary_text": "Mocked summary"}]

        result = await textSummarizationJobDescription(text)

        mock_summarizer.assert_called_once()
        self.assertEqual(result, "Mocked summary")

    async def test_textSummarizationPersonalInformation_short_text(self):

        text = "This is short personal info."
        result = await textSummarizationPersonalInformation(text)
        self.assertEqual(result, text)

    @patch("WebApplication.Text_Preprocessing.spacy_summarizer.summarizer")
    async def test_textSummarizationPersonalInformation_long_text(self, mock_summarizer):

        text = " ".join(["word"] * 60)
        mock_summarizer.return_value = [{"summary_text": "Mocked summary"}]

        result = await textSummarizationPersonalInformation(text)

        mock_summarizer.assert_called_once()
        self.assertEqual(result, "Mocked summary")


if __name__ == "__main__":
    unittest.main()
