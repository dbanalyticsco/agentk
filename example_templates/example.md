{{ config(
		to_email = 'dylan+to@dbanalytics.co',
		from_email = 'dylan+from@dbanalytics.co',
		subject = 'This is a test email.'
	)}}

# Hello, 

### This is an email from Dylan. 

{% if look_single_value(5061) < 0 %}
We lost **{{ look_single_value(5061)|abs }}** clients yesterday.
{% else %}
We added **{{ look_single_value(5061) }}** new clients yesterday.
{% endif %}

## This is a table:

{{ look_table(5062) }}