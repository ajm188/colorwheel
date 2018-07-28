import argparse
import sys
from collections import defaultdict
from collections import deque
from pathlib import Path

from colorwheel import nodes


class Layer(defaultdict):

    def __init__(self):
        super().__init__(lambda: 0)


def analyze(path):
    with open(path) as f:
        root = ast.parse(f.read()).body[0]

    layers, queue = [], deque()
    queue.append((root, 0))

    while queue:
        node, depth = queue.pop()
        # ensure we have layers up to our depth
        layers.extend([Layer() for _ in range(len(layers), depth + 1)])
        layer = layers[depth]

        color = nodes.color[node]
        points = nodes.
        layer[nodes.color[node]]
        layer[node_color(node)] += 1
        if type(node) in nodes.terminal:
            continue

        if type(node) in nodes.scoped:
            d = depth + 1
            if isinstance(node, ast.comprehension):
                # special handling bc no .body attr
                # work with .iter and .ifs attrs instead
                queue.extend([(n, d) for n in node.iter])
                queue.extend([(n, d) for n in node.ifs])
            else:
                queue.extend([(n, d) for n in node.body])

        # this is the part where we iterate over the child nodes, but maybe
        # also attributes? i'm not 100% sure yet


def collect_files(path):
    if path.is_file():
        return [path] if path.suffix == '.py' else []

    return path.glob('**/*.py')


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('module')
    return parser


def _main(argv):
    parser = build_parser()
    parsed_args = parser.parse_args(argv)
    files = collect_files(Path(parsed_args.module))
    wheels = map(analyze, files)
    wheel = reduce(lambda a, b: a + b, wheels, Layer())
    return 0


def main():
    sys.exit(_main(sys.argv[1:]))


"""
if __name__ == '__main__':
    main()

"""
