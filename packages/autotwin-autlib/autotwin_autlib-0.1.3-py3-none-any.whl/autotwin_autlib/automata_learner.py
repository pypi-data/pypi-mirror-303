import os
from dateutil.parser import parse

os.environ['NEO4J_SCHEMA'] = 'croma'

from semantic_main.autotwin_mapper import write_semantic_links
from sha_learning.autotwin_learn import learn_automaton
from skg_main.autotwin_connector import store_automaton, delete_automaton

SAVE_PATH = os.path.dirname(os.path.abspath(__file__)).split('autotwin_autlib')[0] + 'autotwin_autlib'
DATE_FORMAT = '{}-{}-{}-{}-{}-{}'

def start_automata_learning(pov, start, end):
    # 1: Automata Learning experiment.
    try:
        start = int(start)
        learned_sha = learn_automaton(pov, start_ts=int(start), end_ts=int(end), save_path=SAVE_PATH)
    except ValueError:
        parsed_start = parse(start, fuzzy=True)
        parsed_end = parse(end, fuzzy=True)

        start_dt = DATE_FORMAT.format(parsed_start.year, parsed_start.month, parsed_start.day,
                                      parsed_start.hour, parsed_start.minute, parsed_start.second)
        end_dt = DATE_FORMAT.format(parsed_end.year, parsed_end.month, parsed_end.day,
                                    parsed_end.hour, parsed_end.minute, parsed_end.second)

        learned_sha = learn_automaton(pov, start_dt=start_dt, end_dt=end_dt, save_path=SAVE_PATH)

    # 2: Delete learned automaton from the SKG, if there already exists one with the same name.
    delete_automaton(learned_sha, pov, start, end)

    # 3: Store the learned automaton into the SKG.
    automaton, new_automaton_id = store_automaton(learned_sha, pov, start, end, SAVE_PATH)

    # 4: Create semantic links between learned model and existing SKG nodes.
    write_semantic_links(learned_sha, pov, start, end, SAVE_PATH)

    return learned_sha, new_automaton_id
