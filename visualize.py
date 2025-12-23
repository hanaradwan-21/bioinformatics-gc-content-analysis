import matplotlib.pyplot as plt
import pandas as pd

# Read data from Excel
try:
    df = pd.read_excel("DNA_Analysis_Results.xlsx")
except:
    print("Error: Please run main.py first!")
    exit()

# Setup the plot
plt.figure(figsize=(10, 6))
colors = ['#3498db', '#2ecc71', '#e74c3c']
bars = plt.bar(df["Species"], df["GC Content (%)"], color=colors, edgecolor='black')

# Add values above bars
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 1,
        f'{yval:.2f}%',
        ha='center',
        va='bottom',
        fontweight='bold'
    )

plt.title('GC Content Comparison Across Species', fontsize=14, fontweight='bold')
plt.ylabel('GC Content (%)')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save high-quality image
plt.savefig("Professional_Chart.png", dpi=300)
plt.show()