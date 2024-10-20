"""Application commands."""
import click

from cr_enhanced_report.db import DB, use_db
from cr_enhanced_report.reporter import Reporter


@click.command()
@click.option("--only-completed/--not-only-completed", default=False)
@click.option("--skip-success/--include-success", default=False)
@click.argument("session-file", type=click.Path(dir_okay=False, readable=True, exists=True))
def cr_enhanced_report(only_completed, skip_success, session_file) -> None:
    """
    Create an enhanced Cosmic-Ray report.

    Args:
        only_completed: If `True`, only the completed work items.
        skip_success: If `True`, skip all successful work items.
        session_file: The path to the session file.
    """
    with use_db(session_file, DB.Mode.open) as db:
        db.skip_success = skip_success
        report = Reporter(db=db, only_completed=only_completed)
        report.create_report()
