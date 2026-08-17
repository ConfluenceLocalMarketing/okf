# Directory Update Log

## 2026-08-18

- **Creation**: Built the Friendly Ford (Monroe, MI) OKF v0.1 bundle (14 concept files plus index files).
- **Data sources**: Direct browser crawl of yourfriendlyford.com (homepage, about, staff, service) and the PromptGraph `friendly-ford` slug (business, vehicles, offers, prompts, gbp-context, llms.txt, ai-manifest, robots.txt).
- **Note**: The `/vehicles` endpoint was crawled from `friendlyford.com` (an unrelated Roselle, IL dealership), so inventory counts should be treated with caution.
- **Note**: PromptGraph `/testimonials` returns an empty array; review data came from `/gbp-context` (4.5/5, 1,201 reviews).
