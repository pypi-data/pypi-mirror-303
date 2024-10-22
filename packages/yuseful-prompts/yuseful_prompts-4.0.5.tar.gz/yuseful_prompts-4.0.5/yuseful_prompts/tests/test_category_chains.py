import os
import pytest
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from yuseful_prompts.chains import (
    capture_relationship_between_categories
)


@pytest.mark.parametrize(
    "categories,expected",
    [
        (
            {
                "category1": "technology",
                "category2": "artificial intelligence",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "artificial intelligence",
                "category2": "technology",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "electric vehicles",
                "category2": "automotive",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "cooking",
                "category2": "politics",
            },
            {
                "relationship": "unrelated",
            },
        ),
        (
            {
                "category1": "russia-ukraine conflict",
                "category2": "international conflict crisis",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "environment disaster",
                "category2": "environment",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "cryptocurrency",
                "category2": "blockchain",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "sports",
                "category2": "basketball",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "economics",
                "category2": "monetary policy",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "online shopping",
                "category2": "e-commerce",
            },
            {
                "relationship": "related",
            },
        ),
        (
            {
                "category1": "music",
                "category2": "cooking",
            },
            {
                "relationship": "unrelated",
            },
        ),
        (
            {
                "category1": "data science",
                "category2": "machine learning",
            },
            {
                "relationship": "related",
            },
        ),
    ],
)
def test_capture_relationship_between_categories(categories, expected):
    res = capture_relationship_between_categories(
        categories["category1"],
        categories["category2"],
        include_reasoning_description=True,
    )
    print(res)
    assert res["relationship"] == expected["relationship"]
