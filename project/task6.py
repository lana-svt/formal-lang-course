from pyformlang.cfg import CFG, Epsilon, Terminal, Variable


def cfg_to_whnf(cfg: CFG) -> CFG:
    """
    Returns CFG in Weak Normal Chomsky Form that is equivalent to the original
    :param cfg: CFG
    :return: CFG in Weak Normal Chomsky Form
    """

    cfg = cfg.eliminate_unit_productions().remove_useless_symbols()

    new_productions = cfg._get_productions_with_only_single_terminals()
    new_productions = cfg._decompose_productions(new_productions)

    return CFG(
        start_symbol=cfg.start_symbol,
        productions=set(new_productions),
    )


def cfg_from_file(path: str) -> CFG:
    """
    Returns CFG built from the text file
    :param path: path to the file with CFG description
    :return: CFG built by description in file
    """
    with open(path) as file:
        return CFG.from_text(file.read())


def whnf_from_file(path: str) -> CFG:
    return cfg_to_whnf(cfg_from_file(path))
