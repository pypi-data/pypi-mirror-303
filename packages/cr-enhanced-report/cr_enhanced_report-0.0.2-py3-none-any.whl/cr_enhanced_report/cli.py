"""Console script for cr_enhanced_report."""
import sys

from cr_enhanced_report.commands import cr_enhanced_report


def main() -> None:
    """Entry point."""
    sys.exit(cr_enhanced_report())
