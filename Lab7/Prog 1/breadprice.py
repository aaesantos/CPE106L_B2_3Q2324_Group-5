'''
**********LABORATORY 7 - POST LAB - PROGRAMMING PROBLEM 1  **********
CPE106L B2 Group 5

Members:
Claros, Angelica
Facal, Ma. Catherina
Santos, Angelica Anne

'''


import pandas as pd
import matplotlib.pyplot as plt

# Define months globally so it's accessible in all functions
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def load_and_clean_data(filepath):
    # Load the data
    data = pd.read_csv(filepath)
    
    # Convert all month columns to float, assuming months are in the correct format
    for month in months:
        data[month] = pd.to_numeric(data[month], errors='coerce')

    # Drop rows where all months are NaN
    data.dropna(subset=months, how='all', inplace=True)

    return data

def plot_average_prices(data):
    # Calculate the average price for each year across all months
    data['Average Price'] = data[months].mean(axis=1)
    
    # Plotting the average prices
    plt.figure(figsize=(10, 5))
    plt.plot(data['Year'], data['Average Price'], marker='o')
    plt.title('Average Bread Price per Year')
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.grid(True)
    plt.xticks(data['Year'].unique())  # Ensure all years are labeled
    plt.show()

def main():
    filepath = 'breadprice.csv'
    data = load_and_clean_data(filepath)
    plot_average_prices(data)

if __name__ == "__main__":
    main()
