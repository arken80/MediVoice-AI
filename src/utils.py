# Utility Classes for Metrics, Visualization, and Data Utilities

class Metrics:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def calculate_mean(self):
        return sum(self.data) / len(self.data) if self.data else 0

    def calculate_median(self):
        sorted_data = sorted(self.data)
        mid = len(sorted_data) // 2
        if len(sorted_data) % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]


class Visualization:
    @staticmethod
    def plot(data, title="Data Visualization"):
        import matplotlib.pyplot as plt
        plt.plot(data)
        plt.title(title)
        plt.show()


class DataUtilities:
    @staticmethod
    def load_csv(filepath):
        import pandas as pd
        return pd.read_csv(filepath)

    @staticmethod
    def save_csv(data, filepath):
        import pandas as pd
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)