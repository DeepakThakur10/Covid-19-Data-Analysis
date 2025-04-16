# Covid-19-Data-Analysis
This Python script provides a comprehensive exploratory data analysis (EDA) of provisional COVID-19 death statistics in the U.S., segmented by sex, age group, and state. 
The data is visualized using histograms, time series, bar charts, and correlation heatmaps.

📦 Dependencies
Make sure you have the following Python libraries installed:

pip install pandas numpy seaborn matplotlib

▶️ How to Run


Place the dataset in the specified location or update the DATA_PATH in the script.

Run the script:

python covid_analysis.py

You'll be prompted:

Do you want to run interactive analysis? (y/n):

Enter y for an interactive menu-driven analysis.

Enter n to run all plots automatically.

📊 Features & Plots

The script includes the following functionalities:

Basic Data Statistics

Summary of COVID-19 deaths

Percentage of total deaths due to COVID-19

Distribution of COVID-19 Deaths

Histogram with KDE of COVID-19 death counts

COVID-19 Deaths Over Time

Time series showing cumulative deaths

Deaths by Sex

Bar chart comparing male vs. female deaths

Deaths by Age Group

Bar chart comparing age groups

Top States by COVID-19 Deaths

Top 10 states with the highest COVID-19 death totals

Correlation Heatmap

Heatmap showing relationships between different death causes

Mean COVID-19 Deaths by Age Group and Sex

Grouped bar chart visualizing average deaths by category

🧹 Data Cleaning Steps

Rows with missing critical values (death counts) are removed.

Non-essential columns like Footnote and Data As Of are dropped.

Date columns are parsed as datetime objects for time-based plotting.

✅ Output

The tool produces a series of interactive or auto-displayed plots and statistics in the terminal and graphical windows.



