few_shot_examples = [
    {
        "input": "Find me companies that are attending Oil & Gas related events over the next 12 months.",
        "output": """
        SELECT company_name FROM events
        JOIN companies ON events.event_url = companies.homepage_base_url
        WHERE event_type = 'Oil & Gas' AND event_date BETWEEN CURRENT_DATE AND DATE_ADD(CURRENT_DATE, INTERVAL 12 MONTH)
        """
    },
    {
        "input": "Find sales people for companies that are attending events in Singapore over the next 9 months.",
        "output": """
        SELECT people_name, email FROM events
        JOIN companies ON events.event_url = companies.homepage_base_url
        JOIN people ON companies.homepage_base_url = people.homepage_base_url
        WHERE event_location = 'Singapore' AND event_date BETWEEN CURRENT_DATE AND DATE_ADD(CURRENT_DATE, INTERVAL 9 MONTH) AND job_description LIKE '%sales%'
        """
    },
    {
        "input": "Find me events that companies in the Pharmaceuticals sector are attending.",
        "output": """
        SELECT event_name FROM events
        JOIN companies ON events.event_url = companies.homepage_base_url
        WHERE company_industry = 'Pharmaceuticals'
        """
    },
    {
        "input": "Find email addresses of people working in tech companies attending finance events.",
        "output": """
        SELECT people_name, email FROM events
        JOIN companies ON events.event_url = companies.homepage_base_url
        JOIN people ON companies.homepage_base_url = people.homepage_base_url
        WHERE company_industry = 'Technology' AND event_type = 'Finance'
        """
    },
    {
        "input": "List all events attended by companies with revenue over $1M.",
        "output": """
        SELECT event_name FROM events
        JOIN companies ON events.event_url = companies.homepage_base_url
        WHERE company_revenue > 1000000
        """
    },
    {
        "input": "Show me all tech-related events happening in the next 6 months.",
        "output": """
        SELECT event_name FROM events
        WHERE event_type = 'Technology' AND event_date BETWEEN CURRENT_DATE AND DATE_ADD(CURRENT_DATE, INTERVAL 6 MONTH)
        """
    }
]
