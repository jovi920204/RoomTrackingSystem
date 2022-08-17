# Read Data in Google Sheets Using Python

## Why do this?
In my dorm at school, the residents have to check out in the end of semester, and some body will move to other room, so we have a Excel can know which room are empty right now, let resident know when it can move into.
But when he/she want to check, they have to open the Excel, and use their eyes to find which room they want to check.
So I made a program, you can input the "room" number and "bed" number, it will return "True" or "False", let you know it empty or not.

## Approch
1. In order to get the data in google sheets, we need to use the Google API, let we can have right to connect python and google sheets.
2. Create a class object, it can connect to the Google sheet with its "id", in URL.
3. When we get data, transform to pandas, it's better for me to do my work. Like, data analysis.

