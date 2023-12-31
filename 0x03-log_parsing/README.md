## AUTHOR: DANIEL AJIBOYE

# Log Parsing

This repository contains a script for parsing logs and computing metrics based on the provided input format. The script reads stdin line by line and performs the following tasks:

## Tasks

**0. Log Parsing (mandatory)**

Write a script that reads stdin line by line and computes the following metrics based on the provided input format:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- After every 10 lines and/or a keyboard interruption (CTRL + C), print the following statistics from the beginning:
  - Total file size: File size: `<total size>`, where `<total size>` is the sum of all previous `<file size>`
  - Number of lines by status code:
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
    - If a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order

**Example:**

```bash
$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

Please note that the output might vary due to random values in the provided example.

**Note:** If the log format does not match the specified one, the line will be skipped.

For more details and the source code, please refer to the [`0x03-log_parsing` directory in the alx-interview repository](https://github.com/alx-interview/0x03-log_parsing).
