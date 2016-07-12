# Django REST Framework Crash Course
This is a talk by Kyle Rich for OpenWest 2016.

## Images
To generate the dot file for the model graph representation, run this

`server/manage.py graph_models api > slides/graph.dot`

To convert that to a high-resolution PNG, run this

`dot slides/graph.dot -Tpng -Gdpi=300 -o slides/graph.png`
