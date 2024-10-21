IndieJobs
==========

IndieJobs is a Python-based tool for managing and automating job tasks. The tool integrates with AWS SSM Parameter Store to retrieve necessary parameters for your applications, allowing you to run various jobs efficiently.

Features
--------

- Retrieve parameters securely from AWS SSM Parameter Store.
- Easy to configure logging for monitoring purposes.
- Modular structure with task and utility folders for better organization.

Installation
------------

To use IndieJobs, ensure you have Python 3.6 or later installed. You can then clone the repository and install the required dependencies.

```bash
git clone https://github.com/FranciscoRSilva/indiejobs.git
cd indiejobs
pip install -r requirements.txt  # Ensure you have the necessary packages