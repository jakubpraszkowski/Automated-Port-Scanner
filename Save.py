from csv import writer
from datetime import datetime


class Save:
    def __init__(self, input_data):
        self.input_data = input_data

    def writing_to_csv(self):
        now = datetime.now()
        formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
        with open(f"Port Scanner {formatted_date}.csv", mode='w', newline='') as csvfile:
            write = writer(csvfile)
            write.writerow(['Port', 'Protocol', 'Service'])

    def writing_to_txt(self):
        now = datetime.now()
        formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
        with open(f"Port Scanner {formatted_date}.txt", mode='a', newline='') as file:
            file.write(self.input_data + '\n')
