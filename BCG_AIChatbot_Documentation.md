# BCG Financial Chatbot Documentation

This chatbot is a prototype designed to respond to predefined financial queries based on analyzed data from a CSV file. The chatbot provides basic financial insights regarding total revenue, net income, total assets, total liabilities, and Cash Flow from Operating Activities.

## How It Works

The chatbot uses a simple Python script to:
1. Load and prepare financial data from a CSV file.
2. Define predefined queries and map them to specific responses.
3. Use if-else statements to match user input to predefined queries and return the corresponding responses.

## Predefined Queries

The chatbot can respond to the following queries:
- "What is the total revenue?"
- "How has net income changed over the last year?"

## Limitations

- The chatbot can only respond to predefined queries -- this means that it is case-sensitive and word-sensitive.
- It does not handle complex natural language processing or dynamic queries.
- The responses are based on static calculations from the provided data and do not update in real-time.

## Usage

1. Ensure Python and the required libraries (pandas) are installed.
2. Run the script `BCG_AIChatbot.py`.
3. Enter your queries when prompted.
4. To exit the chatbot, type "exit" or "quit".

## Example Interaction (Test Outputs)

Query: What is the total revenue?
Response: The total revenue is 1953761 million.

Query: How has net income changed over the last year?
Response: The net income has changed by -5.133112231095261% over the last year.

Query: What is the net income?
Response: Sorry, I can only provide information on predefined queries.

Query: What are the average balance sheet values by company?
Response: Average Assets, Liabilities, and Cash Flow (Operating) by Company:
Apple: Average Assets = 352113.33 million, Average Liabilities = 293477.33 million, Average Cash Flow = 112244.0 million
Microsoft: Average Assets = 370198.33 million, Average Liabilities = 198614.00 million, Average Cash Flow = 84452.33333333333 million
Tesla: Average Assets = 83695.67 million, Average Liabilities = 36665.67 million, Average Cash Flow = 13159.0 million

Query: Which year had the highest revenue?
Response: The year with the highest revenue was 2022

Query: Which year had the lowest revenue?
Response: The year with the lowest revenue was 2021

Query: exit
Response: Goodbye!