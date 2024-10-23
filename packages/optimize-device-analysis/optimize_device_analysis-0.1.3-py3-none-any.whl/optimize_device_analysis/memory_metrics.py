import psutil
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time, csv
from mail_file import Mailfile

class MemoryMetrics:
    @staticmethod
    def get_virtual_memory_percent():
        return psutil.virtual_memory().percent

    @staticmethod
    def plot_memory_usage(start_time, end_time, interval,  export_csv=False, email_id_for_csv=''):
        timestamps = []
        memory_data = []
        print("Your analysis has begun")

        current_time = start_time
        while current_time <= end_time:
            timestamps.append(current_time)
            memory_percent = MemoryMetrics.get_virtual_memory_percent()
            memory_data.append(memory_percent)

            time.sleep(interval)
            current_time = datetime.now()

        plt.plot(timestamps, memory_data, label='Memory Usage')
        plt.title('Memory Usage Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Percentage')
        plt.legend()
        plt.show()

        import os
        # Export data to CSV if export_csv is True
        if export_csv:
            csv_filename = 'memory_metrics_data.csv'
            import pandas as pd

            # Create a DataFrame with the data
            df = pd.DataFrame({'Timestamp': timestamps, 'CPU Usage (%)': memory_data})

            # Write the DataFrame to a CSV file
            df.to_csv(csv_filename, index=False)

            import re
            pattern = r'\w+@\w+.com'
            match = re.search(pattern, email_id_for_csv)
            report_time_generation = datetime.now()
            subject = 'Memory Metrics file - ' + str(datetime.now())
            body = 'Please find the attachment that you requested'
            csv_location = csv_filename
            if match:
                Mailfile.send_email_with_attachment(email_id_for_csv, subject, body, csv_location)
            else:
                print("Email for report is not sent, verify you email-id")