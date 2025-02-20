#!/usr/bin/python3

import argparse
from sys import exit

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
Calculadora de IRS Jovem

Esta ferramenta calcula o IRS Jovem com base no salário bruto mensal e anos de trabalho.
Aplica-se a jovens entre 18 e 26 anos (até 30 no caso de doutoramento).

A isenção é aplicada da seguinte forma:
    • 1º ano: 100% de isenção
    • 2º a 4º ano: 75% de isenção
    • 5º a 7º ano: 50% de isenção
    • 8º a 10º ano: 25% de isenção
"""
    )
    
    args = parser.parse_args()

    try:
        print("Calculadora de IRS Jovem\n")
        
        # Get salary input with validation
        while True:
            try:
                salary = float(input("Introduza o salário bruto mensal (€): ").replace(',', '.'))
                if salary <= 0:
                    print("O salário deve ser superior a 0€.")
                    continue
                break
            except ValueError:
                print("Por favor, introduza um valor numérico válido.")

        # Get years working with validation
        while True:
            try:
                years = int(input("Introduza o número de anos de trabalho (1-10): "))
                if years < 1 or years > 10:
                    print("O número de anos deve estar entre 1 e 10.")
                    continue
                break
            except ValueError:
                print("Por favor, introduza um número inteiro válido.")
        # Get Holiday and Christmas Allowances in twelfths
        while True:
            try:
                isDuodecimos = str(input("Recebes subsídios em duodécimos? (S / N): "))
                if isDuodecimos not in ["S", "N"]:
                    print("Introduz 'S' para sim ou 'N' para não.")
                    continue
                isDuodecimos = isDuodecimos == "S"
                break
            except ValueError:
                print("Por favor, introduza um número inteiro válido.")

        result = calculate_irs_jovem(salary, years, isDuodecimos)
        
        print("\nResultados:")
        print("-" * 50)
        for key, value in result.items():
            print(f"{key}: {value:.2f}€")

    except KeyboardInterrupt:
        print("\nOperação cancelada pelo utilizador.")
        exit(0)
    except Exception as e:
        print(f"\nErro: {str(e)}")
        exit(1)

def calculate_irs_jovem(salary, years_working, isDuodecimos):
    # Tax brackets for unmarried without dependents (Tabela I)
    tax_brackets = [
        (870.00, 0.00, 0.00),
        (992.00, 0.13, 73.12),
        (1070.00, 0.165, 90.81),
        (1136.00, 0.165, 90.81),
        (1187.00, 0.22, 153.29),
        (1787.00, 0.25, 188.90),
        (2078.00, 0.32, 313.99),
        (2432.00, 0.355, 386.72),
        (3233.00, 0.3872, 465.03),
        (5547.00, 0.4005, 508.03),
        (20221.00, 0.4495, 779.83),
        (float('inf'), 0.4717, 1228.74)
    ]
    
    # Constants
    monthly_exemption_limit = 2052.68  # 55*IAS (522.50)/14 = 28,737.50€/14
    social_security_rate = 0.11  # 11%

    if isDuodecimos:
        # Calculate total monthly gross with duodécimos
        subsidio_ferias = salary
        subsidio_natal = salary
        monthly_ferias = subsidio_ferias / 12
        monthly_natal = subsidio_natal / 12
        monthly_gross = salary + monthly_ferias + monthly_natal
    else:
        monthly_gross = salary

    # Determine exemption percentage
    def get_exemption_percentage(years):
        if years < 1: return 0.0
        elif years == 1: return 1.0    # 100%
        elif 2 <= years <= 4: return 0.75  # 75%
        elif 5 <= years <= 7: return 0.5   # 50%
        elif 8 <= years <= 10: return 0.25  # 25%
        else: return 0.0
    
    exemption_percent = get_exemption_percentage(years_working)
    exempt_value = min(monthly_gross * exemption_percent, monthly_exemption_limit)
    taxable_value = monthly_gross - exempt_value

    # Calculate IRS tax on full salary
    def calculate_full_irs(gross_salary):
        for bracket in tax_brackets:
            upper, rate, deduction = bracket
            if gross_salary <= upper:
                tax = (gross_salary * rate) - deduction
                return max(tax, 0)  # No negative tax
        return 0
    
    full_tax = calculate_full_irs(monthly_gross)
    effective_rate = full_tax / monthly_gross if monthly_gross > 0 else 0
    irs_tax = taxable_value * effective_rate

    # Calculate Social Security and net salary
    social_security = monthly_gross * social_security_rate
    net_salary = monthly_gross - irs_tax - social_security

    if isDuodecimos:
        return {
            "Salário Base (€)": round(salary, 2),
            "Subsídio de Férias Mensal (€)": round(monthly_ferias, 2),
            "Subsídio de Natal Mensal(€)": round(monthly_natal, 2),
            "Salário Bruto Mensal (€)": round(monthly_gross, 2),
            "Valor Isento (€)": round(exempt_value, 2),
            "Valor Sujeito (€)": round(taxable_value, 2),
            "IRS (€)": round(irs_tax, 2),
            "Segurança Social (€)": round(social_security, 2),
            "Salário Líquido (€)": round(net_salary, 2),
        }
    else:
        return {
            "Salário Base (€)": round(salary, 2),
            "Valor Isento (€)": round(exempt_value, 2),
            "Valor Sujeito (€)": round(taxable_value, 2),
            "IRS (€)": round(irs_tax, 2),
            "Segurança Social (€)": round(social_security, 2),
            "Salário Líquido (€)": round(net_salary, 2),
        }

if __name__ == "__main__":
    main()