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

Dylan changed this.

Best,
Dylan
