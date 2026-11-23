# Caption and pairing service update — 0.8.28

Upload and extract the companion ZIP into Cloud Shell, then run from its root:

```bash
bash services/update_caption_service.sh
```

This updates the existing yuntai-api image in yuntai-app / us-central1. Runtime identity, secret references, authorization mode, quotas and existing approvals are preserved. It does not prepare/reset Firestore/IAM, read/rotate keys, or allow anonymous access. Health checks use /v1/health. The consent-free empty POST check sends no audio/text and makes no Groq call; it is not an end-to-end translation test.

## Four-digit private-beta approval

New codes are four numeric digits, including leading zeroes, valid for five minutes, with transactional collision protection and existing issuance limits. Used numbers remain reserved until original expiry. Existing approved devices need no reapproval; old twelve-character codes remain readable until expiry.

Run the updated administrator script from **this package**, replacing 0042 with the device's code:

```bash
python3 services/beta_devices.py --project yuntai-app approve 0042
```

Verify the code is on your intended device, inspect the displayed installation fingerprint and enter `y` to confirm. No fingerprint needs to be typed. The script revalidates identity after confirmation and atomically consumes the request. Only the owner's authenticated Cloud Shell IAM identity can approve; a four-digit code alone cannot unlock the API. Legacy --fingerprint remains supported. This copy does not automatically update scripts in other directories.

## Translation and consent

Android 0.8.28 requires renewed combined audio/text-processing consent. Enable and foreign-text-translation switches remain global and independent. Native Chinese is preferred. With foreign-text translation enabled, the original foreign text is hidden both while waiting and on failure. Bitmap/burned-in captions cannot be translated/removed by this text pipeline.

POST /v1/translate retains device-bound sessions/signatures and X-Subtitle-Consent. Allowed keys: text (1–400 characters), target (zh), optional context (0–600 characters). Bad controls and arbitrary provider/model fields are rejected. Prior text is reference only; semantic translation must preserve names, meaning, numbers and negation, output only the new text, and not invent missing facts. Context stays bounded in RAM; raw audio/text is not intentionally persisted in Firestore, feedback or app logs.

Rolling cues are deduplicated and merged, with 250 ms initial coalescing and a 3.5 s sustained minimum interval compatible with conservative quotas. Eight-second-old results are discarded, rather than accumulating lag indefinitely. Channel/lifecycle reset clears context and invalidates old results. This is near-real-time chunked translation, not an instantaneous streaming or measured latency guarantee.

## Rate limits and unresolved field report

Production quotas are **not raised**. Code defaults: 20 inference calls/device/minute, 18 globally/minute, two concurrent calls, plus daily limits. Deployed configuration can differ. Groq has independent account/model limits. The new client distinguishes quota_reached, provider_busy and busy and honors retry delays. Server logs use fixed error enums/status/stage, including translation exceptions and 429/403; no raw request body is logged.

The owner reported busy feedback (HTTP 429) in 0.8.27. Three supplied requests succeeded in 0.64–0.86 s, which does not identify intermittent failures. Operator versus provider throttling and end-to-end translation remain unverified pending safe failure logs and playback testing. This update does not promise to solve provider capacity.

## Device acceptance

1. Reconfirm combined consent; enable captions and foreign-text translation, then save.
2. Native Chinese shows without ASR; foreign translation off shows original text; translation on never flashes foreign text and displays new Chinese results.
3. Rapid rolling cues retain new words without unbounded queues; test 429/503 without interrupting video.
4. Switch channels, disable captions, revoke consent and background the app during requests: no stale result may appear.
5. Request a fresh short code, cancel owner confirmation (no grant), then confirm; verify code consumption and retained prior approvals.
6. Test first-start top-menu placement, cutouts, transient bars, rotation, resume and TV remote focus on devices.
