# Caption quota service patch — 0.8.28.1

This is a server-only update for Android 0.8.28. No APK reinstall or device reapproval is required.

## Apply in Cloud Shell

From the extracted package root:

```bash
bash services/update_caption_quota.sh
```

The helper updates the existing service image and explicitly sets only the authorized per-installation daily budget to YUNTAI_DEVICE_DAILY_BILLED_SECONDS=7200. Existing global daily/minute limits, authentication mode, runtime identity, secret references and approved devices are retained. In Play Integrity mode the existing package alignment is also retained. It never resets counters, reads secret values, prepares/recreates infrastructure, rotates keys or permits anonymous use.

## Accounting

- Audio requests reserve validated WAV duration rounded up to whole seconds (one to four seconds), instead of ten seconds for every request.
- Native-text translation reserves four seconds per batch. This is an internal caption-service budget estimate, not Groq billing or a claim of audio usage.
- Audio and text consume the same installation daily allowance. Switching modes, sessions or redeploying does not create a fresh allowance. Previously recorded usage retains its original conservative charge for the remainder of the UTC day; it is not erased or recalculated.
- 7,200 budget seconds is roughly two hours of subtitle processing, not an exact two-hour wall-clock viewing timer. Continuous native text at the app's minimum 3.5-second interval can consume the budget in about 105 minutes; batching gaps and speech activity change elapsed time.
- Daily counters reset by the UTC date. Daily-limit rejection now indicates time until the next UTC day in Retry-After; existing clients cap individual waits at one hour. Minute limits keep short retry delays. Provider failures can still consume a reserved allowance, protecting against repeated costly attempts.

The change does **not** raise global limits. Current code defaults remain 18 shared inference requests/minute, 20/device/minute, two concurrent operations and 7,200 global daily budget seconds; deployed global values may differ. Therefore global limits can stop caption service before an individual device uses its full daily allowance. Groq's account/model quotas remain independent and are not increased by this update. A daily budget is a ceiling, not a guaranteed service allocation.

The limit binds to the installation's signing identity. Clearing application data creates a different identity that still requires owner approval in private beta. It is not an unforgeable physical-hardware identifier.

## Acceptance and limitations

Automated tests cover validated half-second and four-second audio charges, text charges, the 7,200-second boundary, persisted quota across sessions/restarts/reapproval, concurrent reservations and Firestore integration. No actual Groq call or cloud deployment is performed by local tests. After deployment, wait for the previous short backoff to expire and test the existing approved device. If quota_reached persists, inspect the unchanged global limits and remaining usage before increasing any global spending protection.
