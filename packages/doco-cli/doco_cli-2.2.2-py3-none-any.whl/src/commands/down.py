import dataclasses
import pathlib

import typer

from src.utils.cli import PROJECTS_ARGUMENT
from src.utils.cli import RUNNING_OPTION
from src.utils.compose_rich import ComposeProject
from src.utils.compose_rich import get_compose_projects
from src.utils.compose_rich import ProjectSearchOptions
from src.utils.compose_rich import rich_run_compose
from src.utils.doco import do_project_cmd
from src.utils.doco import ProjectInfo


@dataclasses.dataclass
class DownOptions:
    remove_volumes: bool
    no_remove_orphans: bool
    force_down: bool


@dataclasses.dataclass
class Options(DownOptions):
    dry_run: bool


def down_project(project: ComposeProject, options: Options, info: ProjectInfo):
    if info.has_running_or_restarting or options.remove_volumes or options.force_down:
        rich_run_compose(
            project.dir,
            project.file,
            command=[
                "down",
                *(["--remove-orphans"] if not options.no_remove_orphans else []),
                *(["-v"] if options.remove_volumes else []),
            ],
            dry_run=options.dry_run,
            cmds=info.cmds,
        )


def main(
    projects: list[pathlib.Path] = PROJECTS_ARGUMENT,
    running: bool = RUNNING_OPTION,
    remove_volumes: bool = typer.Option(
        False, "--remove-volumes", "-v", help="Remove volumes (implies -f / --force)."
    ),
    no_remove_orphans: bool = typer.Option(False, "--no-remove-orphans", help="Keep orphans."),
    force: bool = typer.Option(False, "--force", "-f", help="Force calling down even if not running."),
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Do not actually stop anything, only show what would be done."
    ),
):
    """
    Shutdown projects.
    """

    for project in get_compose_projects(
        projects,
        ProjectSearchOptions(
            print_compose_errors=dry_run,
            only_running=running,
        ),
    ):
        do_project_cmd(
            # pylint: disable=cell-var-from-loop
            project=project,
            dry_run=dry_run,
            cmd_task=lambda info: down_project(
                project,
                options=Options(
                    remove_volumes=remove_volumes,
                    no_remove_orphans=no_remove_orphans,
                    force_down=force,
                    dry_run=dry_run,
                ),
                info=info,
            ),
        )
