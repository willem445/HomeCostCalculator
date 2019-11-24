import argparse
from tabulate import tabulate
import os

class HomeCost:

    def __init__(self, home_cost):
        self.home_cost = home_cost       
        self.down_payment = 0.0
        self.mortgate_amount = 0.0
        self.mortgage_length = 0
        self.closing_cost_amount = 0.0
        self.monthly_pmi_amount = 0.0
        self.monthly_tax_amount = 0.0        
        self.monthly_mortgate_payment_amount = 0.0
        self.monthly_home_insurance_amount = 0.0
        self.pmi_payments = 0

        self.savings_needed = 0.0
        self.total_monthly_cost = 0.0
        self.total_monthly_cost_without_pmi = 0.0
        self.total_pmi_cost = 0.0
        self.total_tax_cost = 0.0
        self.total_home_insurance_cost = 0.0
        self.total_cost = 0.0

    def calculate_totals(self):
        self.savings_needed = self.down_payment + self.closing_cost_amount
        self.total_monthly_cost = self.monthly_pmi_amount + self.monthly_home_insurance_amount + self.monthly_mortgate_payment_amount + self.monthly_tax_amount
        self.total_monthly_cost_without_pmi = self.monthly_home_insurance_amount + self.monthly_mortgate_payment_amount + self.monthly_tax_amount
        self.total_pmi_cost = self.monthly_pmi_amount * self.pmi_payments
        self.total_tax_cost = self.monthly_tax_amount * self.mortgage_length
        self.total_home_insurance_cost = self.monthly_home_insurance_amount * self.mortgage_length
        self._calculate_total_cost()

    def _calculate_total_cost(self):
        if self.pmi_payments == 0:
            self.total_cost = self.total_monthly_cost * self.mortgage_length
        else:
            num_non_pmi_payments = self.mortgage_length - self.pmi_payments
            non_pmi_total = self.total_monthly_cost_without_pmi * num_non_pmi_payments
            pmi_total = self.total_monthly_cost * self.pmi_payments
            self.total_cost = non_pmi_total + pmi_total

class HomeCalculation:

    def __init__(self, min, max, interval):
        self.home_cost_range = []
        self.recommended_monthly_cost = 0.0
        self.max_house_cost = 0.0

        for home_cost in range(min, (max + interval), interval):
            self.home_cost_range.append(HomeCost(home_cost))

    def calculate(self, percent_down_percent, mortgage_rate_percent, loan_length_years, tax_rate_percent, homeowners_insurance_yearly, closing_cost_rate_percent, pmi_percent, gross_income):

        self.recommended_monthly_cost = (gross_income * 0.28) / 12.0
        percent_down = percent_down_percent / 100.0
        mortgage_rate = mortgage_rate_percent / 1200.0
        loan_length_months = loan_length_years * 12
        closing_cost_rate = closing_cost_rate_percent / 100.0
        homeowners_insurance_monthly = homeowners_insurance_yearly / 12.0
        pmi_rate = pmi_percent / 100.0
        tax_rate = tax_rate_percent / 100.0

        for house in self.home_cost_range:
            cost = house.home_cost
            house.mortgage_length = loan_length_months
            house.down_payment = self._calculate_down_payment(cost, percent_down)
            house.mortgate_amount = self._calculate_mortgage_amount(cost, house.down_payment)
            house.closing_cost_amount = self._calculate_closing_cost(cost, closing_cost_rate)
            house.monthly_home_insurance_amount = homeowners_insurance_monthly
            house.monthly_mortgate_payment_amount = self._calculate_mortgage_payment(house.mortgate_amount, mortgage_rate, loan_length_months)
            house.monthly_tax_amount = self._calculate_monthly_tax(cost, tax_rate)

            if percent_down_percent < 20.0:
                house.monthly_pmi_amount = self._calculate_monthly_pmi(house.mortgate_amount, pmi_rate)
                house.pmi_payments = self._calculate_num_pmi_payments(cost, house.mortgate_amount, house.monthly_mortgate_payment_amount, mortgage_rate)

            house.calculate_totals()

        self.max_house_cost = self._find_max_home_cost(self.recommended_monthly_cost)

    def _find_max_home_cost(self, recommended_monthly_cost):
        max_house_cost = 0.0
        for house in self.home_cost_range:
            if house.total_monthly_cost < recommended_monthly_cost:
                max_house_cost = house.home_cost
            else:
                break

        return max_house_cost

    def show_results(self):
        self._report_table()
        print("")
        print("You can afford a house priced at ${} or less.".format(self.max_house_cost))

    def _report_table(self):
        table = []
        headers = [
            "House Cost",
            "Mortgage",
            "Initial Saved",
            "Monthly Payment",
            "Non-PMI Monthly Payment",
            "Total PMI",
            "Total Tax",
            "Total Home Insurance",
            "Total Cost"
        ]

        for house in self.home_cost_range:
            row = []
            row.append(house.home_cost)
            row.append(house.mortgate_amount)
            row.append(house.savings_needed)
            row.append(house.total_monthly_cost)
            row.append(house.total_monthly_cost_without_pmi)
            row.append(house.total_pmi_cost)
            row.append(house.total_tax_cost)
            row.append(house.total_home_insurance_cost)
            row.append(house.total_cost)
            table.append(row)

        print(tabulate(table, headers, tablefmt="github"))

    def _calculate_down_payment(self, home_price, percent_down):
        return home_price * percent_down

    def _calculate_mortgage_amount(self, home_price, down_payment):
        return home_price - down_payment

    def _calculate_closing_cost(self, home_price, closing_rate):
        return home_price * closing_rate

    def _calculate_monthly_pmi(self, mortgage, rate):
        return (mortgage * rate) / 12.0

    def _calculate_monthly_tax(self, home_price, rate):
        return (home_price * rate) / 12.0

    def _calculate_mortgage_payment(self, mortgage, rate, length):
        num = rate * (pow((1+rate), length))
        den = (pow((1+rate), length)) - 1
        return mortgage * ( num / den )

    def _calculate_num_pmi_payments(self, house_value, mortgage, payment, rate):
        ltv80 = house_value * 0.8

        found = False
        payment_number = 1
        while not found:
            balance = (mortgage * (pow((1 + rate), payment_number))) - (payment * (((pow((1 + rate), payment_number)) - 1) / rate))

            if balance <= ltv80:
                found = True
            else:
                payment_number = payment_number + 1

        return payment_number

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-min', action = 'store', dest='range_minimum', help='sum the integers (default: find the max)')
    parser.add_argument('-max', action = 'store', dest='range_maximum', help='sum the integers (default: find the max)')
    parser.add_argument('-interval', action = 'store', dest='range_interval', help='sum the integers (default: find the max)')
    parser.add_argument('-mortgage_rate', action = 'store', dest='mortgate_rate', help='sum the integers (default: find the max)')
    parser.add_argument('-percent_down', action = 'store', dest='percent_down', help='sum the integers (default: find the max)')
    parser.add_argument('-closing_cost_rate', action = 'store', dest='closing_cost_rate', help='sum the integers (default: find the max)')
    parser.add_argument('-pmi_rate', action = 'store', dest='pmi_rate', help='sum the integers (default: find the max)')
    parser.add_argument('-tax_rate', action = 'store', dest='tax_rate', help='sum the integers (default: find the max)')
    parser.add_argument('-homeowners_insurance', action = 'store', dest='homeowners_insurance', help='sum the integers (default: find the max)')
    parser.add_argument('-loan_length', action = 'store', dest='loan_length', help='sum the integers (default: find the max)')
    parser.add_argument('-gross_income', action = 'store', dest='gross_income', help='sum the integers (default: find the max)')
    args = parser.parse_args()

    homeCalculation = HomeCalculation(int(args.range_minimum), int(args.range_maximum), int(args.range_interval))
    homeCalculation.calculate(
        float(args.percent_down),
        float(args.mortgate_rate),
        float(args.loan_length),
        float(args.tax_rate),
        float(args.homeowners_insurance),
        float(args.closing_cost_rate),
        float(args.pmi_rate),
        float(args.gross_income)
    )
    homeCalculation.show_results()

if __name__ == "__main__":
    main()