import importlib

LIB = 'renardo_lib'
FALLBACK = 'FoxDot.lib'
IMPORT_ERROR_MESSAGE = """
    The FoxDotChord package requires the renardo or FoxDot package to be installed.
    You can install this with:
    $ pip install renardo  # https://renardo.org
    OR
    $ pip install FoxDot   # https://foxdot.org
"""  # noqa: E501


def require(module):
    try:  # pragma: no cover
        return importlib.import_module(f'{LIB}.{module}')
    except ModuleNotFoundError as exc:  # pragma: no cover
        try:
            return importlib.import_module(f'{FALLBACK}.{module}')
        except ModuleNotFoundError:
            raise RuntimeError(IMPORT_ERROR_MESSAGE) from exc
