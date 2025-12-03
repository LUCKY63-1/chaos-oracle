from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import random
import hashlib


class RoastGeneratorInput(BaseModel):
    """Input schema for RoastGeneratorTool."""
    question: str = Field(..., description="The question to analyze and generate roasts for")


class RoastGeneratorTool(BaseTool):
    name: str = "Roast Generator"
    description: str = (
        "Analyzes questions to identify insecurity patterns and generates contextual roasts. "
        "Returns brutal but constructive observations about life choices and decision-making patterns. "
        "Perfect for Roast Master's psychological warfare."
    )
    args_schema: Type[BaseModel] = RoastGeneratorInput

    def _run(self, question: str) -> str:
        """
        Generate contextual roasts based on question analysis
        """
        question_lower = question.lower()
        
        # Insecurity pattern detection
        patterns = {
            'relationship': {
                'keywords': ['love', 'relationship', 'dating', 'marriage', 'crush', 'partner'],
                'roasts': [
                    "Asking the Oracle about love? That's like asking a fish about flying.",
                    "The fact you're asking AI about relationships tells me everything I need to know.",
                    "Your love life is so complicated you need mystical intervention? Yikes.",
                    "Imagine needing 6 AI agents to validate your romantic decisions."
                ]
            },
            'career': {
                'keywords': ['job', 'quit', 'career', 'work', 'boss', 'promotion'],
                'roasts': [
                    "Asking if you should quit? You already know the answer, you just lack courage.",
                    "Your career confusion is showing. It's not a good look.",
                    "The fact you're here instead of LinkedIn says volumes about your priorities.",
                    "Let me guess - you've been 'thinking about it' for months?"
                ]
            },
            'money': {
                'keywords': ['money', 'invest', 'crypto', 'bitcoin', 'stock', 'rich', 'wealth'],
                'roasts': [
                    "Asking AI about money? That's exactly why you don't have any.",
                    "If you need mystical guidance for investing, you shouldn't be investing.",
                    "Your financial literacy is so low you're consulting a chaos oracle.",
                    "The Oracle sees your bank account. It's not impressed."
                ]
            },
            'life_decisions': {
                'keywords': ['should i', 'move', 'change', 'decision', 'future', 'life'],
                'roasts': [
                    "The indecision is strong with this one. Painfully strong.",
                    "You're asking strangers (AI strangers!) to make life decisions for you?",
                    "This level of uncertainty should come with a warning label.",
                    "Your decision-making skills are so weak you need 6 AI personalities to help."
                ]
            },
            'general': {
                'keywords': [],
                'roasts': [
                    "The fact you're here asking this question is already concerning.",
                    "This question radiates 'I make poor choices' energy.",
                    "Your life choices led you here. Think about that.",
                    "Asking a Chaos Oracle for guidance? Bold strategy, Cotton."
                ]
            }
        }
        
        # Detect pattern using scoring approach to handle multiple matches
        pattern_scores = {}
        for pattern_name, pattern_data in patterns.items():
            # Count keyword matches for this pattern
            keyword_matches = sum(1 for keyword in pattern_data['keywords'] if keyword in question_lower)
            pattern_scores[pattern_name] = keyword_matches

        # Select pattern with highest score, using tie-breaker logic
        detected_pattern = 'general'
        max_score = -1

        for pattern_name, score in pattern_scores.items():
            if score > max_score:
                detected_pattern = pattern_name
                max_score = score
            elif score == max_score and score > 0:
                # Tie-breaker: choose pattern with larger keyword set or keep current
                if len(patterns[pattern_name]['keywords']) > len(patterns[detected_pattern]['keywords']):
                    detected_pattern = pattern_name
                # If same size, keep the first one found (current detected_pattern)
        
        # Psychological observations
        observations = [
            "🔍 PSYCHOLOGICAL OBSERVATION: Seeks external validation for internal decisions",
            "🔍 PATTERN DETECTED: Analysis paralysis with a side of self-doubt",
            "🔍 BEHAVIORAL NOTE: Avoidance behavior masked as 'seeking guidance'",
            "🔍 DIAGNOSIS: Chronic overthinking with acute decision anxiety",
            "🔍 ASSESSMENT: Outsourcing personal responsibility to AI entities"
        ]
        
        # Life choice commentary
        life_choices = [
            "Your life choices are like a Netflix series - confusing and probably getting cancelled.",
            "The decision tree of your life looks like a tangled mess of Christmas lights.",
            "You've made questionable choices to end up consulting a Chaos Oracle.",
            "Your decision-making process needs its own support group."
        ]
        
        # Use question hash for deterministic randomness
        question_hash = int(hashlib.md5(question.encode()).hexdigest(), 16)

        # Create local Random instance to avoid race conditions in concurrent runs
        rng = random.Random(question_hash)

        # Select roast elements using local RNG
        main_roast = rng.choice(patterns[detected_pattern]['roasts'])
        observation = rng.choice(observations)
        life_choice = rng.choice(life_choices)
        
        # Build the roast
        roast = f"""
🔥 ROAST ANALYSIS 🔥
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{observation}

MAIN ROAST:
{main_roast}

LIFE CHOICE COMMENTARY:
{life_choice}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Category: {detected_pattern.replace('_', ' ').title()}
Roast Severity: Medium-High 🌶️🌶️🌶️
Uncomfortable Truth Level: 94%
"""
        
        return roast.strip()
