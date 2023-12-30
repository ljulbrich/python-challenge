from pathlib import Path
import csv
import numpy

# Creating variables
txt_file = open('Analysis/data_analysis.txt', 'w+')
csv_path = Path('Resources/election_data.csv')
total_votes = 0
candidates = []
candidates_total = []
candidates_percent = []
candidates_list = []

if __name__ == "__main__":

    # Open the CSV with ',' as the delimeter
    with (open(csv_path, newline='') as csvfile):
        election_data = csv.reader(csvfile, delimiter=',', quotechar='|')

        # Creating internal variables
        header = [next(election_data)]
        row_data = []
        counter = 0

        # row_data will store al the data without headers
        for row in election_data:
            row_data.append(row)

        # This returns the total amount of votes in the CSV file
        total_votes = len(row_data)

        # This adds all the candidates to a list which is then turned into an array
        # further down the code to add the unique names in the candidates list.
        for row in row_data:
            candidates_list.append(row[2])

        candidates_array = numpy.array(candidates_list)
        candidates = numpy.unique(candidates_array)

        # This section first adds a zero to candidates_total for each candidate and then
        # loops through the csv and adds to the candidates_total for each time the candidate
        # names match.
        for candidate in candidates:
            candidates_total.append(0)

            for row in row_data:
                if row[2] == candidates[counter]:
                    candidates_total[counter] += 1
            counter += 1

        # This section calculates the percentages of the votes
        for item in candidates_total:
            candidates_percent.append((item/total_votes)*100)

        print(f'Total votes {total_votes}\n'
              f'Candidates {candidates}\n'
              f'Candidates votes {candidates_total}\n'
              f'Candidate percent {candidates_percent}') # TODO: format decimals

