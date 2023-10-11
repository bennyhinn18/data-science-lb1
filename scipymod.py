from scipy.stats import norm

def calculate_probability(data, value):
    mean = data.mean()
    std_dev = data.std()
    probability = norm.cdf(value, mean, std_dev)
    return probability

def perform_t_test(data1, data2):
    from scipy.stats import ttest_ind
    t_stat, p_value = ttest_ind(data1, data2)
    return t_stat, p_value

def calculate_correlation(data1, data2):
    from scipy.stats import pearsonr
    correlation_coefficient, p_value = pearsonr(data1, data2)
    return correlation_coefficient, p_value
