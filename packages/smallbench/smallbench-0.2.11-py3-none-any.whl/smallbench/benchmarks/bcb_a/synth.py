import asyncio
from zyk import LM
from typing import Any
from apropos.src.bench.bigcodebench.main import (
    BigCodeBenchComplete_Benchmark,
)
from smallbench.benchmarks.bcb_a.aci import BCBEngine, BCBAgentComputerInterface
from smallbench.benchmarks.bcb_a.aci import BCBAgentComputerInterface
from smallbench.baselines.agents.core import Agent
from smallbench.benchmarks.bcb_a.bench import BCB_AgentBenchmark
from smallbench.benchmarks.bcb_a.test import get_contexts_extremely_hacky_please_fix
from src.smallbench.baselines.agents.react import SimpleReActLanguageAgent
from synth_sdk.tracing.upload import upload

# Example get agent
def get_agent(model: str, temperature: float):
    contexts = get_contexts_extremely_hacky_please_fix()

    lm = LM(
        model,
        formatting_model_name=model,
        temperature=temperature,
        structured_output_mode="forced_json"
    )
    
    agent = SimpleReActLanguageAgent(lm=lm, contexts=contexts)
    return agent

async def run_agent_on_question(question: Any, agent: Agent):
    backend = "modal"
    agent_benchmark = BCB_AgentBenchmark(backend=backend)
    backend_instance = BCBEngine(question, backend)
    
    aci = BCBAgentComputerInterface(backend_instance)
    _, submission, _ = await agent_benchmark.evaluate_async(agent, aci, False)
    return submission

async def generate_trajectories_simple(multiplicity: int = 10, base_temperature: float = 0.0):
    for question in questions:
        tasks = []
        for i in range(multiplicity):
            agent = get_agent(model="gpt-4o-mini-2024-07-18", temperature=base_temperature + 0.01 * i)
            task = run_agent_on_question(question, agent)
            tasks.append(task)
        
        submissions = await asyncio.gather(*tasks)
    await upload(
        verbose=True,
    )
    pass



if __name__ == "__main__":
    bcb = BigCodeBenchComplete_Benchmark()
    questions = bcb.train[:1]
    
    asyncio.run(generate_trajectories_simple(
        multiplicity=3, base_temperature=0.0
    ))
    print("Done")