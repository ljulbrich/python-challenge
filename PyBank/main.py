import csv
from pathlib import Path
import numpy

# Creating variables
csv_path = Path('Resources/budget_data.csv')
month_count = 0
net_total = 0
average_change = 0
greatest_increase = 0
greatest_increase_month = None
greatest_decrease = 0
greatest_decrease_month = None



if __name__ == "__main__":

    # This opens up the CSV file which uses ',' as a delimiter
    with open(csv_path, newline='') as csvfile:
        budget_data = csv.reader(csvfile, delimiter=',', quotechar='|')

        # Create internal variables
        header = [next(budget_data)]
        row_data = []
        profit_loss = []

        # row_data will store all the data without the headers
        for row in budget_data:
            row_data.append(row)

        # This returns the amount of months in the csv file
        month_count = len(row_data)

        # This adds the profit/loss column together
        for row in row_data:
            net_total += int(row[1])
            profit_loss.append(row[1])

        print(profit_loss)
        average_change = numpy.mean(profit_loss)

        print(f"Financial Analysis\n"
              f"-------------------------------------\n"
              f"Total Months: {month_count}\n"
              f"Total: {net_total}\n"
              f"Average Change: {average_change}\n"
              f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase})\n"
              f"Greatest Decrease in Profits: {greatest_decrease_month} ({greatest_decrease})\n")