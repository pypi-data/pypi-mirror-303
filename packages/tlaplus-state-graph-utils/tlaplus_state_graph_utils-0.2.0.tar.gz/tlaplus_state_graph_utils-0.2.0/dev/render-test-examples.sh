#!/bin/bash
# Different D2 state rendering styles:
for x in tests/data/long-example/*.d2; do
  D2_LAYOUT=elk d2 \
    --elk-padding '[top=10,left=10,bottom=10,right=10]' \
    --elk-edgeNodeBetweenLayers 20 \
    --elk-nodeNodeBetweenLayers 20 \
    "$x"
done

# Conditional styling (cookbook):
tlaplus-state-graph-utils.py convert --reasonable-json-simple-structured-state \
tests/data/long-example/reasonable.json \
| jq '.states[] |= (.styleClass =
if
  .simpleStructuredState.fs.fileExists == "TRUE"
  and any(.simpleStructuredState.procs[]; .pc | contains("create"))
then
  "danger"
elif all(.simpleStructuredState.procs[]; .pc | contains("done")) then
  "done"
elif any(.simpleStructuredState.procs[]; .pc | contains("crashed")) then
  "crash"
else
  .styleClass
end
)' \
| (
  tlaplus-state-graph-utils.py convert -t d2 --d2-output-state-as latex
  echo
  echo '
    classes { danger: { style: { fill: lemonchiffon } }
    done: { style: { fill: palegreen } }
    crash: { style: { fill: lightsalmon } } }
  '
) \
| D2_LAYOUT=elk d2 --elk-padding "[top=10,left=10,bottom=10,right=10]" - \
> tests/data/long-example/conditional-styling-cookbook.svg
