# Copyright (C) 2024 Kian-Meng Ang
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Resize subcommand."""

import argparse
import logging
import math

from PIL import Image

from fotolab import save_image

log = logging.getLogger(__name__)

DEFAULT_WIDTH = 600
DEFAULT_HEIGHT = 277


def build_subparser(subparsers) -> None:
    """Build the subparser."""
    resize_parser = subparsers.add_parser("resize", help="resize an image")

    resize_parser.set_defaults(func=run)

    resize_parser.add_argument(
        dest="image_filenames",
        help="set the image filename",
        nargs="+",
        type=str,
        default=None,
        metavar="IMAGE_FILENAMES",
    )

    group = resize_parser.add_mutually_exclusive_group(required=False)

    group.add_argument(
        "-wh",
        "--width",
        dest="width",
        help="set the width of the image (default: '%(default)s')",
        type=int,
        default=DEFAULT_WIDTH,
        metavar="WIDTH",
    )

    group.add_argument(
        "-ht",
        "--height",
        dest="height",
        help="set the height of the image (default: '%(default)s')",
        type=int,
        default=DEFAULT_HEIGHT,
        metavar="HEIGHT",
    )


def run(args: argparse.Namespace) -> None:
    """Run resize subcommand.

    Args:
        args (argparse.Namespace): Config from command line arguments

    Returns:
        None
    """
    log.debug(args)

    for image_filename in args.image_filenames:
        original_image = Image.open(image_filename)

        new_width, new_height = _calc_new_image_dimension(original_image, args)
        resized_image = original_image.copy()
        resized_image = resized_image.resize(
            (new_width, new_height), Image.Resampling.LANCZOS
        )

        save_image(args, resized_image, image_filename, "resize")


def _calc_new_image_dimension(image, args) -> tuple:
    new_width = args.width
    new_height = args.height

    old_width, old_height = image.size
    log.debug("old image dimension: %d x %d", old_width, old_height)

    if args.width != DEFAULT_WIDTH:
        aspect_ratio = old_height / old_width
        log.debug("aspect ratio: %f", aspect_ratio)

        new_height = math.ceil(args.width * aspect_ratio)
        log.debug("new height: %d", new_height)

    if args.height != DEFAULT_HEIGHT:
        aspect_ratio = old_width / old_height
        log.debug("aspect ratio: %f", aspect_ratio)

        new_width = math.floor(args.height * aspect_ratio)
        log.debug("new width: %d", new_width)

    log.debug("new image dimension: %d x %d", new_width, new_height)

    return (new_width, new_height)
