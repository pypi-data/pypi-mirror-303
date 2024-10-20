from upycli.runner import reflect


def test_int():
    def __func(arg1: int, arg2: int = 4):
        ...
            
    args = reflect(__func).parse_args([ "--arg1", "5" ])
    assert all([
        args.arg1 == 5,
        args.arg2 == 4,
    ])

def test_float():
    def __func(arg1: float, arg2: float = 4.5):
        ...

    args = reflect(__func).parse_args([ "--arg1", "2.5" ])
    assert all([
        args.arg1 == 2.5,
        args.arg2 == 4.5,
    ])

def test_str():
    def __func(arg1: str, arg2: str = "Bye"):
        ...

    args = reflect(__func).parse_args([ "--arg1", "hello" ])
    assert all([
        args.arg1 == "hello",
        args.arg2 == "Bye",
    ])

def test_list():
    def __func(arg1: list, arg2: list = ["Bye"]):
        ...

    args = reflect(__func).parse_args([ "--arg1", "hello", "brother" ])
    assert all([
        args.arg1 == ["hello", "brother"],
        args.arg2 == ["Bye"],
    ])

def test_bool():
    def __func(arg1: bool, arg2: bool = False):
        ...

    args = reflect(__func).parse_args([ "--arg1" ])
    assert all([
        args.arg1 == True,
        args.arg2 == False,
    ])