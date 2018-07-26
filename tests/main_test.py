from pathlib import Path

from colorwheel import main


class TestCollectFiles(object):

    def test_single_file(self, tmpdir):
        tmpdir.join('foo.py').write('')
        files = main.collect_files(Path(tmpdir.join('foo.py')))
        assert files == [tmpdir.join('foo.py')]

    def test_module(self, tmpdir):
        tmpdir.join('foo.py').write('')
        files = list(main.collect_files(Path(tmpdir)))
        assert files == [tmpdir.join('foo.py')]

    def test_module_python_only(self, tmpdir):
        for ext in ['rb', 'py']:
            tmpdir.join('foo.{ext}'.format(ext=ext)).write('')

        files = list(main.collect_files(Path(tmpdir)))
        assert Path(tmpdir.join('foo.py')) in files
        assert Path(tmpdir.join('foo.rb')) not in files

    def test_module_deeper_nesting(self, tmpdir):
        tmpdir.join('foo.py').write('')
        tmpdir.mkdir('bar').join('foo.py').write('')
        tmpdir.join('bar').join('foo.rb').write('')

        files = list(main.collect_files(Path(tmpdir)))
        assert Path(tmpdir.join('foo.py')) in files
        assert Path(tmpdir.join('bar').join('foo.py')) in files
        assert Path(tmpdir.join('bar').join('foo.rb')) not in files


def test_parser():
    parser = main.build_parser()
    parsed_args = parser.parse_args(['foo'])
    assert parsed_args.module == 'foo'


def test_main():
    assert main._main(['']) == 0
