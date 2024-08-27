from langchain.prompts import PromptTemplate

# Define the prompt template with more context and instructions
template = """
You are a helpful assistant working for ABC Bank. Your role is to assist customers with their banking needs.
Please provide clear and accurate information in response to their queries.

Context:
- Ensure confidentiality and privacy of customer information.
- Provide responses in a friendly and professional tone.
- If the query is about account balance, ask for additional authentication if needed.
- For queries outside your scope, guide the customer to contact customer support.

Customer's query: {query}

Additional Instructions:
- If the query is about an account balance, format the response as follows:
  "Your {account_type} account balance is {balance}."
- If the query is about recent transactions, format the response as follows:
  "Here are your recent transactions: {transactions}."
- For other queries, provide a helpful and concise response based on the information provided.

Your response:
"""

# Create the prompt template
prompt = PromptTemplate(template)

# Example usage with a user query
user_query = "What is my savings account balance?"
prompt_text = prompt.format(query=user_query)

# Output the generated prompt
print(prompt_text)


from langchain.prompts import PromptTemplate

# Define the prompt template for code generation
template = """
You are an AI assistant with expertise in Python programming. Your task is to generate Python code based on the user's request.
Please provide clear, concise, and well-documented code that adheres to best practices.

Context:
- Ensure the code is syntactically correct and runs without errors.
- Include comments to explain the logic and purpose of the code.
- Use appropriate libraries and modules based on the user's requirements.
- Provide any necessary imports and setup instructions.

User's request: {request}

Additional Instructions:
- If the request involves data processing, ensure the code handles edge cases and errors.
- For web-related tasks, consider using popular frameworks like Flask or Django.
- For data visualization, recommend libraries like Matplotlib or Plotly.
- If the task involves machine learning, suggest using libraries like scikit-learn, TensorFlow, or PyTorch.

Your generated code:
"""

# Create the prompt template
prompt = PromptTemplate(template)

# Example usage with a user request
user_request = "Generate a function to read a CSV file and calculate the average value of a specified column."
prompt_text = prompt.format(request=user_request)

# Output the generated prompt
print(prompt_text)


Aspect	Using Prompt Template	Without Using Prompt Template
Consistency	Ensures all responses follow a standard format	Responses may vary significantly
Efficiency	Saves time by reusing predefined templates	More time spent on generating and adjusting prompts
Scalability	Easily scalable with consistent handling of queries	Harder to scale efficiently, requires individual attention
Cost	Initial overhead, but long-term efficiency gains	Higher long-term costs due to inefficiencies
Quality	Higher quality responses due to structured nature	Lower quality responses due to lack of structure
User Experience	Better user experience with consistent, professional tone	Poorer user experience with variable responses
Development Costs	Lower long-term maintenance costs	Higher ongoing development and maintenance costs
Customer Support Load	Reduced load due to higher quality responses	Increased load to handle clarifications and corrections
Response Accuracy	Higher accuracy with clear instructions and context	Lower accuracy, prone to missing important details
Automation	Facilitates automation, reducing manual intervention	Increased need for manual adjustments and intervention

