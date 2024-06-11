import pandas as pd

# Previous financial trends derived in Task 1
df = pd.read_csv('/Users/naishasinha/Downloads/BCGenAI_Task1.csv')

df['Total Revenue (in millions)'] = pd.to_numeric(df['Total Revenue (in millions)'], errors='coerce')
df['Net Income (in millions)'] = pd.to_numeric(df['Net Income (in millions)'], errors='coerce')

df['Total Assets (in millions)'] = pd.to_numeric(df['Total Assets (in millions)'], errors='coerce')
df['Total Liabilities (in millions)'] = pd.to_numeric(df['Total Liabilities (in millions)'], errors='coerce')
df['Cash Flow from Operating Activities (in millions)'] = pd.to_numeric(df['Cash Flow from Operating Activities (in millions)'], errors='coerce')

total_revenue = df['Total Revenue (in millions)'].sum()
net_income_change = df['Net Income (in millions)'].pct_change().iloc[-1] * 100 

mean_values = df.groupby('Company')[['Total Assets (in millions)', 'Total Liabilities (in millions)', 'Cash Flow from Operating Activities (in millions)']].mean()

highest_revenue_year = df.loc[df['Total Revenue (in millions)'].idxmax()]['Fiscal Year']
lowest_revenue_year = df.loc[df['Total Revenue (in millions)'].idxmin()]['Fiscal Year']

# Define predefined queries
def simple_chatbot(user_query):
   if user_query == "What is the total revenue?":
       return f"The total revenue is {total_revenue} million."
   elif user_query == "How has net income changed over the last year?":
       return f"The net income has changed by {net_income_change}% over the last year."
   elif user_query == "What are the average balance sheet values by company?":
       balance = "Average Assets, Liabilities, and Cash Flow (Operating) by Company:\n"
       for company, row in mean_values.iterrows():
        balance += f"{company}: Average Assets = {row['Total Assets (in millions)']:.2f} million, Average Liabilities = {row['Total Liabilities (in millions)']:.2f} million, "\
        f"Average Cash Flow = {row['Cash Flow from Operating Activities (in millions)']} million\n"
       return balance
   elif user_query == "Which year had the highest revenue?":
        return f"The year with the higest revenue was {highest_revenue_year}"
   elif user_query == "Which year had the lowest revenue?":
        return f"The year with the lowest revenue was {lowest_revenue_year}"
   else:
       return "Sorry, I can only provide information on predefined queries."

if __name__ == "__main__":
    print("Welcome to the Financial Chatbot!")
    print("This is the simplest version so far. As of now, you can ask the following questions:")
    print("- What is the total revenue?")
    print("- How has net income changed over the last year?")
    print("- What are the average balance sheet values by company?")
    print("- Which year had the highest revenue?")
    print("- Which year had the lowest revenue?")

    while True:
        user_query = input("Please enter your query (or type exit or quit to end): ")
        if user_query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = simple_chatbot(user_query)
        print(response)
    