# Yuntai TV Privacy Policy

**Effective date and last updated: November 23, 2026**  
**Application:** Yuntai TV for Android TV, Google TV, Android phones and tablets (`com.yuntai.android.apps.livetv`; older review builds used `org.example.iptv`).  
**Operator:** The Yuntai TV project operator.  
**Privacy contact:** [yuntaiapp@gmail.com](mailto:yuntaiapp@gmail.com).

This policy describes the application and services operated for Yuntai TV. Broadcasters, stream/CDN providers, program-guide services, external directories, and external websites operate under their own privacy policies and terms. An app installation does not provide a subscription or content distribution rights.

## 1. Television playback and local storage

The app makes network requests to play channels, retrieve program guides, check source availability, and prefetch limited media for nearby channels. The corresponding providers receive ordinary connection information, such as your public IP address, request time, requested resource, and HTTP headers. Providers may infer an approximate region from the connection. Some third-party streams use unencrypted HTTP, which may be observable on your network. The operator's caption and feedback endpoints use HTTPS.

Channel/source metadata, favorites, the last channel, playback preferences, source-health observations, and bounded diagnostic events are stored in the app's private local storage. The media disk cache has an approximately 32 MiB eviction limit. Program guides and other app data are stored separately, so this is not a limit on all application storage.

The app does not require a user account and does not request microphone, camera, contacts, SMS, or precise-location permissions. It uses internet and network-state permissions.

## 2. Audio-only listening mode

Audio-only mode disables the video track while continuing channel audio. Its frequency spectrum is computed locally from decoded playback audio. It does not use the microphone, create recordings, or automatically send audio to the operator or another service. Network savings depend on whether the source offers an independent audio rendition; disabling video does not necessarily reduce download traffic.

If you separately enable AI captions and consent to cloud audio processing, the audio transmission described in Section 3 may continue while you use audio-only mode. Listening mode and cloud-audio consent are separate controls.

## 3. Optional AI captions and Chinese translation

AI captions are off by default. Version 0.8.28 asks existing users to reconfirm combined audio/text-processing consent instead of silently widening earlier consent. Audio is sent for this feature only after you enable it, explicitly consent to cloud processing, and obtain service authorization for the installation. Short clips of the channel's playback audio are sent over HTTPS to the operator's caption service and then to Groq for speech recognition and Simplified Chinese translation. The service also processes device authorization identifiers, signed proofs, session information, and request counters to authorize access, prevent replay and abuse, and enforce usage limits.

When usable native Chinese captions are supplied by a stream, the app can display them locally without speech recognition. Native foreign-language subtitle translation is **off by default** and requires a global translation choice and the combined explicit consent to cloud audio and subtitle-text processing by the operator and Groq. Only bounded current text excerpts and up to 600 characters of preceding dialogue for context are sent over HTTPS to the operator's authenticated translation endpoint, then to the operator-selected Groq model; they are not submitted to speech recognition. When foreign-text translation is enabled, foreign originals are hidden; a failed translation may leave a subtitle gap. Turning translation off restores original text captions. Bitmap subtitles are displayed as supplied; this feature does not perform OCR.

During native-caption availability the app suppresses duplicate audio transcription. If usable native cues are absent, the enabled and consented audio-caption fallback may run. Switching channels or disabling the relevant feature cancels pending work and rejects outdated results. Native captions and translations may be delayed, missing, or inaccurate.

Audio comes from the media player, not your microphone. The operator does not intentionally persist audio or subtitle text in app recording files, operator databases, or application diagnostic logs. Audio and text are present in memory and network requests during processing. Disabling captions or withdrawing consent stops collection of new upload clips, cancels audio requests, and discards outdated results. A request already sent to a provider may still finish processing.

Groq is a separate service provider. Its processing, data use, and retention depend on its applicable terms, privacy policy, and the operator's account configuration. **We do not promise provider zero retention, and the operator's decision not to write audio to disk does not mean a provider never retains it.** See [Groq's Privacy Policy](https://groq.com/privacy-policy/).

Captions can be delayed, incomplete, or inaccurate. They should not replace professional interpretation of emergency, safety, or medical information.

## 4. Device authorization and security identifiers

On supported devices, the app creates an installation-specific signing key using Android Keystore. The private key is not uploaded. The public key and a derived installation identifier may be sent to the operator for signature verification, device approval, usage limits, and revocation. This is an installation identifier, not an advertising ID, name, or telephone number.

Private beta installations can be approved by the operator using a short-lived four-digit pairing code and administrator confirmation of the installation identity. Device approval normally lasts up to 30 days; short-lived sessions are renewed automatically. A production configuration using Google Play Integrity may transmit integrity tokens to Google and the operator to validate the app and device environment, subject to [Google's Privacy Policy](https://policies.google.com/privacy). Authorization methods can differ between distribution builds.

## 5. Feedback that you explicitly submit

The app uploads a diagnostic report only when you submit it. Reports use an allowlist of technical information, including app version/build, device manufacturer/model, Android version, channel identifier, local source number, a digest of the source address with query parameters removed, issue category, and a bounded set of playback events and metrics. Metrics may include buffering, error codes, first-frame delay, source switching, dropped frames, and estimated bandwidth.

Report bodies do not include full stream URLs, IP addresses, access tokens, Groq keys, audio, subtitle text, or free-text attachments. Source digests and installation identifiers remain linkable technical data; they are not guaranteed anonymous. The network IP and request metadata processed by cloud infrastructure are separate from the report body.

Successful submissions receive a `YT-...` reference. Failed submissions remain on the device, with a maximum of five pending reports and a manual retry option. A `LOCAL-...` reference does not mean a report reached the server. The local diagnostic event ring holds at most 64 structured events and can persist across app restarts.

Cloud feedback records are configured to expire after 14 days. TTL deletion is asynchronous, so physical deletion may occur after the expiry time. The service limits stored feedback to 10,000 reports; additional submissions can be rejected until space becomes available. Do not post raw diagnostics, credentials, signed URLs, or other personal information in public GitHub issues.

## 6. Cloud infrastructure, logs, and international transfers

The operator's caption and feedback services use Google Cloud Run and Firestore, currently deployed in the United States (`us-central1`). Using cloud features may transfer data internationally. Groq and other providers' processing locations depend on their service arrangements.

Operator services may record fixed error categories, HTTP status codes, durations, and necessary operational information. Cloud infrastructure may record access metadata such as IP addresses, request times, paths, and User-Agent values. The app does not intentionally write audio, subtitle text, credentials, or signed stream URLs to those diagnostic logs. Infrastructure logs and security/usage records follow their platform and operational retention configurations; their retention is separate from the feedback report's 14-day expiry. Access is restricted to personnel and service identities needed to operate and secure the service.

The app does not include an operator-integrated advertising or behavioral-marketing analytics SDK. The operator does not sell personal information or use your audio to train an application model. Channels may contain advertisements or use their own delivery and measurement systems; the operator does not control all third-party processing.

## 7. Your choices and deletion requests

- Disable AI captions and withdraw combined cloud-processing consent in settings to stop future audio uploads. Disable native subtitle translation or withdraw the combined processing consent to stop future text translation requests. Available channels can still be watched without cloud captions.
- Source maintenance and limited nearby-channel prefetching are managed automatically. Checks are designed to yield when playback buffer is low, and have time, request-count and media-read budgets. Exiting with the app's Exit action cancels current source checks and their scheduled job; a later launch resumes scheduling. Device-level background-data controls may also apply. Watching a channel still requires requests to its content provider.
- Clear app storage in Android settings or uninstall the app to remove local favorites, settings, caches, and diagnostics. This does not immediately delete existing cloud feedback or authorization records.
- Contact **yuntaiapp@gmail.com** to request access to or deletion of cloud reports, or revocation of device authorization. Provide a report reference or device fingerprint, not a key, recording, or full playback URL. We may need proportionate verification that the request concerns your installation. Records needed for legal obligations or security and abuse prevention may need to be retained longer.

## 8. Children and security

Yuntai TV is not specifically directed to children and does not offer child accounts. Minors should obtain permission from a parent or guardian before using cloud audio processing. Including children's channels does not establish that every third-party program or service is suitable for every age.

We use measures including HTTPS, device signatures, access controls, request limits, and minimized diagnostic content to reduce risk. No system can be guaranteed completely secure. Never disclose API keys, login credentials, or signed links in feedback, GitHub issues, or other public channels.

## 9. Changes and contact

We will update this page for material changes in data uses, processing providers, or privacy practices. Where a new consent is required, it will be requested in the app. This policy is not a statement of Google Play approval and does not replace content providers' licensing terms.

For privacy questions or deletion requests, contact **[yuntaiapp@gmail.com](mailto:yuntaiapp@gmail.com)**.
