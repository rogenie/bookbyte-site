SITE = {
  "name": "BookByte",
  "url": "https://bookbytellc.com",
  "desc": "Plain-English bookkeeping and tax guides for the self-employed: freelancers, contractors, creators and single-owner LLCs and S-corps.",
  "author": "Computatio",
  "cta_url": "https://computatio.io/?",
  "ai": ("/ai-accounting/","AI for Accounting"),
  "newsletter": "https://computatios-newsletter.beehiiv.com/",
  "nav": [("/bookkeeping/","Bookkeeping"),("/estimated-taxes/","Estimated taxes"),("/deductions/","Deductions"),("/business-structure/","Business structure"),("/about/","About")],
}

def hub(path, name, title, desc, intro, covers, hero_extra="", after_list=""):
    lis = "".join(f"<li>{c}</li>" for c in covers)
    body = f'''<section class="hero small"><div class="wrap">
<p class="eyebrow">Guides</p><h1>{name}</h1><p class="lede">{intro}</p>{hero_extra}</div></section>
<section><div class="wrap narrow">
<!--HUB_ARTICLES-->
</div></section>{after_list}<section><div class="wrap narrow">
<h2>What this section covers</h2><ul class="ticks">{lis}</ul>
<p class="muted">New guides are added every week. Each one shows the date it was last checked against official sources.</p>
</div></section>'''
    return {"path":path,"title":title,"desc":desc,"h1":name,"body":body}

HERO_DFY = '\n<p class="hero-dfy">Short on time? <a href="https://computatio.io/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=ai-hub-hero#offers">Have Computatio do your books for you &rarr;</a></p>'
PITCH_DFY = '\n<section class="dfy" id="done-for-you"><div class="wrap">\n<div class="dfy-grid">\n<div class="dfy-copy">\n<p class="eyebrow">Done for you</p>\n<h2>Rather spend your time on clients than on your books?</h2>\n<p>AI makes bookkeeping faster, but someone still has to run the prompts, check every category it guessed, chase the missing receipts and reconcile each account. For most owners that&rsquo;s still a few hours a month, usually late at night, and the month you skip it is the month that turns into a cleanup project before tax time.</p>\n<p>Picture this instead: your books are closed by the 15th of every month, you get a one-page summary in plain English, and a 30-minute call where you can ask anything about your numbers.</p>\n<p>That&rsquo;s Computatio. We use the same AI workflows these guides teach, and a person reviews and signs off on every account.</p>\n</div>\n<div class="dfy-offer">\n<p class="dfy-name">Monthly Books</p>\n<p class="dfy-price">$500<span> / month</span></p>\n<ul class="ticks">\n<li>Books closed monthly: profit and loss, balance sheet and cash summary</li>\n<li>One-page plain-English summary by the 15th</li>\n<li>30-minute monthly review call</li>\n<li>Month to month; cancel with 30 days&rsquo; notice</li>\n</ul>\n<a class="btn" href="https://computatio.io/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=ai-hub-monthly-books#offers">See Monthly Books</a>\n<a class="btn ghost" href="https://computatio.io/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=ai-hub-book-call#book">Book a call first</a>\n<p class="dfy-more">Books more than 2 months behind? Start with a <a href="https://computatio.io/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=ai-hub-cleanup#offers">books cleanup</a>. Need a tax return? Returns start at $350. <a href="https://computatio.io/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=ai-hub-returns#offers">See tax returns</a>.</p>\n</div>\n</div>\n</div></section>'

PAGES = [
 {"path":"/","title":"BookByte | AI for Accounting: Guides for the Self-Employed","h1":"BookByte",
  "desc":"How to use AI for bookkeeping, taxes and accounting tasks, step by step. Practical guides for freelancers, contractors, creators and small-business owners.",
  "body":'''<section class="hero"><div class="wrap">
<p class="eyebrow">AI for accounting, for the self-employed</p>
<h1>Use AI to do your own books and taxes, <span>the right way.</span></h1>
<p class="lede">Prompts, workflows and checks that let AI do the slow parts of bookkeeping and tax prep, without the mistakes. Every rule is checked against official IRS and state sources.</p>
<a class="ai-btn big" href="/ai-accounting/">Start with AI for Accounting</a> &nbsp; <a class="btn ghost" href="/bookkeeping/">Bookkeeping basics</a>
</div></section>
<section class="nlband"><div class="wrap aiflex">
<div><p class="eyebrow">Free download</p><h2>47 write-offs for the self-employed</h2>
<p>A 42-page guide to 47 deductions, with the IRS rules behind each one. Free when you join the Computatio newsletter.</p></div>
<a class="btn" href="https://computatios-newsletter.beehiiv.com/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=home">Get the free guide</a>
</div></section>
<!--LATEST-->
<section><div class="wrap">
<h2>Pick a topic</h2>
<div class="cards">
<a class="card ai" href="/ai-accounting/"><h3>AI for Accounting</h3><p>Use AI to speed up bookkeeping, receipts, month-end and tax prep, and learn how to check its work.</p></a>
<a class="card" href="/bookkeeping/"><h3>Bookkeeping</h3><p>Set up your books, categorize transactions, reconcile accounts and catch up when you&rsquo;re behind. Includes guides for specific trades.</p></a>
<a class="card" href="/estimated-taxes/"><h3>Estimated taxes</h3><p>How much to pay, when, and how. Covers IRS dates and state schedules that differ.</p></a>
<a class="card" href="/deductions/"><h3>Deductions</h3><p>What you can write off, how to prove it, and where state rules differ from federal.</p></a>
<a class="card" href="/business-structure/"><h3>Business structure</h3><p>Sole proprietor, LLC or S-corp, plus state taxes to check before you choose.</p></a>
</div></div></section>
<section class="alt"><div class="wrap narrow">
<h2>How we write these guides</h2>
<ul class="ticks">
<li>Every rule, rate and deadline is checked against the IRS or the relevant state tax agency, and sources are listed at the end of each guide.</li>
<li>Each guide shows the date it was last reviewed. Tax-year guides are refreshed every January.</li>
<li>Examples use made-up numbers and are labeled as examples.</li>
</ul>
<p><a href="/about/">More about BookByte</a></p>
</div></section>'''},
 hub("/ai-accounting/","AI for Accounting","AI for Accounting: Guides for the Self-Employed | BookByte",
     "How to use AI for accounting as a freelancer or owner-operator: bookkeeping, receipts, month-end and tax prep, done accurately and safely.",
     "AI can turn hours of bookkeeping and tax prep into minutes, but only if you know where it&rsquo;s reliable and where it isn&rsquo;t. These guides show you how to use it and how to check its work.",
     ["How to use AI for bookkeeping, and keep your books accurate","How to use AI to categorize business transactions, and check its work","AI receipt scanning: what to look for in a tool","Can AI do your accounting? What it gets right and wrong","Ready-to-use prompts for monthly bookkeeping tasks","Keeping your financial data safe when you use AI","Using AI to get ready for tax season","AI, a bookkeeper, or doing it yourself: time and cost compared"],
     hero_extra=HERO_DFY, after_list=PITCH_DFY),
 hub("/bookkeeping/","Bookkeeping","Bookkeeping Guides for the Self-Employed | BookByte",
     "Do-it-yourself bookkeeping for freelancers and owner-operators: setup, categorizing, reconciling, catching up and trade-specific guides.",
     "Keep accurate books without an accounting degree. Start with the basics, then find the guide for your trade.",
     ["Setting up your books and separating business from personal money","Categorizing transactions with a simple chart of accounts","Reconciling bank and card accounts each month","Catching up when your books are months behind","What receipts to keep, and for how long","Guides for contractors, real estate agents, creators, drivers, consultants and online sellers"]),
 hub("/estimated-taxes/","Estimated taxes","Quarterly Estimated Tax Guides for the Self-Employed | BookByte",
     "Quarterly estimated taxes for the self-employed: who has to pay, how much, IRS and state due dates, and how to pay online.",
     "If no one withholds tax from your pay, you pay it yourself during the year. These guides walk through the IRS rules and the state rules that differ, starting with California.",
     ["Whether you need to make estimated payments","How to calculate each payment, with a worked example","IRS due dates, and state schedules that differ, such as California&rsquo;s 30/40/0/30","Paying online through IRS Direct Pay and state payment sites","What to do if you missed a payment"]),
 hub("/deductions/","Deductions","Self-Employed Tax Deduction Guides | BookByte",
     "Self-employed tax deductions explained: mileage, home office, health insurance, retirement and more, including where state rules differ from federal.",
     "Lower your tax the legitimate way. Each guide explains what qualifies, how to document it, and where state rules differ.",
     ["Mileage, vehicles and the current IRS rate","Home office: simplified vs. regular method","Health insurance and retirement contributions","Schedule C, line by line","1099-NEC and 1099-K forms and thresholds","Federal deductions some states don&rsquo;t allow, such as California and the QBI deduction"]),
 hub("/business-structure/","Business structure","Sole Proprietor, LLC or S-Corp: Choosing a Structure | BookByte",
     "Choosing a business structure: sole proprietor vs. LLC vs. S-corp, state taxes like California's $800 minimum, and paying yourself a reasonable salary.",
     "Your business structure changes how you&rsquo;re taxed. These guides explain the federal rules and the state costs to check before you file anything.",
     ["Sole proprietor vs. S-corp: when the switch pays off","California&rsquo;s $800 annual LLC and corporation tax","Paying yourself from an S-corp: reasonable salary","When an LLC makes sense, and when it doesn&rsquo;t"]),
 {"path":"/about/","title":"About BookByte","h1":"About BookByte",
  "desc":"Who writes BookByte, how each guide is checked, and where to get bookkeeping and tax help if you'd rather not do it yourself.",
  "body":'''<section class="hero small"><div class="wrap"><h1>About BookByte</h1>
<p class="lede">Clear, accurate guides for people who run their own business and want to handle their own books and taxes.</p></div></section>
<section><div class="wrap narrow prose">
<h2>Who writes the guides</h2>
<p>BookByte is written by Computatio, a bookkeeping and tax service for self-employed owners across the US. Computatio&rsquo;s founder, Rogenie Cordero, has 20 years of experience in bookkeeping, tax and finance, a dual degree with a minor in computer science, and more than 20 years of building businesses across industries, both for-profit and nonprofit. <a href="https://www.linkedin.com/in/rogenie" rel="me noopener" target="_blank">Rogenie on LinkedIn</a></p>
<h2>How we check them</h2>
<p>Every rate, threshold and deadline is checked against an official source: the IRS or the relevant state tax agency, such as California&rsquo;s Franchise Tax Board (FTB). Sources are listed at the end of each guide, along with the date it was last reviewed. When a rule changes, the guide is updated.</p>
<h2>What BookByte is not</h2>
<p>These guides are general information for doing the work yourself. They aren&rsquo;t tax or legal advice for your situation. If something is unclear or the stakes are high, talk to a tax professional.</p>
<h2>If you&rsquo;d rather not do it yourself</h2>
<p>Most people who read these guides can do the work. The usual reason not to is time. <a href="https://computatio.io/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=about">Computatio</a> keeps books current for $500 a month and prepares returns at fixed prices, with a person reviewing and signing off on every account.</p>
</div></section>'''},
 {"path":"/privacy/","title":"Privacy Policy | BookByte","h1":"Privacy policy",
  "desc":"How BookByte handles information when you visit the site.",
  "body":'''<section class="hero small"><div class="wrap"><h1>Privacy policy</h1><p class="lede">Last updated October 20, 2026.</p></div></section>
<section><div class="wrap narrow prose">
<h2>What we collect</h2>
<p>BookByte has no accounts, forms or comments, and doesn&rsquo;t set its own cookies. We don&rsquo;t sell or share personal information.</p>
<h2>Newsletter</h2>
<p>If you sign up for the free write-offs guide, your email address is collected by beehiiv, the service that runs the Computatio newsletter, under its own privacy policy. You can unsubscribe from any email.</p>
<h2>Services that load with the site</h2>
<p>The site is hosted on GitHub Pages and loads fonts from Google Fonts. Like any web server, these services receive your IP address and basic browser information when you load a page, under their own privacy policies.</p>
<h2>Visit counts</h2>
<p>We count page visits with GoatCounter, a privacy-friendly analytics service. It sets no cookies and doesn&rsquo;t track you across sites. It records the page you visited, the site that sent you, and general details such as browser, screen size and country. It doesn&rsquo;t store your IP address.</p>
<h2>Changes</h2>
<p>If we add another analytics service or a form, this page will be updated first and will say what is collected and why.</p>
<h2>Contact</h2>
<p>Questions about this policy can be sent through <a href="https://computatio.io/#book">computatio.io</a>.</p>
</div></section>'''},
 {"path":"/404","title":"Page not found | BookByte","h1":"Page not found","noindex":True,
  "desc":"This page doesn't exist.",
  "body":'''<section class="hero small"><div class="wrap"><h1>Page not found</h1><p class="lede">That page doesn&rsquo;t exist, or it has moved.</p><a class="btn" href="/">Go to the home page</a></div></section>'''},
]
