from typing import List, Optional, Union, get_type_hints, get_args, get_origin

from argparse import ArgumentParser


class BaseParser:

    _help = {}

    _abbrev = {}

    def __init__(self):
        args_types = get_type_hints(self)
        parser = ArgumentParser()

        required = {}

        for name, type_ in args_types.items():
            # Handle optional arguments
            if get_origin(type_) == Union:
                assert type(None) in get_args(
                    type_
                ), "Generic Unions not supported - only Optionals"
                required[name] = False
                type_ = get_args(type_)[0]
            else:
                required[name] = not hasattr(self, name)

            flags = [f"--{name}"]
            if abbrev := self._abbrev.get(name, None):
                flags.append(f"-{abbrev}")
            help_ = self._help.get(name, None)

            if get_origin(type_) == list:
                type_ = get_args(type_)[0]

                parser.add_argument(
                    *flags, nargs="+", help=help_, required=required[name], type=type_
                )
            elif type_ == bool:
                parser.add_argument(*flags, action="store_true", help=help_)
            else:
                parser.add_argument(
                    *flags,
                    action="store",
                    type=type_,
                    default=getattr(self, name, None),
                    help=help_,
                    required=required[name],
                )

        args = parser.parse_args()

        for name in args_types:
            try:
                value = getattr(args, name)
                if value is not None:
                    setattr(self, name, value)

            except AttributeError:
                # value = self._default.get(name, None)
                has_value = hasattr(self, name)
                if not has_value and required[name]:
                    raise AttributeError(
                        f"Required argument {name} not entered and not given a default value."
                    )
                else:
                    continue
                    # setattr(self, name, value)

    def to_dict(self):
        return vars(self)