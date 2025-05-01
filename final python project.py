# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 14:11:30 2025

@author: yashi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="ticks")

#dataset
data = pd.read_csv('C:/Users/shish/OneDrive/Desktop/comprehensive-results-of-general-election-to-lok-sabha-2024.csv')

# Handle missing values
data['EVM_votes'] = data['EVM_votes'].fillna(0)
data['postal_votes'] = data['postal_votes'].fillna(0)
data['total_votes'] = data['total_votes'].fillna(0)


cols_to_fix = ['EVM_votes', 'postal_votes', 'total_votes']
for col in cols_to_fix:
    data[col] = pd.to_numeric(data[col], errors='coerce')


np.random.seed(99)
data['candidate_age'] = np.random.randint(30, 70, size=len(data))
data['gender_identity'] = np.random.choice(['F', 'M', 'X'], size=len(data))
data['license_type'] = np.random.choice(['Verified', 'Lapsed', 'Revoked'], size=len(data))

#ANALYSIS & VISUALIZATIONS
# Bar:Vote counts per top parties
party_votes = data.groupby('party_name')['total_votes'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(11,6))
sns.barplot(x=party_votes.index, y=party_votes.values, palette='cubehelix')
plt.xticks(rotation=45)
plt.title('Major Parties by Vote Count')
plt.ylabel('Votes (in total)')
plt.xlabel('Political Party')
plt.tight_layout()
plt.show()

#Pie: Seat distribution among top parties
top_rank = data[data['rank'] == 1]
party_distribution = top_rank['party_name'].value_counts().head(7)
plt.figure(figsize=(7,7))
plt.pie(party_distribution, labels=party_distribution.index, autopct='%1.2f%%', colors=sns.color_palette('pastel'), startangle=160)
plt.title('Winning Seats Share (Top Parties)')
plt.axis('equal')
plt.show()

#Horizontal Bar: Seats per state
state_rep = top_rank['state_name'].value_counts().sort_values()
plt.figure(figsize=(9,10))
sns.barplot(x=state_rep.values, y=state_rep.index, palette='coolwarm')
plt.title('🏛️ State-wise Winning Constituencies')
plt.xlabel('Number of Seats')
plt.ylabel('State Name')
plt.tight_layout()
plt.show()

#Histogram: Vote distribution
plt.figure(figsize=(9,5))
sns.histplot(data=data, x='total_votes', bins=35, kde=True, color='mediumvioletred')
plt.title('Distribution of Votes per Candidate')
plt.xlabel('Total Votes Received')
plt.ylabel('Frequency')
plt.show()

#Count plot: Gender demographics
plt.figure(figsize=(6,4))
sns.countplot(data=data, x='gender_identity', palette='Set2')
plt.title('🧍 Gender Identity of Contestants (Dummy)')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

#Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(data[['EVM_votes', 'postal_votes', 'total_votes', 'candidate_age']].corr(), annot=True, cmap='flare')
plt.title('Relationship Between Numerical Features')
plt.show()

#summary
print("\n Highlights & Observations:")
print(f"- Leading party by total votes: {party_votes.idxmax()}")
print(f"- Party with highest seats: {party_distribution.idxmax()}")
print(f"- States with maximum seats: \n{state_rep.tail(3)}")
print("\n- Gender distribution:")
print(data['gender_identity'].value_counts())
print("- Avg candidate age (synthetic):", round(data['candidate_age'].mean(), 1))