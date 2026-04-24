# Lab 16 Benchmark Report

## Metadata
- Dataset: hotpot_mini.json
- Mode: real
- Records: 200
- Agents: react, reflexion

## Summary
| Metric | ReAct | Reflexion | Delta |
|---|---:|---:|---:|
| EM | 0.94 | 0.99 | 0.05 |
| Avg attempts | 1 | 1.07 | 0.07 |
| Avg token estimate | 528.3 | 602.37 | 74.07 |
| Avg latency (ms) | 3361.3 | 13782.88 | 10421.58 |

## Failure modes
```json
{
  "react": {
    "none": 94,
    "wrong_final_answer": 6
  },
  "reflexion": {
    "none": 99,
    "reflection_overfit": 1
  }
}
```

## Extensions implemented
- structured_evaluator
- reflection_memory

## Discussion
Reflexion significantly improves performance on multi-hop questions by allowing the agent to correct its trajectory after a failed first attempt. The structured evaluator ensures reliable scoring, and reflection memory provides cumulative feedback across attempts. However, this comes at the cost of higher latency and token usage.
