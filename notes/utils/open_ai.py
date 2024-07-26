import openai
import os
from django.conf import settings

# Assuming Django settings are used and OPENAI_KEY is set in your settings.py file
openai.api_key = settings.OPKEY

def query_openai(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            temperature=0.5,
            max_tokens=4096,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            messages=[
                {"role": "system", "content": "You are an helpful assistant."},
                {"role": "user", "content": f"""You're an expert AI question generator with a Ph.D. in natural language processing and a keen interest in education technology. You have developed question generation systems for various educational platforms and are well-versed in creating engaging and informative questions that cater to diverse learning styles.

Your task is to generate AI multiple-choice questions based on a given set of notes. The questions should be concise, clear, and relevant to the content, with four to six options, one correct answer, and a brief explanation for each option.

Here are the project requirements -

The software, titled "Poppy," aims to create 5 AI multiple-choice questions based on a student's selected notes. Once an answer is selected, a succinct explanation should be provided on why it's either correct or incorrect. For every correct answer, the user earns a point, and accumulated points can be redeemed for gift cards to incentivize studying.

Please generate questions based on the following notes -

Notes Title: >>__
Notes Content: >>'''{prompt}'''
When generating questions, keep the following in mind -
Ensure the questions are relevant to the content and cover key concepts
Use simple and clear language
Make the correct answer challenging but not ambiguous
Provide explanations for each option why it is wrong and correct not bundle two options that are similar
Ensure the questions are engaging and informative
If possible, provide an example of a generated question to demonstrate your approach.
Must be separated into four sections. Question, Correct Answer, Explanation, Why Wrong
                Describe the correct option name as this option in Explanation section.
                Include markings to facilitate recognizing each section like QUESTIONSTART, QUESTIONEND, CORRECTANSWERSTART, CORRECTANSWEREND,
                EXPLANATIONSTART, EXPLANATIONEND, WHYWRONGSTART, WHYWRONGEND.
                Include only above four sections. Don't include any unnecessary explanation."""},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None