from fluid_sbom.pkg.cataloger.elixir.parse_mix_lock import (
    parse_mix_lock,
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


def on_next_elixir(
    source: reactivex.Observable[str],
) -> reactivex.Observable[Request]:
    def subscribe(
        observer: ObserverBase[Request],
        scheduler: SchedulerBase | None = None,
    ) -> reactivex.abc.DisposableBase:
        def on_next(value: str) -> None:
            try:
                if fnmatch(value, "**/mix.lock"):
                    observer.on_next(
                        Request(
                            real_path=value,
                            parser=parse_mix_lock,
                            parser_name="parse-elixir-mix-lock",
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
