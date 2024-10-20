from .calculator import calculate_profit, calculate_roi
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calc net profit and ROI")
    parser.add_argument('--revenue', type=float, required=True, help='revenue')
    parser.add_argument('--costs', type=float, required=True, help='costs')

    args = parser.parse_args()

    net_profit = calculate_profit(args.revenue, args.costs)
    roi = calculate_roi(args.revenue, args.costs)

    print("PROFIT:", net_profit)
    print(f"ROI {roi:.2f}% rubles",)



if __name__ == '__main__':
    main()

