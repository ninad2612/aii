import pandas as pd
import scipy.stats as stats

df = pd.read_excel('exp3_Pre_Post_Score.xlsx')

print("Initial Data:")
print(df.info())
print(df.head(11))

column_name = 'Rice_Bag_Weight'  

df = df.dropna(subset=[column_name])

population_mean = 25

t_stat, p_value = stats.ttest_1samp(df[column_name], population_mean)

# Display results
print("\nOne-Sample t-test Results:")
print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")


alpha = 0.05  # Significance level
if p_value < alpha:
    print("Result: Reject the null hypothesis (Significant difference found).")
else:
    print("Result: Fail to reject the null hypothesis (No significant difference found).")


# # import pandas as pd
# import scipy.stats as stats

# # Load Pre-Post Score dataset
# pre_post_file = "exp3_Pre_Post_Score.xlsx"
# pre_post_df = pd.read_excel(pre_post_file)

# # Display first few rows to inspect the data
# print("Pre-Post Score Data:")
# print(pre_post_df.head())

# # Assuming 'Pre_Score' and 'Post_Score' are the correct column names
# pre_col, post_col = 'Pre_Score', 'Post_Score'


# # Drop NaN values if any
# pre_post_df = pre_post_df.dropna(subset=[pre_col, post_col])


# # Perform Paired Sample t-test
# t_stat, p_value_two_tail = stats.ttest_rel(pre_post_df[pre_col], pre_post_df[post_col])
# p_value_one_tail = p_value_two_tail / 2

# # T Critical Values
# alpha = 0.05



# # Conclusion based on p-value
# if p_value_two_tail < alpha:
#     print("Result: Reject the null hypothesis (Significant difference found).")
# else:
#     print("Result: Fail to reject the null hypothesis (No significant difference found).")
