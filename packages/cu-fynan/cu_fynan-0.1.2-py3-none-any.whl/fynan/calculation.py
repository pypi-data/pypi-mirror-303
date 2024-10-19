def calculate_net_profit(revenue: float, costs: float) -> float:
    """Функция для расчёта чистой прибыли."""
    return revenue - costs

def calculate_roi(revenue: float, costs: float) -> float:
    """Функция для расчёта ROI (рентабельности инвестиций)."""
    net_profit = calculate_net_profit(revenue, costs)
    if costs == 0:
        return 0
    return (net_profit / costs) * 100
