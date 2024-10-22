from langchain_core.prompts import PromptTemplate


def get_categories_relation_prompt(
    include_reasoning_description: bool = False,
) -> PromptTemplate:
    categories_relation_prompt_template = """You are an investment news analyst. Compare these two news categories:

    category1: "{category1}"
    category2: "{category2}"

    Your task is to determine whether category1 is related to category2.

    Choose one answer:

    1. Related: category1 and category2 are related
    2. Unrelated: category1 and category2 are not related

    Important rules:
    - Always analyze how category1 relates to category2
    - Consider if the topics overlap, are in the same field, or commonly associated

    Respond with a JSON object. The key should be "relationship" and the value should be:
    - "related" if you chose 1
    - "unrelated" if you chose 2"""
    if include_reasoning_description:
        categories_relation_prompt_template += """

Also include a "reasoning" key in the JSON, with a brief explanation of your choice as the value."""

    categories_relation_prompt = PromptTemplate.from_template(
        categories_relation_prompt_template
    )
    return categories_relation_prompt


def get_fully_answered_prompt() -> PromptTemplate:
    fully_answered_prompt = PromptTemplate(
        template="""You will determine if the provided question is fully answered by the provided answer.
Question:
{question}

Answer:
{answer}

You will respond with a JSON having "fully_answered" as key and exactly either "yes" or "no" as value.""",
        input_variables=["question", "answer"],
    )
    return fully_answered_prompt


def get_headline_dynamic_category_prompt(
    include_reasoning_description: bool = False,
) -> PromptTemplate:
    headline_dynamic_category_prompt_template = """You are an investment analyst. You will be given a news headline. Your task is to derive an appropriate category for this headline. 
The category should have the right balance in granularity: not too general and not too specific. This is important because it helps in organizing and classifying news content effectively.

Guidelines for determining appropriate granularity:
1. Too general: Avoid broad categories like "News" or "Current Events" that could apply to almost any headline.
2. Too specific: Avoid categories that are so narrow they would rarely be used for other headlines.
3. Aim for a middle ground: The category should be specific enough to give a clear idea of the headline's content, but general enough to potentially include other similar stories.

Analyze the headline carefully, considering its main topic, themes, and context. Think about what section of a news website or newspaper this headline might appear in.

Here is the headline text you need to analyze, delimited by dashes:

--------------------------------------------------
{headline_text}
--------------------------------------------------

Remember, the goal is to find a category that is neither too broad nor too narrow, but just right for classifying this headline and potentially similar news stories."""
    if include_reasoning_description:
        headline_dynamic_category_prompt_template += """You will respond with a JSON having as key/value pairs:
- "category" as key, with the category you have chosen as value
- "reasoning" as key, with a brief text explaining your reasoning as value"""
    else:
        headline_dynamic_category_prompt_template += """You will respond with a JSON having only "category" as key with the derived category as value."""
    headline_dynamic_category_prompt = PromptTemplate.from_template(
        headline_dynamic_category_prompt_template
    )
    return headline_dynamic_category_prompt


def get_headline_obj_extraction_prompt() -> PromptTemplate:
    headline_obj_extraction_prompt_template = """You are an investment analyst clerck. Your job is to extract the headline, excerpt, and URL from the following HTML text.

Here is the HTML text:

--------------------------------------------------
{html_text}
--------------------------------------------------

You will respond with a JSON having ONLY the following key/value pairs:
- "title" as key, with the headline as value
- "excerpt" as key, with the excerpt as value
- "url" as key, with the URL as value

DO NOT modify the original content.
DO NOT make up additional content or add punctuation, quotes, characters, or any formatting.
DO NOT keep the HTML code, keep only the required information."""
    headline_obj_extraction_prompt = PromptTemplate.from_template(
        headline_obj_extraction_prompt_template
    )
    return headline_obj_extraction_prompt


def get_headline_predefined_category_prompt(include_reasoning_description: bool = False) -> PromptTemplate:
    headline_predefined_category_prompt_template = """You are an investment analyst. Your job is to label a news headline with a predefined category.

Here is the headline text you need to label, delimited by dashes:

--------------------------------------------------
{headline_text}
--------------------------------------------------

Here is the list, delimited by commas, of the authorized categories:

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
analyst-ratings
buybacks
compliance-regulatory
corporate-governance
corporate-strategy
dividends
economic-indicators
earnings
executive-changes
global-events
industry-trends
innovations
lawsuits-settlements
mergers-acquisitions
policy-change
price-targets
product-launches
product-recalls
supply-chain
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

You are to output ONLY ONE DISTINCT CATEGORY, unchanged, from the list of authorized categories.
DON'T MAKE UP CATEGORIES THAT ARE NOT IN THE LIST!

"""
    if include_reasoning_description:
        headline_predefined_category_prompt_template += """You will respond with a JSON having as key/value pairs:
- "category" as key, with the category you have chosen as value
- "reasoning" as key, with a brief text explaining your reasoning as value"""
    else:
        headline_predefined_category_prompt_template += """You will respond with a JSON having only "category" as key, with the category you have chosen as value"""
    headline_predefined_category_prompt_template += """DO NOT comment your output or add additional content, punctuation, quotes, characters, or any formatting."""
    headline_predefined_category_prompt = PromptTemplate.from_template(
        headline_predefined_category_prompt_template
    )
    return headline_predefined_category_prompt


def get_headline_relevance_prompt(
    include_reasoning_description: bool = False,
) -> PromptTemplate:
    headline_relevance_prompt_template = """You are an investment analyst and data scientist specializing in identifying news that could impact stock markets. 
You will be given a news headline: your task is to analyze it and to determine its potential relevance in analyzing stock market short, long, and mid-term trends.

To do your task, consider the following factors:

Consider potential direct impacts on:
- economic indicators
- industry sectors
- overall market sentiment
- specific companies or stocks

Evaluate possible indirect effects, such as:
- changes in consumer behavior
- geopolitical events affecting trade routes and supply chains or happening in regions with strategic natural resources
- long-term trends or societal changes
- ripple effects across industries

The psychological impact of the news on market participants is also an important factor to consider. 

Assess the likelihood and magnitude of any potential impact before making your decision
If the impact is sizable, the headline is relevant. If the impact is minor or unlikely, the headline is irrelevant.
Be mindful of not overestimating the relevance of the headline: only consider the most likely and significant impacts.

Here is the headline text you need to analyze, delimited by dashes:

--------------------------------------------------
{headline_text}
--------------------------------------------------"""
    if include_reasoning_description:
        headline_relevance_prompt_template += """You will respond with a JSON having as key/value pairs:
- "relevance" as key, with either `true` or `false` (without the backticks) as value
- "reasoning" as key, with a string explaining your decision as value"""
    else:
        headline_relevance_prompt_template += """You will respond with a JSON having only "relevance" as key and either `true` or `false` (without the backticks) as value."""
    headline_relevance_prompt = PromptTemplate.from_template(
        headline_relevance_prompt_template
    )
    return headline_relevance_prompt


def get_headline_sentiment_prompt() -> PromptTemplate:
    headline_sentiment_prompt_template = """You are an investment analyst. Your job is to label a headline with a sentiment IN ENGLISH.

Headlines that mention upside or positive developments range from slightly bullish to very bullish. This includes headlines that mention or imply positive developments such as:
- awards or recognitions
- beneficial mergers or acquisitions
- strategic partnerships or collaborations
- favorable market conditions
- increased revenue or profits
- market expansion
- new product launches or innovations
- positive financial results or forecasts
- regulatory approvals or favorable legislation

Headlines that range from slightly bearish to volatile mention or imply one or more of the following:
- declines in stock prices or market value
- economic slowdown or negative economic indicators
- increased selling pressure on shares
- instability or uncertainty in the market
- labor issues or strikes
- legal challenges, disputes, or lawsuits
- regulatory hurdles or investigations
- decline in sales or profits
- cancellations or delays of important events or releases
- executive resignations or leadership changes

Legal issues, regulatory challenges, and any other adverse proceedings are NEVER TO BE LABELED AS NEUTRAL and should be classified within the range of slightly bearish to uncertain depending on the severity implied by the headline.

Only label a headline as neutral if it is purely informative and does not imply any positive or negative sentiment, and does not allow deriving any negative or positive outlook on the market.

Only label a headline as "very" bearish or bullish if it indicates far-reaching consequences or a significant change in the market.

Uncertainty or mixed signals are never in the range of bullish headlines.

Only label a headline as "volatile" if it clearly indicates a high level of uncertainty and unpredictability in the market due to the headline's content.

Note: the tone of the headline is to be factored in; for instance, dismissive or sarcastic tone should never be labeled as bullish or neutral.

Here is the headline text you need to label, delimited by dashes:

--------------------------------------------------
{headline_text}
--------------------------------------------------

Here is the list of the possible sentiments:

- very bullish
- bullish
- slightly bullish
- neutral
- slightly bearish
- bearish
- very bearish
- uncertain
- volatile

You are to output ONLY ONE DISTINCT SENTIMENT, unchanged, from the list of possible sentiments.
DO NOT make up sentiments that are not in the list.
You will respond with a JSON having "sentiment" as key, with the sentiment you have chosen as value.
DO NOT add additional content, punctuation, explanation, characters, or any formatting in your output."""
    headline_sentiment_prompt = PromptTemplate.from_template(
        headline_sentiment_prompt_template
    )
    return headline_sentiment_prompt
