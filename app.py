#!/usr/bin/env python3
"""Pocket Universe Generator - a playful tiny CLI app."""

from __future__ import annotations

import random
import textwrap

ADJECTIVES = [
    "whispering",
    "clockwork",
    "luminous",
    "velvet",
    "restless",
    "ancient",
    "electric",
    "floating",
]

PLACES = [
    "library in the clouds",
    "desert of mirrors",
    "subway station between dimensions",
    "forest where compasses spin",
    "market under the moon",
    "city built on sleeping giants",
]

TWISTS = [
    "Time runs backward every Tuesday.",
    "Everyone communicates through songs.",
    "Gravity only works when nobody is watching.",
    "Shadows reveal your future, not your shape.",
    "Dreams are taxed by the local government.",
]

QUESTS = [
    "Find the key made of thunder.",
    "Convince a storm to change direction.",
    "Steal a recipe from the royal dragon chef.",
    "Deliver a letter to your past self.",
    "Win a chess match against a mountain.",
]


def generate_world(seed: int | None = None) -> str:
    rng = random.Random(seed)
    title = f"The {rng.choice(ADJECTIVES).title()} {rng.choice(['Realm', 'Orbit', 'Kingdom', 'Archive'])}"
    place = rng.choice(PLACES)
    twist = rng.choice(TWISTS)
    quest = rng.choice(QUESTS)

    return textwrap.dedent(
        f"""
        {title}
        {'=' * len(title)}

        Setting: A {rng.choice(ADJECTIVES)} {place}.
        Rule: {twist}
        Objective: {quest}
        """
    ).strip()


def main() -> None:
    print("Welcome to the Pocket Universe Generator.")
    seed_text = input("Enter a seed number (or press Enter for random): ").strip()
    seed = int(seed_text) if seed_text else None

    print()
    print(generate_world(seed))


if __name__ == "__main__":
    main()