# TODO

## Next

## Soon

[ ] Publish on PyPI

## Later

[ ] At least try to output line numbers etc. in exceptions raised from TLA+
    state parsing
[ ] Allow parsing of various structured state formats in reasonable-json
[ ] ^ Use some kind of library, Pydantic or Marshmallow or whatever...
[ ] ^ Error if mismatch between different reprs (TLA+, own structured, ITF)
[ ] Make tests cover 100% of CLI, but with everything behind the CLI mocked
[ ] ... and/or just move more stuff out of CLI into core and add tests for that
[ ] Clean up container rendering stuff (separate modules, refactor more)
[ ] 'rg TODO' and resolve remaining issues
[ ] Option to include D2 preamable? Not really needed b/c
    `(cat preamble.d2 && ...)` does the trick just fine, but might be
    convenient

## Much later

[ ] Switch to a reasonable CLI library once one exists. argparse pain points:
    - No way for `choices` to be an enum
    - No way for `choices` to be reasonably formatted in help, or more
      generally to have exceptions from auto-formatting/wrapping
    - No way to specify default subcommand
[ ] Add built-in support for styleClass conditional on predicates on the states
    (easier-to-use alternative to cookbook approach via `jq`)
    [ ] Alternative: Write completely separate tool reminiscient of `jq` but
        for TLA+ states; but how to add `styleClass` specifically with that?

## Conditional on other developments

After https://github.com/pypa/packaging.python.org/issues/1605 PR is done
(either in the Packaging Guide or elsewhere) and I know what the actual best
solution for handling missing extras is:

[ ] Replace current "missing extra" handling (for both D2 output & state
    parsing extras) by this

After d2 fmt bug is fixed https://github.com/terrastruct/d2/issues/1577

[ ] use that to simplify D2 styleClass output test (cf. TODOs there)

As soon as py-tree-sitter-type-provider allows outputting .py sources somehow
(directly or via stubgen)
https://github.com/wenkokke/py-tree-sitter-type-provider/issues/93

[ ] Use py-tree-sitter-type-provider to simplify TLA+ state parsing
