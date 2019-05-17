# Agent K

Agent K is a command-line tool to send emails with content generated from Looker. You can write Markdown files with Jinja templating and Agent K will pull data from Looker, render the HTML and send an email to your desired recipients. 

This tool is named after the greatest Men In Black agent of all-time, [Kevin 'Agent K' Brown](https://en.wikipedia.org/wiki/Agent_K). After his first retirement, Agent K worked in the post office, hence the name for this tool. (Tenuous, I know.)  

## Installation

To run Agent K, you need Python 3.5+.

To install, clone the repo and use pip:

```bash
git clone git@github.com:dbanalyticsco/agentk.git
cd agentk
pip install .
```

## Setup

For the moment, Agent K uses Sendgrid and Cloudinary for email sending and image storage. It also requires a Looker API user. In the future, we will allow you to easily create your own adapter for the email client and image storage.

To run, the following environment variables need to be present:

* SENDGRID_API_KEY
* LOOKER_BASE_URL
* LOOKER_CLIENT_ID
* LOOKER_CLIENT_SECRET
* CLOUDINARY_CLOUD_NAME
* CLOUDINARY_API_KEY
* CLOUDINARY_API_SECRET

## Running Agent K

#### Making a template
