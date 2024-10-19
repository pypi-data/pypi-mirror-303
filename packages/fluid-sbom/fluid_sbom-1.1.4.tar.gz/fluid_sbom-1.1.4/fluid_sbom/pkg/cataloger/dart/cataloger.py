from fluid_sbom.pkg.cataloger.dart.parse_pubspec_lock import (
    parse_pubspec_lock,
)
from fluid_sbom.pkg.cataloger.dart.parse_pubspec_yaml import (
    parse_pubspec_yaml,
)
from fluid_sbom.pkg.cataloger.generic.cataloger import (
    Request,
)
from fnmatch import (
    fnmatch,
)
import reactivex
from reactivex.abc import (
    ObserverBase,
    SchedulerBase,
)


def on_next_dart(
    source: reactivex.Observable[str],
) -> reactivex.Observable[Request]:
    def subscribe(
        observer: ObserverBase[Request],
        scheduler: SchedulerBase | None = None,
    ) -> reactivex.abc.DisposableBase:
        def on_next(value: str) -> None:
            try:
                if any(
                    fnmatch(value, pattern)
                    for pattern in ("**/pubspec.lock", "pubspec.lock")
                ):
                    observer.on_next(
                        Request(
                            real_path=value,
                            parser=parse_pubspec_lock,
                            parser_name="dart-parse-pubspec-lock",
                        )
                    )
                elif any(
                    fnmatch(value, pattern)
                    for pattern in ("**/pubspec.yaml", "pubspec.yaml")
                ):
                    observer.on_next(
                        Request(
                            real_path=value,
                            parser=parse_pubspec_yaml,
                            parser_name="dart-parse-pubspec-yaml",
                        )
                    )
            except Exception as ex:  # pylint:disable=broad-exception-caught
                observer.on_error(ex)

        return source.subscribe(
            on_next,
            observer.on_error,
            observer.on_completed,
            scheduler=scheduler,
        )

    return reactivex.create(subscribe)
