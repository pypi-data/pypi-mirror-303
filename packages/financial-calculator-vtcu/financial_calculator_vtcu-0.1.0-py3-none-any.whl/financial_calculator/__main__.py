import argparse
from .calculations import net_profit, calculate_roi


def main_menu():
    parser = argparse.ArgumentParser(
        description="Рассчёт чистой прибыли и рентабельности инвестиций (ROI)."
    )

    parser.add_argument(
        '--revenue',
        type=float,
        required=True,
        help='Доходы компании (руб.)'
    )

    parser.add_argument(
        '--costs',
        type=float,
        required=True,
        help='Затраты компании (руб.)'
    )

    args = parser.parse_args()

    try:
        profit = net_profit(args.revenue, args.costs)
        roi = calculate_roi(profit, args.costs)
        print(f"Чистая прибыль: {profit} руб.")
        print(f"ROI: {roi:.2f}%")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main_menu()
