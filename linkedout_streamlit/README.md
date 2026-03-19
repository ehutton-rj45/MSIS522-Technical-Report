# LinkedOut — MSIS 522 Project Showcase

**Team:** Hardik Sharma, Aria Wang, Ethan Hutton, Jingying Deng  
**Course:** MSIS 522 — University of Washington

An interactive Streamlit showcase page for **LinkedOut**: an AI-powered portfolio that lets recruiters talk live to a digital video avatar of the candidate — anytime, without scheduling.

---

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud

1. Fork or push this repo to your GitHub account.
2. Go to [share.streamlit.io](https://share.streamlit.io) → New app → select this repo.
3. Set **Main file path** to `app.py`.
4. Click **Deploy**.

## Project stack

| Layer | Tools |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JS |
| AI / Avatar | LiveAvatar API, ElevenLabs Conversational Agent |
| Real-time streaming | LiveKit WebRTC, livekit-client SDK |
| Backend | Node.js, Express, dotenv |

## Assets

Screenshots and the architecture diagram are in `assets/`. The technical report PDF is also included.
