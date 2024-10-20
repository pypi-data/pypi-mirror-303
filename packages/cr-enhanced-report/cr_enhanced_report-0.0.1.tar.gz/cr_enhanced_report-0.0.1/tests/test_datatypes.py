"""Set of tests to test datatypes."""
from pathlib import Path

import pytest

from cr_enhanced_report.datatypes import SummaryDetail


class TestDataTypes():
    """Tests for data typess."""

    @pytest.mark.parametrize(
        'path_a,path_a_is_dir,path_b,path_b_is_dir,expected',
        [
            [
                '/folder1',
                True,
                '/folder1',
                True,
                True,
            ],
            [
                '/file1.py',
                False,
                '/file1.py',
                False,
                True,
            ],
            [
                '/',
                True,
                '/folder1',
                True,
                False,
            ],
            [
                '/folder1',
                True,
                '/',
                True,
                False,
            ],
            [
                '/folder1',
                True,
                '/folder2',
                True,
                False,
            ],
            [
                '/folder2',
                True,
                '/folder1',
                True,
                False,
            ],
            [
                '/folder1',
                True,
                '/folder1/folder2',
                True,
                False,
            ],
            [
                '/folder1/folder2',
                True,
                '/folder1',
                True,
                False,
            ],
            [
                '/',
                True,
                '/file1.py',
                False,
                False,
            ],
            [
                '/file1.py',
                False,
                '/',
                True,
                False,
            ],
            [
                '/folder1',
                True,
                '/gfile1.py',
                False,
                False,
            ],
            [
                '/gfile1.py',
                False,
                '/folder1',
                True,
                False,
            ],
            [
                '/folder1/folder2',
                True,
                '/folder1/file1.py',
                False,
                False,
            ],
            [
                '/folder1/file1.py',
                False,
                '/folder1/folder2',
                True,
                False,
            ],
            [
                '/folder1/file1.py',
                False,
                '/folder1/folder2/file2.py',
                False,
                False
            ],
            [
                '/folder1/folder2/file2.py',
                False,
                '/folder1/file1.py',
                False,
                False
            ],
        ],
    )
    def test_eq(self, path_a: str, path_a_is_dir: bool, path_b: str, path_b_is_dir: bool, expected: bool):
        """
        Test to ensure the equal than logic is correct.

        Args:
            path_a (str): Path to the first file.
            path_a_is_dir (bool): True if the first file is a directory.
            path_b (str): Path to the second file.
            path_b_is_dir (bool): True if the second file is a directory.
            expected (bool): The expected result of the comparison.
        """
        summary_a = SummaryDetail(
            path=Path(path_a),
            is_dir=path_a_is_dir,
        )
        summary_b = SummaryDetail(
            path=Path(path_b),
            is_dir=path_b_is_dir,
        )
        result = summary_a == summary_b
        assert result == expected, f'{path_a} == {path_b} expected: {expected} got: {result}'

    def test_eq_incorrect_datatype(self):
        """Test to ensure the equal than logic is correct when datatypes do not match."""
        summary = SummaryDetail(
            path=Path('/folder1'),
            is_dir=False,
        )
        result = summary == 'SomeString'
        assert result is False, f'/folder1 == False expected: {False} got: {result}'

    @pytest.mark.parametrize(
        'path_a,path_a_is_dir,path_b,path_b_is_dir,expected',
        [
            [
                '/folder1',
                True,
                '/folder1',
                True,
                False,
            ],
            [
                '/file1.py',
                False,
                '/file1.py',
                False,
                False,
            ],
            [
                '/',
                True,
                '/folder1',
                True,
                True,
            ],
            [
                '/folder1',
                True,
                '/',
                True,
                False,
            ],
            [
                '/folder1',
                True,
                '/folder2',
                True,
                True,
            ],
            [
                '/folder2',
                True,
                '/folder1',
                True,
                False,
            ],
            [
                '/folder1',
                True,
                '/folder1/folder2',
                True,
                True,
            ],
            [
                '/folder1/folder2',
                True,
                '/folder1',
                True,
                False,
            ],
            [
                '/',
                True,
                '/file1.py',
                False,
                True,
            ],
            [
                '/file1.py',
                False,
                '/',
                True,
                False,
            ],
            [
                '/folder1',
                True,
                '/gfile1.py',
                False,
                True,
            ],
            [
                '/gfile1.py',
                False,
                '/folder1',
                True,
                False,
            ],
            [
                '/folder1/folder2',
                True,
                '/folder1/file1.py',
                False,
                True,
            ],
            [
                '/folder1/file1.py',
                False,
                '/folder1/folder2',
                True,
                False,
            ],
            [
                '/folder1/file1.py',
                False,
                '/folder1/folder2/file2.py',
                False,
                False
            ],
            [
                '/folder1/folder2/file2.py',
                False,
                '/folder1/file1.py',
                False,
                True
            ],
        ],
    )
    def test_lt(self, path_a, path_a_is_dir, path_b, path_b_is_dir, expected):
        """
        Test to ensure the less than logic is correct.

        Args:
            path_a (str): Path to the first file.
            path_a_is_dir (bool): True if the first file is a directory.
            path_b (str): Path to the second file.
            path_b_is_dir (bool): True if the second file is a directory.
            expected (bool): The expected result of the comparison.
        """
        summary_a = SummaryDetail(
            path=Path(path_a),
            is_dir=path_a_is_dir,
        )
        summary_b = SummaryDetail(
            path=Path(path_b),
            is_dir=path_b_is_dir,
        )
        result = summary_a < summary_b
        assert result == expected, f'{path_a} < {path_b} expected: {expected} got: {result}'

    @pytest.mark.parametrize(
        'killed,incompetent,survived,expected',
        [
            [
                10,
                5,
                5,
                50,
            ],
            [
                0,
                5,
                5,
                0,
            ],
        ],
    )
    def test_score(self, killed: int, incompetent: int, survived: int, expected):
        """
        Test the score method.

        Args:
            killed (str): The number to set as killed.
            incompetent (int): The number to set as incompetent.
            survived (int): The number to set as survived.
            expected (str): The expected value from score.
        """
        summary = SummaryDetail(
            path=Path('/'),
            is_dir=False,
            killed=killed,
            incompetent=incompetent,
            survived=survived,
        )

        assert summary.score == expected, f'expected: {expected} got: {summary.score}'

    @pytest.mark.parametrize(
        'attribute,value',
        [
            [
                'killed',
                9,
            ],
            [
                'incompetent',
                27,
            ],
            [
                'survived',
                47,
            ],
        ],
    )
    def test_setter_getter(self, attribute: str, value: int):
        """
        Test setters and getters.

        Args:
            attribute (str): Attribute name.
            value (int): Value of the attribute.
        """
        summary = SummaryDetail(
            path=Path('/folder1/file1.py'),
            is_dir=False,
            killed=0,
            incompetent=0,
            survived=0,
        )
        assert getattr(summary, attribute) == 0
        setattr(summary, attribute, value)
        assert getattr(summary, attribute) == value

    @pytest.mark.parametrize(
        'path,is_dir,killed,incompetent,survived,expected',
        [
            [
                '/',
                True,
                7,
                4,
                100,
                "SummaryDetail(path='/', is_dir=True, killed=7, incompetent=4, survived=100)"
            ],
            [
                '/some_file.py',
                False,
                35,
                1,
                0,
                "SummaryDetail(path='/some_file.py', is_dir=False, killed=35, incompetent=1, survived=0)"
            ],
        ]
    )
    def test_str(self, path: str, is_dir: bool, killed: int, incompetent: int, survived: int, expected: str):
        """
        Test the to string method.

        Args:
            path (str): The path.
            is_dir (bool): True if the path is a directory.
            killed (int): The number to set as survived.
            incompetent (int): The number to set as survived.
            survived (int): The number to set as survived.
            expected (str): The expected value from __str__.
        """
        summary = SummaryDetail(
            path=Path(path),
            is_dir=is_dir,
            killed=killed,
            incompetent=incompetent,
            survived=survived,
        )
        assert str(summary) == expected, f'{str(summary)} == {expected}'
