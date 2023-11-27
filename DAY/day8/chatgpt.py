import os
import openai

if __name__ == '__main__':
    openai.organization = "cxm123"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()