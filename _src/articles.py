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
]
