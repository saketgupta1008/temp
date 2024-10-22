import streamlit as st

# Title and description
st.title("Prompt Template Use Case for Machine Learning and Generative AI")
st.write("This application demonstrates how to use prompt templates in various professional machine learning and generative AI scenarios.")

# Sidebar for user input
st.sidebar.header("Choose a Scenario")
use_case = st.sidebar.selectbox(
    "Select a use case:",
    ["Summarization", "Report Insight Generation", "Fraud Detection", "Code Conversion"]
)

# Variable to store generated prompt text
generated_prompt = ""

# Summarization Use Case
if use_case == "Summarization":
    st.subheader("Summarization")

    # Sidebar: Select the technique
    technique = st.sidebar.radio(
        "Select Technique:",
        ("About", "Default", "Abstractive", "Extractive", "Specific")
    )

    # Technique-based input field
    summarization_prompts = {
        "About": "Summarization involves creating a concise and coherent summary of a larger body of text. This process can be achieved using different techniques such as abstractive or extractive methods.",
        "Abstractive": "Using an abstractive summarization method, create a coherent summary that rephrases the original text: {text}",
        "Extractive": "Using an extractive summarization method, pick out the most relevant sentences from the following text: {text}",
        "Specific": "Summarize the following content, focusing on the key points and insights most relevant to the provided topic: {text}"
    }

    if technique == "About":
        st.write(summarization_prompts["About"])

    elif technique == "Default":
        text_input = st.sidebar.text_area("Enter Text to Summarize:")
        generated_prompt = text_input
        st.write("You can summarize the text without a specific prompt template.")

    else:
        text_input = st.sidebar.text_area("Enter Text to Summarize:")
        if technique == "Abstractive":
            generated_prompt = summarization_prompts["Abstractive"].format(text=text_input)
        elif technique == "Extractive":
            generated_prompt = summarization_prompts["Extractive"].format(text=text_input)
        elif technique == "Specific":
            generated_prompt = summarization_prompts["Specific"].format(text=text_input)

    # Generate and Run prompt buttons
    if st.button("Generate Prompt"):
        if technique == "About":
            generated_prompt = summarization_prompts["About"]
        elif technique == "Default":
            generated_prompt = text_input
        st.text_area("Generated Prompt:", generated_prompt, height=200)

    if st.button("Run Prompt"):
        st.text_area("Prompt Execution Result:", generated_prompt, height=200)

# Report Insight Generation Use Case
elif use_case == "Report Insight Generation":
    st.subheader("Report Insight Generation")

    # Sidebar: Select the technique
    technique = st.sidebar.radio(
        "Select Technique:",
        ("About", "Default", "Contextual Analysis", "Trend Identification", "Specific")
    )

    # Technique-based input field
    report_insight_prompts = {
        "About": "Report Insight Generation focuses on identifying key findings and providing insights from structured reports. This can involve analyzing data, identifying trends, and understanding the broader context of the report.",
        "Contextual Analysis": "Analyze the following report data and provide contextual insights, highlighting patterns and anomalies: {report_data}",
        "Trend Identification": "Identify key trends from the following report, with an emphasis on emerging issues and future opportunities: {report_data}",
        "Specific": "Analyze this report to provide insights on specific aspects, such as financial performance, operational efficiency, and strategic risks: {report_data}"
    }

    if technique == "About":
        st.write(report_insight_prompts["About"])

    elif technique == "Default":
        report_data = st.sidebar.text_area("Enter Report Data:")
        generated_prompt = report_data
        st.write("You can generate insights from the report without a specific prompt template.")

    else:
        report_data = st.sidebar.text_area("Enter Report Data:")
        if technique == "Contextual Analysis":
            generated_prompt = report_insight_prompts["Contextual Analysis"].format(report_data=report_data)
        elif technique == "Trend Identification":
            generated_prompt = report_insight_prompts["Trend Identification"].format(report_data=report_data)
        elif technique == "Specific":
            generated_prompt = report_insight_prompts["Specific"].format(report_data=report_data)

    # Generate and Run prompt buttons
    if st.button("Generate Prompt"):
        if technique == "About":
            generated_prompt = report_insight_prompts["About"]
        elif technique == "Default":
            generated_prompt = report_data
        st.text_area("Generated Prompt:", generated_prompt, height=200)

    if st.button("Run Prompt"):
        st.text_area("Prompt Execution Result:", generated_prompt, height=200)

# Fraud Detection Use Case
elif use_case == "Fraud Detection":
    st.subheader("Fraud Detection")

    # Sidebar: Select the technique
    technique = st.sidebar.radio(
        "Select Technique:",
        ("About", "Default", "Chain of Thought", "Example-Based", "Specific")
    )

    # Define prompt templates for Fraud Detection
    fraud_detection_prompts = {
        "About": "Fraud detection involves identifying potentially fraudulent activities based on transaction patterns, anomalies, and risk factors. It requires analyzing behavior and transactions to detect irregularities.",
        "Chain of Thought": "Using a step-by-step reasoning process, analyze the following transaction data: {transaction_data}. What could be potential indicators of fraud, and how would you prioritize investigation?",
        "Example-Based": "Based on the provided examples of normal and suspicious transactions: {transaction_examples}, identify which transactions are most likely fraudulent and explain your reasoning.",
        "Specific": "Analyze the following data for potential fraud: Account Holder Info: {account_info}, Transaction History: {transaction_history}, Behavior Anomalies: {anomalies}, Risk Factors: {risk_factors}. Provide recommendations for actions to be taken."
    }

    # Input variables
    fraud_input = ""
    account_info = ""
    transaction_history = ""
    anomalies = ""
    risk_factors = ""

    # Technique-based input fields
    if technique == "About":
        st.write(fraud_detection_prompts["About"])

    elif technique == "Default":
        transaction_data = st.sidebar.text_area("Enter Transaction Data:")
        generated_prompt = transaction_data
        st.write("You can analyze the transaction data without a specific prompt template.")

    elif technique == "Chain of Thought":
        transaction_data = st.sidebar.text_area("Enter Transaction Data (e.g., Date, Amount, Merchant, Location):")
        generated_prompt = fraud_detection_prompts["Chain of Thought"].format(transaction_data=transaction_data)

    elif technique == "Example-Based":
        transaction_examples = st.sidebar.text_area("Enter Transaction Examples (Normal and Suspicious Transactions):")
        generated_prompt = fraud_detection_prompts["Example-Based"].format(transaction_examples=transaction_examples)

    elif technique == "Specific":
        account_info = st.sidebar.text_area("Enter Account Holder Information:")
        transaction_history = st.sidebar.text_area("Enter Transaction History:")
        anomalies = st.sidebar.text_area("Describe any Anomalies (e.g., transactions that deviate from normal behavior):")
        risk_factors = st.sidebar.text_area("Enter Risk Factors:")
        generated_prompt = fraud_detection_prompts["Specific"].format(
            account_info=account_info,
            transaction_history=transaction_history,
            anomalies=anomalies,
            risk_factors=risk_factors
        )

    # Generate and Run prompt buttons
    if st.button("Generate Prompt"):
        if technique == "About":
            generated_prompt = fraud_detection_prompts["About"]
        elif technique == "Default":
            generated_prompt = transaction_data
        st.text_area("Generated Prompt:", generated_prompt, height=200)

    if st.button("Run Prompt"):
        st.text_area("Prompt Execution Result:", generated_prompt, height=200)

# Code Conversion Use Case
elif use_case == "Code Conversion":
    st.subheader("Code Conversion")

    # Sidebar: Select the technique
    technique = st.sidebar.radio(
        "Select Technique:",
        ("About", "Default", "Python to JavaScript", "JavaScript to Python", "Specific")
    )

    # Define prompt templates for Code Conversion
    code_conversion_prompts = {
        "About": "Code conversion involves translating code from one programming language to another while ensuring that the logic, structure, and functionality remain consistent.",
        "Python to JavaScript": "Convert the following Python code into JavaScript, ensuring the logic remains consistent: {code}",
        "JavaScript to Python": "Convert the following JavaScript code into Python, maintaining the same logic: {code}",
        "Specific": "Translate the following code between specified languages while addressing key syntax differences: {code}"
    }

    if technique == "About":
        st.write(code_conversion_prompts["About"])

    elif technique == "Default":
        code_input = st.sidebar.text_area("Enter Code to Convert:")
        generated_prompt = code_input
        st.write("You can convert the code without a specific prompt template.")

    else:
        code_input = st.sidebar.text_area("Enter Code to Convert:")
        if technique == "Python to JavaScript":
            generated_prompt = code_conversion_prompts["Python to JavaScript"].format(code=code_input)
        elif technique == "JavaScript to Python":
            generated_prompt = code_conversion_prompts["JavaScript to Python"].format(code=code_input)
        elif technique == "Specific":
            generated_prompt = code_conversion_prompts["Specific"].format(code=code_input)

    # Generate and Run prompt buttons
    if st.button("Generate Prompt"):
        if technique == "About":
            generated_prompt = code_conversion_prompts["About"]
        elif technique == "Default":
            generated_prompt = code_input
        st.text_area("Generated Prompt:", generated_prompt, height=200)

    if st.button("Run Prompt"):
        st.text_area("Prompt Execution Result:", generated_prompt, height=200)
