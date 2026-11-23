# Native subtitle translation update (0.8.27)

The new Android beta can display native Chinese text captions without ASR. Native foreign-language captions are translated only after the user explicitly enables the global translation option and grants separate subtitle-text consent. If the server does not yet support the route or is unavailable, the original captions remain visible. No API key is placed in the APK.

## Existing Cloud Run deployment

Upload and extract the companion deployment ZIP into Cloud Shell, then run from its extracted root:

```bash
bash services/update_caption_service.sh
```

This verifies project yuntai-app / 605035871673, builds a replacement image with the existing build identity, and updates the **existing** yuntai-api service in us-central1. It preserves its runtime identity, secret references, limits, billing-related budgets and authorization mode. It does not run prepare, reset Firestore, recreate accounts, rotate keys, or weaken device authorization. In Play Integrity mode it aligns YUNTAI_PACKAGE with com.yuntai.android.apps.livetv; existing app-signing certificate settings are retained and must already match the Play signing certificate.

The script makes two small checks: healthz and rejection of a consent-free empty text request. Neither sends television audio/subtitles or calls Groq. These checks are not end-to-end acceptance of translation.

## New route

POST /v1/translate requires application/json, an exact {text, target} object, target zh, 1–400 characters, X-Subtitle-Consent true, and the existing device-bound session/signature over path and body. It shares audio inference request/day limits, circuit breaking, and distributed Firestore slots. Clients cannot select a model or provider. No raw subtitle text is persisted in reports, Firestore or logs.

The model/provider are operator-controlled. Current deployed quota and latency must be measured; this change does not assume free-tier capacity or promise instantaneous subtitles.

## Device acceptance

1. Enable global captions and audio-processing consent as before.
2. Play a controlled HLS with English and Chinese WebVTT tracks: Chinese is selected, with no audio ASR request while native cues arrive.
3. On an English-only source, leave translation off: verify original English captions and no text request.
4. Enable native-caption translation and separately consent to text processing. Verify Simplified Chinese results and absence of ASR requests for the same cues.
5. Revoke consent or switch channel while a request is in flight: old text must not appear and new requests must stop.
6. Simulate 404, 429 and 503: original captions stay usable, rate limits/backoff apply and playback continues.

Device approval remains governed by the existing service mode. This update does not silently convert a private beta into a public, unauthenticated service.
