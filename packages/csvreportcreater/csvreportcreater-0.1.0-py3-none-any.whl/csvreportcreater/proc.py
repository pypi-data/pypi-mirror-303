import csv


def create_report(input,output):
    with open(input, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        report = {}
        for row in reader:
            if row['category'] in report.keys():
                report[row['category']][0] += int(row['sales'])
                report[row['category']][1] += int(row['quantity'])
            else:
                report[row['category']] = [int(row['sales']),int(row['quantity'])]

        with open(output, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['category', 'sales', 'quantity'])


            writer.writeheader()
            report_list = []
            for key, value in report.items():
                report_list.append({
                    'category': key,
                    'sales': value[0],
                    'quantity': value[1]
                })
            writer.writerows(report_list)
