from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import random
import hashlib


class StatisticsFinderInput(BaseModel):
    """Input schema for StatisticsFinderTool."""
    topic: str = Field(..., description="The topic to generate cursed statistics about")


class StatisticsFinderTool(BaseTool):
    name: str = "Cursed Statistics Finder"
    description: str = (
        "Generates bizarre, oddly specific, and uncomfortable statistics related to any topic. "
        "Creates fake but believable correlations and cites questionable sources. "
        "Perfect for Fact-Checker's arsenal of cursed data."
    )
    args_schema: Type[BaseModel] = StatisticsFinderInput

    def _run(self, topic: str) -> str:
        """
        Generate cursed statistics based on topic
        """
        topic_lower = topic.lower()
        
        # Cursed statistic templates
        stat_templates = [
            "{percent}% of people who {action} also {correlation} at {time}",
            "Studies show that {percent}% of {group} experience {outcome} within {timeframe}",
            "According to {source}, {percent}% of people asking about {topic} have {trait}",
            "Research indicates {percent}% correlation between {thing1} and {thing2}",
            "{percent}% of people who ask '{question_type}' questions end up {outcome}",
            "Data suggests {percent}% of {group} secretly {behavior} when {condition}",
            "Surveys reveal {percent}% of people in this situation {action} within {timeframe}",
            "{source} reports that {percent}% of similar cases resulted in {outcome}"
        ]
        
        # Questionable sources
        sources = [
            "The Journal of Questionable Life Choices",
            "Institute of Uncomfortable Truths",
            "University of Regret Studies",
            "International Database of Bad Decisions",
            "The Archive of Cursed Correlations",
            "Center for Awkward Statistics",
            "Bureau of Unfortunate Data",
            "Academy of Regrettable Patterns"
        ]
        
        # Topic-specific correlations
        correlations = {
            'love': [
                "search for cat videos",
                "online shop at midnight",
                "check their ex's social media",
                "eat ice cream alone",
                "watch romantic comedies they claim to hate"
            ],
            'job': [
                "update their resume on company time",
                "browse job listings during meetings",
                "complain to their pets",
                "stress-eat at their desk",
                "fantasize about winning the lottery"
            ],
            'money': [
                "make impulsive purchases",
                "avoid checking their bank account",
                "watch financial advice videos without taking action",
                "calculate lottery odds",
                "compare themselves to billionaires"
            ],
            'future': [
                "doom-scroll at 3 AM",
                "make plans they never execute",
                "consult random internet sources",
                "overthink simple decisions",
                "seek validation from strangers"
            ]
        }
        
        # Detect topic category
        topic_category = 'future'  # default
        for category in correlations.keys():
            if category in topic_lower:
                topic_category = category
                break
        
        # Use topic hash for deterministic randomness
        topic_hash = int(hashlib.md5(topic.encode()).hexdigest(), 16)
        random.seed(topic_hash)
        
        # Generate statistics
        num_stats = random.randint(3, 5)
        statistics = []
        
        for i in range(num_stats):
            # Reseed for each stat to get variety
            random.seed(topic_hash + i)
            
            percent = random.randint(47, 94)  # Oddly specific percentages
            source = random.choice(sources)
            correlation = random.choice(correlations[topic_category])
            
            # Generate stat based on template
            if i == 0:
                stat = f"{percent}% of people asking about {topic} also {correlation}"
            elif i == 1:
                stat = f"According to {source}, {percent}% of similar situations end in regret"
            elif i == 2:
                stat = f"Studies show {percent}% correlation between asking this question and {correlation}"
            else:
                stat = f"{source} reports {percent}% of people in this scenario {correlation}"
            
            statistics.append(stat)
        
        # Additional cursed facts - use deterministic random based on topic_hash
        topic_rng = random.Random(topic_hash)
        cursed_facts = [
            f"🔍 People who ask about {topic} spend {topic_rng.randint(2, 8)} hours per week overthinking it",
            f"🔍 {topic_rng.randint(60, 85)}% of similar questions are asked between 11 PM and 3 AM",
            f"🔍 This type of question has been asked {topic_rng.randint(1000, 9999)} times this month alone",
            f"🔍 {topic_rng.randint(70, 90)}% of people asking this already know the answer but seek validation"
        ]

        selected_facts = topic_rng.sample(cursed_facts, 2)
        
        # Build the statistics report
        report = f"""
📊 CURSED STATISTICS REPORT 📊
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UNCOMFORTABLE CORRELATIONS:

{chr(10).join(f'• {stat}' for stat in statistics)}

ADDITIONAL CURSED FACTS:

{chr(10).join(selected_facts)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Sources: Questionable but cited
⚠️ Accuracy: Uncomfortably believable
⚠️ Usefulness: Debatable
"""
        
        return report.strip()
