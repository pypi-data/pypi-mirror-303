import csv
import os


class CSVLogger:
    def __init__(self, filename):
        self.filename = filename
        self.fields = ["model_name", "preprocessing", "with_preprocessing", "time"]

        # Create file and write the header if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()

    def log(self, model_name, runtime, preprocessing, with_preprocessing):
        with open(self.filename, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writerow(
                {
                    "model_name": model_name,
                    "preprocessing": preprocessing,
                    "with_preprocessing": with_preprocessing,
                    "time": runtime.mid,
                }
            )
