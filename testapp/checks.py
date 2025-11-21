from collections.abc import Iterable

from msgspec import UNSET, Struct, UnsetType, to_builtins

from maykin_health_checks.types import HealthCheck, HealthCheckResult, JSONValue


class DummyResult(Struct):
    success: bool
    identifier: str
    message: str = ""
    extra: dict | UnsetType = UNSET

    def to_builtins(self) -> JSONValue:
        return to_builtins(self)


class DummyCheck:
    identifier = "dummy"

    def run(self) -> HealthCheckResult:
        return DummyResult(
            success=True, identifier=self.identifier, message="Everything is great."
        )


class DummyCheckFail:
    identifier = "dummy_fail"

    def run(self) -> HealthCheckResult:
        return DummyResult(
            success=False, identifier=self.identifier, message="Everything is sad."
        )


class CheckWithException:
    identifier = "check_with_exception"

    def run(self) -> HealthCheckResult:
        raise Exception("HELLO EXCEPTION!")


def check_collector() -> Iterable[HealthCheck]:
    return [DummyCheck(), DummyCheckFail()]
