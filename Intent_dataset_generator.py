import pandas as pd
import random

# Define categories of techniques according to the intents
technique_categories = {
    "plot_graph": [
        'Scatter Chart', 'Point Graph', 'XY Plot', 'Bivariate Distribution Chart', 'Data Scatter Plot',
        'Heatmap', 'Intensity Map', 'Data Matrix Visualization', 'Color-Coded Thermal Map', 'Line Plot',
        'Trend Graph', 'Time Series Plot', 'Continuous Line Graph', 'Data Line Graph'
    ],
    "test_stats": [
        'Normality Test', 'Distribution Assessment', 'Goodness-of-Fit Test', 'Statistical Normalcy Check',
        'Standard Deviation Test', 'Single-Sample Z-test', 'Two-Sample Z-test', 'Z Test'
    ],
    "detect_anomaly": [
        'ADFuller', 'Stationarity Test', 'Time Series Analysis Test', 'Dickey-Fuller Test', 'DBScan',
        'Density Clustering', 'Spatial Clustering', 'Noise Filtering Analysis', 'Isolation Forest',
        'Anomaly Detection', 'Outlier Identification', 'Isolation Analysis', 'ABOD', 'Outlier Detection',
        'Angle-Based Anomaly Detection', 'Multivariate Outlier Analysis'
    ]
}

# Define banking features
banking_features = [
    "customer age", "customer income", "account balance", "length of relationship with bank", "transaction history",
    "credit score", "number of accounts", "loan amounts and types", "payment history", "employment status",
    "residential status", "marital status", "educational background", "investment holdings", "digital engagement level",
    "overdraft frequency", "savings account usage", "debit and credit card usage", "ATM withdrawals",
    "direct deposit information", "geographic location", "insurance policies", "customer feedback and satisfaction levels",
    "mobile banking usage", "social media activity", "fraud reports", "loan default rates", "website interaction patterns",
    "call center interaction frequencies", "product portfolio size"
]

# Define actions associated with each intent
actions = {
    "plot_graph": [
        "plot a histogram for", "visualize the trend of", "create a pie chart for", "generate a line graph of",
        "show a bar chart for"
    ],
    "test_stats": [
        "conduct a normality test for", "perform a t-test on", "execute an ANOVA for", "calculate the chi-square for",
        "determine the correlation between"
    ],
    "detect_anomaly": [
        "detect anomalies in", "identify outliers within", "find unusual patterns in", "isolate abnormal transactions in",
        "highlight unusual customer behavior in"
    ]
}

# Function to generate a meaningful query based on intent, action, and feature
def generate_query_with_category(intent, action, feature):
    technique = random.choice(technique_categories[intent])
    return f"{action} {feature} using {technique}."

# Generate the dataset
data_categorized = {"Query Generated": [], "Intent": []}
for _ in range(2000):
    intent = random.choice(list(actions.keys()))
    action = random.choice(actions[intent])
    feature = random.choice(banking_features)
    query = generate_query_with_category(intent, action, feature)
    data_categorized["Query Generated"].append(query)
    data_categorized["Intent"].append(intent)

# Create DataFrame and save to CSV
df_categorized = pd.DataFrame(data_categorized)
csv_file_path_categorized = "/mnt/data/generated_queries_dataset_categorized.csv"
df_categorized.to_csv(csv_file_path_categorized, index=False)
