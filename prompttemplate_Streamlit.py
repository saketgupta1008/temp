import streamlit as st

# Title and description
st.title("Prompt Template Use Case for Machine Learning and Generative AI")
st.write("This application demonstrates how to use prompt templates in professional machine learning and generative AI scenarios.")

# Sidebar for user input
st.sidebar.header("Choose a Scenario")
scenario = st.sidebar.selectbox(
    "Select a use case:",
    ["Data Preprocessing", "Model Evaluation", "Generative AI Content Creation", 
     "Portfolio Optimization", "Fraud Detection"]
)

# Define prompt templates
templates = {
    "Data Preprocessing": "You are a data scientist preparing a dataset for a machine learning model. Based on the following data description, {data_description}, provide a detailed preprocessing strategy.",
    "Model Evaluation": "You are evaluating a {model_type} trained on {dataset}. Provide a summary of the model's performance metrics and suggest potential improvements.",
    "Generative AI Content Creation": "You are a generative AI expert tasked with creating content. Based on the following input, {input_description}, generate a creative piece that meets the specified requirements.",
    "Portfolio Optimization": "Generate a customized investment portfolio for a client with the following profile: Risk Tolerance: {risk_tolerance}, Investment Horizon: {investment_horizon}, Financial Goals: {financial_goals}, Current Portfolio: {current_portfolio}, Expected Annual Return: {expected_return}, Market Conditions: {market_conditions}, Additional Constraints: {constraints}. Ensure the portfolio is diversified, aligns with the client's goals, and adheres to the given constraints.",
    "Fraud Detection": "Analyze the following transaction data to identify potential fraudulent activities: Account Holder Information: {account_info}, Transaction History: {transaction_history}, Account Behavior: {account_behavior}, Anomalies: {anomalies}, Risk Factors: {risk_factors}. Generate a list of flagged transactions with a risk score and a brief explanation of why each transaction was identified as potentially fraudulent. Suggest immediate actions, such as transaction reversal or account suspension, if needed."
}

# Get user input based on the selected scenario
prompt = ""
if scenario == "Data Preprocessing":
    data_description = st.sidebar.text_area("Describe your dataset (e.g., 'A CSV file with missing values in the target column'):")
    prompt = templates["Data Preprocessing"].format(data_description=data_description)

elif scenario == "Model Evaluation":
    model_type = st.sidebar.text_input("Enter the model type (e.g., 'Random Forest'):")
    dataset = st.sidebar.text_input("Enter the dataset name or description (e.g., 'Iris dataset'):")
    prompt = templates["Model Evaluation"].format(model_type=model_type, dataset=dataset)

elif scenario == "Generative AI Content Creation":
    input_description = st.sidebar.text_area("Describe the content requirements (e.g., 'Generate a blog post on AI ethics'):")
    prompt = templates["Generative AI Content Creation"].format(input_description=input_description)

elif scenario == "Portfolio Optimization":
    risk_tolerance = st.sidebar.text_input("Enter risk tolerance (e.g., 'Moderate'):")
    investment_horizon = st.sidebar.text_input("Enter investment horizon (e.g., 'Long-term'):")
    financial_goals = st.sidebar.text_area("Enter financial goals (e.g., 'Wealth accumulation, Retirement planning'):")
    current_portfolio = st.sidebar.text_area("Describe the current portfolio (e.g., 'Equities, Bonds, Mutual Funds'):")
    expected_return = st.sidebar.text_input("Enter expected annual return (e.g., '8%'):")
    market_conditions = st.sidebar.text_input("Describe current market conditions (e.g., 'Bullish'):")
    constraints = st.sidebar.text_area("Enter any additional constraints (e.g., 'Ethical investing preferences'):")
    prompt = templates["Portfolio Optimization"].format(
        risk_tolerance=risk_tolerance, investment_horizon=investment_horizon, 
        financial_goals=financial_goals, current_portfolio=current_portfolio, 
        expected_return=expected_return, market_conditions=market_conditions, 
        constraints=constraints
    )

elif scenario == "Fraud Detection":
    account_info = st.sidebar.text_area("Enter account holder information (e.g., 'Name, Account Number'):")
    transaction_history = st.sidebar.text_area("Enter transaction history (e.g., 'List of transactions with date, amount, merchant, location'):")
    account_behavior = st.sidebar.text_area("Describe normal account behavior (e.g., 'Typical spending patterns, average transaction amount'):")
    anomalies = st.sidebar.text_area("Describe any anomalies (e.g., 'Transactions that deviate from normal behavior'):")
    risk_factors = st.sidebar.text_area("Enter any risk factors (e.g., 'Recent account activities, high-risk merchants'):")
    prompt = templates["Fraud Detection"].format(
        account_info=account_info, transaction_history=transaction_history, 
        account_behavior=account_behavior, anomalies=anomalies, 
        risk_factors=risk_factors
    )

# Button to generate prompt
if st.button("Generate Prompt"):
    # Display the generated prompt
    st.text_area("Generated Prompt:", prompt, height=200)

# Example Outputs
st.write("## Use Case Examples")
if st.checkbox("Show Example Outputs"):
    if scenario == "Data Preprocessing":
        st.write("**Example 1:**")
        st.write("Prompt: " + templates["Data Preprocessing"].format(data_description="A dataset with outliers and missing values."))
        st.write("**Generated Output:** Handle missing values using mean imputation, remove outliers using IQR, and normalize the dataset.")

    elif scenario == "Model Evaluation":
        st.write("**Example 2:**")
        st.write("Prompt: " + templates["Model Evaluation"].format(model_type="SVM", dataset="MNIST"))
        st.write("**Generated Output:** The SVM model achieved 95% accuracy on the MNIST dataset. Consider tuning hyperparameters or using a different kernel for improvement.")

    elif scenario == "Generative AI Content Creation":
        st.write("**Example 3:**")
        st.write("Prompt: " + templates["Generative AI Content Creation"].format(input_description="Generate a LinkedIn post about the impact of AI on finance."))
        st.write("**Generated Output:** AI is revolutionizing finance by enabling better decision-making, automating tasks, and providing new insights. Embrace AI to stay ahead in the financial industry.")

    elif scenario == "Portfolio Optimization":
        st.write("**Example 4:**")
        st.write("Prompt: " + templates["Portfolio Optimization"].format(
            risk_tolerance="Moderate", investment_horizon="Long-term", 
            financial_goals="Retirement planning", current_portfolio="Equities, Bonds", 
            expected_return="8%", market_conditions="Bullish", constraints="Ethical investing preferences"
        ))
        st.write("**Generated Output:** A diversified portfolio with 60% equities, 30% bonds, and 10% alternative investments. Consider including ESG funds to align with ethical preferences.")

    elif scenario == "Fraud Detection":
        st.write("**Example 5:**")
        st.write("Prompt: " + templates["Fraud Detection"].format(
            account_info="John Doe, Account Number 12345678", transaction_history="List of transactions with date, amount, merchant, location", 
            account_behavior="Typical spending patterns, average transaction amount", anomalies="Transactions that deviate from normal behavior", 
            risk_factors="Recent account activities, high-risk merchants"
        ))
        st.write("**Generated Output:** Transaction #7890 flagged as potentially fraudulent due to unusual location and amount. Recommend immediate account suspension and further investigation.")
