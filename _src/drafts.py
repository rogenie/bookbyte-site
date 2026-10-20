# Week 1 drafts. Move an entry into PAGES (pages.py) to publish it.
CTA = "https://computatio.io/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign="

def article(path, hub, hub_name, title, h1, desc, published, intro, sections, cta_html, sources, slug):
    src = "".join(f'<li><a href="{u}">{t}</a></li>' for t,u in sources)
    body = f'''<section class="hero small"><div class="wrap narrow">
<p class="eyebrow"><a href="{hub}" style="color:inherit;text-decoration:none">{hub_name}</a></p>
<h1>{h1}</h1>
<p class="lede">{intro}</p>
<p class="muted" style="color:#bbb">By Rogenie Cordero &middot; Last reviewed {published}</p>
</div></section>
<section><div class="wrap narrow prose">
{sections}
<div class="cta"><b>Short on time?</b> {cta_html.replace("CTAURL", CTA+slug)}</div>
<h2>Sources</h2><ul>{src}</ul>
<p class="muted">This guide is general information, not tax advice for your situation.</p>
</div></section>'''
    return {"path":path,"hub":hub,"hub_name":hub_name,"title":title,"h1":h1,"desc":desc,"body":body,
            "article":True,"published":published,"reviewed":published}

DRAFTS = [
article("/bookkeeping/do-your-own-bookkeeping/","/bookkeeping/","Bookkeeping",
 "How to Do Your Own Bookkeeping When You're Self-Employed",
 "How to do your own bookkeeping when you&rsquo;re self-employed",
 "A step-by-step bookkeeping routine for freelancers and owner-operators: separate accounts, simple categories, monthly reconciling, receipts and tax set-asides.",
 "2026-10-26",
 "Bookkeeping for a one-person business comes down to eight habits. Set them up once, spend about an hour a month, and your books will be ready when tax time comes.",
 '''<h2>1. Open a separate business account</h2>
<p>Use one checking account and, if you need one, one credit card for business only. You don&rsquo;t need an LLC to do this; a second personal account used only for business works. Mixing business and personal spending is the most common reason books take hours to fix later.</p>
<p>If you&rsquo;ve already mixed them, don&rsquo;t try to untangle years of history. Pick a start date, move to separate accounts from that date, and clean up only the current tax year.</p>

<h2>2. Choose where your books live</h2>
<p>A spreadsheet works if you have fewer than about 50 transactions a month and one or two accounts. Beyond that, bookkeeping software that imports your bank transactions saves time and mistakes. What matters most is using one system and keeping it up to date.</p>

<h2>3. Set up categories that match your tax form</h2>
<p>Sole proprietors and single-member LLCs report business income and expenses on Schedule C. Use its expense lines as your categories, such as advertising, car and truck expenses, contract labor, insurance, office expense, supplies, travel, meals and utilities. Your books then line up with your tax return almost line for line.</p>
<p>Add two categories that aren&rsquo;t expenses: <b>owner draws</b> (money you move to yourself) and <b>owner contributions</b> (personal money you put into the business). Neither is a deduction or income, and getting them right keeps your profit accurate.</p>

<h2>4. Record transactions every week</h2>
<p>Once a week, categorize every new transaction. It takes about 15 minutes when it&rsquo;s a habit. Write a short note on anything unusual, such as who a payment was for or what a large purchase was, because you won&rsquo;t remember in April.</p>

<h2>5. Keep your receipts</h2>
<p>Keep a digital copy of receipts, invoices, 1099s and bank statements. Phone photos saved to one folder per year are enough. The IRS generally expects you to keep records for 3 years after you file, 6 years if you leave out more than 25% of your income, and 7 years if you claim a bad debt or a worthless securities loss. Keep employment tax records at least 4 years.</p>

<h2>6. Reconcile every account each month</h2>
<p>Reconciling means checking that your books match your bank and card statements. At the end of each month, compare the ending balance in your books with the statement. If they don&rsquo;t match, look for missing, duplicate or mistyped transactions. A month that reconciles is a month you can trust.</p>

<h2>7. Look at your profit and set aside tax</h2>
<p>After you reconcile, check your profit for the month: income minus expenses. Self-employment tax alone is 15.3% on most of your net earnings, before federal and California income tax. Many owners move a fixed percentage of each payment into a separate savings account so the money is there when estimated taxes are due. See our <a href="/estimated-taxes/quarterly-estimated-taxes-california/">guide to quarterly estimated taxes</a>.</p>

<div class="callout"><b>California note.</b> If you sell physical products in California, you generally need a seller&rsquo;s permit from the California Department of Tax and Fee Administration (CDTFA) and must track sales tax separately from your income. Sales tax you collect isn&rsquo;t your income.</div>

<h2>8. Close the year in January</h2>
<p>In January, reconcile December, make sure every transaction has a category, and list anyone you paid as a contractor. Starting with payments made in 2026, you generally need to send a Form 1099-NEC to contractors you paid $2,000 or more during the year, up from $600. Then run a profit and loss report for the full year. That report is the starting point for your Schedule C.</p>

<h2>A monthly routine that fits in an hour</h2>
<ul>
<li><b>Weekly (15 minutes):</b> categorize new transactions and save receipts.</li>
<li><b>Monthly (30 minutes):</b> reconcile each account, review profit, move money for taxes.</li>
<li><b>Quarterly:</b> make estimated tax payments.</li>
<li><b>Yearly:</b> close the books, send 1099s, prepare your return.</li>
</ul>''',
 'If your books are already behind, or you&rsquo;d rather not spend the hour, <a href="CTAURL">Computatio</a> keeps your books current for $500 a month, with a person reviewing every account.',
 [("IRS: How long should I keep records?","https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records"),
  ("IRS: About Schedule C (Form 1040)","https://www.irs.gov/forms-pubs/about-schedule-c-form-1040"),
  ("Littler: 1099 reporting thresholds under the 2025 tax law","https://www.littler.com/news-analysis/asap/tax-bill-changes-1099-reporting-thresholds"),
  ("CDTFA: Seller's permit","https://www.cdtfa.ca.gov/taxes-and-fees/sutprograms.htm")],
 "do-your-own-bookkeeping"),

article("/estimated-taxes/quarterly-estimated-taxes-california/","/estimated-taxes/","Estimated taxes",
 "Quarterly Estimated Taxes in California: 2026 Guide",
 "Quarterly estimated taxes in California: a 2026 guide",
 "Who must pay estimated taxes in California, how much, the IRS and FTB due dates for 2026, the 30/40/0/30 schedule and safe harbor rules, with a worked example.",
 "2026-10-28",
 "When you&rsquo;re self-employed, no one withholds tax from your income, so you pay it during the year in installments. California and the IRS both expect payments, but on different schedules.",
 '''<h2>Do you need to pay estimated tax?</h2>
<p><b>Federal:</b> you generally must pay estimated tax if you expect to owe at least $1,000 for the year after withholding and refundable credits.</p>
<p><b>California:</b> the threshold is lower. You generally must pay if you expect to owe at least $500 ($250 if married or in a registered domestic partnership filing separately).</p>
<p>Your federal amount covers both income tax and self-employment tax. Self-employment tax is 15.3% (12.4% Social Security and 2.9% Medicare) on 92.35% of your net earnings. The Social Security part applies only up to the 2026 wage base of $184,500.</p>

<h2>2026 due dates</h2>
<table class="tbl"><tr><th>Payment</th><th>IRS</th><th>California (FTB)</th></tr>
<tr><td>1</td><td>April 15, 2026: 25%</td><td>April 15, 2026: 30%</td></tr>
<tr><td>2</td><td>June 15, 2026: 25%</td><td>June 15, 2026: 40%</td></tr>
<tr><td>3</td><td>September 15, 2026: 25%</td><td>September 15, 2026: 0%</td></tr>
<tr><td>4</td><td>January 15, 2027: 25%</td><td>January 15, 2027: 30%</td></tr></table>
<p>California front-loads its payments: 70% of the year&rsquo;s estimate is due by June 15, and nothing is due in September.</p>

<h2>How much to pay: the safe harbor rules</h2>
<p>You avoid an underpayment penalty if your payments (plus any withholding) cover the smaller of:</p>
<ul>
<li>90% of this year&rsquo;s tax, or</li>
<li>100% of last year&rsquo;s tax, or 110% if last year&rsquo;s adjusted gross income was over $150,000 ($75,000 if married filing separately).</li>
</ul>
<p>California uses the same 90% / 100% / 110% tests, with one addition: if your California adjusted gross income this year is $1,000,000 or more ($500,000 if married or RDP filing separately), you must base payments on 90% of this year&rsquo;s tax.</p>
<p>Using last year&rsquo;s tax is the simplest method for most people. It works even if your income grows, as long as you pay on time.</p>

<h2>Worked example (hypothetical)</h2>
<p>Ana is a freelance designer in San Diego. Her 2025 adjusted gross income was under $150,000. Her 2025 returns showed $12,000 total federal tax and $3,000 California tax.</p>
<ul>
<li><b>Federal:</b> 100% of $12,000, split into four payments of $3,000.</li>
<li><b>California:</b> 100% of $3,000 on the 30/40/0/30 schedule: $900 on April 15, $1,200 on June 15, nothing on September 15, $900 on January 15, 2027.</li>
</ul>
<p>If Ana&rsquo;s 2026 income is much higher, she&rsquo;ll still owe the difference when she files, but she won&rsquo;t owe an underpayment penalty.</p>

<h2>How to pay</h2>
<ul>
<li><b>IRS:</b> IRS Direct Pay from your bank account at no cost, or the Electronic Federal Tax Payment System (EFTPS). Choose &ldquo;estimated tax&rdquo; and the 2026 tax year.</li>
<li><b>California:</b> FTB Web Pay from your bank account at no cost. Paper payments use Form 540-ES vouchers.</li>
</ul>
<p>Keep the confirmation numbers. You&rsquo;ll enter the payments on your 2026 returns.</p>

<div class="callout"><b>Next payment:</b> the fourth 2026 payment for both the IRS and California is due January 15, 2027.</div>

<h2>If you missed a payment</h2>
<p>Pay as soon as you can. The underpayment penalty works like interest and grows with each day the payment is late, so a late payment costs less than no payment.</p>''',
 'Monthly Books from <a href="CTAURL">Computatio</a> includes a quarterly estimate check, so you know what to pay before each deadline. $500 a month.',
 [("IRS: Estimated tax FAQ","https://www.irs.gov/faqs/estimated-tax"),
  ("FTB: Estimated tax payments","https://www.ftb.ca.gov/pay/estimated-tax-payments.html"),
  ("IRS: Self-employment tax","https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes"),
  ("Social Security wage base for 2026","https://www.maximizemysocialsecurity.com/blog/social-security-wage-base-changes-for-2026")],
 "quarterly-estimated-taxes-california"),

article("/business-structure/s-corp-vs-sole-proprietor-california/","/business-structure/","Business structure",
 "S Corp vs Sole Proprietor in California: When to Switch",
 "S-corp vs. sole proprietor in California: when the switch pays off",
 "How an S-corp can lower self-employment tax, what it costs in California (1.5% tax, $800 minimum, payroll), and a worked example to see where the break-even is.",
 "2026-10-30",
 "An S-corp can lower your self-employment tax, but in California it also adds costs. Whether it pays off depends on your profit, the salary you pay yourself, and what the extra paperwork costs you.",
 '''<h2>How each one is taxed</h2>
<p><b>Sole proprietor</b> (including a single-member LLC taxed the default way): all of your net profit is subject to self-employment tax of 15.3% on 92.35% of net earnings (the Social Security part only up to $184,500 in 2026), plus income tax.</p>
<p><b>S-corp</b>: you&rsquo;re an employee of your own company. You pay yourself a salary, and Social Security and Medicare taxes apply to that salary through payroll. Profit you take out beyond the salary, as distributions, isn&rsquo;t subject to those taxes. That difference is where the savings come from.</p>

<h2>What an S-corp costs in California</h2>
<ul>
<li><b>California S-corp tax:</b> 1.5% of the company&rsquo;s California net income, with an $800 minimum each year.</li>
<li><b>Payroll:</b> you have to run payroll for yourself, file payroll returns and pay California payroll taxes through the Employment Development Department (EDD). Most owners pay a payroll service.</li>
<li><b>A separate business tax return:</b> federal Form 1120-S and California Form 100S, usually prepared for a fee.</li>
<li><b>Bookkeeping:</b> an S-corp needs clean, reconciled books. You can&rsquo;t mix personal and business money.</li>
</ul>
<div class="callout"><b>California note.</b> A newly formed corporation&rsquo;s first-year $800 minimum tax is generally waived, though first-year income is still taxed at 1.5%. California LLCs owe their own $800 annual tax from the first year. If you&rsquo;re forming an LLC and electing S-corp status, check with the FTB which rules apply to you.</div>

<h2>The reasonable salary rule</h2>
<p>The IRS requires S-corp owners who work in the business to pay themselves a reasonable salary for the work they do before taking distributions. Setting your salary very low to avoid payroll tax is a common audit issue. A reasonable salary is roughly what you&rsquo;d have to pay someone else to do your job.</p>

<h2>Worked example (hypothetical, simplified)</h2>
<p>Jordan, a consultant, has $100,000 of net profit and pays himself a $55,000 salary as an S-corp.</p>
<table class="tbl"><tr><th></th><th>Sole proprietor</th><th>S-corp</th></tr>
<tr><td>Self-employment or payroll tax</td><td>About $14,130 (15.3% &times; 92.35% &times; $100,000)</td><td>About $8,415 (15.3% &times; $55,000)</td></tr>
<tr><td>California S-corp tax</td><td>None</td><td>$800 (1.5% of remaining profit is less than the minimum)</td></tr>
<tr><td>Payroll service and extra tax return</td><td>None</td><td>Varies: get quotes</td></tr></table>
<p>After the $800 California tax, Jordan saves about $4,900 in Social Security and Medicare taxes ($14,130 &minus; $8,415 &minus; $800). Payroll fees, the business return, California payroll taxes and his time reduce that. The example also ignores income tax effects, such as the qualified business income deduction, which can change the result. Run your own numbers, or have them run, before you switch.</p>

<h2>A rough rule of thumb</h2>
<p>If your profit is modest, the fixed costs usually eat the savings. The switch tends to make sense once profit is well above what a reasonable salary for your work would be, and steady enough that you&rsquo;ll keep up with payroll every month.</p>

<h2>How to switch</h2>
<ol>
<li>Form a corporation or LLC with the California Secretary of State, if you haven&rsquo;t already.</li>
<li>File IRS Form 2553 to elect S-corp status, generally within 2 months and 15 days of the start of the tax year you want it to apply.</li>
<li>Set up payroll and register with the EDD as an employer.</li>
<li>Open a business bank account and keep the books separate from day one.</li>
</ol>''',
 'Thinking about an S-corp? <a href="CTAURL">Book a free 20-minute call with Computatio</a> to go through your own numbers. Owner-operator returns are quoted on the call.',
 [("FTB: S corporations","https://www.ftb.ca.gov/file/business/types/corporations/s-corporations.html"),
  ("IRS: S corporation compensation and medical insurance issues","https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues"),
  ("IRS: About Form 2553","https://www.irs.gov/forms-pubs/about-form-2553"),
  ("IRS: Self-employment tax","https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes"),
  ("LLC University: California AB 85 expired","https://www.llcuniversity.com/california-llc/annual-llc-tax-exemption-ab-85/")],
 "s-corp-vs-sole-proprietor-california"),
article("/ai-accounting/how-to-use-ai-for-bookkeeping/","/ai-accounting/","AI for Accounting",
 "How to Use AI for Bookkeeping (and Keep Your Books Accurate)",
 "How to use AI for bookkeeping, and keep your books accurate",
 "A practical, safe workflow for using AI tools to categorize transactions, read receipts and prepare for month-end and tax season, plus what AI still gets wrong.",
 "2026-10-26",
 "AI can do the slowest parts of bookkeeping in minutes: sorting transactions, reading receipts, drafting summaries. It also makes confident mistakes. Here&rsquo;s how to get the speed without the errors.",
 '''<h2>What AI is good at</h2>
<ul>
<li><b>Categorizing transactions</b> from the bank description, once you give it your category list and a few rules.</li>
<li><b>Reading receipts and invoices</b> and pulling out the date, vendor, amount and what was bought.</li>
<li><b>Spotting oddities</b> such as duplicate charges, a subscription that doubled, or a payment with no matching invoice.</li>
<li><b>Explaining your reports</b> in plain English, such as why profit dropped this month.</li>
<li><b>Drafting routine writing</b> like invoice reminders and notes for your tax preparer.</li>
</ul>

<h2>What AI gets wrong</h2>
<ul>
<li><b>It can&rsquo;t know your context.</b> A charge at a warehouse store might be office supplies or groceries. Only you know.</li>
<li><b>It states tax rules confidently, even when they&rsquo;re outdated or wrong.</b> Rates, thresholds and deadlines change every year. Check any rule against an IRS or FTB page.</li>
<li><b>It can slip on arithmetic</b> across long tables. Totals should come from your bookkeeping software or spreadsheet, not from a chat answer.</li>
<li><b>It doesn&rsquo;t reconcile.</b> Matching your books to your bank statement is still your job, or your bookkeeper&rsquo;s.</li>
</ul>

<h2>A safe workflow for categorizing with AI</h2>
<ol>
<li><b>Export</b> last month&rsquo;s transactions from your bank or bookkeeping software as a spreadsheet file.</li>
<li><b>Remove sensitive details</b> such as full account numbers before you paste or upload anything.</li>
<li><b>Give it your categories.</b> Use the expense lines from Schedule C plus &ldquo;owner draw&rdquo; and &ldquo;owner contribution.&rdquo; Our <a href="/bookkeeping/do-your-own-bookkeeping/">bookkeeping guide</a> explains why.</li>
<li><b>Ask for a reason and a confidence level</b> for each category, using the prompt below.</li>
<li><b>Review</b> every low-confidence item and anything over an amount you choose, such as $200.</li>
<li><b>Reconcile</b> the month against your bank statement in your bookkeeping system. If the totals don&rsquo;t match, the categories don&rsquo;t matter yet.</li>
<li><b>Keep the receipts.</b> AI summaries don&rsquo;t replace the records the IRS expects you to keep.</li>
</ol>

<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;You are helping me categorize transactions for a self-employed business. Use only these categories: [paste your list]. Rules: [for example, &lsquo;Shell, Chevron = car and truck expenses&rsquo;; &lsquo;transfers to savings = owner draw&rsquo;]. For each transaction, return the date, description, amount, category, a confidence level (high, medium or low) and a one-line reason. Mark anything that could be personal as low confidence. Don&rsquo;t total anything.&rdquo;</div>

<h2>Keep your data safe</h2>
<ul>
<li>Never paste Social Security numbers, full bank or card numbers, or passwords into an AI chat.</li>
<li>Check the tool&rsquo;s data settings, including whether your inputs can be used to train its models, and turn that off where you can.</li>
<li>If you handle other people&rsquo;s financial information, such as clients or employees, use a business plan with a clear data agreement, or leave that data out.</li>
</ul>

<h2>You&rsquo;re still responsible for the result</h2>
<p>The IRS holds taxpayers responsible for what&rsquo;s on their return, whoever, or whatever, prepared it. Treat AI like a fast assistant whose work you check, not a replacement for checking.</p>

<h2>A realistic monthly routine with AI</h2>
<ul>
<li><b>Weekly:</b> snap receipts and let AI extract the details.</li>
<li><b>Month-end:</b> run the categorizing prompt, review the flagged items, then reconcile.</li>
<li><b>Quarterly:</b> ask AI to summarize the quarter&rsquo;s profit, then check the numbers against your profit and loss report before you make <a href="/estimated-taxes/quarterly-estimated-taxes-california/">estimated tax payments</a>.</li>
</ul>''',
 'This is how <a href="CTAURL">Computatio</a> works: AI does the sorting and reconciling, and a person reviews and signs off on every account. Monthly Books is $500 a month.',
 [("IRS Fact Sheet FS-14-11: Choosing a tax return preparer","https://www.irs.gov/pub/irs-news/FS-14-11.pdf"),
  ("IRS: How long should I keep records?","https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records"),
  ("IRS: About Schedule C (Form 1040)","https://www.irs.gov/forms-pubs/about-schedule-c-form-1040")],
 "how-to-use-ai-for-bookkeeping"),
]
