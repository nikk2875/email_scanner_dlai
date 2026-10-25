# email_scanner_dlai
There are many news letters I get in my Gmail account, but I don't have the time to go through all of them. So, I am building a couple of tools that will help me to produce summaries and let me focus only on those that really matter to me. The first group of mails I wanted to analyze, is those that I get from *Deeplearning.AI*.

### About Deeplearning.AI (DLAI) newsletter
Deeplearning.AI newsletter typically has a message from Andrew Ng, then news and articles on various ML & AI topics. I have created `dlai_scan.py`, which performs the following actions:
1. Logins into an Gmail account.
2. Fetches all e-mails in a given label. Please note that:
    - I have created a specific label in my inbox to store these mails, so there is no filtering logic. I just fetch all mails from that folder.
    - I set a maximum limit on the number of e-mails that I will fetch. Default is 1.
    - I get only unread e-mails in reverse chronological order. Therefore, I start from older e-mails and gradually come to the fresh ones.
3. Goes though each e-mail and produces a summary. I use models from OpenAI and Openrouter for the summarization.
4. Produces a summary output that goes to an output folder and all fetched e-mails are marked as read in the Gmail account.

## How to run
Just execute `uv run python dlai_scan.py`. You can set 2 parameters: `model` and `limit`, but only inside the python script:
- With `model` you can define any of 2 providers: *openai*, *openrouter* (default is `openai`). Remember to define a `.env` file with your keys. You can use `.env.sample` as an example.
- With `limit` you define the maximum number of e-mails to fetch (default is `1`).
