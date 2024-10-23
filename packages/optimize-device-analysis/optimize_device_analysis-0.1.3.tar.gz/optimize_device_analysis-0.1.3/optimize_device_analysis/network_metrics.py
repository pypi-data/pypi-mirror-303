import psutil
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time, csv
from mail_file import Mailfile

class NetworkMetrics:
    @staticmethod
    def get_network_io_counters():
        network_stats = psutil.net_io_counters()
        return network_stats.bytes_sent, network_stats.bytes_recv

    @staticmethod
    def plot_network_activity(start_time, end_time, interval,  export_csv=False, email_id_for_csv=''):
        timestamps = []
        sent_data = []
        recv_data = []
        print("Your analysis has begun")

        current_time = start_time
        while current_time <= end_time:
            timestamps.append(current_time)
            bytes_sent, bytes_recv = NetworkMetrics.get_network_io_counters()
            sent_data.append(bytes_sent)
            recv_data.append(bytes_recv)

            time.sleep(interval)
            current_time = datetime.now()

        plt.plot(timestamps, sent_data, label='Bytes Sent')
        plt.plot(timestamps, recv_data, label='Bytes Received')
        plt.title('Network Activity Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Bytes')
        plt.legend()
        plt.show()

        # Export data to CSV if export_csv is True
        if export_csv:
            csv_filename = 'network_metrics_data.csv'
            import pandas as pd

            # Create a DataFrame with the data
            df = pd.DataFrame({'Timestamp': timestamps, 'Bytes Sent': sent_data, 'Bytes Received': recv_data})

            # Write the DataFrame to a CSV file
            df.to_csv(csv_filename, index=False)

            import re
            pattern = r'\w+@\w+.com'
            match = re.search(pattern, email_id_for_csv)
            subject = 'Network Usage Metrics file - ' + str(datetime.now())
            body = 'Please find the attachment that you requested'
            if match:
                Mailfile.send_email_with_attachment(email_id_for_csv, subject, body, csv_filename)
            else:
                print("Email for report is not sent, verify you email-id")

