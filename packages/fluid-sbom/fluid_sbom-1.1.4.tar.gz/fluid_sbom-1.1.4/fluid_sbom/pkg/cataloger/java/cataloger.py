from fluid_sbom.pkg.cataloger.generic.cataloger import (
    Request,
)
from fluid_sbom.pkg.cataloger.java.archive_parser import (
    parse_java_archive,
)
from fluid_sbom.pkg.cataloger.java.parse_android_apk import (
    parse_apk,
)
from fluid_sbom.pkg.cataloger.java.parse_gradle_lockfile import (
    parse_gradle_lockfile,
)
from fluid_sbom.pkg.cataloger.java.parse_pom_xml import (
    parse_pom_xml,
)
from fnmatch import (
    fnmatch,
)
import reactivex
from reactivex.abc import (
    ObserverBase,
    SchedulerBase,
)


def on_next_java(
    source: reactivex.Observable[str],
) -> reactivex.Observable[Request]:
    def subscribe(
        observer: ObserverBase[Request],
        scheduler: SchedulerBase | None = None,
    ) -> reactivex.abc.DisposableBase:
        def on_next(value: str) -> None:
            try:
                if any(
                    fnmatch(value, x)
                    for x in (
                        "**/pom.xml",
                        "/pom.xml",
                        "pom.xml",
                    )
                ):
                    observer.on_next(
                        Request(
                            real_path=value,
                            parser=parse_pom_xml,
                            parser_name="java-parse-pom-xml",
                        )
                    )
                elif any(
                    fnmatch(value, x)
                    for x in (
                        "**/*.jar",
                        "*.jar",
                        "**/*.war",
                        "*.war",
                        "**/*.ear",
                        "*.ear",
                        "**/*.par",
                        "*.par",
                        "**/*.sar",
                        "*.sar",
                        "**/*.nar",
                        "*.nar",
                        "**/*.jpi",
                        "*.jpi",
                        "**/*.hpi",
                        "*.hpi",
                        "**/*.lpkg",
                        "*.lpkg",
                    )
                ):
                    observer.on_next(
                        Request(
                            real_path=value,
                            parser=parse_java_archive,
                            parser_name="java-archive-parse",
                        )
                    )
                elif any(
                    fnmatch(value, x)
                    for x in (
                        "gradle.lockfile*",
                        "**/gradle.lockfile*",
                    )
                ):
                    observer.on_next(
                        Request(
                            real_path=value,
                            parser=parse_gradle_lockfile,
                            parser_name="java-parse-gradle-lock",
                        )
                    )
                elif any(
                    fnmatch(value, x)
                    for x in (
                        "**/*.apk",
                        "*.apk",
                    )
                ):
                    observer.on_next(
                        Request(
                            real_path=value,
                            parser=parse_apk,
                            parser_name="java-parse-apk",
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
