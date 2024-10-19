def nested_get(root, *args, default=None):
    _args = list(args)
    _root = root
    try:
        while _args:
            _root = _root[_args.pop(0)]
    except (KeyError, TypeError):
        return default
    return root


def get_paginated(next_url, session, get_next):
    with session:
        while next_url:
            response = session.get(url=next_url)
            yield response
            next_url = get_next(response)


class IteratorExhausted(Exception):
    pass


class Iterator:
    def __iter__(self):
        return self


class cutoff_filter(Iterator):
    def __init__(self, func, it):
        self.it = iter(it)
        self.func = func

    def __next__(self):
        if self.func(_next := next(self.it)):
            return _next
        else:
            raise StopIteration()


def check_cond(cond, it):
    for item in it:
        if not cond(item):
            return False
    return True


class chain(Iterator):
    def __init__(self, *iterables):
        self.iterables = iter(iterables)
        self.cur = iter(next(self.iterables, []))

    def __next__(self):
        try:
            return next(self.cur)
        except StopIteration:
            self.cur = iter(next(self.iterables))
            return self.__next__()


class zip_longest(Iterator):
    def __init__(self, *its, fill):
        self.its = [iter(it) for it in its]
        self.fill = fill
        self.n_it = len(self.its)
        self.n_empty = 0

    def __next__(self):
        ret = []
        for i, it in enumerate(self.its):
            if it is None:
                ret.append(self.fill)
            else:
                try:
                    ret.append(next(it))
                except StopIteration:
                    self.its[i] = None
                    self.n_empty += 1
                    ret.append(self.fill)

        if self.n_empty == self.n_it:
            raise StopIteration
        else:
            return tuple(ret)


class product(Iterator):
    def __init__(self, it1, it2, group=False):
        self.it1 = iter(it1)
        self.lst2 = list(it2)
        self.group = group
        self.it = None

    def __next__(self):
        if self.group:
            return zip_longest([], self.lst2, fill=next(self.it1))
        else:
            if self.it is None:
                self.it = zip_longest([], self.lst2, fill=next(self.it1))
                return next(self)
            else:
                try:
                    return next(self.it)
                except StopIteration:
                    self.it = None
                    return next(self)


class group(Iterator):

    def __init__(self, it, eq, ret=None):
        self.it = it
        self.eq = eq
        self.ret = ret

    def __next__(self):
        _next = next(self.it)
        if self.eq(_next):
            return self.ret(_next) if self.ret is not None else _next
        else:
            self.it = chain([_next], self.it)
            raise StopIteration()


class grouped(Iterator):
    def __init__(self, it, group_func=None):
        self.it = it
        self.group_func = group_func if group_func is not None else lambda x: x
        self.comp = (
            (lambda el, val: group_func(el) == val)
            if group_func is not None
            else (lambda el, val: el == val)
        )
        self.group = None

    def __next__(self):
        if self.group is None:
            _next = next(self.it)
            val = self.group_func(_next)
            self.group = group(chain([_next], self.it), lambda el: self.comp(el, val))
            return (val, self.group)
        else:
            it = list(self.group)
            self.it = self.group.it
            self.group.it = iter(it)
            self.group = None
            return next(self)


class flatten(Iterator):
    def __init__(self, it, dim):
        if not dim > 0:
            raise ValueError("Dimension must be greater than 0")
        self.dim = dim
        self.its = [iter(it)]

    def __next__(self):
        try:
            while len(self.its) != self.dim:
                self.its.append(iter(next(self.its[-1])))
            return next(self.its[-1])
        except StopIteration:
            if len(self.its) == 1:
                raise
            self.its.pop()
            return next(self)


class islice(Iterator):
    def __init__(self, it, n):
        self.it = it
        self.n = n

    def __next__(self):
        if not self.n:
            raise StopIteration()
        self.n -= 1
        return next(self.it)


class chunked_iterator(Iterator):
    def __init__(self, it, chunksize):
        self.it = it
        self.chunksize = chunksize
        self.chunk = None

    def __next__(self):
        if self.chunk is None:
            _next = next(self.it)
            self.chunk = islice(chain([_next], self.it), self.chunksize)
            return self.chunk
        else:
            it = list(self.chunk)
            self.it = self.chunk.it
            self.chunk.it = iter(it)
            self.chunk.n = -1
            self.chunk = None
            return next(self)


def peek(it, default=None):
    try:
        _next = next(it)
        return (_next, chain([_next], it))
    except StopIteration:
        return (default, iter([]))


def _catch_wrapper_helper(it, ex_callback):
    try:
        while True:
            yield next(it)
    except StopIteration:
        raise IteratorExhausted()
    except Exception as err:
        ex_callback(err)
        return


def catch_wrapper(it, ex_callback=None):
    try:
        while True:
            yield from _catch_wrapper_helper(it, ex_callback)
    except IteratorExhausted:
        return


class starmap(Iterator):
    def __init__(self, func, it, dim=1):
        self.func = func
        self.it = it
        self.dim = dim

    def __iter__(self):
        return map(lambda arg: self.func(*flatten(arg, self.dim)), self.it)
