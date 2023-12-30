import csv
from pathlib import Path
import statistics

# Creating variables
txt_file = open('Analysis/data_analysis.txt', 'w+')
csv_path = Path('Resources/budget_data.csv')
month_count = 0
net_total = 0
average_change = 0
increase = []
decrease = []

if __name__ == "__main__":

    # This opens up the CSV file which uses ',' as a delimiter
    with (open(csv_path, newline='') as csvfile):
        budget_data = csv.reader(csvfile, delimiter=',', quotechar='|')

        # Create internal variables
        header = [next(budget_data)]
        row_data = []
        profit_loss = []
        change = []
        register = 0

        # row_data will store all the data without the headers
        for row in budget_data:
            row_data.append(row)

        # This returns the amount of months in the csv file
        month_count = len(row_data)

        # This adds the profit/loss column together and creates a
        # list of only the profit/loss column
        for row in row_data:
            net_total += int(row[1])
            profit_loss.append(int(row[1]))

        # This column calculates the change between each month and
        # then calculates the average of that change
        for row in profit_loss:
            if register == 0:
                register = row
            else:
                change.append(row - register)
                register = row

        average_change = statistics.mean(change)

        # These two variables store the largest increases and decreases as a list
        increase.append(max(profit_loss))
        decrease.append(min(profit_loss))

        # This loop will go through the data to add the month to the second item in the lists
        for i in row_data:
            if int(i[1]) == increase[0]:
                increase.append(i[0])
            elif int(i[1]) == decrease[0]:
                decrease.append(i[0])

        # This is the output string
        output = (f'Financial Analysis\n'
                  f'-------------------------------------\n'
                  f'Total Months: {month_count}\n'
                  f'Total: ${net_total}\n'
                  f'Average Change: ${"%.2f" % average_change}\n'
                  f'Greatest Increase in Profits: {increase[1]} (${increase[0]})\n'
                  f'Greatest Decrease in Profits: {decrease[1]} (${decrease[0]})\n')

        # This section prints the output to the terminal and then saves it as a text file
        print(output)
        txt_file.write(output)
        txt_file.close()