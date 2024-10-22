import os
import pytest
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from yuseful_prompts.chains import (
    extract_headline_obj_from_html,
    verifies_if_question_is_fully_answered,
)


@pytest.mark.parametrize(
    "html,expected",
    [
        (
            {
                "input": """<div class="gap-4 border-gray-300 bg-white p-4 shadow last:pb-1 last:shadow-none dark:border-dark-600 dark:bg-dark-800 sm:border-b sm:px-0 sm:shadow-none sm:last:border-b-0 lg:gap-5 sm:grid sm:grid-cols-news sm:py-6"><a aria-hidden="true" class="sm:mt-1" href="https://www.businessinsider.com/waymo-tesla-opposite-problems-driverless-cars-technology-competition-market-dominance-2024-9" rel="nofollow noopener noreferrer" tabindex="-1" target="_blank"><img alt="" class="h-full w-full rounded object-cover" loading="lazy" src="https://cdn.snapi.dev/images/v1/t/s/tsla1-2479966-2643358.jpg"/></a> <div class="flex flex-col"><h3 class="mb-2 mt-3 text-xl font-bold leading-snug sm:order-2 sm:mt-0 sm:leading-tight"><a class="text-default hover:text-blue-brand_sharp dark:text-neutral-300 dark:hover:text-blue-darklink" href="https://www.businessinsider.com/waymo-tesla-opposite-problems-driverless-cars-technology-competition-market-dominance-2024-9" rel="nofollow noopener noreferrer" target="_blank">Waymo and Tesla have opposite problems as they compete for driverless tech dominance</a></h3> <p class="overflow-auto text-[0.95rem] text-light sm:order-3">Tesla and Waymo are locked in a battle for market dominance in the driverless tech sector. Waymo has an early advantage with its functional software but problems scaling its autonomous fleet.</p> <div class="mt-1.5 inline text-light sm:order-4 sm:mt-1"><span>Other symbols:</span> <a class="ticker" href="/stocks/goog/">GOOG</a><a class="ticker" href="/stocks/googl/">GOOGL</a></div>"""
            },
            {
                "excerpt": """Tesla and Waymo are locked in a battle for market dominance in the driverless tech sector. Waymo has an early advantage with its functional software but problems scaling its autonomous fleet.""",
                "title": "Waymo and Tesla have opposite problems as they compete for driverless tech dominance",
                "url": "https://www.businessinsider.com/waymo-tesla-opposite-problems-driverless-cars-technology-competition-market-dominance-2024-9",
            },
        ),
        (
            {
                "input": """<a class="titles noUnderline yf-13p9sh2" data-ylk="elm:hdln;elmt:link;itc:0;ct:story;sec:personal-finance;subsec:pf_lead" href="https://finance.yahoo.com/personal-finance/we-buy-houses-ripoff-181654510.html" data-rapid_p="207" data-v9y="1"><div class="lead-wrapper yf-udwyfo"><div style="display: contents; --aspect-ratio: 16/9; --border-radius: var(--border-radius-m); --object-fit: cover;"><img class="tw-bg-opacity-25  yf-13q9uv1" alt="Some “we buy houses” signs and cold calls are legitimate, but others are scams. Learn how to tell the difference." src="https://s.yimg.com/uu/api/res/1.2/cpG7HvxBcs34TIRZnXayCw--~B/Zmk9c3RyaW07aD0yMTA7cT04MDt3PTI3NTthcHBpZD15dGFjaHlvbg--/https://s.yimg.com/os/creatr-uploaded-images/2024-09/52935f40-71f9-11ef-aabe-814ed3abfd0e.cf.webp" srcset="https://s.yimg.com/uu/api/res/1.2/cpG7HvxBcs34TIRZnXayCw--~B/Zmk9c3RyaW07aD0yMTA7cT04MDt3PTI3NTthcHBpZD15dGFjaHlvbg--/https://s.yimg.com/os/creatr-uploaded-images/2024-09/52935f40-71f9-11ef-aabe-814ed3abfd0e.cf.webp 275w, https://s.yimg.com/uu/api/res/1.2/ikJC.Nv95a39lc6JdUNCWg--~B/Zmk9c3RyaW07aD00MjA7cT04MDt3PTU1MDthcHBpZD15dGFjaHlvbg--/https://s.yimg.com/os/creatr-uploaded-images/2024-09/52935f40-71f9-11ef-aabe-814ed3abfd0e.cf.webp 550w, https://s.yimg.com/uu/api/res/1.2/SOu69mIj1BwyP9dhUEFkNA--~B/Zmk9c3RyaW07aD01MTA7cT04MDt3PTY4MDthcHBpZD15dGFjaHlvbg--/https://s.yimg.com/os/creatr-uploaded-images/2024-09/52935f40-71f9-11ef-aabe-814ed3abfd0e.cf.webp 680w, https://s.yimg.com/uu/api/res/1.2/8f8Sw_mUCDQIGa3xPGgcnQ--~B/Zmk9c3RyaW07aD0xMDIwO3E9ODA7dz0xMzYwO2FwcGlkPXl0YWNoeW9u/https://s.yimg.com/os/creatr-uploaded-images/2024-09/52935f40-71f9-11ef-aabe-814ed3abfd0e.cf.webp 1360w" sizes="(min-width: 1050px) 575px, (min-width: 768px) 80vw, 100vw" fetchpriority="auto" loading="lazy"></div> <div class="content-wrapper yf-udwyfo"><div class="topic-bottom font-condensed yf-udwyfo">Editor's Pick</div> <h3 class="title yf-udwyfo">Are 'we buy houses' offers a scam? Here's how to tell.</h3> <p class="summary yf-udwyfo">Some “we buy houses” signs and cold calls are legitimate, but others are scams. Learn how to tell the difference.</p></div></div> </a>""",
            },
            {
                "excerpt": """Some “we buy houses” signs and cold calls are legitimate, but others are scams. Learn how to tell the difference.""",
                "title": "Are 'we buy houses' offers a scam? Here's how to tell.",
                "url": "https://finance.yahoo.com/personal-finance/we-buy-houses-ripoff-181654510.html",
            },
        )
    ],
)
def test_extract_headline_obj_from_html(html, expected):
    res = extract_headline_obj_from_html(html["input"])
    assert res["excerpt"] == expected["excerpt"]
    assert res["title"] == expected["title"]
    assert res["url"] == expected["url"]


@pytest.mark.parametrize(
    "q_a,expected",
    [
        (
            {
                "question": "What is the capital of France?",
                "answer": "Paris",
            },
            {"fully_answered": "yes"},
        ),
        (
            {
                "question": "What is the capital of France?",
                "answer": "It's a magic city with a lot of history and culture.",
            },
            {"fully_answered": "no"},
        ),
        (
            {
                "question": "What is 2 + 2?",
                "answer": "4",
            },
            {"fully_answered": "yes"},
        ),
        (
            {
                "question": "What is 2 + 2?",
                "answer": "It's a basic arithmetic question.",
            },
            {"fully_answered": "no"},
        ),
        (
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "answer": "Harper Lee",
            },
            {"fully_answered": "yes"},
        ),
        (
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "answer": "It was written by a famous author in the 20th century.",
            },
            {"fully_answered": "no"},
        ),
        (
            {
                "question": "What is the largest planet in our solar system?",
                "answer": "Jupiter",
            },
            {"fully_answered": "yes"},
        ),
        (
            {
                "question": "What is the largest planet in our solar system?",
                "answer": "It's a gas giant and the most massive planet.",
            },
            {"fully_answered": "no"},
        ),
        (
            {
                "question": "What is the boiling point of water at sea level?",
                "answer": "100 degrees Celsius",
            },
            {"fully_answered": "yes"},
        ),
        (
            {
                "question": "What is the boiling point of water at sea level?",
                "answer": "It's the temperature at which water turns into vapor.",
            },
            {"fully_answered": "no"},
        ),
        (
            {
                "question": "What is the speed of light?",
                "answer": "Approximately 299,792 kilometers per second",
            },
            {"fully_answered": "yes"},
        ),
        (
            {
                "question": "What is the speed of light?",
                "answer": "It's the speed at which light travels through a vacuum.",
            },
            {"fully_answered": "no"},
        ),
    ],
)
def test_verifies_if_question_is_fully_answered(q_a, expected):
    assert (
        verifies_if_question_is_fully_answered(**q_a)["fully_answered"]
        == expected["fully_answered"]
    )
