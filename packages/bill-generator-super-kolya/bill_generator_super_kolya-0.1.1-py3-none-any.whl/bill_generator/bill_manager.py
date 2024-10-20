import json


class BillManager:
    def __init__(self, input_file: str):
        self.input_file = input_file

        with open(input_file, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def generate_report(self, output_file: str):
        with open(output_file, 'w', encoding='utf-8') as file:
            order = self.data
            total_bill = 0

            file.write(f"customer_name: {order['customer_name']}\n")
            for item in order['items']:
                file.write(f'\t Name: {item["name"]}\n')
                file.write(f'\t Quantity: {item["quantity"]}\n')
                file.write(f'\t Price: {item["price"]}\n')

                total_bill += item['price'] * item['quantity']

            file.write(f'\n GENERAL BILL: {total_bill}')

        print(f"Bill generated in {output_file}")
