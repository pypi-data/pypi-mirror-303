import os
import pytest
import sys
from time import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from yuseful_prompts.chains import (
    check_headline_for_stocks_market_relevance,
    classify_headline_batch,
    classify_headline_with_predefined_category,
    classify_headline_sentiment,
    classify_headline_with_dynamic_category,
)

tsla_bearish = """'It Is Desolate': China's Glut of Unused Car Factories - Manufacturers like BYD, 
Tesla and Li Auto are cutting prices to move their electric cars. For gasoline-powered vehicles, the surplus of 
factories is even worse."""
tsla_bearish2 = """U.S. Accuses Two Men of Stealing Tesla Trade Secrets - Federal prosecutors said the pair tried to 
sell technology to manufacture batteries for electric cars that belonged to the company."""
headline_sentiment_test_cases = [
    (
        {
            "headline_text": (
                "Asure Partners with Key Benefit Administrators",
                "to Offer Proactive Health Management Plan (PHMP) to Clients",
            )
        },
        {
            "possible_sentiments": [
                "bullish",
                "slightly bullish",
                "very bullish",
            ]
        },
    ),
    (
        {
            "headline_text": (
                "Everbridge Cancels Fourth Quarter",
                "and Full Year 2023 Financial Results Conference Call",
            )
        },
        {
            "possible_sentiments": [
                "bearish",
                "slightly bearish",
                "very bearish",
                "uncertain",
                "volatile",
            ]
        },
    ),
    (
        {
            "headline_text": (
                "This Analyst With 87% Accuracy Rate Sees Around 12% Upside In Masco -",
                "Here Are 5 Stock Picks For Last Week From Wall Street's Most Accurate Analysts "
                "- Masco (NYSE:MAS)",
            )
        },
        {"possible_sentiments": ["bullish", "slightly bullish", "very bullish"]},
    ),
    (
        {
            "headline_text": "Tesla leads 11% annual drop in EV prices as demand slowdown continues"
        },
        {"possible_sentiments": ["bearish", "slightly bearish", "very bearish"]},
    ),
    (
        {
            "headline_text": "Elon Musk Dispatches Tesla's 'Fireman' to China Amid Slowing Sales"
        },
        {"possible_sentiments": ["bearish", "slightly bearish", "uncertain"]},
    ),
    (
        {
            "headline_text": "OpenAI co-founder Ilya Sutskever says he will leave the startup"
        },
        {
            "possible_sentiments": [
                "bearish",
                "slightly bearish",
                "uncertain",
            ]
        },
    ),
    (
        {
            "headline_text": "Hedge funds cut stakes in Magnificent Seven to invest in broader AI boom"
        },
        {
            "possible_sentiments": [
                "neutral",
                "slightly bearish",
                "slightly bullish",
                "uncertain",
            ]
        },
    ),
    (
        {
            "headline_text": "Current Climate: California, Tesla And The EV Market's Mixed Signals"
        },
        {"possible_sentiments": ["neutral", "slightly bearish", "uncertain"]},
    ),
    (
        {
            "headline_text": "Musk, Tesla shareholder to propose a stay of pay ruling during appeal - court filing"
        },
        {"possible_sentiments": ["slightly bearish", "uncertain"]},
    ),
    (
        {
            "headline_text": "Tesla settles with former employee over racial discrimination claims"
        },
        {"possible_sentiments": ["bearish", "slightly bearish"]},
    ),
    (
        {
            "headline_text": "Microsoft Seeks to Dismiss Parts of Suit Filed by The New York Times"
        },
        {"possible_sentiments": ["bearish", "slightly bearish", "uncertain"]},
    ),
    (
        {
            "headline_text": "Any hope for a cheaper Tesla model may be on hold for now. But how about a Tesla taxi for your troubles?"
        },
        {
            "possible_sentiments": [
                "slightly bearish",
                "uncertain",
            ]
        },
    ),
    (
        {
            "headline_text": "Musk Now Says He Opposes Tariffs On Chinese EVs—Here's What He Had Said Earlier"
        },
        {"possible_sentiments": ["neutral", "slightly bearish", "uncertain"]},
    ),
    (
        {
            "headline_text": "China's BYD, SAIC's MG undecided on EV price hikes due to tariffs, sources say"
        },
        {
            "possible_sentiments": [
                "neutral",
                "slightly bearish",
                "uncertain",
            ]
        },
    ),
    (
        {
            "headline_text": "The fight over the future of plastics - As countries negotiate a landmark agreement to reduce plastic pollution, the industry is fighting a battle over regulations and over its image."
        },
        {"possible_sentiments": ["neutral", "slightly bearish", "uncertain"]},
    ),
    (
        {
            "headline_text": "Hackers for China, Russia and Others Used OpenAI Systems, Report Says - Microsoft and OpenAI said the A.I. had helped groups with ties to China, Russia, North Korea and Iran mostly with routine tasks."
        },
        {
            "possible_sentiments": [
                "bearish",
                "slightly bearish",
                "uncertain",
            ]
        },
    ),
    (
        {
            "headline_text": tsla_bearish,
        },
        {
            "possible_sentiments": [
                "bearish",
                "slightly bearish",
                "uncertain",
                "very bearish",
            ]
        },
    ),
    (
        {
            "headline_text": tsla_bearish2,
        },
        {
            "possible_sentiments": [
                "bearish",
                "slightly bearish",
                "uncertain",
                "very bearish",
            ]
        },
    ),
]


@pytest.mark.parametrize(
    "headline_input,expected",
    [
        (
            {
                "headline_text": (
                    "Mum and chef die after carnival weekend attacks - Both deaths are now being treated as murder investigations, say police.",
                )
            },
            {
                "relevance": False,
            },
        ),
        (
            {
                "headline_text": (
                    "Russia pushes on key Ukraine city while Kyiv's Kursk incursion slows - Russia is poised to assault Pokrovsk, a crucial supply and reinforcement hub for Ukraine's frontline troops.",
                )
            },
            {
                "relevance": True,
            },
        ),
        (
            {
                "headline_text": (
                    "Oasis gigs selling out as fans scramble for tickets - Some fans face difficulties accessing the websites selling tickets for the band's comeback gigs in the UK and Ireland next year.",
                )
            },
            {
                "relevance": False,
            },
        ),
        (
            {
                "headline_text": (
                    "US rapper Fatman Scoop dies after collapsing on stage - The New Yorker, who has collaborated with artists like Mariah Carey, collapsed during a gig in Connecticut.",
                )
            },
            {
                "relevance": False,
            },
        ),
        (
            {
                "headline_text": (
                    "Thunderstorm warning for England and east Wales - There is a risk of flooding in some areas, with Met Office saying hail and lighting are also likely.",
                )
            },
            {
                "relevance": False,
            },
        ),
        (
            {
                "headline_text": (
                    "China and Philippines trade blame as ships collide - The crash is the latest incident in an escalating row over key zones in the South China Sea.",
                )
            },
            {
                "relevance": True,
            },
        ),
    ],
)
def test_check_headline_for_stocks_market_relevance(headline_input, expected):
    res = check_headline_for_stocks_market_relevance(
        headline_input["headline_text"], 
        True
    )
    print(res)
    assert res["relevance"] == expected["relevance"]


@pytest.mark.parametrize("headline_input,expected", headline_sentiment_test_cases)
def test_classify_headline_sentiment(headline_input, expected):
    assert (
        classify_headline_sentiment(**headline_input)["sentiment"]
        in expected["possible_sentiments"]
    )


@pytest.mark.parametrize(
    "headline_input,expected",
    [
        (
            {"headline_text": ("TJX Stock: Analyst Estimates & Ratings",)},
            {
                "category": "analyst-ratings",
            },
        ),
        (
            {
                "headline_text": (
                    "Stellantis Announces Launch of Third Tranche of Its 2024 Share Buyback Program",
                )
            },
            {
                "category": "buybacks",
            },
        ),
        (
            {
                "headline_text": (
                    "SKZ expands regulatory training of plastics selection with intensive course",
                )
            },
            {
                "category": "compliance-regulatory",
            },
        ),
        (
            {
                "headline_text": (
                    "How governance plays a role in HP's award-winning ESG reporting",
                )
            },
            {
                "category": "corporate-governance",
            },
        ),
        (
            {
                "headline_text": (
                    "Pantheon International outlines next phase of its corporate strategy",
                )
            },
            {
                "category": "corporate-strategy",
            },
        ),
        (
            {
                "headline_text": (
                    "TGC-14 plans to pay dividends for the first half of the year for 619.47 million rubles",
                )
            },
            {
                "category": "dividends",
            },
        ),
        (
            {
                "headline_text": (
                    "U.S heading for a recession? Here are all the key indicators that point towards it",
                )
            },
            {
                "category": "economic-indicators",
            },
        ),
        (
            {"headline_text": ("A rollercoaster earnings season for tech stocks",)},
            {
                "category": "earnings",
            },
        ),
        (
            {
                "headline_text": (
                    "Scott Russell and Julia White to Leave SAP Executive Board",
                )
            },
            {
                "category": "executive-changes",
            },
        ),
        (
            {
                "headline_text": (
                    "Inaugural Forum of the Global Coalition for Social Justice",
                )
            },
            {
                "category": "global-events",
            },
        ),
        (
            {"headline_text": ("Top Smartphone Trends Revealed for Q2 2024",)},
            {
                "category": "industry-trends",
            },
        ),
        (
            {
                "headline_text": (
                    "Economie - Les innovations du Clermontois Carbios intéressent de la Chine à la Turquie",
                )
            },
            {
                "category": "innovations",
            },
        ),
        (
            {
                "headline_text": (
                    "Steamboat Springs to consider joining Kroger opioid settlement",
                )
            },
            {
                "category": "lawsuits-settlements",
            },
        ),
        (
            {"headline_text": ("Nvidia is on a startup buying spree",)},
            {
                "category": "mergers-acquisitions",
            },
        ),
        (
            {
                "headline_text": (
                    "Driving Policy Change - Update on FCDO Donor Dialogue on Localisation process and follow-up",
                )
            },
            {
                "category": "policy-change",
            },
        ),
        (
            {
                "headline_text": (
                    "Netflix price target raised: Analyst's 3 catalysts for the stock",
                )
            },
            {
                "category": "price-targets",
            },
        ),
        (
            {
                "headline_text": (
                    "Eviden launches Digital Passport Solution for products and goods",
                )
            },
            {
                "category": "product-launches",
            },
        ),
        (
            {
                "headline_text": (
                    "Nestle recalling Gerber baby cereal in Canada after testing finds Cronobacter",
                )
            },
            {
                "category": "product-recalls",
            },
        ),
        (
            {
                "headline_text": (
                    "Can Morocco's phosphate wealth put it at the centre of the global battery supply chain?",
                )
            },
            {
                "category": "supply-chain",
            },
        ),
    ],
)
def test_classify_headline_with_predefined_category(headline_input, expected):
    res = classify_headline_with_predefined_category(headline_input["headline_text"])
    assert (
        res["category"]
        == expected["category"]
    )

# ! testing batch processing performance, comment if you don't want to run it
# @pytest.mark.parametrize("headline_input,expected", headline_sentiment_test_cases)
# def test_classify_headline_batch(headline_input, expected):
#     # counting the time the batch process takes
#     batch_start_time = time()
#     classify_headline_batch(headline_input["headline_text"])
#     batch_end_time = time()
#     # counting the time it takes to call the  components of batch processing individually
#     start_time_individual = time()
#     classify_headline_with_predefined_category(headline_input["headline_text"])
#     classify_headline_sentiment(headline_input["headline_text"])
#     classify_headline_with_dynamic_category(headline_input["headline_text"])
#     end_time_individual = time()
#     print()
#     print(f"Time taken for headline batch processing: {batch_end_time - batch_start_time} seconds")
#     print(f"Time taken for headline individual processing: {end_time_individual - start_time_individual} seconds")
#     # assert that the batch process is faster than the individual process
#     assert (batch_end_time - batch_start_time) < (end_time_individual - start_time_individual)