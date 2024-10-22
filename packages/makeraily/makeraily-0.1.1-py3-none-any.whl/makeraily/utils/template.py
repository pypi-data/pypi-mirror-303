from jinja2 import Template, Environment

env = Environment()
env.policies['json.dumps_kwargs']['ensure_ascii'] = False


def render(tpl: Template, **context):
    return tpl.render(**context)
