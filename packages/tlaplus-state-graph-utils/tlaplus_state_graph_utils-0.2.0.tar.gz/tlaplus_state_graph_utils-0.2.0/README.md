# tlaplus-state-graph-utils.py

Python utilities for working with TLA+ state graphs

## Installation

```bash
pip install tlaplus-state-graph-utils
```

## Using the CLI

Installing the package puts a CLI program named `tlaplus-state-graph-utils.py` in your
`PATH`. Here is its `--help` text:

```
usage: tlaplus-state-graph-utils.py [-h] [--version] COMMAND ...

utilities for working with TLA+ state graphs

options:
  -h, --help  show this help message and exit
  --version   show program's version number and exit

subcommands:
  COMMAND     description
    convert   convert between state graph formats
```

It currently has only one subcommand called `convert` which can be used to
convert between different representations of TLA+ state graphs. Here is its
`--help` text:

```
usage: tlaplus-state-graph-utils.py convert [-h] [--output OUTPUT]
                                    [--from {reasonable-json,tlaplus-dot-json}]
                                    [--to {reasonable-json,d2}] [--pretty]
                                    [--reasonable-json-structured-state]
                                    [--reasonable-json-simple-structured-state]
                                    [--reasonable-json-itf-state]
                                    [--d2-output-state-as D2_OUTPUT_STATE_AS]
                                    [input]

convert between TLA+ state graph formats/representations

positional arguments:
  input                 input file path or '-' to use stdin (the default)

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        output file path or '-' to use stdout (the default)
  --from {reasonable-json,tlaplus-dot-json}, -f {reasonable-json,tlaplus-dot-json}
                        input format (guessed from extension & content if not
                        given)
  --to {reasonable-json,d2}, -t {reasonable-json,d2}
                        output format (if not given, defaults to reasonable-
                        json when outputting to stdout, otherwise guessed from
                        extension)
  --pretty              produce pretty-printed rather than compact output

reasonable-json options:
  options relevant when outputting in reasonable-json format

  --reasonable-json-structured-state
                        include state contents represented as structured JSON
  --reasonable-json-simple-structured-state
                        include state contents represented as simplified
                        structured JSON (lossy, i.e. doesn't encode all
                        details of TLA+, but easy to work with)
  --reasonable-json-itf-state
                        include state contents represented in ITF state format
                        (see: https://apalache-mc.org/docs/adr/015adr-
                        trace.html)

D2 options:
  options relevant when outputting in D2 format

  --d2-output-state-as D2_OUTPUT_STATE_AS
                        how to represent individual states in the D2 output:
                        label: without modification as a D2 node label; latex:
                        as a LaTeX equation which D2 will render; nested-
                        containers: as nested containers, one per variable,
                        record, etc.; nested-containers-simple-values-inline:
                        as above but with terminal/simple values not getting
                        their own container; nested-containers-simple-values-
                        inline-newline: as above but with keys and terminal
                        values separated by newlines
```

For instance, this converts a GraphViz dot file produced by TLA+'s state
diagram output into a "reasonable" JSON format that's easier to work with:

```bash
# In your TLA+ Model directory:
dot -Tjson Model_1.dot | tlaplus-state-graph-utils.py convert -t reasonable-json
```

The following sections go into more details about the supported input and
output formats.

### Input formats

#### dot JSON

TLA+ does not currently have a "canonical" format for state graphs (see
[TLA+ GitHub issue #639](https://github.com/tlaplus/tlaplus/issues/639)) and
so the only halfway convenient way to get this information out of TLA+ is to
process the GraphViz `dot` files it produces.

In particular, as suggested in
[a comment](https://github.com/tlaplus/tlaplus/issues/639#issuecomment-1003163720)
on the aforementioned issue, `dot` itself can convert these into a JSON
representation (`dot -Tjson`), which can then by read in by this utility (it
automatically considers filenames ending in `.dot.json` to be such files).

#### Reasonable JSON

Another possible input format is the "reasonable JSON" format produced by this
tool itself - it is explained in more detail in the *Output formats* section
below.

### Output formats

#### "Reasonable JSON"

The aforementioned "reasonable JSON" format is meant to make it easier for
other tools to work with TLA+ state graphs. It looks like this:

```json5
{
  "metadata": {
    "format": {
      "name": "reasonable-tlaplus-state-graph-json",
      "version": "0.1.1"
    }
  },
  "states": [
    {
      "id": 1,
      "labelTlaPlus": "/\\ a = 1 /\\ b = 2 \n ...",
      // optional, if requested:
      "structuredState": ...,
      "simpleStructuredState": ...,
      "itfState": ...
      // optional, if added by user:
      "styleClass": "someclass"
    },
    ...
  ],
  "steps": [
    {
      "id": 0,
      "actionName": "CheckFileExists",
      "fromStateId": 1,
      "toStateId": 2,
      "colorId": "1"
    },
    ...
  ]
}
```

##### Structured state

If present, the optional fields `structuredState`, `simpleStructuredState` and
`itfState` contain different JSON representations of each state's
"content" (i.e. the set of variables and their values for that state).
They can be switched on independently of one another via the
`--reasonable-json-structured-state`,
`--reasonable-json-simple-structured-state`, and
`--reasonable-json-simple-structured-state` CLI flags.

The "structured" and "simple-structured" formats are ad-hoc formats defined by
this tool (if you need docs for this please open an issue).

The ITF state format is the same as that used in traces output by the
[Apalache model checker](https://apalache-mc.org/) and described in the "State
object" section of its
[ADR-015](https://apalache-mc.org/docs/adr/015adr-trace.html).

##### Style class

The optional field `styleClass` represents a "class" of styling options to
apply to the state in question and will be included in output formats that
support such a "class" concept (e.g. D2 - see below).

#### D2

Another supported output format is [D2](https://d2lang.com/), but to use it,
the package's `d2` extra needs to be installed:

```bash
pip install tlaplus-state-graph-utils[d2]'
```

Here is an example showing how to go from a `dot` file produced by TLA+ to
a graph rendered using D2 in one shell command:

```bash
# In your TLA+ Model directory:
dot -Tjson Model_1.dot \
| tlaplus-state-graph-utils.py convert -t d2 \
| D2_LAYOUT=elk d2 - > Model_1.svg
```

There are many different ways to represent the *contents* of each state (i.e.
the set of variables and their values) in D2, which can be configured via
the `--d2-output-state-as` option:

##### `label`

<img src="./tests/data/long-example/non-latex.svg" width="400px">

##### `latex`

<img src="./tests/data/long-example/latex.svg" width="400px">

##### `nested-containers`

<img src="./tests/data/long-example/containers-simple-values-not-inline.svg" width="400px">

##### `nested-containers-simple-values-inline`

<img src="./tests/data/long-example/containers-simple-values-inline.svg" width="400px">

##### `nested-containers-simple-values-inline-newline`

<img src="./tests/data/long-example/containers-simple-values-inline-newline.svg" width="400px">


### Cookbook / advanced techniques

#### Conditional styling

While there is no built-in support for making `styleClass` dependent on the
TLA+ state contents (yet?), it's possible to hack something together using
structured/JSON state output and the [`jq`](https://jqlang.github.io/jq/) JSON
processing tool, e.g.:

```bash
tlaplus-state-graph-utils.py convert --reasonable-json-simple-structured-state \
| jq '.states[] |= (.styleClass =
if .someKey == "some-value" then
  "class1"
elif .someKey == "some-other-value" then
  "class2"
else
  .styleClass
end
)'
```

This overwrites the `styleClass` attribute of each state (adding it if it
doesn't exist) depending on the value of the `someKey` variable in it.

It is recommended to use the `simple-structured-state` format for such kinds of
processing because it's designed to be easy to work with in `jq`.

`styleClass` is included in e.g. the D2 output, making it possible to create
graphs like this with this technique (see `dev/render-test-examples.sh` for the
full script to generate this one):

<img src="./tests/data/long-example/conditional-styling-cookbook.svg" width="400px">


## Use as a library

I'm too lazy to write this or set up automated API docs, especially considering
nobody is going to use it.
If you want to use this as a library, please just open an issue saying so and
I'll get started (and maybe clean things up a little).
