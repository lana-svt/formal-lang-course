from project.task3 import FiniteAutomaton, transitive_closure
from itertools import product
from pyformlang.finite_automaton import State
from scipy.sparse import kron


def reachability_with_constraints(fa: FiniteAutomaton, constraints_fa: FiniteAutomaton) -> dict[int, set[int]]:
    intersection_m = {
        label: kron(fa.m[label], constraints_fa.m[label], "csr")
        for label in fa.m.keys() & constraints_fa.m.keys()
    }

    closure_m = transitive_closure(FiniteAutomaton(intersection_m))

    intersection_start_indices = {
        len(constraints_fa.mapping) * fa.mapping[state] + constraints_fa.mapping[State(label)]
        for state, label in product(fa.start, constraints_fa.start)
    }
    intersection_final_indices = {
        len(constraints_fa.mapping) * fa.mapping[state] + constraints_fa.mapping[State(label)]
        for state, label in product(fa.final, constraints_fa.final)
    }

    state_mapping = {v: i for i, v in enumerate(fa.mapping)}
    result_dict = {state_mapping[index]: set() for index in fa.start}

    for source, target in zip(*closure_m.nonzero()):
        source_label = closure_m[source, target]
        if source in intersection_start_indices and target in intersection_final_indices and source_label in intersection_m:
            result_dict[state_mapping[source // len(constraints_fa.mapping)]].add(
                state_mapping[target // len(constraints_fa.mapping)])

    return result_dict
