from langchain_core.tools import tool

@tool
def roe(net_income: float, equity: float) -> float:
    return net_income / equity

@tool
def roic(operating_income: float, total_debt: float, equity: float, cash_and_equivalents: float, tax_rate: float = 0.35) -> float:
    net_operating_profit_after_tax = operating_income * (1 - tax_rate)
    invested_capital = total_debt + equity - cash_and_equivalents
    return net_operating_profit_after_tax / invested_capital

@tool
def owner_earnings(net_income: float, depreciation_amortization: float = 0.0, capital_expenditures: float = 0.0) -> float:
    return net_income + depreciation_amortization - capital_expenditures

@tool
def intrinsic_value(free_cash_flow: float, growth_rate: float = 0.05, discount_rate: float = 0.10, terminal_growth_rate: float = 0.02, num_years: int = 5) -> float:
    cash_flows = [free_cash_flow * (1 + growth_rate) ** i for i in range(num_years)]
    present_values = [cash_flows[i] / (1 + discount_rate) ** (i + 1) for i in range(num_years)]
    terminal_value = cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    terminal_present_value = terminal_value / (1 + discount_rate) ** num_years
    return sum(present_values) + terminal_present_value