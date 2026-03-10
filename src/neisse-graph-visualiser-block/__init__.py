from nessie_api.models import Plugin, Action, plugin , Graph
import json
import os



def visualise_graph_handler(action: Action):
    graph_data = action.payload
    if not isinstance(graph_data, Graph):
        print("Invalid graph data provided.")
        raise ValueError("Expected a Graph object as payload.")
    graph_dict = graph_data.to_dict()
    TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "blockVisualiser.html")
    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()
    graph_json = json.dumps(graph_dict)
    html_content = template.replace("__GRAPH_DATA__", graph_json)
    return html_content




    

@plugin(name="Neisse_graph_visualiser_block")
def neisse_graph_visualiser_block_plugin():
    handlers = {
        "visualise_graph": visualise_graph_handler,
    }
    requires = []
    return handlers, requires

if __name__ == "__main__": 
    plugin_instance = neisse_graph_visualiser_block_plugin()
    print(f"Plugin '{plugin_instance.name}' initialized with actions: {plugin_instance.provided_actions}")
    Graph = Graph(nodes=[{"id": "A", "attributes": {"color": "red"}}, {"id": "B", "attributes": {"color": "blue"}}], edges=[{"source": "A", "target": "B", "attributes": {"weight": 5}}])
    action = Action(name="visualise_graph", payload=Graph)
    result = plugin_instance.handle(action)
    #The result is svg context that is here going to be added to html block and saved as html file
    html_content =    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0
        <title>Graph Visualisation</title>
        <script src="https://d3js.org/d3.v7.min.js"></script
    </head>
    <body>
        <div id="graph-container">
        """ + result + """ 
        </div>
    """
    with open("graph_visualisation.html", "w") as f:
        f.write(html_content)
    