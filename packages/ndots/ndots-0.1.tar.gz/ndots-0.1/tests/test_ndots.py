import pytest

from textwrap import dedent
from pathlib import Path
import sys
import os

if __name__ == "__main__":  # to make the tests run without the pytest cli
    file_folder = Path(__file__).parent
    top_folder = (file_folder / ".." / "ndots").resolve()
    sys.path.insert(0, str(top_folder))
    os.chdir(file_folder)


from ndots import fiftydots

grid = fiftydots.grid
coordinates = fiftydots.coordinates
grid_to_str = fiftydots.grid_to_str


def grid_to_str1(grid, leftborder="<", rightborder=">"):
    result = ""
    for l in grid:
        result += leftborder + ("".join("*" if vl else " " for vl in l)) + rightborder + "\n"
    return result


def test_grid_NonProportional_0():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=False, width=None, align="c") == dedent(
        """\
<                                                                       >
<      *                     *          *        *       *     *    *** >
<      *                     *         * *       *             *   *   *>
< ***  * **   ***         ** *  ***    *    **** * **   **     *   *   *>
<    * **  * *           *  ** *   *  ***  *   * **  *   *     *   *****>
< **** *   * *           *   * *****   *   *   * *   *   *     *   *   *>
<*   * *   * *   *       *   * *       *   *  ** *   *   *         *   *>
< ****  ***   ***         ****  ***    *    ** * *   *  ***    *   *   *>
<                                              *                        >
<                                           ***                         >"""
    )


def test_grid_NonProportional_1():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=False, width=80, align="c") == dedent(
        """\
<                                                                                >
<          *                     *          *        *       *     *    ***      >
<          *                     *         * *       *             *   *   *     >
<     ***  * **   ***         ** *  ***    *    **** * **   **     *   *   *     >
<        * **  * *           *  ** *   *  ***  *   * **  *   *     *   *****     >
<     **** *   * *           *   * *****   *   *   * *   *   *     *   *   *     >
<    *   * *   * *   *       *   * *       *   *  ** *   *   *         *   *     >
<     ****  ***   ***         ****  ***    *    ** * *   *  ***    *   *   *     >
<                                                  *                             >
<                                               ***                              >"""
    )


def test_grid_NonProportional_2():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=False, width=80, align="c") == dedent(
        """\
<                                                                                >
<          *                     *          *        *       *     *    ***      >
<          *                     *         * *       *             *   *   *     >
<     ***  * **   ***         ** *  ***    *    **** * **   **     *   *   *     >
<        * **  * *           *  ** *   *  ***  *   * **  *   *     *   *****     >
<     **** *   * *           *   * *****   *   *   * *   *   *     *   *   *     >
<    *   * *   * *   *       *   * *       *   *  ** *   *   *         *   *     >
<     ****  ***   ***         ****  ***    *    ** * *   *  ***    *   *   *     >
<                                                  *                             >
<                                               ***                              >"""
    )


def test_grid_NonProportional_3():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=False, width=80, align="c") == dedent(
        """\
<                                                                                >
<          *                     *          *        *       *     *    ***      >
<          *                     *         * *       *             *   *   *     >
<     ***  * **   ***         ** *  ***    *    **** * **   **     *   *   *     >
<        * **  * *           *  ** *   *  ***  *   * **  *   *     *   *****     >
<     **** *   * *           *   * *****   *   *   * *   *   *     *   *   *     >
<    *   * *   * *   *       *   * *       *   *  ** *   *   *         *   *     >
<     ****  ***   ***         ****  ***    *    ** * *   *  ***    *   *   *     >
<                                                  *                             >
<                                               ***                              >"""
    )


def test_grid_NonProportional_4():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=False, width=40, align="c") == dedent(
        """\
<                                        >
<             *          *        *      >
<             *         * *       *      >
<*         ** *  ***    *    **** * **   >
<         *  ** *   *  ***  *   * **  *  >
<         *   * *****   *   *   * *   *  >
< *       *   * *       *   *  ** *   *  >
<*         ****  ***    *    ** * *   *  >
<                               *        >
<                            ***         >"""
    )


def test_grid_NonProportional_5():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=False, width=40, align="c") == dedent(
        """\
<                                        >
<             *          *        *      >
<             *         * *       *      >
<*         ** *  ***    *    **** * **   >
<         *  ** *   *  ***  *   * **  *  >
<         *   * *****   *   *   * *   *  >
< *       *   * *       *   *  ** *   *  >
<*         ****  ***    *    ** * *   *  >
<                               *        >
<                            ***         >"""
    )


def test_grid_NonProportional_6():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=False, width=40, align="c") == dedent(
        """\
<                                        >
<             *          *        *      >
<             *         * *       *      >
<*         ** *  ***    *    **** * **   >
<         *  ** *   *  ***  *   * **  *  >
<         *   * *****   *   *   * *   *  >
< *       *   * *       *   *  ** *   *  >
<*         ****  ***    *    ** * *   *  >
<                               *        >
<                            ***         >"""
    )


def test_grid_NonProportional_7():
    assert grid_to_str(s="", default=" ", intra=1, proportional=False, width=None, align="c") == dedent(
        """\
<>
<>
<>
<>
<>
<>
<>
<>
<>
<>"""
    )


def test_grid_NonProportional_8():
    assert grid_to_str(s=" ", default=" ", intra=1, proportional=False, width=None, align="c") == dedent(
        """\
<     >
<     >
<     >
<     >
<     >
<     >
<     >
<     >
<     >
<     >"""
    )


def test_grid_Proportional_0():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=True, width=None, align="c") == dedent(
        """\
<                                                             >
<      *                  *         *        *      *  *  *** >
<      *                  *        * *       *         * *   *>
< ***  * **   ***      ** *  ***   *    **** * **  **  * *   *>
<    * **  * *        *  ** *   * ***  *   * **  *  *  * *****>
< **** *   * *        *   * *****  *   *   * *   *  *  * *   *>
<*   * *   * *   *    *   * *      *   *  ** *   *  *    *   *>
< ****  ***   ***      ****  ***   *    ** * *   * *** * *   *>
<                                          *                  >
<                                       ***                   >"""
    )


def test_grid_Proportional_1():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=True, width=80, align="c") == dedent(
        """\
<                                                                                >
<               *                  *         *        *      *  *  ***           >
<               *                  *        * *       *         * *   *          >
<          ***  * **   ***      ** *  ***   *    **** * **  **  * *   *          >
<             * **  * *        *  ** *   * ***  *   * **  *  *  * *****          >
<          **** *   * *        *   * *****  *   *   * *   *  *  * *   *          >
<         *   * *   * *   *    *   * *      *   *  ** *   *  *    *   *          >
<          ****  ***   ***      ****  ***   *    ** * *   * *** * *   *          >
<                                                   *                            >
<                                                ***                             >"""
    )


def test_grid_Proportional_2():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=True, width=80, align="c") == dedent(
        """\
<                                                                                >
<               *                  *         *        *      *  *  ***           >
<               *                  *        * *       *         * *   *          >
<          ***  * **   ***      ** *  ***   *    **** * **  **  * *   *          >
<             * **  * *        *  ** *   * ***  *   * **  *  *  * *****          >
<          **** *   * *        *   * *****  *   *   * *   *  *  * *   *          >
<         *   * *   * *   *    *   * *      *   *  ** *   *  *    *   *          >
<          ****  ***   ***      ****  ***   *    ** * *   * *** * *   *          >
<                                                   *                            >
<                                                ***                             >"""
    )


def test_grid_Proportional_3():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=True, width=80, align="c") == dedent(
        """\
<                                                                                >
<               *                  *         *        *      *  *  ***           >
<               *                  *        * *       *         * *   *          >
<          ***  * **   ***      ** *  ***   *    **** * **  **  * *   *          >
<             * **  * *        *  ** *   * ***  *   * **  *  *  * *****          >
<          **** *   * *        *   * *****  *   *   * *   *  *  * *   *          >
<         *   * *   * *   *    *   * *      *   *  ** *   *  *    *   *          >
<          ****  ***   ***      ****  ***   *    ** * *   * *** * *   *          >
<                                                   *                            >
<                                                ***                             >"""
    )


def test_grid_Proportional_4():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=True, width=40, align="c") == dedent(
        """\
<                                        >
<               *         *        *     >
<               *        * *       *     >
<   ***      ** *  ***   *    **** * **  >
<* *        *  ** *   * ***  *   * **  * >
<* *        *   * *****  *   *   * *   * >
<* *   *    *   * *      *   *  ** *   * >
<   ***      ****  ***   *    ** * *   * >
<                                *       >
<                             ***        >"""
    )


def test_grid_Proportional_5():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=True, width=40, align="c") == dedent(
        """\
<                                        >
<               *         *        *     >
<               *        * *       *     >
<   ***      ** *  ***   *    **** * **  >
<* *        *  ** *   * ***  *   * **  * >
<* *        *   * *****  *   *   * *   * >
<* *   *    *   * *      *   *  ** *   * >
<   ***      ****  ***   *    ** * *   * >
<                                *       >
<                             ***        >"""
    )


def test_grid_Proportional_6():
    assert grid_to_str(s="abc defghi!A", default=" ", intra=1, proportional=True, width=40, align="c") == dedent(
        """\
<                                        >
<               *         *        *     >
<               *        * *       *     >
<   ***      ** *  ***   *    **** * **  >
<* *        *  ** *   * ***  *   * **  * >
<* *        *   * *****  *   *   * *   * >
<* *   *    *   * *      *   *  ** *   * >
<   ***      ****  ***   *    ** * *   * >
<                                *       >
<                             ***        >"""
    )


def test_grid_Proportional_7():
    assert grid_to_str(s="", default=" ", intra=1, proportional=True, width=None, align="c") == dedent(
        """\
<>
<>
<>
<>
<>
<>
<>
<>
<>
<>"""
    )


def test_grid_Proportional_8():
    assert grid_to_str(s=" ", default=" ", intra=1, proportional=True, width=None, align="c") == dedent(
        """\
<  >
<  >
<  >
<  >
<  >
<  >
<  >
<  >
<  >
<  >"""
    )


if __name__ == "__main__":
    pytest.main(["-vv", "-s", "-x", __file__])
