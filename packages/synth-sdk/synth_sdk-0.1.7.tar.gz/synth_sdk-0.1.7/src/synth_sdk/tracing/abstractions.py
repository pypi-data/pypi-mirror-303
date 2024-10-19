from typing import Dict, List, Optional, Union
from pydantic import BaseModel

class TrajectoryTrace(BaseModel):
    agent_id: str
    spans: List[Dict] = []

    def add_span(self, span: Dict):
        assert isinstance(span, dict)
        self.spans.append(span)

    def to_dict(self) -> Dict:
        return {
            "agent_id": self.agent_id,
            "spans": self.spans
        }

    def to_json(self) -> str:
        import json
        return json.dumps(self.to_dict(), indent=2, default=str)

class TrainingQuestion(BaseModel):
    intent: str
    criteria: str
    question_id: Optional[str] = None

    def to_dict(self):
        return {
            "intent": self.intent,
            "criteria": self.criteria,
        }
    
class RewardSignal(BaseModel):
    question_id: Optional[str] = None
    agent_id: str
    reward: Union[float, int, bool]
    annotation: Optional[str] = None

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "agent_id": self.agent_id,
            "reward": self.reward,
            "annotation": self.annotation,
        }


class Dataset(BaseModel):
    questions: List[TrainingQuestion]
    reward_signals: List[RewardSignal]

    def to_dict(self):
        return {
            "questions": [question.to_dict() for question in self.questions],
            "reward_signals": [signal.to_dict() for signal in self.reward_signals],
        }