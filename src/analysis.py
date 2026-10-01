import pandas as pd
import matplotlib.pyplot as plt
import pycountry

file_path = "dataset/API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"

df = pd.read_csv(file_path, skiprows=4)

# Get ISO-3 country codes
country_codes = {country.alpha_3 for country in pycountry.countries}

# Keep only actual countries
countries = df[df["Country Code"].isin(country_codes)].copy()

# Select country name and 2024 population
population_2024 = countries[["Country Name", "2024"]].copy()

# Remove missing values
population_2024 = population_2024.dropna(subset=["2024"])

# Sort from highest to lowest
population_2024 = population_2024.sort_values(
    "2024",
    ascending=False
)

# Select top 10 countries
top_10 = population_2024.head(10)

# Create chart
fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(
    top_10["Country Name"],
    top_10["2024"]
)

ax.set_title(
    "Top 10 Most Populous Countries in 2024",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel("Country", fontsize=12)
ax.set_ylabel("Population", fontsize=12)

plt.xticks(rotation=45, ha="right")

# Give extra space above the tallest bar
ax.set_ylim(0, top_10["2024"].max() * 1.12)

# Add values above each bar
for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + (top_10["2024"].max() * 0.01),
        f"{height / 1e9:.2f}B",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

# Save chart
plt.savefig(
    "output/top_10_population_2024.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()