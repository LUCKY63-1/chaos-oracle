from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import re


class SentimentAnalysisInput(BaseModel):
    """Input schema for SentimentAnalysisTool."""
    text: str = Field(..., description="The text to analyze for sentiment and emotional tone")


class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analyzer"
    description: str = (
        "Analyzes the emotional tone and sentiment of text. "
        "Returns sentiment polarity (positive/negative/neutral), emotional intensity, "
        "and key emotional keywords. Useful for understanding the user's emotional state."
    )
    args_schema: Type[BaseModel] = SentimentAnalysisInput

    def _run(self, text: str) -> str:
        """
        Analyze sentiment using keyword-based approach
        Returns a formatted sentiment analysis
        """
        text_lower = text.lower()
        
        # Emotional keyword dictionaries
        positive_words = {
            'happy', 'joy', 'excited', 'love', 'great', 'amazing', 'wonderful',
            'fantastic', 'excellent', 'good', 'hope', 'optimistic', 'confident',
            'blessed', 'grateful', 'success', 'win', 'achieve', 'dream'
        }
        
        negative_words = {
            'sad', 'angry', 'hate', 'terrible', 'awful', 'bad', 'worried',
            'anxious', 'fear', 'scared', 'depressed', 'hopeless', 'fail',
            'failure', 'lose', 'lost', 'stuck'
        }

        uncertainty_words = {
            'should', 'could', 'would', 'maybe', 'perhaps', 'unsure',
            'confused', 'doubt', 'uncertain', 'wondering', 'thinking'
        }
        
        # Compile regex patterns for word-boundary matching to avoid false positives
        positive_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, positive_words)) + r')\b')
        negative_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, negative_words)) + r')\b')
        uncertainty_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, uncertainty_words)) + r')\b')

        # Count emotional indicators using word-boundary matching
        positive_count = len(positive_pattern.findall(text_lower))
        negative_count = len(negative_pattern.findall(text_lower))
        uncertainty_count = len(uncertainty_pattern.findall(text_lower))
        
        # Check for question marks (indicates uncertainty)
        question_marks = text.count('?')
        
        # Calculate sentiment score (-1.0 to 1.0)
        total_emotional_words = positive_count + negative_count + 1  # Avoid division by zero
        sentiment_score = (positive_count - negative_count) / total_emotional_words
        
        # Determine overall sentiment
        if sentiment_score > 0.2:
            sentiment = "Positive"
            emoji = "😊"
        elif sentiment_score < -0.2:
            sentiment = "Negative"
            emoji = "😟"
        else:
            sentiment = "Neutral/Mixed"
            emoji = "😐"
        
        # Determine emotional intensity
        total_intensity = positive_count + negative_count + uncertainty_count
        if total_intensity > 5:
            intensity = "High"
        elif total_intensity > 2:
            intensity = "Moderate"
        else:
            intensity = "Low"
        
        # Detect key emotional themes
        themes = []
        if uncertainty_count > 0 or question_marks > 0:
            themes.append("Uncertainty/Seeking Guidance")
        if negative_count > positive_count:
            themes.append("Concern/Anxiety")
        if positive_count > negative_count:
            themes.append("Hope/Optimism")
        if not themes:
            themes.append("Neutral Inquiry")
        
        # Format the analysis
        analysis = f"""
{emoji} SENTIMENT ANALYSIS {emoji}
━━━━━━━━━━━━━━━━━━━━━━
Overall Sentiment: {sentiment}
Sentiment Score: {sentiment_score:.2f} (-1.0 to 1.0)
Emotional Intensity: {intensity}
Key Themes: {', '.join(themes)}
━━━━━━━━━━━━━━━━━━━━━━
Positive Indicators: {positive_count}
Negative Indicators: {negative_count}
Uncertainty Markers: {uncertainty_count}
Question Marks: {question_marks}
"""
        
        return analysis.strip()
