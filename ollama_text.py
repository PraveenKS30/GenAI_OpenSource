from ollama import chat
from pydantic import BaseModel

class Movies(BaseModel):
  title : str
  year : int
  actors : list[str]
  ratings : int

response = chat(
  messages=[
    {
      'role': 'user',
      'content': 'What is the imdb rating of Prison Break?',
    }
  ],
  model='llama3.2',
  format= Movies.model_json_schema()
)

print(Movies.model_validate_json(response.message.content))