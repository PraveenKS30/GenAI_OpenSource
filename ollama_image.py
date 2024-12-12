from ollama import chat
from pydantic import BaseModel

class Movies(BaseModel):
  title : str
  year : int
  actors : list[str]
  ratings : int

path = 'structured_output\image.PNG'

response = chat(
  messages=[
    {
      'role': 'user',
      'content': 'Analyze this image and describe what you see',
      'images' : [path]
    }
  ],
  model='llama3.2-vision',
  format= Movies.model_json_schema()
)

print(response.message.content)