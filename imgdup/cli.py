#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 koma <okunoya@path-works.net>
# All rights reserved.

"""Main CLI Setup and Entrypoint."""

from __future__ import absolute_import, division, print_function

# Import the main click library
import click
# Import the sub-command implementations
from .imgdup import imgdup
# Import the version information
from imgdup.version import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def cli():
    """cli tool: Image Duplicate finder using Image Hash."""
    pass


#  ahash:          Average hash
@cli.command()
@click.argument('PATH', type=click.Path(exists=True))
@click.option(
    '--hash-size', '-s', default=8, type=int,
    metavar='<size>',
    help='hash size to use for image hashing'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def ahash(**kwargs):
    """Use Average hash to find duplicates in PATH"""
    imgdup.find_dup(kwargs, hashmethod='ahash')
    pass

#  phash:          Perceptual hash
@cli.command()
@click.argument('PATH', type=click.Path(exists=True))
@click.option(
    '--hash-size', '-s', default=8, type=int,
    metavar='<size>',
    help='hash size to use for image hashing'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def phash(**kwargs):
    """Use Perceptual hash to find duplicates in PATH"""
    imgdup.find_dup(kwargs, hashmethod='phash')
    pass

#  dhash:          Difference hash
@cli.command()
@click.argument('PATH', type=click.Path(exists=True))
@click.option(
    '--hash-size', '-s', default=8, type=int,
    metavar='<size>',
    help='hash size to use for image hashing'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def dhash(**kwargs):
    """Use Difference hash to find duplicates in PATH"""
    imgdup.find_dup(kwargs, hashmethod='dhash')
    pass

@cli.command()
@click.argument('PATH', type=click.Path(exists=True))
@click.option(
    '--hash-size', '-s', default=8, type=int,
    metavar='<size>',
    help='hash size to use for image hashing'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def haar(**kwargs):
    """Use Haar wavelet hash to find duplicates in PATH"""
    imgdup.find_dup(kwargs, hashmethod='whash-haar')
    pass

@cli.command()
@click.argument('PATH', type=click.Path(exists=True))
@click.option(
    '--hash-size', '-s', default=8, type=int,
    metavar='<size>',
    help='hash size to use for image hashing'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def db4(**kwargs):
    """Use Daubechies wavelet hash to find duplicates in PATH"""
    imgdup.find_dup(kwargs, hashmethod='whash-db4')
    pass

@cli.command()
@click.argument('PATH', type=click.Path(exists=True))
@click.option(
    '--hash-size', '-s', default=8, type=int,
    metavar='<size>',
    help='hash size to use for image hashing'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def color(**kwargs):
    """Use HSV color hash to find duplicates in PATH"""
    imgdup.find_dup(kwargs, hashmethod='colorhash')
    pass

@cli.command()
@click.argument('PATH', type=click.Path(exists=True))
@click.option(
    '--hash-size', '-s', default=8, type=int,
    metavar='<size>',
    help='hash size to use for image hashing'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def crop(**kwargs):
    """Use Crop resistant hash to find similar images in PATH"""
    imgdup.find_dup(kwargs, hashmethod='crop-resistant')
    pass

# Entry point
def main():
    """Main script."""
    cli()

if __name__ == '__main__':
    main()
