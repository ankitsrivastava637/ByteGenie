from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

def add_to_memory(user_input, ai_output):
    memory.add_user_input(user_input)
    memory.add_ai_output(ai_output)

def get_memory():
    return memory
