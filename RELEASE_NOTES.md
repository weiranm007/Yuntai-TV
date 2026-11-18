# Yuntai TV 0.8.21-beta — Audio-only listening

Version code: **41**. Package: `org.example.iptv`. This is a **pre-release beta** signed with the existing review certificate.

## Downloads

- [Download APK](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.21-beta-review.apk)
- [SHA-256 checksum](https://github.com/weiranm007/Yuntai-TV/blob/main/downloads/SHA256SUMS.txt)
- [Validation manifest](https://github.com/weiranm007/Yuntai-TV/blob/main/downloads/VALIDATION.json)

The APK is stored in this repository's `downloads` folder and linked here directly.

## What's new

- Added an audio-only toggle to the playback toolbar and remote-control main menu.
- Listening mode disables video tracks on the existing Media3 player while retaining audio. The screen shows the current channel logo, name, and a waveform derived from real decoded PCM amplitude.
- Turning the toggle off re-enables video. The preference is remembered locally and remains active when changing channels.
- Channel overview, program guide, deferred channel switching, optional AI captions, and recovery remain available.
- Added audio-progress recovery checks so deliberately disabled video is not treated as a frozen screen. Audio startup is not recorded as a video first-frame event.
- Added a complete privacy-policy link in the app's privacy dialog.
- Kept double-tap pause disabled; tap to show controls. The listening surface adapts to smaller windows.

## Privacy and compatibility

No new permissions, third-party dependencies, or backend deployment are required. The amplitude meter works locally and does not use a microphone, save recordings, or automatically transmit audio. Optional cloud AI captions have independent consent and authorization requirements.

Video and audio can share the same HLS segments, so disabling video does not guarantee lower network traffic. Resuming video may require a video segment and decoder initialization. This version does not add a foreground media service or guarantee playback after leaving the app or locking the screen; existing lifecycle and picture-in-picture behavior remains.

## Completed checks

- **93 Android JVM unit tests passed.**
- Review APK build and lint passed: **0 errors, 52 warnings**, including existing deprecation/accessibility warnings and a gesture-detector accessibility analysis warning.
- Signature verification passed for API 21 and later.
- Upgrade signing certificate matches version 0.8.20-beta.
- 16 KiB ZIP alignment verification passed.
- APK permissions remain internet, network state, and the app-scoped internal receiver permission; no microphone permission.

Tests cover PCM amplitude, silence and saturation, non-consuming buffer reads, inactive metering, and audio progress versus genuine stalls. They do not substitute for playback testing on a television or tablet.

## Outstanding device validation

Real-device audio continuity when toggling, restored video, source failover in listening mode, rotation/PiP behavior, low-end device CPU/heat/memory, and multi-hour playback remain **UNVERIFIED**. No measured startup, switching, latency, or long-session reliability benchmarks are claimed.

## Upgrade

Install over a matching-signature beta to preserve local settings and device authorization. Do not uninstall first unless a clean installation is intended. No new Groq key, re-pairing, or server redeployment is required for this app-only change.

See [Privacy Policy](https://github.com/weiranm007/Yuntai-TV/blob/main/PRIVACY_POLICY.md), `SHA256SUMS.txt`, and `VALIDATION.json`.
