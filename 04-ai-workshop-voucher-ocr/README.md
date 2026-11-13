# Unit 04: Voucher OCR to Excel (`voucher-to-excel`)

> 🌐 **Language**: English | [繁體中文](README.zh-TW.md)

Use natural language to ask an AI Agent to read scanned invoice PDFs, populate an Excel spreadsheet, and finally save the entire verified workflow as a reusable Skill. Next time, a single sentence—"Please help me enter these records into Excel"—is all it takes. No coding required.

> 📥 **Unit Slides**: [Download 04-voucher-ocr.en.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/04-voucher-ocr.en.pptx) (17 slides, with demo clips and speaker notes; the demo clips keep their original Chinese narration; [Chinese version](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/04-voucher-ocr.pptx))

> 🎬 **Tutorial Video**: [Unit 04 | Voucher OCR to Excel](https://youtu.be/Kq0HLK2kIQg) (YouTube, 4 min 45 sec, English narration with English subtitles; [Chinese version](https://youtu.be/XOs_Pf7QyjA))

> 💡 The video and slides use real vouchers (with sensitive fields blurred). This written guide uses the **de-identified practice samples** in [`example_deid/`](example_deid/), so filenames, organization names, and amounts differ from the video while the workflow remains identical.

| Step | Content | Est. Time |
| :--- | :--- | :---: |
| **Step 0** | [Open the Folder and Prepare for Practice](#step-0-open-the-folder-and-prepare-for-practice) | 3 min |
| **Step 1** | [Let AI Understand the Task First](#step-1-let-ai-understand-the-task-first) | 3 min |
| **Step 2** | [Agree on Highlighting Rules](#step-2-agree-on-highlighting-rules) | 2 min |
| **Step 3** | [Process One Record First and Verify](#step-3-process-one-record-first-and-verify) | 3 min |
| **Step 4** | [Fill in the Remaining Four Records](#step-4-fill-in-the-remaining-four-records) | 3 min |
| **Step 5** | [⭐ Turn the Workflow into a Skill](#step-5--turn-the-workflow-into-a-skill) | 5 min |
| **Step 6** | [How to Reuse It Later: New Chat, One Sentence](#step-6-how-to-reuse-it-later-new-chat-one-sentence) | 3 min |
| **Bonus** | [Two AI Agents Collaborating: One Extracts, One Audits](#bonus-two-ai-agents-collaborating-one-extracts-one-audits) | 5 min |

## What It Does

- 🧾 Reads scanned PDFs that have no embedded text layer: upper half "Expenditure Voucher Mounting Form" + lower half attached uniform invoice, e-invoice, or receipt
- 📋 Populates 9 columns in Excel: Account Code (會計科目), Control Number (控帳編號), Invoice Number (發票號碼), Invoice Amount (發票金額), Total Amount (總計金額), Vendor Tax ID (發票統編), Buyer Title (發票抬頭), Liability Account (負債科目), and Project Code (計畫代號)
- 🟨🟦 Highlights missing fields in **yellow** and uncertain fields in **blue**, adding cell comments explaining the reason
- ⭐ Saves the verified workflow as a Skill for one-sentence reuse in future sessions
- 🤝 Splits work between two AI Agents: one fills in the sheet, and another audits the result against the original PDFs

## Recommended Prompting Strategy: Look First, Then Act

Don't dump everything onto the AI in a single prompt. Following this four-step progression produces much more accurate results and makes discrepancies easy to catch early:

1. **Let AI inspect first**: What columns does the Excel file need? Are those fields present in the PDFs?
2. **Set the rules**: How should missing or uncertain values be highlighted?
3. **Test on one record**: Confirm accuracy on a single file before batch processing.
4. **Package into a skill**: Save the verified procedure for future use.

---

## Step 0: Open the Folder and Prepare for Practice

Use Antigravity's **Open Folder** to open the `04-ai-workshop-voucher-ocr` folder directly—do not open the outer `ai-workshop-research` folder, or the AI Agent will not find the unit's skill.

```
04-ai-workshop-voucher-ocr/
├── record.example.xlsx                 ← Excel template (contains 1 sample row; never modified directly)
├── example_deid/                       ← 5 de-identified scanned voucher PDFs
│   ├── SKM_650i25101515330_deid.pdf
│   ├── SKM_650i25101515330_deid.json   ← Ground-truth answer key with matching filename
│   ├── … (331, 340, 341 as above)
│   ├── SKM_650i25101515350_deid.pdf
│   └── SKM_650i25101515350_deid.json
└── .claude/skills/voucher-to-excel/    ← Pre-built demo skill (used in Step 5/6)
```

- Each PDF has the internal voucher mounting form on the top half and the invoice or receipt attached on the bottom half.
- All files are image scans **without a text layer**, so the AI must convert pages to images and inspect them visually.
- Organization names, vendors, amounts, and tax IDs in `example_deid/` are fictional. The buyer is the fictional *"Cloud Intelligence Computing Center, Future Technology Research Institute (財團法人未來科技研究院智慧雲端運算中心)"* (Tax ID `81924865`).

**To experience Steps 1–5 from scratch**: Because this folder already includes the pre-built skill, the AI might use it right away. Either temporarily move `.claude/skills/voucher-to-excel` out of the folder until Step 6, or prepend `"Do not use any skill yet."` to your prompts in Steps 1–4.

## Step 1: Let AI Understand the Task First

> First copy record.example.xlsx to record.xlsx. There are five invoice PDFs in the example_deid folder. Please take a look at what fields need to be filled in the Excel file and check whether they can be found in the PDFs.

Observe whether the AI automatically performs these actions:

- Reads the column headers and sample row in `record.xlsx`.
- Notices that the PDFs have no text layer and converts each PDF page to an image to inspect visually.
- Distinguishes buyer from seller: recognizes that `81924865` on the invoice is our organization (the buyer), so "發票統編 (Invoice Tax ID)" must be filled with the **seller's (vendor's)** Tax ID.
- Proactively flags edge cases: e.g., `…340` is a receipt without an invoice number; `…331` has a different project code from the others; "負債科目 (Liability Account)" does not appear anywhere on the PDF; and the buyer title in the template's sample row differs from the buyer on the practice PDFs.

## Step 2: Agree on Highlighting Rules

> Keep the columns even if data is missing: highlight missing fields in bright yellow, highlight uncertain fields with a light blue background, and add a cell comment explaining the reason. Also find a suitable spot at the top of the Excel sheet to add a legend explaining what these two colors mean.

A color legend will be added in the top-right corner of the sheet (`K1:L2`) so anyone reviewing the spreadsheet immediately understands the highlights:

| Color | Meaning |
| --- | --- |
| 🟨 Yellow fill | Missing: Field does not exist in the PDF; cell left blank |
| 🟦 Blue fill | Uncertain: Best-guess value filled in; requires human review (see cell comment) |

## Step 3: Process One Record First and Verify

> Just process the first file example_deid/SKM_650i25101515330_deid.pdf for now so I can verify that it is correct.

The AI fills in only the first record, highlighting any uncertain cells in blue with explanatory comments such as:

> Invoice Amount: Filled with tax-included total 315,420; if pre-tax is required, it should be 300,400.

Open `record.xlsx` and check this single row against the PDF. Testing on one record catches misunderstandings about column definitions before batch processing.

## Step 4: Fill in the Remaining Four Records

> I checked the first record and it looks good. Please fill in the remaining four PDFs into record.xlsx following the same rules, list the results when done, and explain the reason for each yellow or blue cell.

Answer key (compare with the AI's output; each PDF also has a matching `.json` ground-truth file in `example_deid/`):

| Row | File | Control No. | Invoice No. | Amount | Vendor Tax ID | Project Code |
| --- | --- | --- | --- | ---: | --- | --- |
| 1 | …330 | 203114009187 | KX52816403 | 315,420 | 23831903 | 03114Z1500 |
| 2 | …331 | 203114006142 | QA48017256 | 184,275 | 16480894 | 03114Z1600 |
| 3 | …340 | 203114007326 | 🟨 (Blank, receipt) | 3,250 | 17784483 | 03114Z1500 |
| 4 | …341 | 203114008054 | PM63950418 | 8,500 | 18302983 | 03114Z1500 |
| 5 | …350 | 203114008611 | WD30627719 | 70,560 | 95753514 | 03114Z1500 |
| | | | **Total** | **582,005** | | |

- Invoice Amount and Total Amount are identical; Buyer Title is `"財團法人未來科技研究院智慧雲端運算中心"` for all five rows.
- The Total row should use an `=SUM()` formula so future rows are summed automatically.
- `…340` is an invoice-exempt receipt, so its Invoice Number cell is left blank and highlighted in yellow.

## Step 5: ⭐ Turn the Workflow into a Skill

By now, the AI understands every detail of this task: where to find each field, how to cross-check amounts, and when to apply yellow or blue highlights. However, that knowledge only lives inside **this single conversation**—start a new chat and it forgets everything. **A Skill saves that institutional knowledge as a persistent operating manual.**

No coding is needed—just ask the AI in plain language to package what you did:

> Later I will upload new PDF invoices and receipts, and I want to simply say "Please help me enter these records into Excel" and have you automatically follow today's workflow. Please package the procedure we confirmed today into a skill, including where to read each field from the PDF, the yellow and blue highlighting rules, and how to cross-check the amounts. Also give this skill a name and show me a few example phrases I can use to invoke it.

In the demonstration, the AI created `voucher-to-excel` (included in this folder):

```
.claude/skills/voucher-to-excel/
├── SKILL.md               ← Operating manual: workflow, field mapping rules, highlight criteria
└── scripts/
    ├── render_pdfs.py     ← Converts scanned PDF pages into images
    └── append_rows.py     ← Writes rows to Excel, applies colors/comments, and updates the SUM row
```

- **`SKILL.md`** captures the parts requiring visual judgment: where to read each field on the mounting form vs. the invoice, how to cross-check totals, and when to highlight in yellow or blue.
- **`scripts/`** encapsulates the deterministic operations that must run identically every time: writing to Excel, applying cell styles, skipping duplicate control numbers, and backing up the file before editing.

When you generate your own skill, its exact name and structure may vary slightly—that is completely normal.

## Step 6: How to Reuse It Later: New Chat, One Sentence

Restore the demo skill into `.claude/skills/` (or keep the one you created in Step 5), delete `record.xlsx`, open a brand-new chat session, and simply say:

> There are five new invoice PDFs in example_deid, please help me enter these records into Excel

The AI will automatically discover `voucher-to-excel` and execute the entire workflow. Other ways you can phrase it:

| Goal | Example Prompt |
| --- | --- |
| Verify one before batch processing | New receipts have arrived—process one first for me to check, and do the rest if it looks good |
| Append only unlogged PDFs | Enter all the PDFs in example_deid that haven't been logged yet |
| Explicitly invoke the skill | Type `/voucher-to-excel` |

**Before reusing a skill, check which AI Agent you are using** so the skill is placed where that agent looks for it:

| AI Agent | Project Skill Directory |
| --- | --- |
| Claude Code | `.claude/skills/` |
| Other agents (e.g., Antigravity's built-in Gemini) | `.agents/skills/` |

> In our demo, Gemini also found the skill inside `.claude/skills/`. If your agent does not pick it up automatically, copy the `voucher-to-excel` folder into `.agents/skills/` or mention the skill by name in your prompt.

### Refine Rules via Conversation to Make the Skill Smarter

The pre-built demo skill was originally created using real NCHC vouchers where the expected buyer was NCHC (Tax ID `80778299`). When run against the de-identified practice samples (`example_deid/`), the "Buyer Title" column will likely be highlighted in blue because the buyer on the practice invoices does not match NCHC. This gives you a great opportunity to practice refining skill rules through conversation:

> Why are the invoice buyer titles all highlighted in blue? The buyer for this batch of practice data is "財團法人未來科技研究院智慧雲端運算中心" with Tax ID 81924865. Please add this to the skill's rules so it doesn't need to be highlighted in blue anymore.

If too many cells are highlighted in blue, you can also ask the AI why: e.g., *"The blue cells all look right to me—why were you uncertain about them?"* Once human-confirmed rules are written back into `SKILL.md`, only genuinely ambiguous visual values (blurry handwriting, smudged stamps, or mismatched totals) will be flagged in blue.

---

## Bonus: Two AI Agents Collaborating: One Extracts, One Audits

Just like having a colleague double-check your accounting sheet: let one AI Agent fill in the spreadsheet, then switch to a second AI Agent to audit the result against the original PDFs. Delete `record.xlsx` before starting.

### 1. Gemini Extracts the Data

In Antigravity's Agent chat panel (with Gemini selected), enter:

> First copy record.example.xlsx to record.xlsx<br>
> Please recognize example_deid/SKM_650i25101515330_deid.pdf example_deid/SKM_650i25101515331_deid.pdf example_deid/SKM_650i25101515340_deid.pdf example_deid/SKM_650i25101515341_deid.pdf example_deid/SKM_650i25101515350_deid.pdf and fill them into record.xlsx

Gemini locates the `voucher-to-excel` skill and processes all five files. Compare the output with the [Step 4 Answer Key](#step-4-fill-in-the-remaining-four-records): total `582,005`, with `…340` left blank and highlighted in yellow for the missing invoice number.

### 2. Claude Audits the Result

Switch to the Claude Code chat panel and enter:

> I have extracted the invoice contents from SKM_650i25101515330_deid.pdf, SKM_650i25101515331_deid.pdf, SKM_650i25101515340_deid.pdf, SKM_650i25101515341_deid.pdf, and SKM_650i25101515350_deid.pdf in example_deid/ into record.xlsx. Please cross-check the PDFs against the Excel sheet and verify whether everything is accurate.

Claude renders each PDF to images, verifies every invoice number, amount, and tax ID row by row, and reports a complete audit table:

- Confirms that each invoice total matches the mounting form reimbursement amount and tax calculation.
- Verifies that itemized receipt lines sum to the Excel total.
- Checks buyer title, tax ID, project code, account code, and the grand total formula.
- **Formatting note**: Points out if any Tax IDs are stored as numbers vs. text strings (important when a Tax ID starts with `0`) and recommends standardizing them as text.

> 📌 **Key Takeaway**: The auditing agent doesn't need to know how the first agent produced the file—it simply compares the final Excel sheet against the raw PDFs. Moreover, the exact same Skill works across different AI Agents.

---

## Practical Tips

- **Always manually review yellow and blue cells, and spot-check unhighlighted rows.** The two-agent audit above is a great way to automate spot-checking.
- **"發票統編 (Invoice Tax ID)" is the seller's (vendor's) Tax ID**, not the buyer's (your organization's) Tax ID.
- **Invoice Amount uses the tax-included total**; invoice-exempt receipts have no invoice number and should be left blank in yellow.
- **Never overwrite `record.example.xlsx` directly**; to start over, simply delete `record.xlsx`.
- **Adapting to your own organization**: Ask the AI to update the buyer name and Tax ID in `SKILL.md` to match your organization.
- **Protect confidential data.** When an AI Agent inspects images, those images are sent to the model provider's servers. Handle real financial documents according to your institution's data governance policies, and always de-identify files before sharing publicly.

---

## Project Contents

| Path | Description |
| --- | --- |
| `record.example.xlsx` | Excel template (contains 1 sample row; never modified) |
| `record.xlsx` | Working copy created from the template during practice (not tracked on GitHub; delete to reset) |
| [`example_deid/`](example_deid/) | 5 de-identified scanned voucher PDFs (fictional data) with matching `.json` ground-truth files |
| [`.claude/skills/voucher-to-excel/`](.claude/skills/voucher-to-excel/) | Pre-built skill created during the demo (`SKILL.md` + `scripts/`) |
| `tutorial.md` | Full transcript of the live demo video |
| [`AGENTS.md`](AGENTS.md) | Project rules for AI Agents (always use `uv` for Python) |

## Next Step

Unit 05 moves into scientific computing: using natural language on NCHC HPC to run a complete QIIME 2 gut microbiome analysis pipeline and generate an illustrated PDF report.
