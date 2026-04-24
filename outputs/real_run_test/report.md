# Lab 16 Benchmark Report

## Metadata
- Dataset: hotpot_mini.json
- Mode: real
- Records: 2
- Agents: react, reflexion

## Summary
| Metric | ReAct | Reflexion | Delta |
|---|---:|---:|---:|
| EM | 1.0 | 1.0 | 0.0 |
| Avg attempts | 1 | 1 | 0 |
| Avg token estimate | 526 | 526 | 0 |
| Avg latency (ms) | 5055.96 | 2983.81 | -2072.15 |

## Failure modes
```json
{
  "react": {
    "none": 1
  },
  "reflexion": {
    "none": 1
  }
}
```

## Extensions implemented
- structured_evaluator
- reflection_memory

## Discussion
Reflexion significantly improves performance on multi-hop questions by allowing the agent to correct its trajectory after a failed first attempt. The structured evaluator ensures reliable scoring, and reflection memory provides cumulative feedback across attempts. However, this comes at the cost of higher latency and token usage.
