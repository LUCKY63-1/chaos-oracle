from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import random
import hashlib


class ChaosMeterInput(BaseModel):
    """Input schema for ChaosMeterTool."""
    question: str = Field(..., description="The question to measure chaos potential")


class ChaosMeterTool(BaseTool):
    name: str = "Chaos Meter"
    description: str = (
        "Measures the chaos potential of a question and determines if chaotic intervention is needed. "
        "Returns chaos score, intervention probability, and appropriate cursed emojis. "
        "Used by The Gremlin to decide when to cause disruption."
    )
    args_schema: Type[BaseModel] = ChaosMeterInput

    def _run(self, question: str) -> str:
        """
        Calculate chaos score and determine intervention strategy
        """
        # Chaos-inducing keywords
        chaos_keywords = {
            'love': 3, 'relationship': 3, 'marriage': 4, 'dating': 3,
            'job': 2, 'quit': 4, 'career': 2, 'money': 3, 'invest': 4,
            'crypto': 5, 'bitcoin': 5, 'stock': 3, 'gamble': 5,
            'move': 3, 'travel': 2, 'buy': 3, 'sell': 3,
            'start': 3, 'business': 3, 'venture': 4, 'risk': 4,
            'future': 2, 'life': 2, 'change': 3, 'decision': 3
        }
        
        # Calculate base chaos score
        question_lower = question.lower()
        chaos_score = 0
        
        for keyword, weight in chaos_keywords.items():
            if keyword in question_lower:
                chaos_score += weight
        
        # Add randomness based on question hash (deterministic but appears random)
        question_hash = int(hashlib.md5(question.encode()).hexdigest(), 16)
        rng = random.Random(question_hash)
        chaos_modifier = rng.uniform(0.5, 1.5)
        chaos_score = int(chaos_score * chaos_modifier)
        
        # Cap chaos score at 100
        chaos_score = min(chaos_score, 100)
        
        # Determine chaos level
        if chaos_score >= 15:
            chaos_level = "CRITICAL"
            emoji = "🦎💀🗑️"
            intervention = "MANDATORY"
            probability = 100
        elif chaos_score >= 10:
            chaos_level = "HIGH"
            emoji = "🦎🔥"
            intervention = "HIGHLY RECOMMENDED"
            probability = 85
        elif chaos_score >= 6:
            chaos_level = "MODERATE"
            emoji = "🦎"
            intervention = "OPTIONAL"
            probability = 50
        else:
            chaos_level = "LOW"
            emoji = "😴"
            intervention = "NOT NEEDED"
            probability = 15
        
        # Generate chaos event suggestions
        chaos_events = [
            "Flip the outcome prediction",
            "Add cursed emoji intervention",
            "Introduce random variable",
            "Question the question itself",
            "Suggest the opposite of consensus",
            "Invoke Murphy's Law",
            "Remind them of cosmic uncertainty",
            "Single emoji response only"
        ]
        
        # Select events based on chaos level
        num_events = min(chaos_score // 5, len(chaos_events))
        selected_events = rng.sample(chaos_events, max(1, num_events))
        
        # Format the chaos report
        report = f"""
{emoji} CHAOS METER READING {emoji}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Chaos Score: {chaos_score}/100
Chaos Level: {chaos_level}
Intervention Status: {intervention}
Probability: {probability}%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recommended Chaos Events:
{chr(10).join(f'• {event}' for event in selected_events)}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cursed Emoji Arsenal: 🦎 🗑️ 💀 💊 🔥 ⚡
"""
        
        return report.strip()
