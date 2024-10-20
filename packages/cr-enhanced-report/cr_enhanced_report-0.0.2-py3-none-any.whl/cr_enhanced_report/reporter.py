"""Module to create the Cosmic Ray report."""
import pathlib
import re
from datetime import datetime

from cosmic_ray.tools.html import pycharm_url
from cosmic_ray.work_item import TestOutcome
from yattag import Doc, SimpleDoc

from cr_enhanced_report.datatypes import HtmlColor, SummaryDetail
from cr_enhanced_report.db import DB


class Reporter(object):
    """Create an enhanced cosmic-ray work report from scratch."""

    __slots__ = (
        '_db',
        '_only_completed',
    )

    def __init__(self, db: DB, only_completed: bool) -> None:
        """
        Initialize Reporter.

        Args:
            db: Instance of MyDB
            only_completed: If `True`, only completed work items are reported.
        """
        self._db: DB = db
        self._only_completed: bool = only_completed

    def create_report(self) -> None:
        """Create a report from scratch."""
        doc, _, _, _ = Doc().ttl()
        doc.asis("<!DOCTYPE html>")
        with (doc.tag("html", lang="en")):
            with doc.tag("head"):
                doc.stag("meta", charset="utf-8")
                doc.stag("meta", name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no")
                doc.stag(
                    "link",
                    rel="stylesheet",
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
                    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH",
                    crossorigin="anonymous",
                )
                self._css(doc=doc)
                with doc.tag("title"):
                    doc.text("Cosmic Ray Enhanced Report")
            with doc.tag("body"):
                with doc.tag("div", klass="container"):
                    self._create_summary(doc=doc)
                    self._create_analysis(doc=doc)
                with doc.tag("script"):
                    doc.attr(src="https://code.jquery.com/jquery-3.7.1.js")
                    doc.attr(
                        ("integrity", "sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=")
                    )
                    doc.attr(("crossorigin", "anonymous"))
                with doc.tag("script"):
                    doc.attr(src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js")
                    doc.attr(
                        ("integrity", "sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy")
                    )
                    doc.attr(("crossorigin", "anonymous"))

        print(doc.getvalue())

    def _create_analysis(self, doc: SimpleDoc) -> None:
        """
        Create analysis section from scratch.

        Args:
            doc: SimpleDoc object.
        """
        with doc.tag("section", id="file-analysis"):
            work_item_data = self._fetch_work_items_data()
            with doc.tag("div", klass="accordion accordion-flush", id="accordian-files"):
                file_id = 1
                for file_name in sorted(work_item_data.keys()):
                    with doc.tag("div", klass="accordion-item"):
                        with doc.tag("h2", klass="accordion-header", id=f"flush-heading{file_id}"):
                            with doc.tag(
                                "button",
                                ("data-bs-toggle", "collapse"),
                                ("data-bs-target", f"#flush-collapse{file_id}"),
                                ("aria-expanded", "false"),
                                ("aria-controls", f"flush-collapse{file_id}"),
                                klass="accordion-button collapsed",
                                type="button",
                                id=self._normalize_path(f'/{file_name}'),
                            ):
                                doc.text(f'/{file_name}')
                        with doc.tag(
                            "div",
                            ("data-bs-parent", "#accordian-files"),
                            ("aria-labelledby", "flush-heading{file_id}"),
                            klass="accordion-collapse collapse",
                            id=f"flush-collapse{file_id}"
                        ):
                            with doc.tag("div", klass="accordion-body"):
                                self._create_file_analysis(
                                    file_id=file_id, file_tasks=work_item_data[file_name], doc=doc
                                )
                    file_id += 1

    def _fetch_work_items_data(self):
        """Fetch and organize work items based on the file."""
        if self._only_completed:
            work_items = self._db.completed_work_items
        else:
            # TODO fix so that this fetches all work items.
            work_items = self._db.completed_work_items
        work_item_groups = {}
        for work_item in work_items:
            if work_item[2].module_path not in work_item_groups:
                work_item_groups[work_item[2].module_path] = []
            work_item_groups[work_item[2].module_path].append(work_item)
        return work_item_groups

    @staticmethod
    def _create_file_analysis(file_id: int, file_tasks, doc: SimpleDoc) -> None:
        with doc.tag("div", klass="accordion-item", id=f"accordian-tasks-{file_id}"):
            task_id = 1
            for file_task in file_tasks:
                with doc.tag("div", klass="accordion-item"):
                    with doc.tag("h2", klass="accordion-header", id=f"flush-heading-{file_id}-{task_id}"):
                        with doc.tag(
                            "button",
                            ("data-bs-toggle", "collapse"),
                            ("data-bs-target", f"#flush-collapse-{file_id}-{task_id}"),
                            ("aria-expanded", "false"),
                            ("aria-controls", f"flush-collapse-{file_id}-{task_id}"),
                            klass=f"accordion-button collapsed {file_task[1].test_outcome.value}",
                            type="button",
                        ):
                            with doc.tag("span", klass="job_id"):
                                doc.text(file_task[0].job_id)
                    with doc.tag(
                        "div",
                        ("aria-labelledby", f"flush-heading-{file_id}"),
                        ("data-bs-parent", f"#accordian-tasks-{file_id}"),
                        klass="accordion-collapse collapse",
                        id=f"flush-collapse-{file_id}-{task_id}",
                    ):
                        with doc.tag("div", klass="accordion-body"):
                            with doc.tag("section", klass=f"task-summary {file_task[1].test_outcome.value}"):
                                with doc.tag("p"):
                                    with doc.tag("b"):
                                        doc.text(file_task[1].test_outcome.value.upper())
                                with doc.tag("p"):
                                    doc.text(f'Worker outcome: {file_task[1].worker_outcome.value}')
                                with doc.tag("p"):
                                    doc.text(f'Test outcome: {file_task[1].test_outcome.value}')

                            with doc.tag("pre", klass="location"):
                                with doc.tag(
                                    "a",
                                    href=pycharm_url(str(file_task[2].module_path), file_task[2].start_pos[0]),
                                    klass="text-secondary",
                                ):
                                    with doc.tag("button", klass="btn btn-outline-dark"):
                                        doc.text(
                                            f"{file_task[2].module_path}, "
                                            + f"start pos: {file_task[2].start_pos}, end pos: {file_task[2].end_pos}"
                                        )
                            with doc.tag("p"):
                                doc.text(
                                    f"Operator: {file_task[2].operator_name}, Occurrence: {file_task[2].occurrence}"
                                )
                            with doc.tag("pre", klass="task-diff"):
                                doc.text(file_task[1].diff)
                            with doc.tag("pre", klass="task-output"):
                                doc.text(file_task[1].output)
                task_id += + 1

    def _create_summary(self, doc: SimpleDoc) -> None:
        """
        Create report summary section from scratch.

        Args:
            doc: SimpleDoc object.
        """
        with doc.tag("section", id="report-summary"):
            with doc.tag("div", id="summary"):
                with doc.tag("h2"):
                    doc.text('Summary')
                with doc.tag("section"):
                    with doc.tag("p"):
                        doc.text(f'Report Ran On: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
                    with doc.tag("p"):
                        doc.text(f'Total Jobs: {self._db.num_work_items}')
                    if self._db.num_results > 0:
                        with doc.tag("p"):
                            doc.text(f'Completed Jobs: {self._db.num_results}')
                        with doc.tag("p"):
                            doc.text(
                                'Surviving Mutants: '
                                + f'{self._db.num_results - self._db.kill_count}({self._db.survival_rate}%)'
                            )
                with doc.tag("div", klass="card card-body"):
                    with doc.tag("table"):
                        with doc.tag("thead"):
                            with doc.tag("tr"):
                                with doc.tag("th"):
                                    doc.text('Path')
                                with doc.tag("th"):
                                    doc.text('Score')
                                with doc.tag("th"):
                                    doc.text(TestOutcome.KILLED.capitalize())
                                with doc.tag("th"):
                                    doc.text(TestOutcome.INCOMPETENT.capitalize())
                                with doc.tag("th"):
                                    doc.text(TestOutcome.SURVIVED.capitalize())
                        with doc.tag("tbody"):
                            summary_data: list[SummaryDetail] = self._fetch_summary_data()
                            for summary_item in summary_data:
                                with doc.tag("tr"):
                                    with doc.tag("td"):
                                        if summary_item.is_dir:
                                            doc.text(str(summary_item.path))
                                        else:
                                            with doc.tag("a", href=f'#{self._normalize_path(str(summary_item.path))}'):
                                                doc.text(str(summary_item.path))
                                    with doc.tag("td", klass=self._score_color(score=summary_item.score)):
                                        doc.text(f'{summary_item.score}%')
                                    with doc.tag("td", klass="killed"):
                                        doc.text(str(summary_item.killed))
                                    with doc.tag("td", klass="incompetent"):
                                        doc.text(
                                            str(summary_item.incompetent)
                                        )
                                    with doc.tag("td", klass="survived"):
                                        doc.text(str(summary_item.survived))

    def _fetch_summary_data(self) -> list[SummaryDetail]:
        """Fetch data used for the report summary."""
        task_data: dict[str, SummaryDetail] = {}
        status_counts = self._db.fetch_status_counts()
        for status_count in status_counts:
            killed = 0
            incompetent = 0
            survived = 0
            if status_count[1] not in task_data:
                task_data[status_count[1]] = SummaryDetail(
                    path=pathlib.Path('/').joinpath(status_count[1]),
                    killed=0,
                    incompetent=0,
                    survived=0,
                )
            if status_count[0] == TestOutcome.KILLED:
                killed += status_count[2]
            elif status_count[0] == TestOutcome.INCOMPETENT:
                incompetent += status_count[2]
            elif status_count[0] == TestOutcome.SURVIVED:
                survived += status_count[2]

            task_data[status_count[1]].killed += killed
            task_data[status_count[1]].incompetent += incompetent
            task_data[status_count[1]].survived += survived
            for directory in task_data[status_count[1]].path_list():
                if str(directory) not in task_data:
                    task_data[str(directory)] = SummaryDetail(
                        path=directory,
                        is_dir=True,
                        killed=0,
                        incompetent=0,
                        survived=0,
                    )
                task_data[str(directory)].killed += killed
                task_data[str(directory)].incompetent += incompetent
                task_data[str(directory)].survived += survived
        return sorted(task_data.values())

    @staticmethod
    def _normalize_path(path: str) -> str:
        """
        Normalize a path to use as a document link.

        Args:
            path: Path to normalize.

        Returns:
            Normalized path.
        """
        return re.sub(pattern=r'[\/.]', repl='_', string=path)

    @staticmethod
    def _score_color(score: float) -> str:
        """
        Calculate the score color.

        Args:
            score: Score as a percentage to 2 decimal places.

        Returns:
            HtmlColor based on the score.
        """
        if score >= 80.01:
            return 'killed'
        if score >= 50.01:
            return 'incompetent'
        return 'survived'

    @staticmethod
    def _css(doc: SimpleDoc) -> None:
        with doc.tag("style"):
            doc.text(f"""
                .survived {{
                    background-color: {HtmlColor.red.value};
                    color: white;
                }}
                .incompetent {{
                    background-color: {HtmlColor.amber.value};
                }}
                .killed {{
                    background-color: {HtmlColor.green.value};
                    color: white;
                }}
                .task-output, .task-diff {{
                    background-color: {HtmlColor.lightgrey.value};
                    padding: 30px;
                }}
                .task-summary {{
                    padding: 10px 30px;
                    margin-bottom: 20px;
                }}
            """)
