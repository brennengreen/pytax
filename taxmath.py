def calc_total_sale(rate, pre_tax_total):
    total_tax = pre_tax_total * rate
    total_cost = pre_tax_total + total_tax
    return total_cost


def remove_tax(rate, total):
    divide_by = 1 + rate
    no_tax_total = total / divide_by
    return no_tax_total
