- this is the code generated from chatgpt by following the requirements 

- support multiple chat session and this chat bot is able to record the chat history

- an openai API service should be deployed at some where(VPS) and provide exetrnal wrapper API as general HTTP POST to user. this wrapper API is leveraged from the repo here: https://github.com/ayaka14732/ChatGPTAPIFree
  - env should be set, on linux it looks like: export API_KEYS='["sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]'
  - when deploy this wrapper API on VPS, you to run command "netstat -tulnp" to check the port used by wrapper service.  if you have some issue to access it, you can try to use updated version: https://github.com/flyingcloud2048/ChatGPTAPIFree
