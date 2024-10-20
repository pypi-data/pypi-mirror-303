"""Module to declare datatypes used in the cosmic-ray report."""
import enum
import functools
import pathlib
from dataclasses import dataclass


class HtmlColor(enum.Enum):
    """Enum to store HTML colors for different states."""

    amber = 'orange'
    green = 'green'
    lightgrey = 'lightgrey'
    red = 'red'


@dataclass
class TaskData:
    """Data class to store report summary data."""

    module_path: str
    status_count: dict[str, int]


@functools.total_ordering
class SummaryDetail(object):
    """Object to store summary details for a given file."""

    __slots__ = (
        '_is_dir',
        '_killed',
        '_incompetent',
        '_path',
        '_survived',
    )

    def __init__(
        self,
        path: pathlib.Path,
        is_dir: bool = False,
        killed: int = 0,
        incompetent: int = 0,
        survived: int = 0,
    ) -> None:
        """
        Initialize a SummaryDetail object.

        Args:
            path (pathlib.Path): Path to the summary file.
            is_dir (bool, optional): Whether the summary file is a directory. Defaults to False.
            killed (int, optional): Killed status. Defaults to 0.
            incompetent (int, optional): Incompetent status. Defaults to 0.
            survived (int, optional): Survived status. Defaults to 0.
        """
        self._path = path
        self._is_dir = is_dir
        self._incompetent = incompetent
        self._killed = killed
        self._survived = survived

    @property
    def is_dir(self) -> bool:
        """
        Whether the summary file is a directory.

        Returns:
            bool: Whether the summary file is a directory.
        """
        return self._is_dir

    @property
    def killed(self) -> int:
        """
        Property for killed status. Defaults to 0.

        Returns:
            int: Killed status.
        """
        return self._killed

    @killed.setter
    def killed(self, killed: int) -> None:
        """
        Setter for killed status. Defaults to 0.

        Args
            killed (int): Killed status.
        """
        self._killed = killed

    @property
    def incompetent(self) -> int:
        """
        Property for incompetent status. Defaults to 0.

        Returns:
            int: Incompetent status.
        """
        return self._incompetent

    @incompetent.setter
    def incompetent(self, incompetent: int) -> None:
        """
        Setter for incompetent status. Defaults to 0.

        Args
            incompetent (int): Incompetent status.
        """
        self._incompetent = incompetent

    @property
    def path(self) -> pathlib.Path:
        """
        Property for file and path.

        Returns:
            pathlib.Path: Path for the file the summary is for.
        """
        return self._path

    def path_list(self) -> list[pathlib.Path]:
        """
        Fetch a list of directories the file is in.

        Returns:
            list[pathlib.Path]: List of directories the file is in.
        """
        path_parts = self.path.parts[1:] if self.is_dir else self.path.parts[1: -1]
        part_count = len(path_parts)
        paths: list[pathlib.Path] = [
            pathlib.Path('/'),
        ]
        paths.extend(pathlib.Path('/').joinpath('/'.join(path_parts[:i+1])) for i in range(part_count))
        return paths

    @property
    def score(self) -> float:
        """
        Property for the score for the file.

        Returns:
            Float: Score for the file.
        """
        total_tests = self.killed + self.incompetent + self.survived
        return 0.0 if self.killed == 0 else round(self.killed / total_tests * 100, 2)

    @property
    def survived(self) -> int:
        """
        Property for survived status. Defaults to 0.

        Returns:
            int: Survived status.
        """
        return self._survived

    @survived.setter
    def survived(self, survived: int = 0) -> None:
        """
        Setter for survived status. Defaults to 0.

        Args
            survived (int): Survived status.
        """
        self._survived = survived

    def __eq__(self, other: object) -> bool:
        """
        Equals operator.

        Args:
            other (object): Other object.

        Returns:
            True if self equals other, False otherwise.
        """
        return self._path == other._path if isinstance(other, SummaryDetail) else False

    def __lt__(self, other: 'SummaryDetail') -> bool:
        """
        Less than operator.

        Args:
            other (SummaryDetail): Other object.

        Returns:
            True if self less than other, False otherwise.
        """
        if not isinstance(other, SummaryDetail):
            raise NotImplementedError()
        if self.is_dir == other.is_dir:
            if self.path == other.path:
                return False
            if self.is_dir:
                return self.path < other.path
            if self.path_list()[-1] == other.path_list()[-1]:
                return self.path < other.path
            if str(other.path).startswith(str(self.path_list()[-1])):
                return False
            if str(self.path).startswith(str(other.path_list()[-1])):
                return True
            return self.path_list()[-1] < other.path_list()[-1]
        if self.is_dir:
            other_path = other.path_list()[-1]
            self_path = self.path_list()[-1]
            if self.path == other_path:
                return True
            if str(self.path).startswith(str(other_path)):
                return True
            return self.path < other.path
        # The following is reached if other.is_dir is True
        self_path = self.path_list()[-1]
        if other.path == self_path:
            return False
        if str(other.path).startswith(str(self_path)):
            return False
        return self.path < other.path

    def __str__(self) -> str:
        """
        Represent the object as a string.

        Return:
            String representation of the summary file.
        """
        return (
            f"SummaryDetail(path='{self.path}', is_dir={self.is_dir}, killed={self.killed}, "
            + f"incompetent={self.incompetent}, survived={self.survived})"
        )
