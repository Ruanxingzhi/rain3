import re, itertools, logging
from app.models.target import Target
from app.controllers.db import get_db

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
        host_name = tar[0]
        port = int(tar[1])

        if port < 1 or port > 65535:
            raise ValueError

        res.append(Target(host_name, port))

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


def get_all_targets():
    db = get_db()

    return db.execute('SELECT id, host, port, enabled FROM target')  \
             .fetchall()

def set_many_targets(tars):
    todo = parse_input(tars)
    db = get_db()

    exists = [{'info': Target(x['host'], x['port']),
               'enabled': x['enabled'],
               'id': x['id']} for x in get_all_targets()]

    to_enable = []
    to_add = []

    for x in todo:
        is_in = False

        for now in exists:
            if x == now['info']:
                is_in = True

                if now['enabled'] == False:
                    to_enable.append(now)
                break

        print(is_in)
        if not is_in:
            to_add.append(x)

    db.executemany(
        'INSERT INTO target (host, port) VALUES (?, ?)',
        [(x.host, x.port) for x in to_add]
    )

    db.executemany(
        'UPDATE target SET enabled = true WHERE id = ?',
        [(x['id'], ) for x in to_enable]
    )

    db.commit()



    return to_add, to_enable


def disable_many_targets(tars):
    todo = parse_input(tars)
    db = get_db()

    exists = [{'info': Target(x['host'], x['port']),
               'enabled': x['enabled'],
               'id': x['id']} for x in get_all_targets()]

    to_disable = []

    for x in todo:
        for now in exists:
            if x == now['info']:
                if now['enabled'] == True:
                    to_disable.append(now)
                break

    db.executemany(
        'UPDATE target SET enabled = FALSE WHERE id = ?',
        [(x['id'], ) for x in to_disable]
    )

    db.commit()

    return to_disable

if __name__ == '__main__':
    res = parse_input('192.168.1.1:80,lilac.run:11451')
    print(res[0])
    print(res[1])
