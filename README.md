# Agent K

Agent K is a command-line tool to send emails with content generated from Looker. You can write Markdown files with Jinja templating and Agent K will pull data from Looker, render the HTML and send an email to your desired recipients. 

This tool is named after the greatest Men In Black agent of all-time, [Kevin 'Agent K' Brown](https://en.wikipedia.org/wiki/Agent_K). After his first retirement, Agent K worked in the post office, hence the name for this tool. (Tenuous, I know.)  

## Requirements

To run Agent K, you need Python 3.5+.

To install, clone the repo and use pip:

```bash
git clone git@github.com:dbanalyticsco/agentk.git
cd agentk
pip install .
```