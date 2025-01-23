from litellm import completion
from litellm import embedding
import litellm

response = embedding(model='text-embedding-ada-002', input=["good morning from litellm"])

print(response)