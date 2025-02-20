

# Calculadora IRS Jovem 2025 🇵🇹
Script em Python para calcular o IRS Jovem para 2025. O script tem em consideração [esta nota](https://info.portaldasfinancas.gov.pt/pt/atualidades/instrucoesadmin/Paginas/Oficio_circulado_20274_2025.aspx).

## Descrição

Esta calculadora aplica os benefícios fiscais do IRS Jovem de acordo com as seguintes regras de isenção:
- 1º ano: 100% de isenção
- 2º ao 4º ano: 75% de isenção
- 5º ao 7º ano: 50% de isenção
- 8º ao 10º ano: 25% de isenção

A isenção aplica-se até ao limite mensal de 2.052,68€.

## Pré-requisitos

- Python 3.x

## Instalação

1. Clona este repositório:
```sh
git clone https://github.com/yourusername/irs_jovem_2025.git
cd irs_jovem_2025
```

2. Torna o script executável (sistemas Unix/Linux):
```sh
chmod +x calculate_irs_jovem.py
```

## Utilização
Podes executar o script de duas formas:

1. Usando Python diretamente:
```sh
python3 calculate_irs_jovem.py
```

2. Como executável (sistemas Unix/Linux):
```sh
./calculate_irs_jovem.py
```

O script pedirá interactivamente:
- Salário bruto mensal
- Número de anos de trabalho (1-10)
- Se recebe subsídios de Férias e Natal em duodécimos

### Exemplo de Resultado

```sh
Calculadora de IRS Jovem

Introduza o salário bruto mensal (€): 1500
Introduza o número de anos de trabalho (1-10): 1
Recebes subsídios em duodécimos? (S / N): N

Resultados:
--------------------------------------------------
Salário Base (€): 1500.00€
Valor Isento (€): 1500.00€
Valor Sujeito (€): 0.00€
IRS (€): 0.00€
Segurança Social (€): 165.00€
Salário Líquido (€): 1335.00€
```

## Licença
Este projeto está licenciado sob a Apache License 2.0 - consulta o ficheiro [LICENSE](/LICENSE) para mais detalhes.

## Contribuições
Sente-te à vontade para abrir issues ou submeter pull requests com melhorias.





# IRS JOVEM 2025 🏴󠁧󠁢󠁥󠁮󠁧󠁿
Python script to calculate IRS Jovem for 2025. The script takes into consideration [this note](https://info.portaldasfinancas.gov.pt/pt/atualidades/instrucoesadmin/Paginas/Oficio_circulado_20274_2025.aspx).

## Description

This calculator applies the IRS Jovem tax benefits according to the following exemption rules:
- 1st year: 100% exemption
- 2nd to 4th year: 75% exemption 
- 5th to 7th year: 50% exemption
- 8th to 10th year: 25% exemption

The exemption applies up to a monthly limit of 2,052.68€.

## Prerequisites

- Python 3.x

## Installation

1. Clone this repository:
```sh
git clone https://github.com/yourusername/irs_jovem_2025.git
cd irs_jovem_2025
```

2. Make the script executable (Unix/Linux systems):

```sh
chmod +x calculate_irs_jovem.py
```


## Usage
You can run the script in two ways:

1. Using Python directly:

```sh
python3 calculate_irs_jovem.py
```

2. As an executable (Unix/Linux systems):

```sh
./calculate_irs_jovem.py
```

The script will interactively ask for:

Monthly gross salary - Salário Bruto
Number of years working (1-10)
Whether you receive holiday and Christmas allowances in twelfths ("duodécimos")

The script will interactively ask for:

### Example Output

```sh
Calculadora de IRS Jovem

Introduza o salário bruto mensal (€): 1500
Introduza o número de anos de trabalho (1-10): 1
Recebes subsídios em duodécimos? (S / N): N

Resultados:
--------------------------------------------------
Salário Base (€): 1500.00€
Valor Isento (€): 1500.00€
Valor Sujeito (€): 0.00€
IRS (€): 0.00€
Segurança Social (€): 165.00€
Salário Líquido (€): 1335.00€
```


## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](/LICENSE) file for details.

## Contributing
Feel free to open issues or submit pull requests with improvements.
