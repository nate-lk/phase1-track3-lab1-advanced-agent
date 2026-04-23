import json
from .llm import call_llm
from .prompts import ACTOR_SYSTEM, EVALUATOR_SYSTEM, REFLECTOR_SYSTEM
from .schemas import QAExample, JudgeResult, ReflectionEntry

def actor_answer(example: QAExample, attempt_id: int, agent_type: str, reflection_memory: list[str]) -> tuple[str, int, float]:
    context_str = "\n".join([f"Title: {c.title}\nText: {c.text}" for c in example.context])
    
    reflection_str = ""
    if reflection_memory:
        reflection_str = "\nPrevious Reflections:\n" + "\n".join([f"- {r}" for r in reflection_memory])
    
    user_prompt = f"""Context:\n{context_str}\n{reflection_str}\nQuestion: {example.question}"""
    
    content, tokens, latency = call_llm(ACTOR_SYSTEM, user_prompt)
    return content, tokens, latency

def evaluator(example: QAExample, answer: str) -> tuple[JudgeResult, int, float]:
    user_prompt = f"""Gold Answer: {example.gold_answer}\nPredicted Answer: {answer}"""
    
    content, tokens, latency = call_llm(
        EVALUATOR_SYSTEM, 
        user_prompt, 
        response_format={"type": "json_object"}
    )
    
    data = json.loads(content)
    return JudgeResult(**data), tokens, latency

def reflector(example: QAExample, attempt_id: int, answer: str, judge: JudgeResult) -> tuple[ReflectionEntry, int, float]:
    user_prompt = f"""Question: {example.question}
Failed Answer: {answer}
Feedback: {judge.reason}
Missing: {judge.missing_evidence}
Spurious: {judge.spurious_claims}"""
    
    content, tokens, latency = call_llm(
        REFLECTOR_SYSTEM, 
        user_prompt, 
        response_format={"type": "json_object"}
    )
    
    data = json.loads(content)
    # Ensure attempt_id is included as per schema
    data["attempt_id"] = attempt_id
    return ReflectionEntry(**data), tokens, latency
