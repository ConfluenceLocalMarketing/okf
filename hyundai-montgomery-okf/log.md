# Directory Update Log

## 2026-08-08
- **Creation**: Initial bundle created for Hyundai Montgomery.
- **Data sources**: Main website (headless eyebrowse fetch of homepage, about-us, contact-us, service, finance, new-vehicles, used-inventory, new-vehicle-specials), PromptGraph API (business, vehicles, prompts, testimonials, offers, gbp-context, site-content, llms.txt, ai-manifest, config), customer reviews from dealership website (Google and DealerRater)
- **Scope**: Dealership profile (family-owned since 1970), new vehicles (full Hyundai lineup, 1,061 units listed, UP FRONT pricing), used vehicles (319 used and certified used, multi-make), staff (compiled from customer reviews, no official staff page), service center (3 current service specials), FAQs, AI discovery infrastructure (PromptGraph endpoints, AI Manifest), llms.txt, testimonials (reviews from website), prompts library (20 prompts), and model comparison tables (12 models)
- **Notes**: PromptGraph /vehicles and /testimonials endpoints currently return empty lists; inventory and review data sourced from the dealership website instead. Site sitemap.xml is blocked by the bot challenge; navigation structure sourced from site pages.
