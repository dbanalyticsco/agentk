# Agent K

Agent K is a command-line tool to send emails with content generated from Looker. You can write Markdown files with Jinja templating and Agent K will pull data from Looker, render the HTML and send an email to your desired recipients. 

This tool is named after the greatest Men In Black agent of all-time, [Kevin 'Agent K' Brown](https://en.wikipedia.org/wiki/Agent_K). After his first retirement, Agent K worked in the post office, hence the name for this tool. (Tenuous, I know.)  

## What does an Agent K template look like?

```markdown
{{ config(
	to_email = 'dylan+to@dbanalytics.co',
	from_email = 'dylan+from@dbanalytics.co',
	subject = 'This is a test email.'
	)}}

Hello everyone, 

Here's your daily stats update.

## Add a single number to some text!

{% if look_single_value(5061) < 0 %}
We lost **{{ look_single_value(5061)|abs }}** clients yesterday.
{% else %}
We added **{{ look_single_value(5061) }}** new clients yesterday.
{% endif %}

## Create a table in HTML

{{ look_table(5062) }}

## Take a visualisation directly from the PNG

{{ look_png(5062, 600, 200) }}

## And another one

{{ look_png(5064, 600, 300) }}

Best,
Dylan
```

When you run Agent K, it will query Looker for the relevant data and visualisations based on `{{ }}` references in your template. Currently, you can insert a Single Value, HTML Table, and Visualisation png file. The config is set from within the file as well.

You can use conditional logic within your Jinja as well, allowing you to dynamically change your text based on results pulled from Looker. You could even choose to include certain graphs over others, depending on what you dynamically want to highlight on a given day.

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



