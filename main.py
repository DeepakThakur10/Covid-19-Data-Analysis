import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
DATA_PATH = "E:\\Python CA2\\Provisional_COVID-19_Deaths_by_Sex_and_Age.csv"
# ---------------------- Data Loading ------------------------
print(" Loading CSV file...")
df = pd.read_csv(DATA_PATH)
print(f"Successfully loaded data with {df.shape[0]} rows and {df.shape[1]} columns")


# ---------------------- Basic Overview ----------------------
print("\n Basic Info:")
print(df.info())

print("\n First 5 Rows:")
print(df.head(5))

print("\n Statistical Summary:")
print(df.describe())

# ---------------------- Missing Values ----------------------
print("\n Checking for missing values:")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])  # Only show columns with missing values

# ---------------------- Data Cleaning -----------------------
print("\n Cleaning data: Removing rows with missing critical values...")
# Track original row count
original_count = len(df)

df_cleaned = df.dropna(subset=[
    "COVID-19 Deaths", "Total Deaths", "Pneumonia Deaths", 
    "Pneumonia and COVID-19 Deaths", "Influenza Deaths", 
    "Pneumonia, Influenza, or COVID-19 Deaths"
])

print(f" Removed {original_count - len(df_cleaned)} rows with missing values")

print(" Dropping unnecessary columns...")
df_cleaned = df_cleaned.drop(columns=["Footnote", "Data As Of"])

print(" Converting date columns to datetime format...")
df_cleaned["Start Date"] = pd.to_datetime(df_cleaned["Start Date"])
df_cleaned["End Date"] = pd.to_datetime(df_cleaned["End Date"])

df_cleaned.reset_index(drop=True, inplace=True)
print(f"\n Cleaned data now has {len(df_cleaned)} rows")

# ------------------ Set Plot Style ----------------------
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# ------------------ Interactive Plotting Functions ------------------------

def plot_distribution():
    """Plot distribution of COVID-19 deaths"""
   
    print("\n Plotting Distribution of COVID-19 Deaths...")

    sns.histplot(df_cleaned["COVID-19 Deaths"], bins=50, kde=True, color="red")
    plt.title("Distribution of COVID-19 Deaths")
    plt.xlabel("Number of Deaths")
    plt.show()

def plot_time_series():
    """Plot COVID-19 deaths over time"""
    
    print("\n COVID-19 Deaths Over Time...")
 
    covid_time = df_cleaned.groupby("End Date")["COVID-19 Deaths"].sum()
    covid_time.plot(title="COVID-19 Deaths Over Time", color='red')
    plt.xlabel("Date")
    plt.ylabel("Deaths")
   
    plt.show()

def plot_deaths_by_sex():
    """Plot deaths by sex"""
   
    print("\n Plotting Deaths by Sex...")
   
    sex_group = df_cleaned.groupby("Sex")[["COVID-19 Deaths", "Total Deaths"]].sum()
    sex_group.plot(kind="bar", title="Deaths by Sex")
    plt.ylabel("Number of Deaths")
   
    plt.show()

def plot_deaths_by_age():
    """Plot deaths by age group"""
     
    print("\n Plotting Deaths by Age Group...")
   
    age_group = df_cleaned.groupby("Age Group")[["COVID-19 Deaths", "Total Deaths"]].sum()
    age_group.plot(kind="bar", title="Deaths by Age Group")
    plt.ylabel("Number of Deaths")
    plt.xticks(rotation=45)
  
    plt.show()

def plot_top_states():
    """Plot top states by COVID-19 deaths"""
    print(f"\n Top 10 States by COVID-19 Deaths...")

    state_group = df_cleaned.groupby("State")["COVID-19 Deaths"].sum().sort_values(ascending=False).head(10)
    state_group.plot(kind="bar", title=f"Top 10 States by COVID-19 Deaths", color='purple')
    plt.ylabel("COVID-19 Deaths")
    plt.xticks(rotation=45)
    plt.show()

def plot_correlation_heatmap():
    """Plot correlation heatmap between death types"""

    print("\n Correlation between causes of death...")
   
    corr_matrix = df_cleaned[[
        "COVID-19 Deaths", "Total Deaths", "Pneumonia Deaths",
        "Pneumonia and COVID-19 Deaths", "Influenza Deaths",
        "Pneumonia, Influenza, or COVID-19 Deaths"
    ]].corr()

    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
    plt.title("Correlation Between Causes of Death")
    plt.tight_layout()
    plt.show()

def plot_deaths_by_age_and_sex():
    """Plot mean deaths by age group and sex"""
      
    print("\n Mean COVID-19 Deaths by Age Group and Sex...")
    
    grouped_mean = df_cleaned.groupby(["Age Group", "Sex"])["COVID-19 Deaths"].mean().unstack()
    grouped_mean.plot(kind="bar", stacked=False)
    plt.ylabel("Average COVID-19 Deaths")
    plt.title("Mean COVID-19 Deaths by Age Group and Sex")
    plt.xticks(rotation=45)
    plt.legend(title="Sex")
    
    plt.show()

def run_interactive_analysis():
    """Run an interactive menu for analysis options"""
    while True:
        print("\n" + "="*50)
        print("COVID-19 DATA ANALYSIS MENU")
        print("="*50)
        print("1. Basic Data Statistics")
        print("2. Distribution of COVID-19 Deaths")
        print("3. COVID-19 Deaths Over Time")
        print("4. Deaths by Sex")
        print("5. Deaths by Age Group")
        print("6. Top States by COVID-19 Deaths")
        print("7. Correlation Heatmap")
        print("8. Mean Deaths by Age Group and Sex")
        print("9. Run All Analyses")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-9): ")
        
        if choice == '1':
            print("\n COVID-19 Death Statistics:")
            death_stats = df_cleaned["COVID-19 Deaths"].describe()
            print(death_stats)
            
            total_covid = df_cleaned["COVID-19 Deaths"].sum()
            total_deaths = df_cleaned["Total Deaths"].sum()
            print(f"\nTotal COVID-19 Deaths: {total_covid:,}")
            print(f"COVID-19 as % of Total Deaths: {(total_covid/total_deaths)*100:.2f}%")
            
        elif choice == '2':
            plot_distribution()
        elif choice == '3':
            plot_time_series()
        elif choice == '4':
            plot_deaths_by_sex()
        elif choice == '5':
            plot_deaths_by_age()
        elif choice == '6':
            plot_top_states()
        elif choice == '7':
            plot_correlation_heatmap()
        elif choice == '8':
            plot_deaths_by_age_and_sex()
        elif choice == '9':
            plot_distribution()
            plot_time_series()
            plot_deaths_by_sex()
            plot_deaths_by_age()
            plot_top_states()
            plot_correlation_heatmap()
            plot_deaths_by_age_and_sex()
        elif choice == '0':
            print("\nThank you for using the COVID-19 Data Analysis Tool!")
            break
        else:
            print("Invalid choice. Please try again.")

# ------------------- MAIN EXECUTION ----------------------

# Ask user if they want to run interactive mode
run_interactive = input("\nDo you want to run interactive analysis? (y/n): ")
if run_interactive.lower() == 'y':
    run_interactive_analysis()
else:
    # Run all plots automatically
    print("You Entered Wrong Input , Now You Have To Face So Many Graphs And All")
    plot_distribution()
    plot_time_series()
    plot_deaths_by_sex()
    plot_deaths_by_age()
    plot_top_states()
    plot_correlation_heatmap()
    plot_deaths_by_age_and_sex()
    
    print("\n All analysis complete!")
