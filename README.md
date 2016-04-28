# Cloudspotting

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/travis/pinax/cloudspotting.svg)](https://travis-ci.org/pinax/cloudspotting)
[![](https://img.shields.io/coveralls/pinax/cloudspotting.svg)](https://coveralls.io/r/pinax/cloudspotting)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/cloudspotting/)

## Pinax

[Pinax](http://pinaxproject.com/pinax/) is an open-source platform built on the
Django Web Framework. It is an ecosystem of reusable Django apps, themes, and
starter project templates.

This demo project was developed to illustrate the use of Pinax starter projects and Pinax apps.

## cloudspotting

`cloudspotting` allows you to create collections of similar cloud images, view other people’s collections, “like” a collection, etc.
It demonstrates integration of `pinax-images`, `pinax-likes`, `pinax-testimonials`, and `pinax-announcements` with a real Django application.

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

Clone the repository, then:

```
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites
./manage.py runserver
```

## Documentation

The `cloudspotting` documentation is currently under construction.

## Contribute

See [this blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/) including a video, or our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our [Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you [join our Pinax Slack team](http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our [Open Source and Self-Care blog post](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).

## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found [here](http://pinaxproject.com/pinax/code_of_conduct/). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.

## Pinax Project Blog and Twitter

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our [blog]( http://blog.pinaxproject.com).
