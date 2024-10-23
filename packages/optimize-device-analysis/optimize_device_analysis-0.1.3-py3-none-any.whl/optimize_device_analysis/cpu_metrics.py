import psutil
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time, csv
from mail_file import Mailfile

class CPUMetrics:
    @staticmethod
    def get_cpu_percent():
        return psutil.cpu_percent()

    @staticmethod
    def plot_cpu_usage(start_time, end_time, interval, export_csv=False, email_id_for_csv=''):
        timestamps = []
        cpu_data = []
        print("Your analysis has begun")

        current_time = start_time
        while current_time <= end_time:
            timestamps.append(current_time)
            cpu_percent = CPUMetrics.get_cpu_percent()
            cpu_data.append(cpu_percent)

            time.sleep(interval)
            current_time = datetime.now()

        plt.plot(timestamps, cpu_data, label='CPU Usage')
        plt.title('CPU Usage Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Percentage')
        plt.legend()
        plt.show()

        # Export data to CSV if export_csv is True
        if export_csv:
            csv_filename = 'cpu_metrics_data.csv'
            import pandas as pd

            # Create a DataFrame with the data
            df = pd.DataFrame({'Timestamp': timestamps, 'CPU Usage (%)': cpu_data})

            # Write the DataFrame to a CSV file
            df.to_csv(csv_filename, index=False)

            import re
            pattern = r'\w+@\w+.com'
            match = re.search(pattern, email_id_for_csv)
            subject = 'CPU Performance Metrics file - ' + str(datetime.now())
            body = 'Please find the attachment that you requested'
            if match:
                Mailfile.send_email_with_attachment(email_id_for_csv, subject, body, csv_filename)
            else:
                print("Email for report is not sent, verify you email-id")