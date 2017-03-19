# statboard

Statistics/Metric Dashboard for your product

## Requirements:

1. Redis

## Up and Running

1. Fork & Clone this repo
1. `pip install -r requirements.txt` (Hopefully, in your virtualenv)
1. Ensure redis is running
1. Run `./manage.py seed_db` to create your ORM objects
1. `./manage runserver` to start server
1. `./manage.py run_huey` to start the worker (that periodically fetches your metric data and stores them in DB). Also please note that you need to manually stop and start huey whenever there is a change in your data fetcher code


## Adding new metrics

Lets say you need to add new metric called `foo` metric. You need to do following (detailed explanations are below):

1. Update `statboard/settings.py` with variable `METRIC_FOO='foo'`
1. Run `./manage.py seed_db` to create your ORM objects (You need to run this everytime you add a new metric)
1. Create a `statboard/core/metrics/foo.py` which should declare `def fetch(metric):` function
1. Create a `statboard/core/templates/foo.html` to render your data

### Updating Settings

If you need to add a new metric, first add a variable called `METRIC_<YOUR_METRIC_IN_CAPS>='<your_metric>'` in your `settings.py` file. This will be used by `seed_db` command to create a new `Metric` object in your DB & `url.py` to create a new URL `/metric/<your_metric>` automatically. Just be sure that it should start with the exact `METRIC_` prefix for this to work.

### Seed DB

Run `./manage.py seed_db`. This will create the `Metric` object for you. You can then use `metric.data` and `metric.set_data(<json_dict>)` to get and set your data data respectively.

### Fetching Metrics

You should create a file `statboard/core/metrics/<your_metric>.py`. Your file will look something like this:

```
def fetch(metric):
	"""
	This fetch function will be automatically called by our worker
	You will get the `metric` orm object
	"""
	<json_dict> = some_logic_that_fetches_your_data()
	metric.set_data(<json_dict>)
```

If you need any sensitive keys, make sure you put them in environment variable and access it from there. Please make sure that `<json_dict>` is a simple python dict with primitive data.

### Rendering Your Metrics

Create a `statboard/core/templates/<your_metric>.html` file which looks come thing like this:

```
{% extends 'base.html' %}

{% block title %}
Your Metric
{% endblock %}

{% block content %}

{% for name in metric.data.foo_names %}
{{name}}
{% endfor %}


{% endblock %}
```

Your `metric` ORM object will automatically be available in your template. Whatever `<json_dict>` data that you set in the previous step will be available through `metric.data` in your templates.
