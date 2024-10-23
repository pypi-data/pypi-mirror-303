def net_profit(revenue, costs):
    return revenue - costs


def calculate_roi(profit, costs):
    if costs == 0:
        raise ValueError("Затраты не могут быть равны нулю при расчёте ROI.")

    roi = (profit / costs) * 100

    return round(roi, 2)
