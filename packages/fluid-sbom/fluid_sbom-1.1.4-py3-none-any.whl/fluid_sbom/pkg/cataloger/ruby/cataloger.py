from fluid_sbom.pkg.cataloger.generic.cataloger import (
    Request,
)
from fluid_sbom.pkg.cataloger.ruby.parse_gemfile_lock import (
    parse_gemfile_lock,
)
from fnmatch import (
    fnmatch,
)
import reactivex
from reactivex.abc import (
    ObserverBase,
    SchedulerBase,
)


def on_next_ruby(
    source: reactivex.Observable[str],
) -> reactivex.Observable[Request]:
    def subscribe(
        observer: ObserverBase[Request],
        scheduler: SchedulerBase | None = None,
    ) -> reactivex.abc.DisposableBase:
        def on_next(value: str) -> None:
            try:
                if fnmatch(value, "**/Gemfile.lock"):
                    observer.on_next(
                        Request(
                            real_path=value,
                            parser=parse_gemfile_lock,
                            parser_name="parse-gemfile-lock",
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
