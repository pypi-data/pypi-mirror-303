# Introduction

This repo. serves to develop the strategy to assess whether user has entered anomalous value while
filling the expenses. 

It assumes xml that will be exported from BPM solution and extracts meaning ful data from it, later uses 
language model to assess and detect anomalies.



# Only for live devvelopment of the project

```bash
pip install -e . 
uvicorn xmlAnomalyDetection.app:app  --port 8357 --reload 
```




# Build the project and run server

Following will build the project binaries so that it could be installed via `pip`  

ist create a `.env` file with key `GROQ_API_KEY` , (get the free api key from [groq server](groq.com))


```bash

python setup.py bdist_wheel
python setup.py sdist 

```
This will create some binaries in dist and build folders, install it as package like:

```bash
cd dist
pip install xmlAnomalyDetection-2.0-py3-none-any.whl
```


## Run server

Once the project is built , run following in the terminal, it will run the server:
```bash
xml_anomaly_detection
```


# Run without building

Binaries are already pushed to pypi, do following to just pull them and install them:

```bash

pip install xmlAnomalyDetection==2.0
```

Then run following in the terminal, it will run the server:
```bash
xml_anomaly_detection
```


# Test request

```curl
curl -X 'POST' \
  'http://0.0.0.0:8357/detect_anomaly' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'xml_file=@xml_sample.xml;type=text/xml'

```

It will return response like:

```bash
[
  {
    "user_entered_values": [
      "2022-11-08",
      "Travel | Car Rental",
      "200",
      "21"
    ],
    "entered_values_decriptions": [
      "Date of expense",
      "Type of expense",
      "Expense amount",
      "Brief description"
    ],
    "is_anomaly": "False",
    "reason": []
  },
  {
    "user_entered_values": [
      "2022-11-08",
      "Transportation | Fuel",
      "200",
      "212"
    ],
    "entered_values_decriptions": [
      "Date of expense",
      "Type of expense",
      "Expense amount",
      "Brief description"
    ],
    "is_anomaly": "False",
    "reason": []
  }
]

```

If `is_anomaly` is  `True` in any of the returned records, it means there is anomaly. Rest of the items in record are metadata.


# New possible prompt ✍️

```
# Expense Report Anomaly Detection

You are an AI system designed to analyze expense reports and detect potential anomalies or irregularities. Given an expense report, examine each entry and the report as a whole for the following types of issues:

1. Duplicate entries: Identify multiple entries for the same expense type on the same date.

2. Excessive amounts: Flag expenses that exceed typical or policy-defined limits for their category.

3. Unusual patterns: Detect atypical expense patterns, such as multiple meals of the same type in one day.

4. Documentation issues: Highlight entries lacking required receipts or supporting documents.

5. Verification problems: Note expenses marked as unverified or failing standard verification processes.

6. Date inconsistencies: Identify expenses outside the stated trip dates or clustered unusually.

7. Round number anomalies: Flag suspicious occurrences of round numbers or repeating patterns in amounts.

8. Error indicators: Pay attention to any system-generated error flags or comments.

9. Category mismatches: Detect expenses that seem miscategorized based on their description or amount.

10. Missing expected expenses: Note the absence of typical expense categories for the type of trip.

11. Policy violations: Identify any expenses that directly contradict stated company policies.

12. Unusual descriptions: Flag expenses with vague, inappropriate, or suspicious descriptions.

For each potential anomaly detected, provide:
- The specific entry or entries involved
- The type of anomaly detected
- A brief explanation of why it's considered anomalous
- A suggestion for further investigation or correction if applicable

Analyze the given expense report and provide a detailed list of any detected anomalies, following the guidelines above.

```