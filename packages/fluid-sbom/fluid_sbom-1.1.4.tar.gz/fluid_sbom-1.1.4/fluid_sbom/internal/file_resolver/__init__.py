from fluid_sbom.file.resolver import (
    Resolver,
)
from fluid_sbom.pkg.cataloger.generic.cataloger import (
    Request,
    Task,
)
import reactivex
from reactivex import (
    Observable,
)
from reactivex.abc import (
    ObserverBase,
    SchedulerBase,
)
from typing import (
    Callable,
)


def gen_location(
    resolver: Resolver,
) -> Callable[[Observable[Request]], Observable]:
    def _handle(source: Observable[Request]) -> Observable:
        def subscribe(
            observer: ObserverBase[Task],
            scheduler: SchedulerBase | None = None,
        ) -> reactivex.abc.DisposableBase:
            def on_next(value: Request) -> None:
                try:
                    locations = resolver.files_by_path(value.real_path)
                    for location in locations:
                        observer.on_next(
                            Task(
                                location=location,
                                parser=value.parser,
                                parser_name=value.parser_name,
                            )
                        )
                except (
                    Exception  # pylint:disable=broad-exception-caught
                ) as ex:
                    observer.on_error(ex)

            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler=scheduler,
            )

        return reactivex.create(subscribe)

    return _handle
