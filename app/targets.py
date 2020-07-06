import re, itertools, logging

logger = logging.getLogger(__name__)

def expand_input_line(inp):
    var = []

    logger.info(f'add target {inp}')

    def push_var(num_range):
        var.append(tuple(int(x) for x in num_range.group().split('-')))
        return '{}'

    fmt = re.sub(r'\d+-\d+', push_var, inp)
    res = []

    for x in itertools.product(*[range(x[0], x[1] + 1) for x in var]):
        tar = fmt.format(*x)

        if re.match(r'\S*?:\d', tar) is None:
            raise ValueError

        tar = tar.split(':')
        ip = tar[0]
        port = int(tar[1])

        if port < 1 or port > 65535:
            raise ValueError

        res.append((ip, port))

    return res

def parse_input(inp):
    inp = inp.strip().split(',' if ',' in inp else None)

    res = []

    for line in inp:
        try:
            res += expand_input_line(line.strip())
        except ValueError:
            raise ValueError(f'target format error: {line}')

    return res

if __name__ == '__main__':
    print(parse_input('192.168.1.1:80,192.168.1.1:909999'))