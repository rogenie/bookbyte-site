# All guides. build.py publishes an article only when its "published" date (Pacific time) has arrived.
# Scheduled runs append new article(...) entries to ARTICLES. See _src/PUBLISHING.md.
CTA = "https://computatio.io/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign="
from urllib.parse import quote
from html import unescape

def share_box(path, h1):
    """Share buttons for an article: LinkedIn, Facebook, X, email, copy link."""
    url = "https://bookbytellc.com" + path
    u = quote(url, safe="")
    t = quote(unescape(h1), safe="")
    links = [
        ("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={u}"),
        ("Facebook", f"https://www.facebook.com/sharer/sharer.php?u={u}"),
        ("X", f"https://twitter.com/intent/tweet?url={u}&amp;text={t}"),
        ("Email", f"mailto:?subject={t}&amp;body={u}"),
    ]
    a = "".join(f'<a href="{h}"{"" if n == "Email" else " target=\"_blank\" rel=\"noopener\""}>{n}</a>' for n, h in links)
    copy = (f'<button type="button" data-url="{url}" onclick="var b=this;navigator.clipboard.writeText(b.dataset.url)'
            f'.then(function(){{b.textContent=\'Link copied\'}},function(){{prompt(\'Copy this link:\',b.dataset.url)}})">Copy link</button>')
    return f'<div class="share" aria-label="Share this guide"><b>Share this guide:</b> {a}{copy}</div>'

def article(path, hub, hub_name, title, h1, desc, published, intro, sections, cta_html, sources, slug):
    src = "".join(f'<li><a href="{u}">{t}</a></li>' for t,u in sources)
    body = f'''<section class="hero small"><div class="wrap narrow">
<p class="eyebrow"><a href="{hub}" style="color:inherit;text-decoration:none">{hub_name}</a></p>
<h1>{h1}</h1>
<p class="lede">{intro}</p>
<p class="muted" style="color:#bbb">By: Computatio &middot; Last reviewed {published}</p>
</div></section>
<section><div class="wrap narrow prose">
{sections}
<div class="cta"><b>Short on time?</b> {cta_html.replace("CTAURL", CTA+slug)}</div>
{share_box(path, h1)}
<div class="callout"><b>Free download:</b> <a href="https://computatio.io/free-guide/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign={slug}">47 write-offs for the self-employed</a>, a 42-page guide with the IRS rules behind each deduction. Free when you join the Computatio newsletter.</div>
<h2>Sources</h2><ul>{src}</ul>
<p class="fine">This guide is general information, not financial, tax or legal advice for your situation. We work hard to get it right, but we can make mistakes, and rules change. Check the official sources above before you act.</p>
</div></section>'''
    return {"path":path,"hub":hub,"hub_name":hub_name,"title":title,"h1":h1,"desc":desc,"body":body,
            "article":True,"published":published,"reviewed":published}

ARTICLES = [
article("/bookkeeping/do-your-own-bookkeeping/","/bookkeeping/","Bookkeeping",
 "How to Do Your Own Bookkeeping When You're Self-Employed",
 "How to do your own bookkeeping when you&rsquo;re self-employed",
 "A step-by-step bookkeeping routine for freelancers and owner-operators: separate accounts, simple categories, monthly reconciling, receipts and tax set-asides.",
 "2026-11-16",
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
 'If your books are already behind, or you&rsquo;d rather not spend the hour, <a href="CTAURL">Computatio</a> keeps your books current for $500 a month, with an accountant reviewing every account.',
 [("IRS: How long should I keep records?","https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records"),
  ("IRS: About Schedule C (Form 1040)","https://www.irs.gov/forms-pubs/about-schedule-c-form-1040"),
  ("Littler: 1099 reporting thresholds under the 2025 tax law","https://www.littler.com/news-analysis/asap/tax-bill-changes-1099-reporting-thresholds"),
  ("CDTFA: Seller's permit","https://www.cdtfa.ca.gov/taxes-and-fees/sutprograms.htm")],
 "do-your-own-bookkeeping"),

article("/estimated-taxes/quarterly-estimated-taxes-california/","/estimated-taxes/","Estimated taxes",
 "Quarterly Estimated Taxes in California: 2026 Guide",
 "Quarterly estimated taxes in California: a 2026 guide",
 "Who must pay California estimated tax, IRS and FTB due dates for 2026, the 30/40/0/30 schedule and safe harbor rules, with a worked example.",
 "2026-10-23",
 "You&rsquo;re self-employed in California. Nobody withholds tax from your income, so you&rsquo;re supposed to pay it yourself during the year. But how much? When? And to whom: the IRS, the state, or both?",
 '''<div class="callout"><b>Quick answer:</b> if you expect to owe at least <b>$1,000</b> to the IRS or <b>$500</b> to California for 2026, you generally must pay estimated tax. The IRS takes four equal payments (April 15, June 15, September 15, January 15, 2027). California takes <b>30% in April, 40% in June, nothing in September and 30% in January</b>. Paying 100% of last year&rsquo;s tax on time (110% if last year&rsquo;s AGI was over $150,000) avoids the underpayment penalty.</div>

<h2>Two tax agencies, two different schedules</h2>
<p>Here&rsquo;s the first problem. The IRS and California&rsquo;s Franchise Tax Board (FTB) both want estimated payments, but not on the same plan.</p>
<table class="tbl"><tr><th>Payment</th><th>IRS</th><th>California (FTB)</th></tr>
<tr><td>1</td><td>April 15, 2026: 25%</td><td>April 15, 2026: 30%</td></tr>
<tr><td>2</td><td>June 15, 2026: 25%</td><td>June 15, 2026: 40%</td></tr>
<tr><td>3</td><td>September 15, 2026: 25%</td><td>September 15, 2026: 0%</td></tr>
<tr><td>4</td><td>January 15, 2027: 25%</td><td>January 15, 2027: 30%</td></tr></table>
<p><b>California wants 70% of the year&rsquo;s estimate by June 15, and nothing in September.</b> If you pay the state on the IRS schedule, you fall behind by June.</p>

<h2>And you don&rsquo;t know how much to pay</h2>
<p>The second problem: your income moves. A big client in March, a slow summer. You can&rsquo;t know this year&rsquo;s tax until the year is over, so any number feels like a guess.</p>
<p>The federal amount isn&rsquo;t just income tax, either. It also covers self-employment tax: <b>15.3%</b> (12.4% Social Security and 2.9% Medicare) on 92.35% of your net earnings. The Social Security part applies only up to the 2026 wage base of $184,500.</p>

<h2>What it costs to guess wrong</h2>
<ul>
<li><b>The penalty grows every day.</b> The federal underpayment penalty is figured separately for each due date, on the amount that was short and the number of days it stayed unpaid.</li>
<li><b>Catching up late doesn&rsquo;t erase it.</b> A later payment is applied first to the earliest unpaid installment, so a short April payment keeps costing you until it&rsquo;s covered.</li>
<li><b>The cash isn&rsquo;t there.</b> Guess low all year and you face one large bill in April, on top of the first payment for the new year.</li>
</ul>

<h2>Picture this instead</h2>
<p>Four dates on your calendar. A tax savings account that already holds the money when each one arrives. Payments sized by a rule, not a guess. <b>No underpayment penalty, even in a year your income jumps.</b> That&rsquo;s what the method below sets up.</p>

<h2>How much estimated tax to pay in California: the last-year method</h2>
<p>The safe harbor rules give you a way to pay without predicting the future. You avoid the underpayment penalty if your payments (plus any withholding) cover the smaller of:</p>
<ul>
<li>90% of this year&rsquo;s tax, or</li>
<li>100% of last year&rsquo;s tax, or 110% if last year&rsquo;s adjusted gross income was over $150,000 ($75,000 if married filing separately).</li>
</ul>
<p>California uses the same 90% / 100% / 110% tests, with one addition: if your California adjusted gross income this year is $1,000,000 or more ($500,000 if married or RDP filing separately), you must base payments on 90% of this year&rsquo;s tax.</p>
<p><b>California&rsquo;s threshold is lower:</b> you generally must pay if you expect to owe at least $500 ($250 if married or RDP filing separately). For the IRS it&rsquo;s $1,000.</p>

<h3>Step by step</h3>
<ol>
<li><b>Find last year&rsquo;s total tax</b> on your 2025 federal and California returns.</li>
<li><b>Multiply</b> by 100%, or 110% if your 2025 AGI was over $150,000.</li>
<li><b>Split it:</b> four equal payments for the IRS; 30/40/0/30 for California.</li>
<li><b>Put all four dates on your calendar</b> now.</li>
<li><b>Open a separate savings account for taxes</b> and move a fixed share of every client payment into it. Pick the share from last year&rsquo;s total tax divided by last year&rsquo;s income.</li>
<li><b>Once a month, <a href="/bookkeeping/do-your-own-bookkeeping/">update and reconcile your books</a></b> so you can see if this year is running far above last year.</li>
<li><b>Pay on time.</b> IRS Direct Pay or EFTPS for the IRS; FTB Web Pay for California, which lets you schedule a payment up to a year ahead. Paper payments use Form 540-ES vouchers. Keep every confirmation number.</li>
</ol>

<div class="callout"><b>Example (made-up data).</b> Ana is a freelance designer in San Diego. Her 2025 AGI was under $150,000, and her 2025 returns showed $12,000 total federal tax and $3,000 California tax.<br>
<b>Federal:</b> 100% of $12,000 = four payments of $3,000.<br>
<b>California:</b> 100% of $3,000 on the 30/40/0/30 schedule = $900 on April 15, $1,200 on June 15, nothing on September 15, $900 on January 15, 2027.<br>
If Ana earns much more in 2026, she&rsquo;ll owe the difference when she files, but no underpayment penalty.</div>

<div class="callout"><b>Next payment:</b> the fourth 2026 payment for both the IRS and California is due January 15, 2027. For the IRS only, you can skip it if you file your 2026 return by February 1, 2027 and pay the full balance with it.</div>

<h2>What if I miss a California or IRS estimated payment?</h2>
<p>Pay as soon as you can. Because the penalty is figured by the day, a late payment usually costs less than no payment. If most of your income came late in the year, the annualized income method on Form 2210 may lower or remove the federal penalty.</p>

<h2>What if my estimated payments keep growing?</h2>
<p>If your profit keeps climbing, look at how your business is set up. Some owners compare an S corporation with staying a sole proprietor. See <a href="/business-structure/s-corp-vs-sole-proprietor-california/">S-corp vs. sole proprietor</a>, or check your projection with <a href="/ai-accounting/estimate-quarterly-taxes-with-ai/">AI and a line-by-line math check</a>. More in our <a href="/estimated-taxes/">estimated tax guides</a>.</p>
<p>Or hand the whole thing off:</p>''',
 'Want your estimates figured for you before every deadline? <a href="CTAURL">Computatio</a> Monthly Books keeps your books current and includes a quarterly estimate check, so you know what to pay the IRS and California each time. $500 a month.',
 [("IRS: 2026 Form 1040-ES, Estimated Tax for Individuals","https://www.irs.gov/pub/irs-pdf/f1040es.pdf"),
  ("FTB: 2026 Instructions for Form 540-ES","https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html"),
  ("IRS: Self-employment tax (Social Security and Medicare taxes)","https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes"),
  ("SSA: Contribution and benefit base","https://www.ssa.gov/oact/cola/cbb.html"),
  ("IRS: Instructions for Form 2210","https://www.irs.gov/instructions/i2210")],
 "quarterly-estimated-taxes-california"),

article("/business-structure/s-corp-vs-sole-proprietor-california/","/business-structure/","Business structure",
 "S Corp vs Sole Proprietor in California: When to Switch",
 "S-corp vs. sole proprietor in California: when the switch pays off",
 "S-corp vs. sole proprietor in California: how an S-corp can cut self-employment tax, what it costs (1.5%, $800 minimum, payroll) and your break-even.",
 "2026-11-02",
 "Your profit went up, and so did the self-employment tax bill. Someone told you to &ldquo;just become an S-corp.&rdquo; Before you do, here is what changes, what it costs in California, and how to find your own break-even.",
 '''<div class="callout"><b>Quick answer:</b> as a sole proprietor, you pay <b>15.3% self-employment tax on 92.35% of your net profit</b>. As an S-corp owner, you pay Social Security and Medicare tax only on the <b>reasonable salary</b> you pay yourself, not on the rest of the profit. In California, an S-corp also owes <b>1.5% of its net income, with an $800 yearly minimum</b>, plus payroll and an extra tax return. The switch tends to pay off only when your profit is well above a fair salary for your work.</div>

<h2>Self-employment tax takes a big bite</h2>
<p>As a sole proprietor (or a single-member LLC taxed the default way), you pay self-employment tax on your profit. The rate is 15.3%: 12.4% for Social Security and 2.9% for Medicare. It applies to 92.35% of your net earnings.</p>
<p>The Social Security part stops at a yearly cap, $184,500 for 2026. Medicare has no cap. <b>Below the cap, almost every extra dollar of profit carries this tax, on top of income tax.</b></p>

<h2>S-corp vs. sole proprietor in California: the advice conflicts</h2>
<p>One person says an S-corp is a must. Another says it&rsquo;s a trap. Both can be right, because the answer depends on your numbers.</p>
<p>Here is the difference. In an S-corp, you&rsquo;re an employee of your own company. You pay yourself a salary through payroll, and Social Security and Medicare taxes apply to that salary. Profit you take out beyond the salary, as distributions, isn&rsquo;t subject to those taxes. <b>That gap is the whole reason people switch.</b></p>
<p>Outside California, the federal side works the same way, but state taxes and fees differ. Check your own state&rsquo;s rules.</p>

<h2>What an S-corp costs you in California</h2>
<ul>
<li><b>California S-corp tax:</b> 1.5% of the company&rsquo;s California net income, with an $800 minimum each year, even in a loss year.</li>
<li><b>Payroll:</b> you run payroll for yourself, withhold and pay payroll taxes, and file payroll reports. California requires you to register with the Employment Development Department (EDD) within 15 days of paying more than $100 in wages in a quarter. Most owners pay a payroll service.</li>
<li><b>An extra tax return:</b> federal Form 1120-S and California Form 100S each year, usually prepared for a fee.</li>
<li><b>Clean books:</b> an S-corp needs reconciled books and no mixing of personal and business money. See <a href="/ai-accounting/ai-bank-reconciliation/">how to reconcile your bank account</a>.</li>
</ul>
<div class="callout"><b>State note.</b> California waives the $800 minimum for a newly formed S corporation&rsquo;s first tax year, but first-year income is still taxed at 1.5%. California LLCs owe their own $800 annual tax starting in the first year; the temporary first-year exemption ended with tax years starting before 2024. If you plan to form an LLC and elect S-corp status, confirm with the Franchise Tax Board which rules apply to you.</div>

<h2>The salary rule can undo the plan</h2>
<p>The IRS says an S-corp must pay an owner who works in the business reasonable pay for that work before taking distributions. If the salary is too low, the IRS can treat distributions as wages and charge employment taxes on them.</p>
<p>The IRS looks at things like your training, your duties, the time you put in, and what similar businesses pay for similar work. <b>A fair test: what would you have to pay someone else to do your job?</b> If most of your profit comes from your own work, most of it may need to be salary, and the gap shrinks.</p>

<h2>Picture this instead</h2>
<p>You know your break-even number. You know the salary you&rsquo;d pay yourself and why it&rsquo;s defensible. You can see, line by line, what the S-corp would cost in fees, tax and time. You decide once, with your own figures, and stop second-guessing every time someone mentions it.</p>

<h2>When does an S-corp pay off? The break-even method</h2>
<p>You can do this with a calculator or any AI chat tool. You don&rsquo;t need to be technical. Use your real numbers from your books, not a guess.</p>
<ol>
<li><b>Get your net profit.</b> Use last year&rsquo;s Schedule C profit or a 12-month total from your books. If your books are behind, catch them up first; see <a href="/ai-accounting/how-to-use-ai-for-bookkeeping/">how to use AI for bookkeeping</a>.</li>
<li><b>Pick a reasonable salary.</b> Write down what it would cost to hire someone to do your work, and why.</li>
<li><b>Get quotes</b> for a payroll service and for the extra business return.</li>
<li><b>Run the comparison</b> with the prompt below.</li>
<li><b>Check the math yourself</b> with the formulas in the example.</li>
</ol>
<div class="callout"><b>Prompt to copy:</b> &ldquo;Compare two setups for a California business. Net profit: [amount]. Setup A, sole proprietor: self-employment tax = 15.3% &times; 92.35% &times; net profit. Setup B, S-corp: payroll tax = 15.3% &times; salary of [amount]; California S-corp tax = the greater of $800 or 1.5% of (net profit &minus; salary &minus; 7.65% of salary); plus payroll service [amount] and tax return fee [amount]. Show each line with its formula, then the difference. Don&rsquo;t estimate income tax or add any other taxes. List anything you assumed.&rdquo;</div>

<h3>Example (made-up data)</h3>
<p>Jordan is a made-up consultant with $100,000 of net profit. He would pay himself a $55,000 salary as an S-corp.</p>
<table class="tbl"><tr><th></th><th>Sole proprietor</th><th>S-corp</th></tr>
<tr><td>Self-employment or payroll tax</td><td>About $14,130 (15.3% &times; 92.35% &times; $100,000)</td><td>About $8,415 (15.3% &times; $55,000)</td></tr>
<tr><td>California S-corp tax</td><td>None</td><td>$800 (1.5% of about $40,800 is about $612, below the minimum)</td></tr>
<tr><td>Payroll service and extra return</td><td>None</td><td>Get quotes</td></tr></table>
<p>Before fees, the S-corp column is about $4,900 lower ($14,130 &minus; $8,415 &minus; $800). <b>Payroll fees, the business return, California payroll taxes and your time all come out of that.</b> The example also skips income tax effects, such as the deduction for half of self-employment tax and the qualified business income deduction, which can change the result.</p>

<h3>How to check the AI&rsquo;s answer</h3>
<ul>
<li>Redo each line with a calculator using the formulas above. AI tools still slip on arithmetic.</li>
<li>Make sure it used your salary, not a lower number it picked.</li>
<li>Delete any tax it added that you didn&rsquo;t ask for, and any it left out that applies to you.</li>
</ul>
<p><b>Limits:</b> this is a first screen, not a tax plan. It doesn&rsquo;t cover income tax, retirement contributions, health insurance or other states. If profit is modest or swings a lot, the fixed costs usually eat the gap. Keep paying <a href="/estimated-taxes/quarterly-estimated-taxes-california/">quarterly estimated taxes</a> on time either way; more in our <a href="/estimated-taxes/">estimated tax guides</a>.</p>

<h2>How to switch to an S-corp in California</h2>
<ol>
<li>Form a corporation or LLC with the California Secretary of State, if you haven&rsquo;t already.</li>
<li>File IRS Form 2553 to elect S-corp status. To count for a tax year, file it no more than 2 months and 15 days after that year begins (or any time in the year before). The IRS has relief for late elections in some cases.</li>
<li>Register with the EDD as an employer and set up payroll.</li>
<li>Open a business bank account and keep the books separate from day one. Our <a href="/bookkeeping/do-your-own-bookkeeping/">bookkeeping routine for the self-employed</a> shows how.</li>
</ol>
<p>If you&rsquo;d rather not run these numbers alone, the box below is the shortcut.</p>''',
 'Thinking about an S-corp? <a href="CTAURL">Book a free 20-minute call with Computatio</a> to go through your own numbers. Owner-operator returns are quoted on the call.',
 [("FTB: S corporations","https://www.ftb.ca.gov/file/business/types/corporations/s-corporations.html"),
  ("FTB: Limited liability company","https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html"),
  ("IRS: S corporation compensation and medical insurance issues","https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues"),
  ("IRS: Instructions for Form 2553","https://www.irs.gov/instructions/i2553"),
  ("IRS: Topic no. 554, Self-employment tax","https://www.irs.gov/taxtopics/tc554")],
 "s-corp-vs-sole-proprietor-california"),
article("/ai-accounting/how-to-use-ai-for-bookkeeping/","/ai-accounting/","AI for Accounting",
 "How to Use AI for Bookkeeping and Keep Your Books Accurate",
 "How to use AI for bookkeeping, and keep your books accurate",
 "Use AI for bookkeeping without wrong numbers: a 3-pass method to categorize transactions, read receipts and close the month, with a prompt to copy.",
 "2026-10-21",
 "It&rsquo;s the end of the month. Your bank feed has a pile of transactions waiting, your receipts are scattered across your phone and your inbox, and you still don&rsquo;t know if the business made money. You&rsquo;ve heard AI can do bookkeeping now. You just don&rsquo;t trust it with your numbers.",
 '''<div class="callout"><b>Quick answer:</b> use AI for bookkeeping to <b>sort transactions, read receipts and explain your reports</b>, but never to replace reconciling or keeping records. Give it your category list, make it show a reason and a confidence level for every line, review the low-confidence ones yourself, then reconcile to your bank statement. That&rsquo;s the 3-pass method below.</div>

<h2>You&rsquo;re spending hours on bookkeeping that should take minutes</h2>
<p>Most of bookkeeping is sorting. Which category does this charge go in? Is this receipt a business expense? Did I already record this one?</p>
<p>Done by hand, every line is a small decision. A few hundred small decisions is a whole evening, every month. <b>That&rsquo;s the first problem: the work is slow, so it gets put off.</b></p>

<h2>And when you try AI, you don&rsquo;t know if it&rsquo;s right</h2>
<p>So you paste your transactions into a chatbot. It answers instantly, with total confidence. Then you notice it called a grocery run &ldquo;office supplies&rdquo; and added up a column wrong.</p>
<p><b>That&rsquo;s the second problem: AI is fast, but it doesn&rsquo;t know your business, and it never says &ldquo;I&rsquo;m not sure.&rdquo;</b></p>

<h2>What bad bookkeeping costs you</h2>
<p>Put the two problems together and you get the worst of both: books that are late <i>and</i> wrong.</p>
<ul>
<li><b>Wrong categories become wrong tax numbers.</b> Your Schedule C is built from these categories. A personal charge filed as a business expense is a deduction you can&rsquo;t support.</li>
<li><b>You&rsquo;re responsible either way.</b> The IRS holds you responsible for what&rsquo;s on your return, whoever, or whatever, prepared it.</li>
<li><b>Missing records can&rsquo;t be fixed later.</b> If a deduction is questioned, you need the receipt or invoice behind it, not an AI summary of it.</li>
<li><b>You fly blind.</b> If the books are months behind, you can&rsquo;t see profit, can&rsquo;t plan <a href="/estimated-taxes/quarterly-estimated-taxes-california/">estimated tax payments</a>, and find out about problems at tax time.</li>
</ul>

<h2>Picture your books done in under an hour a month</h2>
<p>Now imagine month-end looks like this. AI sorts every transaction and tells you which ones it isn&rsquo;t sure about. You check a short list, not the whole pile. Your books match your bank to the penny. Receipts are saved where you can find them.</p>
<p><b>You know your profit for the month, and you trust the number.</b> That&rsquo;s the goal: AI&rsquo;s speed with a person&rsquo;s judgment.</p>

<h2>How to use AI for bookkeeping: the 3-pass method</h2>
<p>The method has three passes. AI does the first, you do the second, and the third is the check that makes the books trustworthy.</p>

<h3>Pass 1: let AI sort</h3>
<ol>
<li><b>Export</b> last month&rsquo;s transactions from your bank or bookkeeping software as a spreadsheet file.</li>
<li><b>Remove sensitive details</b> such as full account numbers before you paste or upload anything.</li>
<li><b>Give it your categories.</b> Use the expense lines from Schedule C plus &ldquo;owner draw&rdquo; and &ldquo;owner contribution.&rdquo; Our <a href="/bookkeeping/do-your-own-bookkeeping/">bookkeeping guide</a> explains why.</li>
<li><b>Run the prompt below.</b> It forces a reason and a confidence level for every line.</li>
</ol>

<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;You are helping me categorize transactions for a self-employed business. Use only these categories: [paste your list]. Rules: [for example, &lsquo;Shell, Chevron = car and truck expenses&rsquo;; &lsquo;transfers to savings = owner draw&rsquo;]. For each transaction, return the date, description, amount, category, a confidence level (high, medium or low) and a one-line reason. Mark anything that could be personal as low confidence. Don&rsquo;t total anything.&rdquo;</div>

<h3>Pass 2: you review the short list</h3>
<ol start="5">
<li><b>Review</b> every low-confidence line and anything over an amount you choose, such as $200. Accept the rest.</li>
<li><b>Match receipts</b> to the lines you reviewed, and save them. AI summaries don&rsquo;t replace the records the IRS expects you to keep.</li>
</ol>

<div class="callout"><b>Example (made-up data).</b> Three lines a run of the prompt might return:<br>
Oct 3 &middot; ADOBE *CREATIVE CLD &middot; $59.99 &rarr; Office expense &middot; high &middot; &ldquo;Recurring software subscription.&rdquo;<br>
Oct 9 &middot; COSTCO WHSE #0412 &middot; $214.37 &rarr; Supplies &middot; low &middot; &ldquo;Warehouse store; could be personal groceries.&rdquo;<br>
Oct 15 &middot; TRANSFER TO SAV 4471 &middot; $1,500.00 &rarr; Owner draw &middot; medium &middot; &ldquo;Transfer to savings; could be a tax set-aside.&rdquo;<br>
<b>How to check it:</b> open the Costco receipt before accepting the category, confirm the transfer went to your own account, and make sure every line appears exactly once compared with your bank export.</div>

<h3>Pass 3: reconcile</h3>
<ol start="7">
<li><b>Reconcile</b> the month against your bank statement in your bookkeeping software. <b>If the totals don&rsquo;t match, the categories don&rsquo;t matter yet.</b> Totals come from your software or spreadsheet, never from a chat answer.</li>
</ol>

<h2>Is it safe to use AI with your financial data?</h2>
<p>It can be, if you set it up right:</p>
<ul>
<li>Never paste Social Security numbers, full bank or card numbers, or passwords into an AI chat.</li>
<li>Check the tool&rsquo;s data settings, including whether your inputs can be used to train its models, and turn that off where you can.</li>
<li>If you handle other people&rsquo;s financial information, such as clients or employees, use a business plan with a clear data agreement, or leave that data out.</li>
</ul>

<h2>What if the AI gets it wrong?</h2>
<p>It will, sometimes. That&rsquo;s why the method never lets AI have the last word. It can&rsquo;t know your context, it can state outdated tax rules confidently, and it can slip on arithmetic across long tables. Check any tax rule against an IRS or state tax agency page, and let reconciliation catch the rest.</p>

<h2>Your monthly AI bookkeeping routine</h2>
<ul>
<li><b>Weekly:</b> snap receipts and let AI pull out the date, vendor and amount.</li>
<li><b>Month-end:</b> run the 3 passes: sort, review, reconcile.</li>
<li><b>Quarterly:</b> ask AI to summarize the quarter&rsquo;s profit, then check it against your profit and loss report before you pay estimated taxes.</li>
</ul>
<p>More methods like this are in our <a href="/ai-accounting/">AI for Accounting guides</a>. Or skip the routine entirely:</p>''',
 'Want the 3-pass method done for you every month? At <a href="CTAURL">Computatio</a>, AI does the sorting and an accountant reviews and reconciles every account, so your books are current and checked. Monthly Books is $500 a month.',
 [("IRS: Choosing a reputable tax preparer is vital to tax security","https://www.irs.gov/newsroom/choosing-a-reputable-tax-preparer-is-vital-to-tax-security"),
  ("IRS: What kind of records should I keep","https://www.irs.gov/businesses/small-businesses-self-employed/what-kind-of-records-should-i-keep"),
  ("IRS: Instructions for Schedule C (Form 1040)","https://www.irs.gov/instructions/i1040sc"),
  ("IRS: About Schedule C (Form 1040)","https://www.irs.gov/forms-pubs/about-schedule-c-form-1040")],
 "how-to-use-ai-for-bookkeeping"),
article("/ai-accounting/ai-prompts-categorize-transactions/","/ai-accounting/","AI for Accounting",
 "AI Prompts to Categorize Business Transactions",
 "AI prompts to categorize business transactions (copy-paste)",
 "Copy-and-paste AI prompts to categorize business transactions into Schedule C lines, flag personal charges and catch mistakes before they hit your books.",
 "2026-10-26",
 "You opened ChatGPT, pasted in your bank transactions and typed &ldquo;categorize these.&rdquo; What came back looked tidy. But half the categories were made up, and you can&rsquo;t tell which half.",
 '''<div class="callout"><b>Quick answer:</b> the best AI prompts to categorize business transactions do four things. They <b>give the AI your exact category list</b> (for a sole proprietor, the Schedule C expense lines), state your own vendor rules, demand a confidence level and a reason for each line, and ban the AI from doing totals. Copy the five prompts below, run them in order, and review only what they flag.</div>

<h2>Your AI invents categories you never use</h2>
<p>Ask an AI to &ldquo;categorize&rdquo; with no list and it makes one up. You get &ldquo;Technology,&rdquo; &ldquo;Food &amp; Dining&rdquo; and &ldquo;Miscellaneous.&rdquo; None of those match the lines on your tax form.</p>
<p><b>A category that doesn&rsquo;t map to your return is just a second sorting job for later.</b></p>

<h2>And you don&rsquo;t know which answers to trust</h2>
<p>Every line comes back with the same calm confidence. The coffee shop, the hardware store, the transfer to savings. Nothing says &ldquo;I guessed on this one.&rdquo;</p>
<p>So you either check every line, which defeats the point, or check none, which is worse.</p>

<h2>What sloppy categorizing costs you</h2>
<ul>
<li><b>Wrong lines on your return.</b> Schedule C has fixed expense lines, from line 8 (Advertising) to line 27b (Other expenses). Your categories should land on them.</li>
<li><b>Meals at the wrong amount.</b> Business meals are generally only 50% deductible, so they need their own category, not a spot inside &ldquo;Supplies.&rdquo;</li>
<li><b>Personal charges posing as business ones.</b> An expense must be ordinary and necessary for your business. If a car or phone is used for both, you split the cost by business use.</li>
<li><b>Paying yourself recorded as an expense.</b> Amounts you pay yourself are not wages on Schedule C. They&rsquo;re owner draws.</li>
<li><b>A bank line isn&rsquo;t proof.</b> The IRS says proof of payment alone doesn&rsquo;t show you&rsquo;re entitled to a deduction. You still need the invoice or receipt.</li>
</ul>

<h2>Picture month-end with a 10-line review list</h2>
<p>You export the month. You paste one prompt. Back comes every transaction on a real Schedule C line, each with a reason. A short list is marked &ldquo;check this.&rdquo; You look at those, pull a few receipts, and reconcile.</p>
<p><b>You review the 10 lines that need you, not the 200 that don&rsquo;t.</b></p>

<h2>The copy-and-paste prompt library for categorizing transactions</h2>
<p>Run these five prompts in order, in the same chat. They work in ChatGPT, Claude, Gemini or Copilot. Before you start, export the month as a spreadsheet and <b>delete full account and card numbers</b>. Our <a href="/ai-accounting/financial-data-safety-ai/">data safety guide</a> covers the rest.</p>

<h3>Prompt 1: set the rules</h3>
<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;You will categorize transactions for my sole proprietorship. Use only these categories: Advertising; Car and truck expenses; Commissions and fees; Contract labor; Insurance (other than health); Interest; Legal and professional services; Office expense; Rent or lease; Repairs and maintenance; Supplies; Taxes and licenses; Travel; Meals; Utilities; Other expenses (name it); Owner draw; Owner contribution; Transfer between my accounts; Income; Needs review. Never invent a new category. If unsure, use Needs review. Reply &lsquo;ready&rsquo; and wait.&rdquo;</div>
<p>Using a business entity, or have your own chart of accounts? Paste that list instead. Our <a href="/ai-accounting/chart-of-accounts-with-ai/">chart of accounts guide</a> shows how to build one.</p>

<h3>Prompt 2: teach it your vendors</h3>
<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;Apply these rules before anything else: [vendor = category, for example &lsquo;GUSTO = Contract labor&rsquo;, &lsquo;transfers to account ending 4471 = Owner draw&rsquo;]. These are fixed. Mark lines you matched by a rule as &lsquo;rule.&rsquo;&rdquo;</div>

<h3>Prompt 3: categorize with a confidence level</h3>
<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;Categorize the transactions below. Return a table: date, description, amount, category, confidence (high, medium, low), one-line reason. Mark as low anything that could be personal, any warehouse, grocery or big-box store, any restaurant, any payment to a person, and any transfer. Keep every row, in the same order. Don&rsquo;t add, merge or total anything. [paste transactions]&rdquo;</div>

<h3>Prompt 4: hunt for problems</h3>
<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;Now list only the rows that may be wrong: possible personal spending, possible duplicates (same amount and vendor within 5 days), refunds coded as expenses, deposits that may not be income (loans, transfers, owner contributions), and anything in Other expenses. Say why for each.&rdquo;</div>

<h3>Prompt 5: build your rules for next month</h3>
<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;From the rows I approved, write a list of vendor rules in the form &lsquo;vendor = category&rsquo;. Only include vendors that are always the same category. I&rsquo;ll paste this list into Prompt 2 next month.&rdquo;</div>
<p><b>Prompt 5 is what makes this faster every month:</b> your rule list grows, and the review list shrinks.</p>

<div class="callout"><b>Example (made-up data).</b> Four lines a run of Prompt 3 might return:<br>
Oct 2 &middot; GOOGLE *WORKSPACE &middot; $14.00 &rarr; Office expense &middot; high &middot; &ldquo;Monthly business software.&rdquo;<br>
Oct 8 &middot; HOME DEPOT #6621 &middot; $187.42 &rarr; Supplies &middot; low &middot; &ldquo;Big-box store; could be home repair.&rdquo;<br>
Oct 14 &middot; BLUE BOTTLE COFFEE &middot; $23.50 &rarr; Meals &middot; low &middot; &ldquo;Restaurant; business purpose unknown.&rdquo;<br>
Oct 20 &middot; ZELLE TO M RIVERA &middot; $600.00 &rarr; Needs review &middot; low &middot; &ldquo;Payment to a person; could be contract labor.&rdquo;<br>
<b>How to check it:</b> open the Home Depot receipt, write down who you met and why for the coffee, and confirm the Zelle payment against an invoice. Then count rows: the AI&rsquo;s table should have exactly as many rows as your export.</div>

<h2>How do you check AI&rsquo;s transaction categories?</h2>
<ol>
<li><b>Count the rows.</b> Same number in, same number out. A missing row is a missing expense.</li>
<li><b>Review every low and medium line,</b> plus anything over an amount you pick, such as $200.</li>
<li><b>Match receipts</b> for the lines you reviewed, and keep them. The IRS generally expects records for 3 years after you file, and longer in some cases.</li>
<li><b>Post the categories in your bookkeeping software or spreadsheet,</b> then <a href="/ai-accounting/ai-bank-reconciliation/">reconcile to your bank statement</a>. <b>Totals come from your software, never from the chat.</b></li>
</ol>

<h2>What these prompts can&rsquo;t do</h2>
<p>AI can&rsquo;t know why you bought something. It can&rsquo;t tell a client lunch from a personal one, or a work tool from a gift. It can also state a tax rule that is out of date. Treat its reason as a guess, and check tax rules on an IRS or state tax agency page. You&rsquo;re responsible for your return whoever, or whatever, sorted the numbers.</p>
<p>Not technical? You don&rsquo;t need to be. If you can copy a spreadsheet and paste text, you can run all five prompts. For the full monthly routine around them, read <a href="/ai-accounting/how-to-use-ai-for-bookkeeping/">how to use AI for bookkeeping</a> and our <a href="/bookkeeping/do-your-own-bookkeeping/">guide to doing your own bookkeeping</a>.</p>
<p>More prompt methods are in our <a href="/ai-accounting/">AI for Accounting guides</a> and the <a href="/bookkeeping/">bookkeeping hub</a>. Rather hand off the whole monthly job?</p>''',
 'Want the categorizing done for you? At <a href="CTAURL">Computatio</a>, AI does the sorting and an accountant reviews and reconciles every account each month. Monthly Books is $500 a month.',
 [("IRS: 2025 Schedule C (Form 1040)","https://www.irs.gov/pub/irs-prior/f1040sc--2025.pdf"),
  ("IRS: Instructions for Schedule C (Form 1040) (2025)","https://www.irs.gov/instructions/i1040sc"),
  ("IRS: Publication 583, Starting a Business and Keeping Records","https://www.irs.gov/publications/p583"),
  ("IRS: Publication 463 (2025), Travel, Gift, and Car Expenses","https://www.irs.gov/publications/p463"),
  ("IRS: How long should I keep records?","https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records")],
 "ai-prompts-categorize-transactions"),
article("/ai-accounting/quickbooks-ai-banking-suggestions/","/ai-accounting/","AI for Accounting",
 "QuickBooks AI banking suggestions: review before you post",
 "QuickBooks AI banking suggestions: review before you post",
 "What the green, blue and orange QuickBooks AI banking signals mean, when to use Ready to post, and a month-end check that catches wrong matches.",
 "2026-10-27",
 "You open the QuickBooks banking page and every transaction already has a payee and a category. Some have a green check, some blue, some orange. It&rsquo;s tempting to select all and hit Post.",
 '''<div class="callout"><b>Quick answer:</b> as of October 27, 2026, QuickBooks Online&rsquo;s new banking page fills in payee and category with AI and marks each with a review signal. <b>Green</b> means a strong pattern in your own history, <b>blue</b> means some support but similar transactions vary, and <b>orange</b> means little or no history. Batch-post greens after a quick scan, confirm blues, open every orange, and reconcile at month-end. Suggestions come on all QuickBooks Online versions; the &ldquo;Ready to post&rdquo; batch is on Essentials, Plus and Advanced in the US.</div>

<h2>The suggestions look finished, but are they right?</h2>
<p>The AI fills the From/To and Match or Categorize columns for you. Every row looks done. Nothing tells you at a glance which ones it guessed.</p>
<p><b>A filled-in category is a suggestion, not a decision.</b> Posting it is the decision, and that part is still yours.</p>

<h2>And a wrong match is harder to spot than a wrong category</h2>
<p>A bad category is visible: the coffee shop says &ldquo;Rent.&rdquo; A bad match hides. The bank line gets tied to the wrong invoice or bill, or to nothing when it should have matched a record you already entered. That&rsquo;s how duplicates get in.</p>

<h2>What posting without looking costs you</h2>
<ul>
<li><b>Duplicated expenses or income.</b> If you entered a bill and then categorize the bank payment as a new expense, it&rsquo;s counted twice.</li>
<li><b>A habit copied forward.</b> Green signals come from your own history. If you coded something wrong for months, the AI learns the mistake and suggests it with confidence.</li>
<li><b>A tax deduction with no backup.</b> The IRS says proof of payment alone doesn&rsquo;t show you&rsquo;re entitled to a deduction. A posted bank line still needs the receipt or invoice behind it.</li>
<li><b>Messy fixes later.</b> Undoing a posted line is easy. Changing one that&rsquo;s already reconciled can throw off your balances.</li>
</ul>

<h2>Picture a 10-minute banking session</h2>
<p>You open Pending. You review the Ready to post batch, untick two lines, and post the rest. You open the handful of orange rows, pull receipts, and fix them. At month-end your category totals look normal and the reconciliation ties out.</p>
<p><b>Your time goes to the rows that need judgment, not the ones that repeat every month.</b></p>

<h2>What the QuickBooks AI banking signals mean</h2>
<p>Each pending row can show two signals: one for the category and one for the payee (From/To). Matches get their own green or blue badge.</p>
<table>
<tr><th>Signal</th><th>What QuickBooks says it means</th><th>What to do</th></tr>
<tr><td>Green check</td><td>A strong, consistent pattern in your history, or a payee that matches an existing customer or vendor</td><td>Scan the amount and required fields, then post</td></tr>
<tr><td>Blue info</td><td>Some support, but similar transactions were coded different ways. For payees, a new name pulled from the bank description</td><td>Confirm before posting; add a new payee only if it&rsquo;s real</td></tr>
<tr><td>Orange alert</td><td>Little data, such as no similar transactions in your books</td><td>Open it, get the receipt, set the category yourself</td></tr>
</table>
<p>Select a signal, then <b>More info</b>, to open the Suggestions panel and see why it picked that answer. Orange doesn&rsquo;t apply to matches: low-confidence matches are hidden, so use <b>Find match</b> when you know a record exists.</p>

<h2>The green-blue-orange method for QuickBooks AI banking suggestions</h2>
<ol>
<li><b>Open the page.</b> Go to All apps, then Accounting, then Bank transactions, and pick the <b>Pending</b> tab for the account.</li>
<li><b>Set your Ready to post rules first (Essentials and up).</b> In the feature&rsquo;s policy settings, set an <b>Amount exceeds</b> limit, such as $500, so big items always wait for you. Choose whether payee, class and location are required. A transaction that fails any check is held for review instead.</li>
<li><b>Review the batch.</b> Select <b>Review</b> on the banner, or filter to Ready to post. Untick anything that looks off: a personal-looking vendor, an odd amount, a payment to a person. Then post the rest.</li>
<li><b>Confirm every blue.</b> Check the category against what you actually bought. For a new payee, make sure it&rsquo;s a real vendor before adding it to your list.</li>
<li><b>Open every orange.</b> These are new to your books. Find the receipt, decide the category, and add a short memo.</li>
<li><b>Heed the &ldquo;potential match&rdquo; warning.</b> When QuickBooks thinks a record already exists, it shows this instead of a category. Select Find match. If the bill or invoice is there, match it; categorizing it as new would double-count it.</li>
<li><b>Fix mistakes from the Posted tab.</b> Find the line and select <b>Undo</b> in the Action column. It goes back to Pending. If it&rsquo;s already reconciled, stop and ask whoever reviews your books first.</li>
</ol>
<p>A rule you set in QuickBooks still wins: Intuit says the AI never overrides your bank rules or makes them auto-post. Our <a href="/ai-accounting/ai-prompts-categorize-transactions/">AI categorizing prompts</a> can help you decide what those rules should be.</p>

<div class="callout"><b>Example (made-up data).</b> Five pending lines for a one-person design studio:<br>
Oct 3 &middot; ADOBE *CREATIVE CLD &middot; $59.99 &rarr; Software &middot; green &middot; in the Ready to post batch. Post.<br>
Oct 9 &middot; COSTCO WHSE #0412 &middot; $212.80 &rarr; Supplies &middot; blue. Receipt shows half was groceries. Split it: business part to Supplies, rest to Owner draw.<br>
Oct 12 &middot; DEPOSIT ACME CO &middot; $1,800.00 &rarr; potential match warning. Find match shows open invoice #1043 for $1,800. Match it, don&rsquo;t categorize as new income.<br>
Oct 18 &middot; SQ *RIVERSIDE PRINT &middot; $146.00 &rarr; Advertising &middot; orange. New vendor. Receipt confirms flyers. Post with a memo.<br>
Oct 25 &middot; ADOBE *CREATIVE CLD &middot; $59.99 &rarr; Software &middot; green. Second charge this month. Check the card statement before posting: it could be a duplicate download.</div>

<h2>How to check QuickBooks AI suggestions at month-end</h2>
<ol>
<li><b>Compare category totals to last month.</b> Run a profit and loss by month. A category that jumped or vanished usually means the AI picked a new habit.</li>
<li><b>Scan Uncategorized and Ask My Accountant-type accounts.</b> They should be empty or explained.</li>
<li><b>Look for repeats:</b> same vendor, same amount, a few days apart.</li>
<li><b><a href="/ai-accounting/ai-bank-reconciliation/">Reconcile each account</a></b> to the bank statement. <b>If it doesn&rsquo;t tie out, something was posted wrong or twice.</b></li>
<li><b>Keep the receipts.</b> The IRS generally expects records for 3 years after you file, and longer in some cases.</li>
</ol>

<h2>Is it safe to trust the AI, and what can&rsquo;t it do?</h2>
<p>The suggestions use your own history and the bank&rsquo;s description. They can&rsquo;t know why you bought something, or whether a big-box purchase was half personal. New company files may not show green match badges until you&rsquo;ve accepted that kind of match a few times. Prefer the old screen? QuickBooks offers <b>Switch to previous version</b>.</p>
<p>You don&rsquo;t need to be technical. If you can read three colors and open a receipt, you can run this method. For the bigger routine, see <a href="/ai-accounting/how-to-use-ai-for-bookkeeping/">how to use AI for bookkeeping</a> and our <a href="/bookkeeping/">bookkeeping guides</a>.</p>
<p>Rather have someone else run the banking page every month?</p>''',
 'Want the review done for you? At <a href="CTAURL">Computatio</a>, AI does the first pass and an accountant reviews and reconciles every account each month. Monthly Books is $500 a month.',
 [("Intuit QuickBooks: Learn about updates to the new AI-powered banking page","https://quickbooks.intuit.com/learn-support/en-us/help-article/matching-rules/learn-updates-new-ai-powered-banking-page/L0hR7A9Zf_US_en_US"),
  ("Intuit QuickBooks: Use Ready to post in QuickBooks Online","https://quickbooks.intuit.com/learn-support/en-us/help-article/account-management/use-ready-post-quickbooks-online/L9jzjf8Xe_US_en_US"),
  ("Intuit QuickBooks: How AI suggestions help match and categorize bank transactions","https://quickbooks.intuit.com/learn-support/en-us/help-article/bank-transactions/ai-suggestions-help-match-categorize-bank/L8FHOh4AD_US_en_US"),
  ("Intuit QuickBooks: Unmatch or move downloaded bank transactions","https://quickbooks.intuit.com/learn-support/en-us/help-article/bank-registers/unmatch-downloaded-bank-transactions-move-another/L71oaBb86_US_en_US"),
  ("IRS: Publication 583, Starting a Business and Keeping Records","https://www.irs.gov/publications/p583")],
 "quickbooks-ai-banking-suggestions"),
article("/ai-accounting/ai-bank-reconciliation/","/ai-accounting/","AI for Accounting",
 "AI Bank Reconciliation: How to Reconcile With AI",
 "AI bank reconciliation: how to do it and what AI can&rsquo;t do",
 "Use AI for bank reconciliation: copy-paste prompts to match your books to your statement, find missing and duplicate lines, and check the result yourself.",
 "2026-10-28",
 "Your bank says one number. Your books say another. You scroll both lists line by line, trying to spot the $43.17 that doesn&rsquo;t match, and an hour later you still can&rsquo;t find it.",
 '''<div class="callout"><b>Quick answer:</b> AI bank reconciliation works best as a <b>matching assistant, not a calculator</b>. Export your bank statement and your book entries for the same month, remove account numbers, and ask the AI to pair each statement line with a book line and list everything left over. Then fix those items in your bookkeeping software and let the software confirm that the adjusted bank balance equals your book balance. The IRS recommends reconciling your checking account every month.</div>

<h2>You can&rsquo;t find why the balances don&rsquo;t match</h2>
<p>Two lists, a few hundred lines each, and a gap you can&rsquo;t explain. Is it a missing entry? A typo? A charge you recorded twice?</p>
<p><b>A gap of a few dollars can hide several errors that partly cancel out.</b> That&rsquo;s why eyeballing totals rarely finds it.</p>

<h2>And you&rsquo;re not sure AI can be trusted with numbers</h2>
<p>You&rsquo;ve heard AI can read a bank statement in seconds. You&rsquo;ve also seen it add a column wrong with full confidence. So you don&rsquo;t know whether it saves you an hour or adds a new mistake.</p>
<p>Both are true. The method below uses AI only for the part it&rsquo;s good at.</p>

<h2>What skipping reconciliation costs you</h2>
<ul>
<li><b>Errors stay in your books.</b> The IRS describes reconciling as the way to confirm your balance, make sure bank charges are recorded, and correct mistakes. Skip it, and missing or doubled lines flow into your profit.</li>
<li><b>Your tax return starts from wrong numbers.</b> A duplicated expense lowers your profit on paper. A missed deposit raises it. Either way, the return doesn&rsquo;t match reality.</li>
<li><b>A bank line doesn&rsquo;t prove the deduction.</b> The IRS says proof of payment alone doesn&rsquo;t show you&rsquo;re entitled to a deduction. You still need the invoice or receipt behind it.</li>
<li><b>Months pile up.</b> One month takes minutes. Six months of unreconciled accounts take days, and old charges are harder to remember.</li>
</ul>

<h2>Picture month-end in 20 minutes</h2>
<p>The statement arrives. You export two files and paste one prompt. Back comes a short list: one deposit missing from your books, one charge entered twice, two checks that haven&rsquo;t cleared. You fix two lines, and the reconciliation ties out.</p>
<p><b>You spend your time on the four lines that need you, not the 200 that already match.</b></p>

<h2>Why bank and book balances differ</h2>
<p>A difference doesn&rsquo;t always mean a mistake. The IRS lists three normal reasons your bank balance and your book balance can differ at month-end:</p>
<ul>
<li>bank charges you haven&rsquo;t recorded yet,</li>
<li>deposits you made after the statement date, and</li>
<li>checks you wrote that haven&rsquo;t cleared.</li>
</ul>
<p>Everything else, such as a missing entry, a duplicate or a wrong amount, is an error to fix. <b>AI bank reconciliation is about sorting every difference into one of those two groups.</b></p>

<h2>The match-and-explain method for AI bank reconciliation</h2>
<p>These prompts work in ChatGPT, Claude, Gemini or Copilot. You don&rsquo;t need to be technical: if you can download a file and paste text, you can do this.</p>
<ol>
<li><b>Export two files for the same month.</b> From your bank, download the statement as a CSV or spreadsheet. From your bookkeeping software or spreadsheet, export every entry for that account and month.</li>
<li><b>Remove sensitive details.</b> Delete full account and card numbers, and keep only date, description and amount. Our <a href="/ai-accounting/financial-data-safety-ai/">data safety guide</a> covers the rest.</li>
<li><b>Run Prompt 1</b> to pair the lines.</li>
<li><b>Run Prompt 2</b> to sort what&rsquo;s left over.</li>
<li><b>Fix the errors in your books,</b> not in the chat.</li>
<li><b>Reconcile in your software,</b> and let it do the math.</li>
</ol>

<h3>Prompt 1: match the lines</h3>
<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;I&rsquo;m reconciling one bank account for [month]. List A is the bank statement. List B is my book entries. Match each line in A to one line in B with the same amount and a date within 5 days. Return three tables: matched pairs; lines only in A; lines only in B. Keep every row. Don&rsquo;t merge, round, total or add anything. If two lines could match, put both in a fourth table called &lsquo;unsure&rsquo;. List A: [paste]. List B: [paste].&rdquo;</div>

<h3>Prompt 2: explain the leftovers</h3>
<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;For each line that only appears in one list, suggest the most likely reason: bank fee not yet recorded, deposit after the statement date, check not yet cleared, missing from my books, possible duplicate, or amount typo (same vendor, different amount). Give one line of reasoning each. Mark anything you&rsquo;re unsure about as &lsquo;needs review&rsquo;. Don&rsquo;t calculate balances.&rdquo;</div>
<p><b>Notice what the prompts never ask for: a balance.</b> Matching and explaining are pattern work, which AI handles well. Arithmetic across long tables is where it slips.</p>

<div class="callout"><b>Example (made-up data).</b> A one-person consulting business, September checking account. Prompt 1 matched 61 of 65 statement lines. Prompt 2 sorted the rest:<br>
Sep 30 &middot; MONTHLY SERVICE FEE &middot; $12.00 &rarr; only on statement &middot; &ldquo;Bank fee not yet recorded.&rdquo;<br>
Sep 18 &middot; DEPOSIT NORTHSIDE LLC &middot; $1,250.00 &rarr; only on statement &middot; &ldquo;Missing from books; check for an open invoice.&rdquo;<br>
Sep 22 &middot; CANVA &middot; $15.00 &rarr; in books twice, on statement once &middot; &ldquo;Possible duplicate.&rdquo;<br>
Sep 28 &middot; CHECK 1042 &middot; $400.00 &rarr; only in books &middot; &ldquo;Check not yet cleared.&rdquo;<br>
<b>How to check it:</b> record the $12 fee, match the $1,250 deposit to the client&rsquo;s invoice, delete the second Canva entry after confirming one charge on the statement, and leave check 1042 as outstanding. Then reconcile in your software: the adjusted bank balance should equal your book balance.</div>

<h2>How do you check an AI bank reconciliation?</h2>
<ol>
<li><b>Count the rows.</b> Matched pairs plus leftovers must equal the number of lines in each list. A missing row is a missing transaction.</li>
<li><b>Spot-check five matched pairs</b> against the statement, including the largest one.</li>
<li><b>Confirm every &ldquo;unsure&rdquo; and &ldquo;needs review&rdquo; line</b> yourself, with the receipt or invoice in hand.</li>
<li><b>Let your software do the final math.</b> Following the IRS steps, the adjusted bank balance must equal your adjusted book balance. <b>If the software doesn&rsquo;t tie out, you&rsquo;re not done, whatever the chat said.</b></li>
<li><b>Save the statement and your reconciliation report.</b> The IRS generally expects records for 3 years after you file, and longer in some cases. Electronic copies must meet the same standards as paper ones.</li>
</ol>

<h2>What AI can&rsquo;t do in bank reconciliation</h2>
<ul>
<li><b>It can&rsquo;t see your bank.</b> It only knows what you paste. A wrong export means a wrong answer.</li>
<li><b>It can&rsquo;t sign off.</b> Reconciling is done when your books and the statement agree in your software, not when a chat says so.</li>
<li><b>It can&rsquo;t tell you why you spent money.</b> A match proves a charge happened, not that it was a business expense.</li>
<li><b>It can be confidently wrong.</b> Two $15 charges in one month may be a duplicate, or two real purchases. Only the statement and receipts settle it.</li>
</ul>
<p>Using QuickBooks? Its banking page can match transactions for you; see <a href="/ai-accounting/quickbooks-ai-banking-suggestions/">how to review QuickBooks AI banking suggestions</a>. Still sorting categories first? Start with our <a href="/ai-accounting/ai-prompts-categorize-transactions/">AI prompts to categorize transactions</a>, then come back here. For the whole monthly routine, read <a href="/ai-accounting/how-to-use-ai-for-bookkeeping/">how to use AI for bookkeeping</a>.</p>
<p>Rather have someone else tie out every account each month?</p>''',
 'Want reconciliation done for you? At <a href="CTAURL">Computatio</a>, AI does the matching and an accountant reviews and reconciles every account each month. Monthly Books is $500 a month.',
 [("IRS: Publication 583, Starting a Business and Keeping Records","https://www.irs.gov/publications/p583"),
  ("IRS: How long should I keep records?","https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records")],
 "ai-bank-reconciliation"),
article("/ai-accounting/irs-iris-1099-e-filing-fire-retiring/","/ai-accounting/","AI for Accounting",
 "IRS FIRE is closing: e-file 1099s with IRIS instead",
 "IRS FIRE is closing: e-file 1099s with IRIS instead",
 "IRS FIRE stops taking 1099s on Nov. 19, 2026. How to get an IRIS TCC now, e-file 1099-NECs free in IRIS, and use AI to prep your vendor list safely.",
 "2026-10-29",
 "You filed your contractors&rsquo; 1099s through FIRE last year. This year, that door closes before filing season even opens. And the new system needs a code you don&rsquo;t have yet.",
 '''<div class="callout"><b>Quick answer:</b> as of October 29, 2026, the IRS says <b>November 19, 2026, at 3 p.m. Eastern</b> is the last day to file information returns through FIRE. FIRE users must file tax year 2026 Forms 1099 through <b>IRIS</b>, the IRS&rsquo;s Information Returns Intake System, in the 2027 filing season. IRIS needs its own Transmitter Control Code (TCC), and the IRS says to allow up to 45 calendar days to process the application. <b>Apply now.</b> The IRIS Taxpayer Portal is free and takes typed-in forms or a CSV upload.</div>

<h2>Your FIRE login won&rsquo;t file your 2026 1099s</h2>
<p>FIRE, the IRS&rsquo;s older e-file system for information returns, is being retired. The IRS has already stopped taking new FIRE TCC applications. Existing applications can be updated only through November 9, 2026, and then become read-only.</p>
<p><b>After January 1, 2027, IRIS is the only IRS e-file system for information returns</b>, including current-year, prior-year and corrected returns.</p>

<h2>And your new IRIS code takes weeks</h2>
<p>A FIRE TCC doesn&rsquo;t carry over. IRIS uses a 5-digit TCC that works only in IRIS. The IRS&rsquo;s IRIS portal guide says to allow up to 45 calendar days for the application, and the approval letter comes by mail.</p>
<p>Form 1099-NEC is due to your contractors and to the IRS by January 31. For 2026 forms that date is a Sunday, so the due date moves to the next business day: <b>Monday, February 1, 2027</b>.</p>

<h2>What waiting costs you</h2>
<ul>
<li><b>A scramble in January.</b> Apply in mid-December and 45 days lands you near the end of January, right at the deadline.</li>
<li><b>Paper may not be an option.</b> If you file 10 or more information returns in total (all types added together), the IRS requires you to e-file them.</li>
<li><b>Wrong forms from messy records.</b> Your 1099s are only as right as your vendor totals. A missing payment or a card payment counted by mistake goes straight onto the form.</li>
</ul>

<h2>Picture January with the code already in hand</h2>
<p>Your IRIS TCC letter came in November. In early January you close the year, run one AI prompt on your vendor payments, and get a short list: who needs a 1099-NEC, how much, and what&rsquo;s missing. You fill the IRS template, upload it, and download the copies for your contractors.</p>
<p><b>The work that needs you is a handful of judgment calls, not a hunt through twelve months of payments.</b></p>

<h2>Step 1: Get your IRIS TCC now</h2>
<p>Following the IRS&rsquo;s IRIS Taxpayer Portal guide (Publication 5717):</p>
<ol>
<li>Go to the IRS page <b>IRIS Application for TCC</b> and select the button to access the application.</li>
<li>Sign in, or create an account.</li>
<li>On <b>Select Your Organization</b>, choose <b>Individual</b>.</li>
<li>Select <b>New Application</b>, then <b>IRIS Application for TCC</b>, and complete it.</li>
<li>Each Responsible Official signs the submission page with their 5-digit PIN.</li>
</ol>
<p>If it sits in &ldquo;Submitted Pending Review&rdquo; for more than 45 days, the guide says to contact the help desk.</p>

<h2>Step 2: Use AI to build your 1099 vendor list</h2>
<p>AI is good at sorting a year of payments into per-vendor totals and flagging gaps. It should never see a Social Security number or EIN. <b>Mask every TIN before you paste anything</b>, and add the real numbers yourself, offline. Our <a href="/ai-accounting/financial-data-safety-ai/">financial data safety guide</a> covers what else to strip out.</p>
<ol>
<li>Export every 2026 payment to non-employees from your books: date, payee, amount, payment method, and what it was for.</li>
<li>Replace names with your own vendor IDs if you like, and delete any TIN or bank details.</li>
<li>Paste the export into any AI tool with the prompt below.</li>
</ol>

<div class="callout"><b>Prompt:</b> &ldquo;Below are my 2026 business payments to outside people and companies. Group them by payee and total each one. For each payee, list: total paid by check, ACH or cash; total paid by credit card, payment card or a payment app; whether the payee is a corporation (answer &lsquo;unknown&rsquo; if the data doesn&rsquo;t say); and whether the services were legal services. Flag any payee whose check, ACH and cash total is $2,000 or more. Do not add numbers that aren&rsquo;t in the data. List any payment you couldn&rsquo;t assign to a payee.&rdquo;</div>

<p>The prompt splits payment methods because the IRS says payments made with a credit card or payment card aren&rsquo;t reported on Form 1099-NEC or 1099-MISC; they belong on Form 1099-K. Payments to corporations are generally exempt, except payments for legal services. For tax year 2026, the reporting threshold for nonemployee compensation is <b>$2,000</b>; see our <a href="/deductions/1099-nec-2000-threshold/">guide to the $2,000 threshold</a>.</p>

<div class="callout"><b>Example (made-up data).</b> A one-person marketing studio, 2026:<br>
V-01 &middot; freelance designer &middot; $4,800 by ACH &middot; not a corporation &rarr; <b>1099-NEC, $4,800</b><br>
V-02 &middot; copywriter &middot; $1,650 by check + $900 by card &rarr; the check total is under $2,000, so no 1099-NEC. Card payments are reported on Form 1099-K instead, not by you.<br>
V-03 &middot; web developer, Inc. &middot; $6,000 by ACH &rarr; corporation, not legal services. Generally no 1099-NEC. Confirm the corporate status in your vendor file.<br>
V-04 &middot; law office, PC &middot; $2,500 by check for a contract review &rarr; legal services. The corporation exemption doesn&rsquo;t apply. Check the instructions for which box to use.<br>
One $350 payment had no payee &rarr; find the receipt before you file.</div>

<h2>Step 3: How to check the AI&rsquo;s 1099 list</h2>
<ol>
<li><b>Tie each total to your vendor ledger.</b> Run a 2026 expense-by-vendor report in your books. Every flagged total must match it to the cent.</li>
<li><b>Add it all up.</b> The AI&rsquo;s totals for all payees should equal the total of the export you pasted. A gap means a dropped or doubled payment.</li>
<li><b>Confirm every &ldquo;unknown&rdquo;</b> (corporation status, payment method) from your own records, not the AI&rsquo;s guess.</li>
<li><b>Reconcile December first.</b> If the year&rsquo;s last month isn&rsquo;t reconciled, the totals may be short. Our <a href="/ai-accounting/ai-bank-reconciliation/">AI bank reconciliation guide</a> shows how.</li>
</ol>

<h2>Step 4: File in the IRIS Taxpayer Portal</h2>
<ol>
<li>Sign in and add your business under <b>Issuer Management</b>.</li>
<li>For a few forms, use <b>Start New Form</b> and type them in.</li>
<li>For more, select <b>Upload CSV with Form Data</b>, choose the form type, and download the IRS template. The IRS accepts only its own templates, and one upload holds one tax year and one form type.</li>
<li>Type your checked list into a fresh template. The IRS warns against copying and pasting from another CSV into it, and recommends a new template each time.</li>
<li>Leave empty money cells blank, not $0.00. Use Y or N in check-box fields. Save as <b>CSV UTF-8 (Comma delimited)</b>.</li>
<li>Add each payee&rsquo;s real TIN yourself, on your own computer, never in a chatbot.</li>
<li>After you submit, download the recipient copies from the portal and send them by the due date. Our <a href="/deductions/send-1099-nec-by-january-31/">January deadline guide</a> covers how.</li>
</ol>
<p>Made a mistake? IRIS also takes corrections and automatic extension requests. Filing large volumes through software? The IRS offers IRIS Application to Application (A2A) for that.</p>

<h2>What AI can&rsquo;t do for your 1099s</h2>
<ul>
<li><b>It can&rsquo;t confirm a payee&rsquo;s tax status.</b> Whether a vendor is a corporation comes from your records, not from its name.</li>
<li><b>It can&rsquo;t file for you.</b> The TCC, the upload and the signature are yours.</li>
<li><b>It can be confidently wrong.</b> Treat its totals as a draft until they tie to your books.</li>
</ul>
<p>You don&rsquo;t need to be technical. If you can export a report and fill a spreadsheet, you can do this. For more, see our <a href="/ai-accounting/">AI for Accounting guides</a> and our <a href="/deductions/">deductions guides</a>.</p>
<p>Not sure who needs a 1099, or how to set up IRIS for your business?</p>''',
 'Not sure where you stand? <a href="CTAURL">Book a free 20-minute call with Computatio</a> to go through your contractor payments and your filing plan.',
 [("IRS: Information return e-file system transitioning to a new platform (IR-2026-99)","https://www.irs.gov/newsroom/irs-reminder-information-return-e-file-system-transitioning-to-a-new-platform"),
  ("IRS: Filing Information Returns Electronically (FIRE)","https://www.irs.gov/e-file-providers/filing-information-returns-electronically-fire"),
  ("IRS: E-file information returns with IRIS","https://www.irs.gov/filing/e-file-information-returns-with-iris"),
  ("IRS: Publication 5717, IRIS Taxpayer Portal User Guide","https://www.irs.gov/pub/irs-pdf/p5717.pdf"),
  ("IRS: Instructions for Forms 1099-MISC and 1099-NEC","https://www.irs.gov/instructions/i1099mec")],
 "irs-iris-1099-e-filing-fire-retiring"),
article("/ai-accounting/can-ai-do-your-accounting/","/ai-accounting/","AI for Accounting",
 "Can AI Do Your Accounting? What It Gets Right and Wrong",
 "Can AI do your accounting? What it gets right and wrong",
 "Can AI do your accounting? See which bookkeeping tasks AI handles well, where it gets things wrong, and a simple test to check it on your own books.",
 "2026-10-30",
 "You keep hearing that AI can run your books now. You open a chatbot, paste in a month of transactions, and get a tidy answer in seconds. Then a question nags at you: is any of this right?",
 '''<div class="callout"><b>Quick answer:</b> AI can do <b>part</b> of your accounting well: sorting transactions, reading receipts, matching lines and explaining reports in plain English. It gets things wrong when a task needs your business context, current tax rules, or exact math across long tables. It can&rsquo;t reconcile your accounts for you, keep your records, or take responsibility for your return. <b>Use AI to draft, and use your books, receipts and official rules to check.</b></div>

<h2>You don&rsquo;t know what to hand over to AI</h2>
<p>Some say AI will replace bookkeeping. Others say never trust it with money. Neither helps on a Tuesday night with 140 unsorted transactions.</p>
<p><b>The real question isn&rsquo;t &ldquo;can AI do accounting?&rdquo; It&rsquo;s &ldquo;which parts, and how do I check them?&rdquo;</b></p>

<h2>And you&rsquo;ve seen it be wrong with total confidence</h2>
<p>Maybe it labeled a family dinner as a business meal. Maybe it gave you a total that was off by a few hundred dollars. It never said &ldquo;I&rsquo;m not sure.&rdquo;</p>
<p>That&rsquo;s the hard part. A wrong answer from AI looks exactly like a right one.</p>

<h2>What a wrong AI answer costs you</h2>
<ul>
<li><b>You&rsquo;re responsible, not the tool.</b> The IRS says taxpayers are ultimately responsible for all the information on their return, no matter who prepares it. That includes a chatbot.</li>
<li><b>A bank line isn&rsquo;t proof.</b> IRS Publication 583 says proof of payment alone doesn&rsquo;t show you&rsquo;re entitled to a deduction. You still need the receipt or invoice, and AI can&rsquo;t create those for you.</li>
<li><b>Old rules sound current.</b> AI often learned from years of articles. For example, restaurant meals were 100% deductible only for amounts paid in 2021 and 2022. The normal rule, generally a 50% limit, applies again. An AI that remembers the old rule can overstate your deduction.</li>
<li><b>Wrong categories become wrong tax numbers.</b> To be deductible, the IRS says an expense must be ordinary (common in your field) and necessary (helpful and appropriate for your business). AI can&rsquo;t know which of your purchases meet that test.</li>
</ul>
<div class="callout"><b>State note.</b> States don&rsquo;t always follow federal changes. California, for example, did not adopt the temporary federal 100% restaurant meal deduction for 2021 and 2022. When AI states a tax rule, ask which year and which government it applies to, then check that agency&rsquo;s own page.</div>

<h2>Picture AI doing the busywork while you make the calls</h2>
<p>AI sorts the month and flags the 12 lines it&rsquo;s unsure about. It reads your receipt photos and fills in date, vendor and amount. It tells you in two sentences why profit dropped. You spend 20 minutes on judgment calls, and your software confirms the books match the bank.</p>
<p><b>You get AI&rsquo;s speed without betting your tax return on its guesses.</b></p>

<h2>What AI gets right in accounting, and what it gets wrong</h2>
<p>Here&rsquo;s how common bookkeeping tasks sort out. Green means AI does it well. Yellow means AI drafts and you check. Red means AI can&rsquo;t do it for you.</p>
<table class="tbl">
<tr><th>Task</th><th>Rating</th><th>Why</th></tr>
<tr><td>Suggesting categories for transactions</td><td>Green</td><td>Pattern work. Give it your category list and rules.</td></tr>
<tr><td>Reading receipts and invoices</td><td>Green</td><td>Pulls date, vendor and amount fast. Check blurry photos.</td></tr>
<tr><td>Matching bank lines to book entries</td><td>Green</td><td>Good at pairing; bad at the final balance.</td></tr>
<tr><td>Explaining a profit and loss report</td><td>Green</td><td>Turns numbers into plain English.</td></tr>
<tr><td>Totals and percentages across long tables</td><td>Yellow</td><td>Can slip. Let your software or spreadsheet do the math.</td></tr>
<tr><td>Business vs. personal calls</td><td>Yellow</td><td>Needs your context. Review anything it marks unsure.</td></tr>
<tr><td>Tax rules, rates and deadlines</td><td>Yellow</td><td>May be outdated. Check the IRS or state agency page.</td></tr>
<tr><td>Reconciling and signing off</td><td>Red</td><td>Done only when your software ties out to the statement.</td></tr>
<tr><td>Keeping your records</td><td>Red</td><td>You keep the receipts and statements, not a chat summary.</td></tr>
<tr><td>Responsibility for your return</td><td>Red</td><td>Always yours.</td></tr>
</table>

<h2>The traffic-light test: check AI on your own books</h2>
<p>Don&rsquo;t take our table on trust. Test AI on a month you know is right. These steps work in ChatGPT, Claude, Gemini or Copilot, and you don&rsquo;t need to be technical.</p>
<ol>
<li><b>Pick a month you&rsquo;ve already reconciled.</b> You know the right answers, so you can grade the AI.</li>
<li><b>Export that month&rsquo;s transactions</b> from your bank or bookkeeping software. Keep date, description and amount only. Remove account numbers and anything personal; see our <a href="/ai-accounting/financial-data-safety-ai/">data safety guide</a>.</li>
<li><b>Run the test prompt below.</b> It asks for categories, confidence levels and a flag list, but no totals.</li>
<li><b>Grade the answers</b> against your reconciled books.</li>
<li><b>Sort your tasks into green, yellow and red</b> based on what you saw, then use the matching guide for each green task.</li>
</ol>

<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;I&rsquo;m testing how well you handle my bookkeeping. Here are one month of transactions for a [type of business]. Use only these categories: [paste list]. For each line, return date, description, amount, suggested category, confidence (high, medium or low) and a one-line reason. Mark anything that could be personal, or that needs a receipt to decide, as low confidence. Then list every tax rule you relied on, with the tax year it applies to. Don&rsquo;t calculate any totals. Transactions: [paste].&rdquo;</div>
<p><b>The last instruction matters most.</b> Asking AI to name each rule and its tax year turns a hidden guess into something you can check.</p>

<div class="callout"><b>Example (made-up data).</b> A freelance designer tests one reconciled month of 48 transactions:<br>
Categories: 44 of 48 matched her books. The 4 misses were all marked low or medium confidence.<br>
Oct 8 &middot; THAI GARDEN &middot; $86.40 &rarr; Meals &middot; low &middot; &ldquo;Could be personal; needs receipt and business purpose.&rdquo;<br>
Rule it listed: &ldquo;Business meals 100% deductible.&rdquo; &rarr; <b>Wrong for this year.</b> That was a 2021&ndash;2022 rule; meals are generally limited to 50%.<br>
Oct 21 &middot; TRANSFER TO SAVINGS &middot; $2,000.00 &rarr; Owner draw &middot; medium &middot; &ldquo;Transfer to own account; not an expense.&rdquo; &rarr; Correct.<br>
<b>Her verdict:</b> categories are green if she reviews the low-confidence lines. Tax rules are yellow: check every one. Totals stay in her software.</div>

<h2>How do you check AI&rsquo;s accounting work?</h2>
<ol>
<li><b>Count the rows.</b> Every transaction you pasted should come back once. A missing row is a missing expense or deposit.</li>
<li><b>Review every low-confidence line</b> with the receipt or invoice in hand.</li>
<li><b>Check each tax rule</b> on the IRS or your state tax agency&rsquo;s site, for the right tax year.</li>
<li><b>Reconcile in your software.</b> The IRS says to reconcile your checking account each month. <b>If the software doesn&rsquo;t tie out, the books aren&rsquo;t done, whatever the chat said.</b></li>
<li><b>Keep the source records.</b> The IRS generally expects records for 3 years after you file. Some cases need longer: 6 years if you left out more than 25% of your gross income, 7 years for a bad debt or worthless securities loss, and at least 4 years for employment tax records. Electronic records must meet the same rules as paper.</li>
</ol>

<h2>Is it safe to let AI do your accounting?</h2>
<p>It can be. Never paste Social Security numbers, full account numbers or passwords, and turn off training on your inputs where you can.</p>

<h2>Where to start with your green tasks</h2>
<p>Start with sorting: our <a href="/ai-accounting/ai-prompts-categorize-transactions/">AI prompts to categorize transactions</a>. Then match lines with <a href="/ai-accounting/ai-bank-reconciliation/">AI bank reconciliation</a>, and put it all together with <a href="/ai-accounting/how-to-use-ai-for-bookkeeping/">the 3-pass AI bookkeeping method</a>. Receipts next? See <a href="/ai-accounting/ai-receipt-scanning/">AI receipt scanning</a>.</p>
<p>Or hand the green, yellow and red tasks to someone who checks all three:</p>''',
 'Want AI speed with a person checking the work? At <a href="CTAURL">Computatio</a>, AI does the sorting and matching, and an accountant reviews and reconciles every account each month. Monthly Books is $500 a month.',
 [("IRS: What taxpayers should know when choosing a tax professional","https://www.irs.gov/newsroom/what-taxpayers-should-know-when-choosing-a-tax-professional"),
  ("IRS: Publication 583, Starting a Business and Keeping Records","https://www.irs.gov/publications/p583"),
  ("IRS: How long should I keep records?","https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records"),
  ("IRS: Notice 2021-25, temporary 100% deduction for business meals","https://www.irs.gov/pub/irs-drop/n-21-25.pdf"),
  ("California FTB: 2022 Instructions for Schedule CA (540)","https://www.ftb.ca.gov/forms/2022/2022-540-ca-instructions.html")],
 "can-ai-do-your-accounting"),
article("/ai-accounting/separate-business-personal-expenses-ai/","/ai-accounting/","AI for Accounting",
 "Separate Business and Personal Expenses With AI",
 "Separate business and personal expenses with AI",
 "How to separate business and personal expenses with AI: a prompt that flags mixed charges, a made-up example, and the IRS rules to check it against.",
 "2026-11-04",
 "Your business card paid for groceries. Your personal card paid for a software plan. Now tax time is coming, and you have to work out which charges belong to the business.",
 '''<div class="callout"><b>Quick answer:</b> To separate business and personal expenses with AI, export your transactions, give the AI your category list and a short set of your own rules, and ask it to mark every line <b>business</b>, <b>personal</b> or <b>split</b>, with a reason and no totals. Then you decide every split line, keep the receipt, and post the results in your books. The IRS says personal, living and family costs generally aren&rsquo;t deductible, and costs used both ways, like a car, must be divided.</div>

<h2>Your business and personal spending are mixed together</h2>
<p>It started small. One coffee on the wrong card. One client lunch on your personal card. A few months later, nobody can tell which charge was which, including you.</p>
<p><b>Mixed accounts turn a 10-minute monthly job into a weekend of guessing.</b></p>

<h2>And some expenses are both at once</h2>
<p>Your phone, your car, your internet and the room you work in all serve your life and your business. You know part of each is deductible. You don&rsquo;t know how much, or how to show it.</p>

<h2>What mixed expenses cost you</h2>
<ul>
<li><b>Personal costs don&rsquo;t count.</b> The IRS says personal, household and family living costs generally can&rsquo;t be deducted, because they aren&rsquo;t ordinary and necessary costs of your business. Leave one in, and your profit is too low on your return.</li>
<li><b>Mixed-use costs must be split.</b> The IRS says you must divide them between business and personal use. For a vehicle, you deduct only the business part. Deduct the whole thing and you overstate the expense.</li>
<li><b>Some rules are specific.</b> For 2025, the Schedule C instructions say you can&rsquo;t deduct the base rate of the first phone line into your home. A home office has to be used regularly and exclusively for business. Business meals are generally limited to 50%.</li>
<li><b>A bank line isn&rsquo;t proof.</b> IRS Publication 583 says proof of payment alone doesn&rsquo;t show you&rsquo;re entitled to a deduction. You need the receipt or invoice too.</li>
</ul>

<h2>Picture a month where every charge has a home</h2>
<p>You open last month&rsquo;s transactions. AI has already marked 90% of them business or personal, with a reason for each. Six lines say &ldquo;split.&rdquo; You decide those six with your receipts and mileage log, and you&rsquo;re done.</p>
<p><b>You make the judgment calls. AI does the sorting.</b></p>

<h2>The business-or-personal method, step by step</h2>
<p>These steps work in ChatGPT, Claude, Gemini or Copilot. You don&rsquo;t need to be technical. You need a transaction export and 30 minutes.</p>
<ol>
<li><b>Export one month of transactions</b> from each account the business touched, business and personal. Keep only date, description and amount. Remove account numbers, names and anything else personal; see our <a href="/ai-accounting/financial-data-safety-ai/">data safety guide</a>.</li>
<li><b>Write your house rules in three to five lines.</b> For example: &ldquo;Groceries are personal. Adobe and Zoom are business. Phone and car are split.&rdquo; AI can&rsquo;t know your business. Your rules tell it.</li>
<li><b>Run the prompt below.</b> It sorts, explains and flags. It doesn&rsquo;t total anything.</li>
<li><b>Decide every &ldquo;split&rdquo; and &ldquo;unsure&rdquo; line yourself.</b> Use a reasonable basis you can show, like a mileage log for your car or a log of business calls for your phone.</li>
<li><b>Post the results in your books.</b> Business costs paid from a personal account are usually recorded as an owner contribution. Personal costs paid from the business account are owner draws, not expenses.</li>
</ol>

<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;Help me separate business and personal spending for my [type of business]. My categories are: [paste list]. My rules: [paste your 3&ndash;5 rules]. For each transaction, return date, description, amount, a label (business, personal, split or unsure), a suggested category if business, and a one-line reason. Use &lsquo;split&rsquo; for anything that may be used both ways, like a phone, car, internet or home. Use &lsquo;unsure&rsquo; when you&rsquo;d need a receipt to decide. Don&rsquo;t guess a business percentage and don&rsquo;t calculate totals. Transactions: [paste].&rdquo;</div>
<p><b>Two lines in that prompt do the heavy lifting:</b> no guessed percentages, and no totals. The percentage needs your records. The totals come from your software.</p>

<div class="callout"><b>Example (made-up data).</b> A freelance photographer runs one month of 62 transactions from her business and personal cards:<br>
Oct 3 &middot; TRADER JOE&rsquo;S &middot; $74.18 &rarr; personal &middot; &ldquo;Groceries, per your rules.&rdquo;<br>
Oct 6 &middot; ADOBE CREATIVE CLOUD &middot; $59.99 &rarr; business &middot; Software &middot; &ldquo;Listed as business in your rules.&rdquo; Paid from her personal card, so she records it as an owner contribution.<br>
Oct 9 &middot; VERIZON WIRELESS &middot; $95.00 &rarr; split &middot; &ldquo;Phone used both ways; needs your business share.&rdquo;<br>
Oct 14 &middot; SHELL OIL &middot; $48.20 &rarr; split &middot; &ldquo;Car fuel; depends on your mileage log.&rdquo;<br>
Oct 22 &middot; BLUE PLATE CAFE &middot; $63.50 &rarr; unsure &middot; &ldquo;Could be a client meal or personal; check the receipt.&rdquo;<br>
<b>Result:</b> 55 lines sorted, 5 split, 2 unsure. She checks the 7 open lines against her receipts and mileage log, then posts the month.</div>

<h2>How do you check AI&rsquo;s business vs. personal split?</h2>
<ol>
<li><b>Count the rows.</b> Every transaction you pasted should come back once.</li>
<li><b>Spot-check five &ldquo;business&rdquo; lines</b> against receipts. Each record should show the payee, amount, date, proof of payment and what it was for.</li>
<li><b>Never accept a percentage AI made up.</b> Your car share comes from your mileage log. Your phone and home office shares come from your own records.</li>
<li><b>Reconcile each account</b> in your software. See <a href="/ai-accounting/ai-bank-reconciliation/">AI bank reconciliation</a>. If it doesn&rsquo;t tie out, the month isn&rsquo;t done.</li>
</ol>

<h2>Stop the mixing at the source</h2>
<p>AI helps you clean up. It doesn&rsquo;t stop the mess from coming back. Publication 583 says to keep your business account separate from your personal checking account. <b>One business account and one business card cut the split work to a handful of lines a month.</b></p>
<p>Already mixed for months? Start with our guide to <a href="/ai-accounting/catch-up-bookkeeping-with-ai/">catching up on bookkeeping with AI</a>, then keep the routine going with <a href="/ai-accounting/ai-prompts-categorize-transactions/">AI prompts to categorize transactions</a>.</p>

<h2>Is this safe, and can AI get it wrong?</h2>
<p>AI can get it wrong, which is why it labels and you decide. Never paste Social Security numbers, full account numbers or passwords. And remember that you&rsquo;re responsible for what goes on your return, whoever or whatever sorted it.</p>
<p>Want the sorting done and checked for you every month?</p>''',
 'Let us keep business and personal apart for you. At <a href="CTAURL">Computatio</a>, AI does the sorting and an accountant reviews every account each month. Monthly Books is $500 a month.',
 [("IRS: Small business FAQs on income and expenses","https://www.irs.gov/faqs/small-business-self-employed-other-business/income-expenses/income-expenses-1"),
  ("IRS: Instructions for Schedule C (Form 1040) (2025)","https://www.irs.gov/instructions/i1040sc"),
  ("IRS: Publication 583, Starting a Business and Keeping Records","https://www.irs.gov/publications/p583"),
  ("IRS: What kind of records should I keep","https://www.irs.gov/businesses/small-businesses-self-employed/what-kind-of-records-should-i-keep")],
 "separate-business-personal-expenses-ai"),
article("/ai-accounting/ai-receipt-scanning/","/ai-accounting/","AI for Accounting",
 "AI Receipt Scanning: Turn Phone Photos Into Records",
 "AI receipt scanning: turn phone photos into bookkeeping records",
 "AI receipt scanning for small business: a prompt that turns receipt photos into bookkeeping rows, a made-up example, and what the IRS expects you to keep.",
 "2026-11-04",
 "There&rsquo;s a shoebox, a glovebox and a camera roll full of receipts. You meant to deal with them every week. Now it&rsquo;s been months.",
 '''<div class="callout"><b>Quick answer:</b> AI receipt scanning means taking a clear photo of each receipt and asking an AI tool to pull out the date, vendor, amount and what you bought, into rows you can match to your bank transactions. It saves typing. It doesn&rsquo;t replace the receipt: keep the image itself, legible and easy to find, because the IRS says electronic records must meet the same rules as paper ones.</div>

<h2>Your receipts are everywhere</h2>
<p>Some are paper. Some are emails. Some are photos you took and never looked at again. When you need one, you can&rsquo;t find it.</p>
<p><b>A receipt you can&rsquo;t find is a receipt you don&rsquo;t have.</b></p>

<h2>And the paper ones are fading</h2>
<p>Thermal paper receipts fade. Ink smudges in a wallet. By the time you sort them, some are blank.</p>

<h2>What missing receipts cost you</h2>
<ul>
<li><b>Your bank statement isn&rsquo;t enough.</b> IRS Publication 583 says proof of payment alone doesn&rsquo;t establish your right to a deduction. You also need documents like the receipt or invoice.</li>
<li><b>Records need specific details.</b> The IRS says your expense documents should show the payee, the amount, proof of payment, the date and a description that shows the business purpose.</li>
<li><b>Travel, gifts and car costs have stricter rules.</b> You must show the amount, time, place and business purpose. The IRS generally requires receipts for all lodging, whatever the amount, and for any other expense of $75 or more.</li>
<li><b>Records must last.</b> Publication 583 says to keep records generally for 3 years after you file, 6 years if you left out more than 25% of your gross income, and 7 years for a bad debt or worthless securities loss. Keep employment tax records at least 4 years.</li>
</ul>
<div class="callout"><b>State note.</b> States set their own time limits. California&rsquo;s Franchise Tax Board says its time to examine a return is usually 4 years from the return&rsquo;s due date or the date you filed it, and longer in some cases. Keep receipts at least as long as your state needs them too.</div>

<h2>Picture a receipt pile that never builds up</h2>
<p>You snap a photo at the register. Once a week, AI reads the new photos and gives you a tidy table. You match each row to a bank line in a few minutes. At tax time, every receipt is in one folder, named and searchable.</p>
<p><b>No shoebox. No fading paper. No hunting.</b></p>

<h2>The snap-read-match method for AI receipt scanning</h2>
<p>This works in any AI chat tool that reads images, like ChatGPT, Claude, Gemini or Copilot. Your bookkeeping software may also have its own receipt capture; the checks below apply either way.</p>
<ol>
<li><b>Snap a clear photo the same day.</b> Flat surface, good light, whole receipt in frame. On the back of a meal or travel receipt, write who you met and why, then photograph that too.</li>
<li><b>Save it in one place.</b> Use one folder per year, with a name like <code>2026-11-04_officedepot_42.17.jpg</code>. This is your record, so back it up.</li>
<li><b>Once a week, upload the week&rsquo;s photos</b> and run the prompt below. Crop out card numbers and loyalty IDs first; see our <a href="/ai-accounting/financial-data-safety-ai/">data safety guide</a>.</li>
<li><b>Match each row to your bank or card transaction</b>, then post the category in your books. Our <a href="/ai-accounting/ai-prompts-categorize-transactions/">categorization prompts</a> help with that step.</li>
<li><b>Flag anything that didn&rsquo;t match.</b> A receipt with no bank line, or a bank line with no receipt, is your to-do list.</li>
</ol>

<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;Read these receipt images. For each one, return a table row with: file name, date, vendor, total, tax shown, payment method (last 4 digits only, if shown), and a short list of items. If any field is blurry, cut off or missing, write &lsquo;UNCLEAR&rsquo; instead of guessing. Don&rsquo;t pick tax categories and don&rsquo;t add up totals. After the table, list every receipt with an UNCLEAR field.&rdquo;</div>
<p><b>&ldquo;Write UNCLEAR instead of guessing&rdquo; is the most important line.</b> AI will otherwise fill a smudged number with something that looks right.</p>

<div class="callout"><b>Example (made-up data).</b> A home-repair contractor uploads 5 photos from one week:<br>
2026-11-02_homedepot.jpg &middot; Nov 2 &middot; Home Depot &middot; $186.43 &middot; tax $15.12 &middot; Visa 4411 &middot; lumber, screws<br>
2026-11-03_shell.jpg &middot; Nov 3 &middot; Shell &middot; $61.05 &middot; tax UNCLEAR &middot; Visa 4411 &middot; fuel<br>
2026-11-04_cafe.jpg &middot; Nov 4 &middot; Corner Cafe &middot; $38.90 &middot; tax $3.10 &middot; cash &middot; 2 lunches<br>
2026-11-05_ferguson.jpg &middot; Nov 5 &middot; Ferguson &middot; UNCLEAR &middot; &mdash; &middot; Visa 4411 &middot; pipe fittings<br>
2026-11-06_motel.jpg &middot; Nov 6 &middot; Valley Inn &middot; $129.00 &middot; tax $13.55 &middot; Visa 4411 &middot; 1 night<br>
<b>What he does next:</b> He reads the Ferguson total from the paper receipt ($94.30) and fixes the row. He matches 4 rows to his card statement. The cash lunch has a note on the back naming the client and the job, so he keeps the photo of both sides. The motel receipt stays on file: lodging always needs one.</div>

<h2>How do you check AI receipt scanning results?</h2>
<ol>
<li><b>Count photos in, rows out.</b> Five photos, five rows.</li>
<li><b>Check every UNCLEAR field</b> against the original receipt, then fix it by hand.</li>
<li><b>Tie each total to a bank or card line.</b> If the amounts differ, the receipt or the posting is wrong. Find out which.</li>
<li><b>Open the image, not just the table.</b> The table is a summary. The image is the record.</li>
<li><b><a href="/ai-accounting/ai-bank-reconciliation/">Reconcile the account</a></b> at month-end. If your software doesn&rsquo;t tie out, the month isn&rsquo;t done.</li>
</ol>

<h2>Can you throw away the paper receipt?</h2>
<p>Sometimes, but be careful. The IRS rule for electronic storage, Revenue Procedure 97-22, allows scanned images if they&rsquo;re highly legible, indexed so you can find them, and kept with controls that protect their accuracy. It lets you destroy the paper only after you&rsquo;ve tested that your electronic copies meet those rules and you have a process to keep meeting them. <b>If a photo isn&rsquo;t sharp enough to read every number, keep the paper.</b></p>

<h2>What AI receipt scanning can&rsquo;t do</h2>
<p>It can&rsquo;t tell whether an expense was for business; you can. It can&rsquo;t apply tax limits like the general 50% limit on business meals; your books and your return do that. And it can&rsquo;t take responsibility for your return. That stays with you.</p>
<p>For the full routine, see <a href="/ai-accounting/how-to-use-ai-for-bookkeeping/">how to use AI for bookkeeping</a>. Or hand the whole pile to us:</p>''',
 'Send us the photos and we&rsquo;ll do the rest. At <a href="CTAURL">Computatio</a>, AI reads and matches your receipts, and an accountant reviews every account each month. Monthly Books is $500 a month.',
 [("IRS: Publication 583, Starting a Business and Keeping Records","https://www.irs.gov/publications/p583"),
  ("IRS: What kind of records should I keep","https://www.irs.gov/businesses/small-businesses-self-employed/what-kind-of-records-should-i-keep"),
  ("IRS: Instructions for Form 2106 (2025), Recordkeeping","https://www.irs.gov/instructions/i2106"),
  ("IRS: Revenue Procedure 97-22, electronic storage of records","https://www.irs.gov/pub/irs-tege/rp-97-22.pdf"),
  ("California FTB: Keeping your tax records","https://www.ftb.ca.gov/file/after-you-file/keeping-your-tax-records.html")],
 "ai-receipt-scanning"),
article("/ai-accounting/google-sheets-canvas-cash-flow-planner/","/ai-accounting/","AI for Accounting",
 "Google Sheets canvas: build a cash flow what-if tool",
 "Google Sheets canvas: build a cash flow what-if tool",
 "Use Google Sheets canvas to turn a 13-week cash flow sheet into a what-if tool with sliders, then check it against your reconciled bank balance.",
 "2026-11-05",
 "A client says they&rsquo;ll pay &ldquo;next month.&rdquo; Sales feel slower. A tax payment is due in January. You want to know one thing: will there be enough in the bank?",
 '''<div class="callout"><b>Quick answer:</b> as of November 5, 2026, Gemini in Google Sheets can turn a sheet into an interactive mini-app called a <b>canvas</b>. Open your cash flow sheet and choose <b>Insert &gt; Create a canvas</b>, then ask for sliders on sales, costs and payment timing. Google lists it for Google AI Pro and Ultra, Workspace Business and Enterprise Standard and Plus, and Google AI Pro for Education, in English, on the web. <b>Start from your reconciled bank balance, and check that the canvas&rsquo;s base case matches the sheet.</b></div>

<h2>You&rsquo;re guessing at next month&rsquo;s bank balance</h2>
<p>Your profit and loss shows what happened. It doesn&rsquo;t show when cash will land or leave. Income can look fine while the account runs thin, because a client pays late or a big bill hits in the same week.</p>
<p><b>Profit is not cash.</b> A cash flow forecast fills that gap, week by week.</p>

<h2>And every &ldquo;what if&rdquo; means rebuilding the spreadsheet</h2>
<p>What if sales drop 20%? What if the big client pays six weeks late? In a normal sheet, you change cells, copy tabs, and lose track of which version is which. Most owners stop after one try.</p>

<h2>What it costs to fly blind</h2>
<ul>
<li><b>Tax dates don&rsquo;t move.</b> The fourth IRS estimated tax payment for 2026 is due January 15, 2027. California&rsquo;s fourth payment, 30% of the year&rsquo;s required amount, is due the same day.</li>
<li><b>Short weeks surprise you.</b> You find out the account is low when a payment bounces, not when you could still plan around it.</li>
<li><b>Bad starting numbers spread.</b> A forecast built on an unreconciled balance is wrong in every week after the first.</li>
</ul>

<h2>Picture this instead</h2>
<p>One tab holds 13 weeks of cash in and out, starting from the balance you reconciled. Next to it, a canvas with three sliders. You drag &ldquo;client pays late&rdquo; to six weeks and see the lowest week turn yellow. <b>You decide what to delay or chase while there&rsquo;s still time.</b></p>

<h2>What is Google Sheets canvas?</h2>
<p>Google announced Sheets canvas on August 13, 2026. Gemini builds a custom layout, such as a dashboard or a scenario model, on top of one tab of your data. Google calls it read-write: <b>if you have edit access, changes you make in the canvas change the sheet</b>, and changes in the sheet show in the canvas. Google&rsquo;s help page says access to a canvas is the same as access to the sheet. A Google Workspace post from September 10 lists a financial scenario model, where you adjust key assumptions and see the effect, as one of its examples.</p>
<p><b>Who gets it:</b> Google AI Pro and Ultra personal plans; Workspace Business and Enterprise Standard and Plus; and Google AI Pro for Education. Google&rsquo;s help page also says personal accounts may be able to use it up to 3 times a month. It&rsquo;s English only and not in the Sheets mobile app.</p>

<h2>The 13-week method for a Google Sheets canvas cash flow tool</h2>
<ol>
<li><b>Reconcile first.</b> <a href="/ai-accounting/ai-bank-reconciliation/">Reconcile your business bank account</a> through the last statement. That ending balance is your opening cash. Not the bank app&rsquo;s number today, and not a guess.</li>
<li><b>Build one tab.</b> Canvas reads one tab, so put everything there: a row of assumptions at the top (weekly sales, weekly costs, sales change %, weeks the big client is late), then 13 rows, one per week, with cash in, cash out and ending balance as formulas. Add fixed items on their dates: rent, loan payments, and the January 15 estimated tax payments. If your forecast is in Excel, use File &gt; Save as Google Sheets first.</li>
<li><b>Work on a copy.</b> Because the canvas writes to the sheet, make a copy of the file to experiment in. Keep the original as your base case.</li>
<li><b>Open canvas.</b> Choose <b>Insert &gt; Create a canvas</b>. Google&rsquo;s help page also lists Tools &gt; Create canvas and the Canvas menu in the bottom bar.</li>
<li><b>Paste the prompt below,</b> then refine it with follow-up prompts.</li>
</ol>

<div class="callout"><b>Prompt to copy:</b><br>
Build a cash flow what-if tool from this tab. Show a slider for &ldquo;Sales change %&rdquo; (&minus;50 to +20), a slider for &ldquo;Weekly costs&rdquo;, and a slider for &ldquo;Weeks the big client pays late&rdquo; (0 to 8). The sliders should change only the assumption cells at the top. Do not change any weekly rows or formulas. Show a line chart of ending cash for all 13 weeks, the lowest week and its balance, and color any week below $5,000 yellow and below $0 red. Show the base-case numbers next to the scenario so I can compare.</div>

<p>Don&rsquo;t put account numbers, client names or anything sensitive in the sheet or the prompt. Use labels like &ldquo;Client A.&rdquo; Our <a href="/ai-accounting/financial-data-safety-ai/">guide to keeping financial data safe with AI</a> covers the rest.</p>

<div class="callout"><b>Example (made-up data).</b> A one-person agency starts the week of November 9 with $9,200, the reconciled October 31 balance. Base case: $3,800 a week in, $3,300 a week out, rent of $1,800 in weeks 4, 8 and 13, a $6,000 client payment in week 3, and $4,700 of estimated tax in week 10 (the week of January 15).<br>
<b>Base case:</b> lowest week is week 1 at $9,700; week 13 ends at $11,600.<br>
<b>Client pays 6 weeks late:</b> lowest week drops to $9,400 in week 4; week 13 still ends at $11,600.<br>
<b>Late client and sales down 20%:</b> week 8 falls to $3,520 and week 13 ends at $1,720.<br>
<b>What the owner does next:</b> she sends the client a reminder now, moves a planned equipment purchase out of December, and keeps the January tax money in a separate savings account.</div>

<h2>How to check the canvas before you trust it</h2>
<ol>
<li><b>Set every slider to zero change.</b> The canvas&rsquo;s numbers must equal the sheet&rsquo;s base case, week by week. Click <b>View data</b> to see the rows behind it.</li>
<li><b>Tie the opening balance</b> to your last bank reconciliation. If they differ, fix the sheet, not the canvas.</li>
<li><b>Recalculate one week by hand.</b> Opening cash plus cash in minus cash out should equal the ending balance shown.</li>
<li><b>Check the sheet after you play.</b> Open the tab and confirm only the assumption cells changed. If a formula was overwritten, undo it or go back to your original.</li>
<li><b>Each month, compare the forecast to actuals</b> from your <a href="/ai-accounting/read-profit-and-loss-with-ai/">profit and loss</a> and bank statement. Adjust the assumptions that were wrong.</li>
</ol>

<h2>What Google Sheets canvas can&rsquo;t do for your cash flow</h2>
<p>Google&rsquo;s help page says not to rely on Gemini features for financial or other professional advice, so review what it builds. A forecast is a planning tool, not a promise: it&rsquo;s only as good as the assumptions you type in. It doesn&rsquo;t replace reconciling, keeping receipts, or making your tax payments on time. Canvas also won&rsquo;t open if downloading, copying or printing is turned off for the file, and the source data must stay under 1 million cells.</p>
<p>You don&rsquo;t need formula skills beyond simple addition to start. If the sheet itself is the hard part, see <a href="/ai-accounting/ai-excel-google-sheets-bookkeeping/">AI for Excel and Google Sheets bookkeeping</a> and our <a href="/estimated-taxes/quarterly-estimated-taxes-california/">estimated tax guide</a> for the payment amounts.</p>
<p>A forecast is only as good as the books under it. Want those handled?</p>''',
 'Want books you can forecast from? At <a href="CTAURL">Computatio</a>, AI does the first pass and an accountant reviews and reconciles every account each month, so your opening balance is one you can trust. Monthly Books is $500 a month.',
 [("Google: Build mini-apps with Gemini in Google Sheets (Aug 13, 2026)","https://blog.google/products-and-platforms/products/workspace/sheets-canvas-for-google-sheets-spreadsheets/"),
  ("Google Docs Editors Help: Create a Sheets canvas","https://support.google.com/docs/answer/17035851?hl=en"),
  ("Google Workspace: 6 mini-apps you can create with Sheets canvas (Sep 10, 2026)","https://workspace.google.com/blog/product-announcements/turn-your-data-into-action-6-mini-apps-you-can-create-with-sheets-canvas"),
  ("IRS: 2026 Form 1040-ES, Estimated Tax for Individuals","https://www.irs.gov/pub/irs-pdf/f1040es.pdf"),
  ("California FTB: 2026 Instructions for Form 540-ES","https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html")],
 "google-sheets-canvas-cash-flow-planner"),
article("/ai-accounting/financial-data-safety-ai/","/ai-accounting/","AI for Accounting",
 "How to Keep Your Financial Data Safe When Using AI",
 "How to keep your financial data safe when you use AI",
 "Keep financial data safe when you use AI for bookkeeping: what to strip out, a redaction prompt, a made-up example, and the IRS and FTC steps that matter.",
 "2026-11-06",
 "You want AI to sort your transactions. But the export has your account number, your clients&rsquo; names and maybe a Social Security number. You&rsquo;re not sure what&rsquo;s safe to paste.",
 '''<div class="callout"><b>Quick answer:</b> to keep financial data safe when you use AI, share only what the task needs. Strip out Social Security numbers, full account and card numbers, passwords and login codes before you upload anything. Replace names with labels like &ldquo;Client A.&rdquo; Turn on multi-factor authentication for your AI, bank and tax accounts, and keep the original files in your own records, not in a chat.</div>

<h2>You don&rsquo;t know what the AI keeps</h2>
<p>A bank export looks harmless. It isn&rsquo;t. It can hold full account numbers, payee names, client names and notes you typed years ago.</p>
<p><b>Once you paste it into a chat, you&rsquo;ve handed it to another company&rsquo;s system.</b> Whether it&rsquo;s stored, reviewed or used to improve the tool depends on that tool&rsquo;s settings and your plan.</p>

<h2>And scammers know you&rsquo;re busy with your books</h2>
<p>Tax season brings fake &ldquo;IRS&rdquo; emails and texts. A rushed owner who just uploaded a stack of documents is an easy target for a message that says &ldquo;verify your account.&rdquo;</p>

<h2>What a slip can cost you</h2>
<ul>
<li><b>Identity theft is slow to undo.</b> A stolen Social Security number can be used to file a fake return in your name. Fixing that means reports, affidavits and letters, while your real refund or account waits.</li>
<li><b>Client data isn&rsquo;t only yours.</b> The FTC tells businesses to use Social Security numbers only for required and lawful purposes, and not to keep card numbers and expiration dates without an essential business need.</li>
<li><b>Fake messages look real.</b> The IRS says a letter or notice is the first way it contacts you. It doesn&rsquo;t make initial contact by email or social media, and it sends texts only with your permission.</li>
</ul>

<h2>Picture this instead</h2>
<p>You keep one clean working file for AI: dates, amounts, vendor names and categories. No account numbers. No client names. No IDs. <b>If that file leaked tomorrow, it wouldn&rsquo;t open a single account.</b> You get the time savings, and your originals stay locked in your own records.</p>

<h2>The share-the-minimum method for AI and financial data</h2>
<p>This works with any AI chat tool. It follows the FTC&rsquo;s five principles for protecting personal information: take stock, scale down, lock it, pitch it, and plan ahead.</p>
<ol>
<li><b>Take stock.</b> Before you upload, open the file and look. List what&rsquo;s in it: account numbers, names, addresses, tax IDs, notes.</li>
<li><b>Scale down.</b> Delete every column the task doesn&rsquo;t need. To categorize transactions, the AI needs the date, description and amount. It doesn&rsquo;t need your account number or balance.</li>
<li><b>Swap names for labels.</b> Replace client and employee names with &ldquo;Client A,&rdquo; &ldquo;Contractor B.&rdquo; Keep the key that maps labels to names in your own files.</li>
<li><b>Check the tool&rsquo;s settings.</b> Find out whether chats are saved, and whether you can turn off use of your chats for training. Business plans often have different terms than free ones. Read them on the vendor&rsquo;s own site.</li>
<li><b>Lock your accounts.</b> The IRS recommends strong, unique passwords for each account and multi-factor authentication wherever it&rsquo;s offered. Do that for your AI tool, your email, your bank and your bookkeeping software.</li>
<li><b>Pitch it.</b> Delete old chats and uploads you no longer need. Keep the real records in your bookkeeping system, where they belong.</li>
</ol>

<div class="callout"><b>Prompt to copy (run it on a file you&rsquo;ve already trimmed):</b><br>
&ldquo;Before you do anything else, scan this data for sensitive details: Social Security or tax ID numbers, full bank or card numbers (more than the last 4 digits), routing numbers, passwords, login codes, home addresses, birth dates and personal names. List each one you find by row. Don&rsquo;t repeat the full value; show only the last 4 characters. Then stop and wait. Don&rsquo;t categorize or summarize anything until I confirm the data is clean.&rdquo;</div>
<p><b>This is a second check, not the first.</b> The safest data is the data you deleted before you uploaded it.</p>

<div class="callout"><b>Example (made-up data).</b> A freelance designer exports 3 months of bank transactions to categorize. The raw file has 7 columns: date, description, amount, balance, account number, check number and memo.<br>
<b>Step 1:</b> She deletes balance, account number and check number. Four columns left.<br>
<b>Step 2:</b> The memo column has &ldquo;Invoice 1042 &ndash; Maria Lopez&rdquo; and &ldquo;Rent &ndash; 418 Elm St.&rdquo; She replaces the names with &ldquo;Client A&rdquo; and deletes the address.<br>
<b>Step 3:</b> She runs the scan prompt. The AI flags one row: a Zelle description that includes a phone number ending in 5521. She deletes it from the description.<br>
<b>Step 4:</b> Now she runs her <a href="/ai-accounting/ai-prompts-categorize-transactions/">categorization prompt</a> on the clean file and posts the results in her books.</div>

<h2>What should you never paste into AI?</h2>
<ul>
<li><b>Social Security numbers, ITINs and EINs</b> (yours, your family&rsquo;s or anyone you pay).</li>
<li><b>Full bank, card and routing numbers.</b> The last 4 digits are enough to tell accounts apart.</li>
<li><b>Passwords, PINs and one-time login codes.</b> No AI task needs them.</li>
<li><b>Your IRS Identity Protection PIN.</b> Treat it like a password.</li>
<li><b>Whole tax returns and W-2s.</b> If you need help with one line, type the line, not the form.</li>
<li><b>Receipt photos with card numbers showing.</b> Crop them first, as our <a href="/ai-accounting/ai-receipt-scanning/">receipt scanning guide</a> shows.</li>
</ul>

<h2>How to keep your financial data safe beyond the chat</h2>
<ol>
<li><b>Get an IRS Identity Protection PIN.</b> It&rsquo;s a six-digit number that stops anyone else from filing a federal return with your Social Security number. Anyone with an SSN or ITIN who can verify their identity can get one through their IRS online account. It&rsquo;s good for one calendar year, and a new one is issued each year.</li>
<li><b>Encrypt files you keep.</b> The IRS suggests encrypting tax records stored on your computer and running security software with automatic updates.</li>
<li><b>Don&rsquo;t email sensitive files unprotected.</b> The FTC warns against sending sensitive information through regular, unencrypted email.</li>
<li><b>Vet anyone you hand your books to.</b> The FTC tells businesses to check a provider&rsquo;s security practices before outsourcing, and to put security expectations in writing. That applies to AI apps and bookkeepers alike.</li>
<li><b>Ignore &ldquo;verify your account&rdquo; messages.</b> Go to the site yourself instead of clicking a link.</li>
</ol>

<div class="callout"><b>State note.</b> States run their own identity theft processes. In California, the Franchise Tax Board takes reports online, by phone at 916-845-7088, or by mail or fax with its Identity Theft Affidavit, Form FTB 3552. Report to the FTC at IdentityTheft.gov and to the IRS as well.</div>

<h2>Can AI still help if you remove all that?</h2>
<p>Yes. Categorizing, spotting duplicates, matching receipts and drafting reports work fine with dates, amounts and vendor names. <b>AI almost never needs the details that make data dangerous.</b> You also don&rsquo;t need to be technical: deleting columns in a spreadsheet is the whole skill.</p>
<p>What AI can&rsquo;t do is take responsibility for your records. You still <a href="/ai-accounting/ai-bank-reconciliation/">reconcile every account</a>, keep your receipts, and own your tax return. For the full routine, see <a href="/ai-accounting/how-to-use-ai-for-bookkeeping/">how to use AI for bookkeeping</a> and <a href="/ai-accounting/can-ai-do-your-accounting/">what AI gets right and wrong</a>.</p>
<p>Rather not trim files every month? We can handle that for you.</p>''',
 'Want the time savings without the data handling? At <a href="CTAURL">Computatio</a>, AI does the first pass on your books and an accountant reviews every account each month. Monthly Books is $500 a month.',
 [("FTC: Protecting Personal Information, A Guide for Business","https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business"),
  ("IRS: Taxes. Security. Together.","https://www.irs.gov/individuals/taxes-security-together"),
  ("IRS: Get an identity protection PIN","https://www.irs.gov/identity-theft-fraud-scams/get-an-identity-protection-pin"),
  ("IRS: Ways to tell if the IRS is reaching out or if it&rsquo;s a scammer","https://www.irs.gov/newsroom/ways-to-tell-if-the-irs-is-reaching-out-or-if-its-a-scammer"),
  ("California FTB: Identity theft","https://www.ftb.ca.gov/help/scams/identity-theft.html")],
 "financial-data-safety-ai"),
article("/ai-accounting/chart-of-accounts-with-ai/","/ai-accounting/","AI for Accounting",
 "Chart of Accounts With AI: Build Yours (Free Template)",
 "Chart of accounts with AI: build yours (free template)",
 "Build a small-business chart of accounts with AI: a free template mapped to Schedule C, a copy-paste prompt, a made-up example and how to check it.",
 "2026-11-09",
 "Your software came with 80 accounts you never asked for. Half your spending lands in &ldquo;Miscellaneous,&rdquo; and you&rsquo;re not sure which account a new charge belongs in.",
 '''<div class="callout"><b>Quick answer:</b> A chart of accounts is the list of buckets your books sort every dollar into: assets, liabilities, equity, income and expenses. To build one with AI, give it your business type and how you get paid, and ask for a short list of accounts with a number, a type and a one-line description, with each expense account tied to a Schedule C line. Then you trim it, check it against the 2025 Schedule C, and load it into your software. Keep it short: about 20 to 35 accounts covers most one-person businesses.</div>

<h2>Your chart of accounts is a junk drawer</h2>
<p>Some accounts you never use. Some overlap, like &ldquo;Software,&rdquo; &ldquo;Subscriptions&rdquo; and &ldquo;Dues.&rdquo; And one account, &ldquo;Other,&rdquo; holds a third of your spending.</p>
<p><b>When the buckets are wrong, every report built on them is wrong too.</b></p>

<h2>And tax time means sorting it all again</h2>
<p>Your accounts don&rsquo;t match the lines on your tax return. So each spring, you or someone you pay re-sorts a year of expenses by hand to fit Schedule C.</p>

<h2>What a messy chart of accounts costs you</h2>
<ul>
<li><b>Some lines have their own rules.</b> The 2025 Schedule C instructions say most business meals are only 50% deductible, and meals go on line 24b, apart from travel on line 24a. Lump them into &ldquo;Travel&rdquo; and the limit gets missed.</li>
<li><b>Some costs aren&rsquo;t deductible at all.</b> The same instructions say you can&rsquo;t deduct the base rate of the first phone line into your home. A vague &ldquo;Utilities&rdquo; account hides that.</li>
<li><b>&ldquo;Other&rdquo; still needs detail.</b> For 2025, other expenses are listed in Part V (line 48) and carried to line 27b. A big catch-all account means itemizing it later anyway.</li>
<li><b>Your records stay around.</b> The IRS says to keep most records at least 3 years, and employment tax records at least 4. A clear chart makes old records readable when you need them.</li>
</ul>

<h2>Picture books that sort themselves into your tax return</h2>
<p>Every expense account points to one Schedule C line. At year-end you run a profit and loss report, and it already reads like your return. Nothing is labeled &ldquo;Other&rdquo; without a reason.</p>
<p><b>You spend tax season checking numbers, not re-sorting them.</b></p>

<h2>Free chart of accounts template for a small business</h2>
<p>Start here and delete what you don&rsquo;t use. The numbering is a common pattern, not a rule: 1000s assets, 2000s liabilities, 3000s equity, 4000s income, 5000s cost of goods, 6000s expenses. Line numbers are from the 2025 Schedule C.</p>
<table>
<tr><th>#</th><th>Account</th><th>Type</th><th>Schedule C line</th></tr>
<tr><td>1000</td><td>Business checking</td><td>Asset</td><td>&mdash;</td></tr>
<tr><td>1200</td><td>Accounts receivable</td><td>Asset</td><td>&mdash;</td></tr>
<tr><td>2000</td><td>Business credit card</td><td>Liability</td><td>&mdash;</td></tr>
<tr><td>2200</td><td>Sales tax payable (if you collect it)</td><td>Liability</td><td>&mdash;</td></tr>
<tr><td>3000</td><td>Owner contributions</td><td>Equity</td><td>&mdash;</td></tr>
<tr><td>3100</td><td>Owner draws</td><td>Equity</td><td>&mdash;</td></tr>
<tr><td>4000</td><td>Sales or service income</td><td>Income</td><td>1</td></tr>
<tr><td>5000</td><td>Cost of goods sold (product sellers)</td><td>Cost of goods</td><td>Part III, to line 4</td></tr>
<tr><td>6000</td><td>Advertising</td><td>Expense</td><td>8</td></tr>
<tr><td>6100</td><td>Car and truck expenses</td><td>Expense</td><td>9</td></tr>
<tr><td>6150</td><td>Commissions and fees</td><td>Expense</td><td>10</td></tr>
<tr><td>6200</td><td>Contract labor</td><td>Expense</td><td>11</td></tr>
<tr><td>6300</td><td>Insurance (other than health)</td><td>Expense</td><td>15</td></tr>
<tr><td>6400</td><td>Legal and professional services</td><td>Expense</td><td>17</td></tr>
<tr><td>6500</td><td>Office expense</td><td>Expense</td><td>18</td></tr>
<tr><td>6550</td><td>Rent: other business property</td><td>Expense</td><td>20b</td></tr>
<tr><td>6600</td><td>Supplies</td><td>Expense</td><td>22</td></tr>
<tr><td>6650</td><td>Taxes and licenses</td><td>Expense</td><td>23</td></tr>
<tr><td>6700</td><td>Travel</td><td>Expense</td><td>24a</td></tr>
<tr><td>6750</td><td>Business meals</td><td>Expense</td><td>24b</td></tr>
<tr><td>6800</td><td>Utilities</td><td>Expense</td><td>25</td></tr>
<tr><td>6900</td><td>Software and subscriptions</td><td>Expense</td><td>Part V, to 27b</td></tr>
<tr><td>6950</td><td>Education and training</td><td>Expense</td><td>Part V, to 27b</td></tr>
</table>
<p>Owner draws and contributions are not income or expenses. They track money moving between you and the business. Home office costs usually aren&rsquo;t a chart account; they&rsquo;re figured separately and go on line 30.</p>

<div class="callout"><b>State note.</b> In California, the CDTFA says you need a seller&rsquo;s permit (there&rsquo;s no fee) if you sell or lease goods that would normally be subject to sales tax, and you must report and pay that tax. If that&rsquo;s you, keep a &ldquo;Sales tax payable&rdquo; account so the tax you collect isn&rsquo;t mixed into your sales. Other states have their own rules; check your state&rsquo;s tax agency.</div>

<h2>How to build a chart of accounts with AI: the 4-step method</h2>
<p>This works in ChatGPT, Claude, Gemini or Copilot. You don&rsquo;t need to be technical, and you don&rsquo;t need to share any bank data to do it.</p>
<ol>
<li><b>Describe your business in three lines.</b> What you sell, how customers pay you, and your five biggest costs. No names or account numbers; see our <a href="/ai-accounting/financial-data-safety-ai/">data safety guide</a>.</li>
<li><b>Run the prompt below.</b> It asks for a short list, each account tied to a tax line, with a reason.</li>
<li><b>Trim and rename.</b> Delete accounts you won&rsquo;t use this year. Merge any two you can&rsquo;t tell apart. Use the plain names you&rsquo;d search for.</li>
<li><b>Load it and test it.</b> Enter the accounts in your software, then sort one month of transactions into them with our <a href="/ai-accounting/ai-prompts-categorize-transactions/">AI prompts to categorize transactions</a>. Any charge with no clear home means a missing account or a fuzzy description.</li>
</ol>

<div class="callout"><b>Prompt you can copy:</b><br>&ldquo;Build a chart of accounts for a sole proprietor who [what you do]. Customers pay by [methods]. Main costs: [list]. I [do / don&rsquo;t] sell physical products and [do / don&rsquo;t] collect sales tax. Return a table with account number, account name, type (asset, liability, equity, income, cost of goods, expense), a one-line description of what goes in it, and the 2025 Schedule C line each income and expense account rolls up to. Keep it under 35 accounts. Keep meals separate from travel. Don&rsquo;t include accounts I didn&rsquo;t describe a need for, and flag any line you&rsquo;re unsure about instead of guessing.&rdquo;</div>

<div class="callout"><b>Example (made-up data).</b> A freelance web designer runs the prompt. She&rsquo;s paid by bank transfer and card through an online invoicing tool. Her main costs are software, a coworking desk, contractors and a laptop.<br>
AI returns 24 accounts. Three come back flagged: &ldquo;Laptop: expense or equipment? Depends on cost and how you handle depreciation; ask your tax preparer.&rdquo; &ldquo;Coworking desk: rent (20b) or office expense (18)?&rdquo; &ldquo;Card processing fees: confirm line 10.&rdquo;<br>
<b>Result:</b> She deletes four accounts she&rsquo;ll never use, settles the three flags with her tax preparer, and loads 20 accounts.</div>

<h2>How do you check an AI chart of accounts?</h2>
<ol>
<li><b>Check every Schedule C line</b> against the 2025 form. A line number AI got wrong will follow you all year.</li>
<li><b>Look for the balance sheet.</b> You need at least one bank account, any credit cards, and owner draws and contributions. Without them, you can&rsquo;t reconcile; see <a href="/ai-accounting/ai-bank-reconciliation/">AI bank reconciliation</a>.</li>
<li><b>Keep &ldquo;Other&rdquo; small.</b> If one account would hold more than a few percent of your spending, give it a real name.</li>
</ol>

<h2>Limits: what AI can&rsquo;t decide for you</h2>
<p>AI doesn&rsquo;t know your facts. Whether a laptop is depreciated, whether a car cost is business, or how much of your phone is business use all depend on your records. IRS Publication 583 says you can use any recordkeeping system that clearly shows your income and expenses, and notes that double-entry bookkeeping has built-in checks. <b>A good chart is the start; reconciling every month keeps it honest.</b></p>
<p>New to all this? Read <a href="/bookkeeping/do-your-own-bookkeeping/">how to do your own bookkeeping</a> and <a href="/ai-accounting/separate-business-personal-expenses-ai/">how to separate business and personal expenses with AI</a>. Want the chart built and kept clean for you?</p>''',
 'Let us set up your chart of accounts and keep it clean. At <a href="CTAURL">Computatio</a>, AI does the monthly bookkeeping and an accountant reviews every account. Monthly Books is $500 a month.',
 [("IRS: Instructions for Schedule C (Form 1040) (2025)","https://www.irs.gov/instructions/i1040sc"),
  ("IRS: Schedule C (Form 1040) 2025","https://www.irs.gov/pub/irs-prior/f1040sc--2025.pdf"),
  ("IRS: Publication 583, Starting a Business and Keeping Records","https://www.irs.gov/publications/p583"),
  ("IRS: How long should I keep records?","https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records"),
  ("CDTFA: Obtaining a seller's permit","https://cdtfa.ca.gov/taxes-and-fees/faqseller.htm")],
 "chart-of-accounts-with-ai"),
article("/ai-accounting/quickbooks-chatgpt-claude-invoices/","/ai-accounting/","AI for Accounting",
 "QuickBooks in ChatGPT or Claude: check invoices first",
 "QuickBooks in ChatGPT or Claude: check invoices first",
 "How to connect QuickBooks to ChatGPT or Claude, draft an invoice from a chat, and check it in QuickBooks before it goes to your customer.",
 "2026-11-10",
 "You finish a job, open ChatGPT or Claude, and type &ldquo;invoice Acme for the logo work.&rdquo; Seconds later there&rsquo;s an invoice. It feels like magic, until you wonder what it just wrote into your books.",
 '''<div class="callout"><b>Quick answer:</b> as of November 10, 2026, Intuit says invoicing through QuickBooks in ChatGPT and Claude is generally available, for US QuickBooks customers on Simple Start through Advanced. The connectors themselves are still labeled beta. <b>An invoice the chatbot creates is a real invoice in QuickBooks right away.</b> Open it in QuickBooks and check the customer, items, amounts, tax, terms and due date before you send it.</div>

<h2>You typed a sentence, and now there&rsquo;s an invoice in your books</h2>
<p>Intuit&rsquo;s Claude help page says every invoice Claude creates lands in QuickBooks right away. There is no draft folder in the chat. The record exists the moment it&rsquo;s made.</p>
<p><b>The chat is the shortcut. QuickBooks is still the record.</b></p>

<h2>And you can&rsquo;t see what it guessed</h2>
<p>A chatbot fills gaps. If two customers have similar names, it may pick the wrong one. If you said &ldquo;the usual rate,&rdquo; it has to decide what that means. If you didn&rsquo;t give a due date, it uses something. None of that is obvious from a one-line reply in the chat window.</p>

<h2>What a wrong invoice costs you</h2>
<ul>
<li><b>Wrong numbers in your reports.</b> An invoice adds to what customers owe you. A wrong amount or a duplicate inflates your income and receivables until someone finds it.</li>
<li><b>An awkward customer email.</b> A wrong name, rate or due date that reaches the customer has to be voided and explained.</li>
<li><b>Weak backup for your return.</b> The IRS lists invoices among the documents that support your gross receipts. An invoice that doesn&rsquo;t match the work is poor support.</li>
<li><b>Records you must keep.</b> The IRS says to keep supporting records until the period of limitations ends, generally 3 years after you file, and longer in some cases.</li>
</ul>

<h2>Picture invoicing in two minutes</h2>
<p>You finish a job and ask the chatbot for the invoice. You open the link in QuickBooks, compare it to your estimate, fix one line, and send. At month-end, your open invoices match what customers really owe.</p>
<p><b>The AI does the typing. You keep the judgment.</b></p>

<h2>Who can use QuickBooks in ChatGPT or Claude?</h2>
<table>
<tr><th></th><th>Claude connector</th><th>ChatGPT plugin</th></tr>
<tr><td>QuickBooks plans</td><td colspan="2">Simple Start through Advanced, per Intuit&rsquo;s fall 2026 release</td></tr>
<tr><td>Where</td><td>US customers only</td><td>US QuickBooks Online customers</td></tr>
<tr><td>Chatbot account</td><td>An active Claude account</td><td>A ChatGPT account; Intuit&rsquo;s page names no plan</td></tr>
<tr><td>What Intuit lists</td><td colspan="2">Create, update and send invoices, reminders for overdue invoices, estimates and payment links. The Claude page also lists importing transactions and P&amp;L and cash flow reports.</td></tr>
</table>
<p>Intuit notes that the AI platform itself may need a paid subscription. Some features, such as payment links, require QuickBooks Payments, and collecting estimate deposits does too.</p>

<h2>The connect, draft, check, send method</h2>
<ol>
<li><b>Connect with the fewest permissions you need.</b> In Claude, go to <b>Customize</b>, then <b>Connectors</b>, find <b>QuickBooks</b> and select <b>Connect</b>. Sign in to Intuit, pick the company and choose which permissions to grant. A checkmark shows it worked. In ChatGPT, open <b>Plugins</b>, search &ldquo;Intuit QuickBooks,&rdquo; select <b>Connect Intuit QuickBooks</b>, sign in, then select <b>Start chat</b>.</li>
<li><b>Give the chatbot everything, so it guesses nothing.</b> Use the exact customer name as it appears in QuickBooks, each item or service, quantity, rate, date and terms. Use this prompt:</li>
</ol>
<div class="callout"><b>Prompt.</b> Create one invoice in QuickBooks. Don&rsquo;t send it. Customer: [exact customer name]. Invoice date: [date]. Terms: [Net 15, Net 30]. Lines: [product or service, quantity, rate] for each. If the customer, any product or the tax setting doesn&rsquo;t match an existing record exactly, stop and ask me instead of creating anything. When you&rsquo;re done, list the invoice number, total, due date and a link to open it in QuickBooks.</div>
<ol start="3">
<li><b>Open it in QuickBooks, not just in the chat.</b> Compare it line by line to the estimate, contract or job notes.</li>
<li><b>Only then ask it to send.</b> Intuit says nothing sends until you approve it. Read the email and the reminder text before you say yes.</li>
<li><b>Tie any number it quotes back to QuickBooks.</b> If it tells you your profit for October, run the profit and loss report for the same dates and make sure the totals agree. Our guide to <a href="/ai-accounting/read-profit-and-loss-with-ai/">reading your profit and loss with AI</a> shows what to look for.</li>
</ol>

<div class="callout"><b>Example (made-up data).</b> A one-person design studio types: &ldquo;Invoice Acme Co for the October logo project.&rdquo; The chatbot creates invoice #1051 for $1,800, due on receipt. The check in QuickBooks finds three problems:<br>
&middot; The customer is <b>Acme Corp</b>, a different client. The right record is <b>Acme Co (Riverside)</b>.<br>
&middot; The estimate says $1,500 for the logo plus $300 for a brand sheet, as two lines. The invoice shows one $1,800 line.<br>
&middot; The contract says Net 15, not due on receipt.<br>
Fix: delete the wrong invoice (the chatbot asks you to confirm deletions first), rerun the prompt with the exact name, two lines and Net 15, recheck, then send.</div>

<h2>How to check a QuickBooks invoice from ChatGPT or Claude</h2>
<ol>
<li><b>Customer:</b> the exact record, with the right email address.</li>
<li><b>Lines:</b> each product or service, quantity and rate match the estimate or contract.</li>
<li><b>Sales tax:</b> taxable lines marked as taxable, others not.</li>
<li><b>Dates and terms:</b> invoice date, terms and due date match your agreement.</li>
<li><b>No duplicates:</b> filter open invoices by that customer. One job, one invoice.</li>
<li><b>Reminders:</b> read each one before it goes. Don&rsquo;t remind a customer who already paid.</li>
</ol>
<div class="callout"><b>State note.</b> Sales tax on invoices depends on your state and what you sell. In California, the CDTFA says a charge for a service alone is generally not taxable, but if you regularly sell goods to customers you generally need a seller&rsquo;s permit. Check your state&rsquo;s rules before you set tax on a product.</div>

<h2>Is it safe to connect QuickBooks to a chatbot?</h2>
<p>The connection signs in through Intuit, and Intuit&rsquo;s Claude page says QuickBooks data isn&rsquo;t used to train Claude. Still, you are giving a chat tool the power to change your books. Grant only what you&rsquo;ll use, and read our guide to <a href="/ai-accounting/financial-data-safety-ai/">keeping financial data safe with AI</a> first.</p>
<p>To stop, disconnect. In Claude, go to <b>Settings</b>, then <b>Connectors</b>. In ChatGPT, use the plugins list.</p>
<p><b>Limits:</b> the chatbot doesn&rsquo;t know your deal unless you tell it. It doesn&rsquo;t replace matching payments to invoices or reconciling your bank. For that, see <a href="/ai-accounting/quickbooks-ai-banking-suggestions/">QuickBooks AI banking suggestions</a> and our <a href="/ai-accounting/ai-invoices-payment-reminders/">guide to AI for invoices and payment reminders</a>.</p>
<p>You don&rsquo;t need to be technical. If you can write one clear sentence and compare two documents, you can use this. More in our <a href="/bookkeeping/">bookkeeping guides</a>.</p>
<p>Rather have someone check every invoice and reconcile every month?</p>''',
 'Want the checking done for you? At <a href="CTAURL">Computatio</a>, AI does the first pass and an accountant reviews every account each month, including what your customers owe you. Monthly Books is $500 a month.',
 [("Intuit QuickBooks: Use Claude to enter transactions and get insights in QuickBooks","https://quickbooks.intuit.com/learn-support/en-us/help-article/accounting-bookkeeping/use-quickbooks-connector-claude/L3YBlo6Ht_US_en_US"),
  ("Intuit QuickBooks: Connect QuickBooks Online to ChatGPT","https://quickbooks.intuit.com/learn-support/en-us/help-article/mobile-and-apps/connect-quickbooks-online-chatgpt/L0RDe9RPd_US_en_US"),
  ("Intuit QuickBooks: What's new in QuickBooks, Fall 2026 release","https://quickbooks.intuit.com/r/product-update/whats-new-quickbooks-fall-2026/"),
  ("IRS: Publication 583, Starting a Business and Keeping Records","https://www.irs.gov/publications/p583"),
  ("IRS: Topic no. 305, Recordkeeping","https://www.irs.gov/taxtopics/tc305"),
  ("CDTFA: Tax Guide for Home-Based Businesses","https://cdtfa.ca.gov/industry/home-based-businesses/industry-topics.htm")],
 "quickbooks-chatgpt-claude-invoices"),
]
