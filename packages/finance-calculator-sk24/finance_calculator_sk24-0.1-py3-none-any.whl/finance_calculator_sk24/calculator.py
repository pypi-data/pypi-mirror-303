def calculate_net_profit(revenue, costs):
    """Calculate net profit."""
    return revenue - costs

def calculate_roi(net_profit, costs):
    """Calculate ROI."""
    if costs == 0:
        raise ValueError("Costs cannot be zero for ROI calculation.")
    return (net_profit / costs) * 100
