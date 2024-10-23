# Copyright 2024, INRAE, France, François Victor <francois.victor@inrae.fr>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""file containing command line interface and the main script that performs ppca"""
import argparse
from dataclasses import dataclass
import sys
from typing import Any

import numpy as np

# from sklearn import datasets
# from tqdm import tqdm
# import pandas as pd

from prob_dim_red import linear_gaussian_ppca as ppca

# from prob_dim_red import utils


@dataclass(kw_only=True, frozen=True)  # pylint: disable=unexpected-keyword-arg
class _BoundedInteger:  # pylint: disable=too-few-public-methods,unsupported-binary-operation
    inf: int | None = None
    sup: int | None = None

    def __call__(self, x):
        y = int(x)
        if self.inf is not None and y < self.inf:
            raise ValueError
        if self.sup is not None and y > self.sup:
            raise ValueError
        return y


# @dataclass
# class CsvArray:
#     filename: str

#     @cached_property
#     def array(self):
#         with argparse.FileType('r')(self.filename) as f:
#             return pd.read_csv(f, engine='python').to_numpy() # indiv name lost


def _parser():
    """
    Argument parser
    """
    common_parser = argparse.ArgumentParser(add_help=False)

    common_parser.add_argument(
        "input", type=argparse.FileType("r"), default=sys.stdin, nargs="?"
    )

    common_parser.add_argument(
        "output", type=argparse.FileType("w"), default=sys.stdout, nargs="?"
    )

    c_fixed_parser = argparse.ArgumentParser(add_help=False)

    c_fixed_parser.add_argument(
        "-c",
        "--components",
        type=_BoundedInteger(inf=1),
        default=2,
        help="Number of components for PPCA (default: 2).",
    )

    parent_parser = argparse.ArgumentParser(
        description="Perform various PPCA methods on a dataset."
    )

    subparsers = parent_parser.add_subparsers(
        dest="method", required=True, help="PPCA method to use"
    )

    # MLE method
    _parser_mle = subparsers.add_parser(
        "mle",
        parents=[common_parser, c_fixed_parser],
        help="Perform PPCA using maximum likelihood estimation.",
    )

    # EM method
    _parser_em = subparsers.add_parser(
        "em",
        parents=[common_parser, c_fixed_parser],
        help="Perform PPCA using expectation maximization.",
    )

    # ARD method
    _parser_ard = subparsers.add_parser(
        "ard",
        parents=[common_parser],
        help="Perform PPCA using automatic relevance determination.",
    )

    return parent_parser


def _build_input_matrix(args: argparse.Namespace):

    return np.loadtxt(args.input)


def _build_output(args: argparse.Namespace, result: Any):
    np.savetxt(args.output, result.W)


def main() -> None:
    """
    Execute the main workflow for performing probabilistic principal component analysis (PPCA)
    """
    args = _parser().parse_args()

    data = _build_input_matrix(args)

    match args.method:
        case "mle":
            model = ppca.LinearGaussianPPCAEstimMLE(
                data=data, n_components=args.components
            )

        case "em":
            model = ppca.LinearGaussianPPCAEstimEM(
                data=data, n_components=args.components
            )

        case "ard":
            model = ppca.LinearGaussianPPCAEstimARD(data=data)
    model.fit()

    _build_output(args, model.result)
