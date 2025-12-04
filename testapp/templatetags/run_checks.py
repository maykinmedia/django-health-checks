from django import template

from maykin_health_checks.runner import HealthChecksRunner

from ..checks import DummyCheck, DummyCheckFail

register = template.Library()


@register.simple_tag
def run_happy_checks():
    runner = HealthChecksRunner(
        checks_collector=lambda: [DummyCheck()],
        include_success=True,
    )
    return runner.run_checks()


@register.simple_tag
def run_unhappy_checks():
    runner = HealthChecksRunner(
        checks_collector=lambda: [DummyCheck(), DummyCheckFail()],
        include_success=True,
    )
    return runner.run_checks()
