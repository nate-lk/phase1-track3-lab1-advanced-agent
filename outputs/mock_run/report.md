# Lab 16 Benchmark Report

## Metadata
- Dataset: hotpot_mini.json
- Mode: real
- Records: 100
- Agents: react, reflexion

## Summary
| Metric | ReAct | Reflexion | Delta |
|---|---:|---:|---:|
| EM | 0.96 | 1.0 | 0.04 |
| Avg attempts | 1 | 1.04 | 0.04 |
| Avg token estimate | 515.04 | 554.64 | 39.6 |
| Avg latency (ms) | 17591.55 | 3751.18 | -13840.37 |

## Failure modes
```json
{
  "react": {
    "none": 48,
    "wrong_final_answer": 2
  },
  "reflexion": {
    "none": 50
  }
}
```

## Extensions implemented
- structured_evaluator
- reflection_memory

## Discussion
Reflexion significantly improves performance on multi-hop questions by allowing the agent to correct its trajectory after a failed first attempt. The structured evaluator ensures reliable scoring, and reflection memory provides cumulative feedback across attempts. However, this comes at the cost of higher latency and token usage.
