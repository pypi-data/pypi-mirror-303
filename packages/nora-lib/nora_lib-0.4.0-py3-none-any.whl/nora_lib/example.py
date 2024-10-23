from nora_lib.interactions.interactions_service import InteractionsService
from nora_lib.interactions.models import *
import uuid

iservice = InteractionsService("http://localhost:9080")
service_cost = ServiceCost(
    dollar_cost=1,
    service_provider="openai",
    description="Step 1 of PaperQA pipeline",
    tool_name="PaperQA",
    details=[
        LLMCost(token_count=1000, model_name="gpt-turbo"),
        LLMTokenBreakdown(prompt_tokens=100, completion_tokens=100),
    ],
)
step_cost = StepCost(
    actor_id=uuid.uuid4(), message_id="string", service_cost=service_cost
)
iservice.report_cost(step_cost)


class OtherLLMCostDetail(CostDetail):
    coolness_factor: float


service_cost2 = ServiceCost(
    dollar_cost=2,
    service_provider="anthropic",
    description="Step 2 of PaperQA pipeline",
    tool_name="PaperQA",
    details=[OtherLLMCostDetail(coolness_factor=0.5)],
)
step_cost2 = StepCost(
    actor_id=uuid.uuid4(), message_id="string", service_cost=service_cost2
)
iservice.report_cost(step_cost2)
