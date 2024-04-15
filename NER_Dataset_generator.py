import pandas as pd
import random

# Define technique categories
technique_categories = [
    'Scatter Chart', 'Point Graph', 'XY Plot', 'Bivariate Distribution Chart', 'Data Scatter Plot',
    'Heatmap', 'Intensity Map', 'Data Matrix Visualization', 'Color-Coded Thermal Map', 'Line Plot',
    'Trend Graph', 'Time Series Plot', 'Continuous Line Graph', 'Data Line Graph',
    'Normality Test', 'Distribution Assessment', 'Goodness-of-Fit Test', 'Statistical Normalcy Check',
    'Standard Deviation Test', 'Single-Sample Z-test', 'Two-Sample Z-test', 'Z Test',
    'ADFuller', 'Stationarity Test', 'Time Series Analysis Test', 'Dickey-Fuller Test', 'DBScan',
    'Density Clustering', 'Spatial Clustering', 'Noise Filtering Analysis', 'Isolation Forest',
    'Anomaly Detection', 'Outlier Identification', 'Isolation Analysis', 'ABOD', 'Outlier Detection',
    'Angle-Based Anomaly Detection', 'Multivariate Outlier Analysis',
    'Chi-Squared Test', 'Mann-Whitney U Test', 'Kruskal-Wallis Test', 'Fisher’s Exact Test', 'Shapiro-Wilk Test',
    'Linear Regression', 'Logistic Regression', 'Support Vector Machines', 'Decision Trees', 'Random Forests',
    'Gradient Boosting Machines', 'K-Means Clustering', 'Hierarchical Clustering', 'Neural Networks', 'Deep Learning',
    'Principal Component Analysis', 'Linear Discriminant Analysis', 'Naive Bayes Classifier', 'K-Nearest Neighbors', 'Ensemble Methods',
    'Convolutional Neural Networks', 'Recurrent Neural Networks', 'Long Short-Term Memory Networks', 'Generative Adversarial Networks',
    'Autoencoders', 'Transformer Models', 'BERT Models', 'ResNet Architectures', 'GANs',
    'Feature Scaling', 'Feature Encoding', 'Data Augmentation', 'Smote', 'Tomek Links', 'Missing Data Imputation',
    'Box Plot', 'Violin Plot', 'Pair Plot', 'Sankey Diagram', 'Radar Chart', 'Tree Map', 'Gantt Chart',
    'Bubble Chart', 'Stream Graph', 'Sunburst Chart',
    'Survival Analysis', 'Time-Series Forecasting', 'Causal Inference Models', 'Recommender Systems',
    'Sentiment Analysis', 'Text Mining', 'Network Analysis', 'Geo-spatial Analysis', 'Bayesian Inference',
    'Monte Carlo Simulation', 'Dynamic Programming', 'Linear Programming', 'Genetic Algorithms', 'Simulated Annealing'
]


# Define banking features (columns)
banking_features = [
    "customer age", "customer income", "account balance", "length of relationship with bank", "transaction history",
    "credit score", "number of accounts", "loan amounts and types", "payment history", "employment status",
    "residential status", "marital status", "educational background", "investment holdings", "digital engagement level",
    "overdraft frequency", "savings account usage", "debit and credit card usage", "ATM withdrawals",
    "direct deposit information", "geographic location", "insurance policies", "customer feedback and satisfaction levels",
    "mobile banking usage", "social media activity", "fraud reports", "loan default rates", "website interaction patterns",
    "call center interaction frequencies", "product portfolio size"
]

# Comparators and example values
comparators = ["greater than", "less than", "equal to"]
values = ["100", "2000", "50000", "100000", "250000"]

# Define types of queries
query_types = [
    "plot {technique} on {column} and {column}",
    "can you do {technique} on {column} when {column} is {comparator} {value}",
    "{column} and {column}",
    "Find me outliers in {column} using {technique}",
    "Show {column} when {column} is {comparator} {value} compared to {column}",
    "What happens to {column} if {column} increases by {value}?",
    "Compare {column} and {column} using {technique} when {column} is {comparator} {value}",
    "Calculate the average of {column} for customers who have {column} {comparator} {value}",
    "Aggregate {column} and {column} by {technique}",
    "Plot a time series of {column} over the last year",
    "How has {column} trended over time? Use {technique} for visualization",
    "Does {column} correlate with {column} when {column} is {comparator} {value}? Use {technique} for analysis",
    "Highlight the peak values in {column} using {technique}",
    "What are the statistical variances between {column} and {column} using {technique}",
    "Identify top {value} {column} using {technique}",
"Display growth in {column} over the past {value} months",
"What is the impact of {column} on {column} when adjusted for {column}?",
"Can {technique} determine the relationship between {column} and {column}?",
"Show changes in {column} after {value} {comparator} in {column}",
"Visualize {column} distribution with {technique}",
"Map {column} against {column} to observe {technique} trends",
"Forecast {column} for the next {value} years using {technique}",
"Assess the risk of {column} based on {column} and {column}",
"Merge {column} and {column} data for advanced {technique} analysis",
"Segment {column} by {column} using {technique} for detailed review",
"Generate a {technique} model to predict {column} from {column}",
"Analyze the cyclic behavior of {column} with {technique}",
"Extract features from {column} to {column} using {technique}",
"Estimate the probability of {column} affecting {column}",
"Review {column} performance by applying {technique}",
"Correlate {column} with multiple variables including {column} and {column}",
"Classify {column} into categories based on {technique}",
"Summarize {column} trends over the last {value} quarters",
"Compare historical data of {column} with current {column} stats",
"Detect seasonality in {column} using {technique}",
"Calculate the growth rate of {column} from {column} data",
"Plot the regression line for {column} against {column} with {technique}",
"Validate {column} consistency across {column} using {technique}",
"Examine the effect of {column} on {column} sales performance",
"Profile customers based on {column} and {column} with {technique}",
"Link {column} to {column} through {technique} pathway analysis",
"Track {column} decline or growth with {technique} over time",
"Align {column} projections with {column} using {technique} insights",
"Query {column} relationships using multidimensional {technique}",
"Overlay {column} on {column} to highlight {technique} findings",
"Simulate potential outcomes if {column} changes by {value} using {technique}",
"Interpret the {technique} output between {column} and {column}",
"Construct a {technique} framework to understand {column} dynamics",
"Dissect {column} contributions to {column} using {technique}",
"Engage in predictive modeling of {column} with {technique}",
"Cross-analyze {column} with {column} under {technique} methodology",
"Devise a strategy to increase {column} based on {technique} results",
"Measure the influence of {column} on {column} with {technique}",
"Break down {column} by {technique} to explore underlying patterns",
"Reconstruct historical changes in {column} with {technique}",
"Apply {technique} to forecast {column} impact on {column}",
"Streamline {column} analysis through automated {technique}",
"Isolate key drivers in {column} using sophisticated {technique}",
"Uncover hidden patterns in {column} with {technique} mapping",
"Examine the linkage between {column} and economic indicators using {technique}",
"Refine {technique} models to increase accuracy in {column} predictions",
"Implement {technique} to overhaul traditional {column} analysis methods",
"Evaluate {column} elasticity in market conditions with {technique}"
]

# Generate queries
data_ner = {"Query": [], "Type": []}
for _ in range(3000):  # Increased dataset size for more diversity
    column1 = random.choice(banking_features)
    column2 = random.choice(banking_features)
    column3 = random.choice(banking_features)
    technique = random.choice(technique_categories)
    comparator = random.choice(comparators)
    value = random.choice(values)
    
    # Avoid using the same column for multiple column entities
    while column1 == column2 or column1 == column3 or column2 == column3:
        column2 = random.choice(banking_features)
        column3 = random.choice(banking_features)

    query_format = random.choice(query_types)
    query = query_format.format(
        technique=technique, 
        column=column1, 
        column2=column2, 
        column3=column3,
        comparator=comparator, 
        value=value
    )

    data_ner["Query"].append(query)
    data_ner["Type"].append("NER Training")

# Create DataFrame and save to CSV
df_ner = pd.DataFrame(data_ner)
csv_file_path_ner = "/mnt/data/generated_ner_queries_dataset.csv"
df_ner.to_csv(csv_file_path_ner, index=False)
