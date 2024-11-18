#!/usr/bin/python3
"""
Log Parsing Script

This script reads log entries from stdin line by line and computes metrics:
- Total file size from all log entries
- Count of HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500)

After every 10 lines of input or upon
receiving a keyboard interrupt (Ctrl + C),
it prints the following statistics:
- Total file size: the sum of all file sizes from the log entries
- Number of lines per status code: only valid status codes are counted and
  printed in ascending order.

Input format expected for each log entry:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Example usage:
$ ./0-generator.py | ./0-stats.py
"""

import sys


def print_stats(file_size, status_counts):
    """
    Prints the current statistics including
    total file size and status code counts.

    Args:
        file_size (int): The total size of all the files processed so far.
        status_counts (dict): A dictionary∫
        with the count of each valid status code.
    """
    print(f"File size: {file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

if __name__ == "__main__":
    file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            parts = line.split()

            if len(parts) >= 7:
                try:
                    file_size += int(parts[-1])
                    status_code = int(parts[-2])

                    if status_code in status_counts:
                        status_counts[status_code] += 1
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)

    print_stats(file_size, status_counts)
