# Automata Learning Routine for Auto-Twin

## Description

Module developed within the [Auto-Twin][autotwin] Horizon EU project perform an automata
learning experiment with data
extracted from a System Knowledge Graph (SKG), store the resulting model in the SKG, and create semantic links between
the learned features and the existing nodes representing the system.

Authors:

| Name           | E-mail address           |
|:---------------|:-------------------------|
| Lestingi Livia | livia.lestingi@polimi.it |

## Requirements

Dependencies are listed in the [`environment.yml`](environment.yml) file.

## Module Structure

This module acts as an orchestrator of the following submodules:

- [`lsha`][lsha]: Automata learning component, specifically implementing algorithm L*_SHA for Stochastic
  Hybrid Automata (SHA) learning;
- [`skg_connector`][connector]: Component performing queries on the SKG to extract data and store the
  newly created model;
- [`sha2dt_semantic_mapper`][mapper]: Component identifying the semantic links between learned features and the existing
  representation of the System Under Learning (e.g., between an edge of the learned automaton and the sensor that
  triggers it).

Upon cloning the repository, run the following commands to initialize the submodules:

	git submodule init	
    git submodule update

Note that it is necessary to run `git submodule update` everytime submodules must synchronize with the corresponding
repositories.

## Configuration

The configuration file for the `skg_connector`
module ([`config.ini`][connector_config]), by default, is set up as follows:

- **instance**: name of the .ini file containing the information necessary to connect to the SKG (mainly URI, user, and
  password). By default, this points to the [`local.ini`][connector_config] file
  pointing to a local Neo4j instance with password `12345678`. Should a connection to a connection to a differently
  parameterized instance be needed, a new file with the same structure as [`local.ini`][connector_config] must be added
  to the same folder, and parameter **instance** accordingly.
- **schema.name**: identifier of the use case targeted by the automata learning experiment. By default, this is set
  to [`legoFactory`][connector_schemas], but it can be changed to any value
  from the [`schema`][connector_schemas] folder.

Note that the following must be added to your local `PYTHONPATH` environment variable:

- path to `autotwin_automata_learning`;
- path to [submodules/lsha](submodules/lsha);
- path to [submodules/sha2dt_semantic_mapper](submodules/sha2dt_semantic_mapper);
- path to [submodules/skg_connector](submodules/skg_connector).

## How to use

The [automata_learner](autotwin_automata_learning.py) script contains an example of a learning procedure for testing purposes:

- function [learn_automaton][lsha_endpoint] takes as input:
    - the **pov**, i.e., a string out of 'item', 'resource', 'plant';
    - the **start** date of the time window for events, e.g., '2023-11-04-13-0-0';
    - the **end** date of the time window for events, e.g., '2023-11-04-14-2-0';
    - The learned automaton will be saved in `resources/learned_sha`.
- function [delete_automaton][connector_endpoint] deletes nodes representing the learned automaton from the SKG, if
  there already exists one with the same name;
- function [store_automaton][connector_endpoint] stores the learned automaton into the SKG;
- function [write_semantic_links][mapper_endpoint] identifies and stores the semantic links between the learned
  automaton and existing SKG nodes.

---

*Copyright &copy; 2024 Livia Lestingi*

[autotwin]: https://www.auto-twin-project.eu/

[lsha]: https://github.com/LesLivia/lsha/tree/master

[lsha_endpoint]: https://github.com/LesLivia/lsha/blob/master/it/polimi/sha_learning/autotwin_learn.py

[connector]: https://github.com/LesLivia/skg_connector

[connector_endpoint]: https://github.com/LesLivia/skg_connector/blob/master/autotwin_connector.py

[mapper]: https://github.com/LesLivia/sha2dt_semantic_mapper

[mapper_endpoint]: https://github.com/LesLivia/sha2dt_semantic_mapper/blob/master/autotwin_mapper.py

[connector_config]: https://github.com/LesLivia/skg_connector/tree/dcf97cff64ae606ab99df94b3446354d4b22045e/resources/config

[connector_schemas]: https://github.com/LesLivia/skg_connector/tree/dcf97cff64ae606ab99df94b3446354d4b22045e/resources/schemas
