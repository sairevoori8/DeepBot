from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

class GenrateText:
    def LlmText(self, givT):
        llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="AIzaSyABbWo-PqVU4xmJd2vL5NsczrAUkDWJYk0")

        prompt_template = PromptTemplate.from_template(
            template="You will be given a text which is extracted from an image. Provide details about the product like its company name , manufacture date, and expiry date.there are spelling mistakes and irregularities in the text be careful . Here is the text: {content}. Generate in the following manner: {length}"
        )

        print("\n")
        prompt = prompt_template.format(
            length="brand name:, manufacture date:, expiry date:",
            content=givT
        )
        print(prompt)

        response = llm.invoke(prompt)
        
        return response


