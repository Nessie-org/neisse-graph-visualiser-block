# neisse-graph-visualiser-block

A [Nessie](https://github.com/Nessie-org) block that takes a graph data structure and returns an interactive HTML visualisation.

---

## Overview

`neisse-graph-visualiser-block` exposes a single action — `visualise_graph` — which accepts a graph object and returns a self-contained HTML string that renders the graph visually in any browser or webview.

---

## Action

### `visualise_graph`

Renders a graph data structure as an HTML visualisation.

| Field         | Details                          |
|---------------|----------------------------------|
| **Action**    | `visualise_graph`                |
| **Payload**   | `Graph`                      |
| **Returns**   | `String` — HTML content          |
| **Side effects** | None                          |
| **Setup required** | None                       |

#### Payload

```json
{
  <Graph>
}
```

The `Graph` object is an object described in nessie-api
#### Return value

A `String` containing a complete, self-contained HTML document (or embeddable HTML fragment) that renders the supplied graph. This can be written to a file, injected into a `<div>`, or loaded inside an `<iframe>`.

---

## Usage

```js
const result = await block.run("visualise_graph", 
Graph(name));

// result is an HTML string — render it however you like
document.getElementById("graph-container").innerHTML = result;
```

---

## Installation

Install directly from the GitHub repository using pip:

```bash
pip install git+https://github.com/Nessie-org/neisse-graph-visualiser-block.git
```

To pin to a specific branch:

```bash
# Latest from main
pip install git+https://github.com/Nessie-org/neisse-graph-visualiser-block.git@main
```

Or add it to your `requirements.txt`:

```
git+https://github.com/Nessie-org/neisse-graph-visualiser-block.git
```

---

## Setup

No setup or configuration is required after installation. The block has no external dependencies that need to be authenticated before use.

---

## Repository

[https://github.com/Nessie-org/neisse-graph-visualiser-block](https://github.com/Nessie-org/neisse-graph-visualiser-block)

---

## License

See [LICENSE](./LICENSE) for details.
