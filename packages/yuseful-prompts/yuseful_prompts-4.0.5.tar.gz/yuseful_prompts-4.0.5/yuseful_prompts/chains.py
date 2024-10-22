import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from yuseful_prompts.llms import get_json_local_model, get_text_local_model
from yuseful_prompts.prompts import (
    get_categories_relation_prompt,
    get_fully_answered_prompt,
    get_headline_dynamic_category_prompt,
    get_headline_obj_extraction_prompt,
    get_headline_predefined_category_prompt,
    get_headline_relevance_prompt,
    get_headline_sentiment_prompt,
)


def capture_relationship_between_categories(
    category1: str,
    category2: str,
    include_reasoning_description: bool = False,
):
    chain = (
        get_categories_relation_prompt(include_reasoning_description)
        | get_json_local_model()
    )
    return json.loads(
        chain.invoke({"category1": category1, "category2": category2}).content
    )


def check_headline_for_stocks_market_relevance(
    headline_text: str,
    include_reasoning_description: bool = False,
):
    chain = (
        get_headline_relevance_prompt(include_reasoning_description)
        | get_json_local_model()
    )
    return json.loads(chain.invoke({"headline_text": headline_text}).content)


def classify_headline_batch(headline_text: str):
    prompts = [
        get_headline_predefined_category_prompt(),
        get_headline_sentiment_prompt(),
        get_headline_dynamic_category_prompt(),
    ]
    messages = [
        [("human", prompt.format(headline_text=headline_text))] for prompt in prompts
    ]
    return get_json_local_model().batch(messages)


def classify_headline_with_dynamic_category(
    headline_text: str,
    include_reasoning_description: bool = False,
):
    chain = (
        get_headline_dynamic_category_prompt(include_reasoning_description)
        | get_json_local_model()
    )
    return json.loads(chain.invoke({"headline_text": headline_text}).content)


def classify_headline_sentiment(headline_text: str):
    chain = get_headline_sentiment_prompt() | get_text_local_model()
    output = chain.invoke({"headline_text": headline_text})
    return json.loads(output.content)


def classify_headline_with_predefined_category(headline_text: str, include_reasoning_description: bool = False):
    chain = get_headline_predefined_category_prompt(include_reasoning_description) | get_json_local_model()
    output = chain.invoke({"headline_text": headline_text})
    return json.loads(output.content)


def extract_headline_obj_from_html(html_text: str):
    chain = get_headline_obj_extraction_prompt() | get_json_local_model()
    output = chain.invoke({"html_text": html_text})
    return json.loads(output.content)


def verifies_if_question_is_fully_answered(question: str, answer: str):
    fully_answered_chain = get_fully_answered_prompt() | get_json_local_model()
    return json.loads(
        fully_answered_chain.invoke({"question": question, "answer": answer}).content
    )
