def calculate_net_profit(revenue,costs):
    return revenue-costs
def calculate_roi(net_profit,costs):
    if costs == 0:
        raise ValueError("Net profit is zero")
    return (net_profit/costs)*100