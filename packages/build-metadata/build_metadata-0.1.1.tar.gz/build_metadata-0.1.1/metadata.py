import os
import re
import tempfile

from build.env import DefaultIsolatedEnv
from build import ProjectBuilder
from pyproject_hooks import quiet_subprocess_runner


def build_metadata(srcdir: str, installer: str = 'pip') -> str:
  with tempfile.TemporaryDirectory() as outdir:
    with DefaultIsolatedEnv(installer=installer) as env:
      builder = ProjectBuilder.from_isolated_env(
        env,
        srcdir,
        runner=quiet_subprocess_runner,
      )
      env.install(builder.build_system_requires)
      env.install(builder.get_requires_for_build('wheel', {}))
      dist_info = builder._call_backend(
        'prepare_metadata_for_build_wheel',
        outdir,
        {}
      )
      with open(os.path.join(dist_info, 'METADATA')) as metadata_fp:
        return metadata_fp.read()
      # with DefaultIsolatedEnv as env
    # with tempfile.TemporaryDirectory as outdir
  # def build_metadata -> str


def parse_metadata(src: str, *metadata) -> list[str]:
  metadata_re = tuple(
    (metadata_item, re.compile(rf'{metadata_item}: (.*)', re.IGNORECASE))
    for metadata_item in metadata
  )
  built_metadata = {
    metadata_item: re_match.group(1)
    for metadata_line in src.splitlines()
    for metadata_item, regex in metadata_re
    if (re_match := regex.match(metadata_line))
  }
  return [
    built_metadata.get(metadata_item, '')
    for metadata_item in metadata
  ]
  # def parse_metadata -> list[str]


def _parser():
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(
    'srcdir',
    type=str,
    nargs='?',
    default=os.getcwd(),
  )
  parser.add_argument(
    '--metadata',
    '-m',
    nargs='+',
    dest='metadata',
  )
  return parser
  # def _parser


if __name__ == '__main__':
  from sys import argv
  args = _parser().parse_args(argv[1:])
  print('\n'.join(parse_metadata(
    build_metadata(
      args.srcdir,
    ),
    *(args.metadata or ['name']),
  )))
