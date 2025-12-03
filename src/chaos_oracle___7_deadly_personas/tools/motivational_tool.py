from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import random
import hashlib


class MotivationalQuoteInput(BaseModel):
    """Input schema for MotivationalQuoteTool."""
    context: str = Field(..., description="The context or topic to generate motivational content for")


class MotivationalQuoteTool(BaseTool):
    name: str = "Motivational Quote Generator"
    description: str = (
        "Generates high-energy motivational quotes, affirmations, and alpha mindset phrases. "
        "Returns CAPS LOCK energy, gym metaphors, and manifestation speak. "
        "Perfect for amplifying Hype Bro's motivational power."
    )
    args_schema: Type[BaseModel] = MotivationalQuoteInput

    def _run(self, context: str) -> str:
        """
        Generate motivational content based on context
        """
        # Alpha mindset quotes database
        alpha_quotes = [
            "LIONS DON'T LOSE SLEEP OVER THE OPINIONS OF SHEEP! 🦁",
            "YOUR ONLY LIMIT IS YOU, BRO! BREAK THROUGH! 💪",
            "WINNERS FOCUS ON WINNING, LOSERS FOCUS ON WINNERS! 🏆",
            "THE GRIND NEVER STOPS! EMBRACE THE PAIN! 🔥",
            "YOU'RE NOT STUCK IN TRAFFIC, YOU ARE THE TRAFFIC! MOVE! 🚀",
            "COMFORT ZONE IS WHERE DREAMS GO TO DIE! 💀",
            "BE SO GOOD THEY CAN'T IGNORE YOU! 👑",
            "PRESSURE MAKES DIAMONDS, BRO! SHINE! 💎",
            "DOUBT KILLS MORE DREAMS THAN FAILURE EVER WILL! ⚡",
            "THE UNIVERSE REWARDS ACTION, NOT INTENTION! 🌟"
        ]
        
        # Manifestation affirmations
        manifestations = [
            "I AM MANIFESTING SUCCESS RIGHT NOW! ✨",
            "THE UNIVERSE IS CONSPIRING IN MY FAVOR! 🌌",
            "I ATTRACT ABUNDANCE LIKE A MAGNET! 🧲",
            "MY ENERGY IS UNSTOPPABLE! 💥",
            "I AM THE ARCHITECT OF MY DESTINY! 🏗️",
            "GREATNESS IS MY BIRTHRIGHT! 👑",
            "I VIBRATE AT THE FREQUENCY OF SUCCESS! 📡",
            "MY POTENTIAL IS LIMITLESS! ∞",
            "I AM BECOMING MY BEST SELF! 🦅",
            "THE WORLD NEEDS WHAT I HAVE TO OFFER! 🌍"
        ]
        
        # Gym/fitness metaphors
        gym_metaphors = [
            "Life is like the gym - NO PAIN, NO GAIN! 💪",
            "You gotta lift heavy to grow, bro! Same with life! 🏋️",
            "Every rep counts! Every decision matters! 🔄",
            "Failure is just another set! Keep pushing! 📈",
            "Your mind is a muscle - TRAIN IT! 🧠",
            "Progressive overload in life = GROWTH! 📊",
            "Rest is for the weak! (Just kidding, recovery is key!) 😤",
            "Spot me, universe! I'm going for a PR! 🎯"
        ]
        
        # Energy boosters
        energy_phrases = [
            "LET'S GOOOOOO! 🚀",
            "UNLEASH THE BEAST WITHIN! 🦁",
            "TIME TO LEVEL UP! ⬆️",
            "ACTIVATE BEAST MODE! 😤",
            "CHANNEL THAT ALPHA ENERGY! ⚡",
            "RISE AND GRIND! ☀️",
            "DOMINATE THE DAY! 👊",
            "CONQUER YOUR FEARS! ⚔️"
        ]
        
        # Use context hash for deterministic randomness
        context_hash = int(hashlib.md5(context.encode()).hexdigest(), 16)

        # Create local Random instance to avoid race conditions in concurrent runs
        rng = random.Random(context_hash)

        # Select motivational elements using local RNG
        selected_quote = rng.choice(alpha_quotes)
        selected_manifestation = rng.choice(manifestations)
        selected_metaphor = rng.choice(gym_metaphors)
        selected_energy = rng.choice(energy_phrases)
        
        # Build motivational package
        motivation = f"""
💪 MOTIVATIONAL ENERGY BOOST 💪
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{selected_energy}

ALPHA WISDOM:
{selected_quote}

MANIFESTATION AFFIRMATION:
{selected_manifestation}

GYM WISDOM:
{selected_metaphor}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Remember: YOU GOT THIS, BRO! 🔥
The universe is YOUR gym! 💯
"""
        
        return motivation.strip()
