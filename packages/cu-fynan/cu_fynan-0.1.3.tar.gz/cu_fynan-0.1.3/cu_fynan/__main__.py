import argparse
from .calculation import calculate_net_profit, calculate_roi

def main():
    
    parser = argparse.ArgumentParser(description="Calculate financial metrics")
    parser.add_argument("--revenue", type=float, required=True, help="Company revenue")
    parser.add_argument("--costs", type=float, required=True, help="Company costs")
    
    args = parser.parse_args()

    revenue = args.revenue
    costs = args.costs

    net_profit = calculate_net_profit(revenue, costs)
    roi = calculate_roi(revenue, costs)

    print(f"Чистая прибыль: {net_profit:.2f} руб.")
    print(f"ROI: {roi:.2f}%")

if __name__ == "__main__":
    main()
