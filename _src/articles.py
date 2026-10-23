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
<div class="callout"><b>Free download:</b> <a href="https://computatios-newsletter.beehiiv.com/?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign={slug}">47 write-offs for the self-employed</a>, a 42-page guide with the IRS rules behind each deduction. Free when you join the Computatio newsletter.</div>
<h2>Sources</h2><ul>{src}</ul>
<p class="muted">This guide is general information, not tax advice for your situation.</p>
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
 'If your books are already behind, or you&rsquo;d rather not spend the hour, <a href="CTAURL">Computatio</a> keeps your books current for $500 a month, with a person reviewing every account.',
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
 "How an S-corp can lower self-employment tax, what it costs in California (1.5% tax, $800 minimum, payroll), and a worked example to see where the break-even is.",
 "2026-11-02",
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
 'Want the 3-pass method done for you every month? At <a href="CTAURL">Computatio</a>, AI does the sorting and a person reviews and reconciles every account, so your books are current and checked. Monthly Books is $500 a month.',
 [("IRS: Choosing a reputable tax preparer is vital to tax security","https://www.irs.gov/newsroom/choosing-a-reputable-tax-preparer-is-vital-to-tax-security"),
  ("IRS: What kind of records should I keep","https://www.irs.gov/businesses/small-businesses-self-employed/what-kind-of-records-should-i-keep"),
  ("IRS: Instructions for Schedule C (Form 1040)","https://www.irs.gov/instructions/i1040sc"),
  ("IRS: About Schedule C (Form 1040)","https://www.irs.gov/forms-pubs/about-schedule-c-form-1040")],
 "how-to-use-ai-for-bookkeeping"),
]
