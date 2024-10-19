import pandas as pd

def generate_report(input_file):
    # Загружаем данные из CSV
    data = pd.read_csv(input_file)

    # Группируем данные по категории
    report = data.groupby('category').agg(
        sales=('sales', 'sum'),
        quantity=('quantity', 'sum')
    ).reset_index()

    return report