# Yuntai TV

A minimal live TV app for Android TV, Google TV, Android phones and tablets.

- [Download the 0.8.29 APK](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.29.apk)
- [Google Play upload AAB](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.29-play.aab)
- [Release notes](releases/v0.8.29.md)
- [Checksums](downloads/SHA256SUMS-0.8.29.txt)
- [Validation manifest](downloads/VALIDATION-0.8.29.json)
- [Privacy Policy](PRIVACY_POLICY.md)
- [Releases](https://github.com/weiranm007/Yuntai-TV/releases)

## Yun subtitles

Version 0.8.29 uses **one global subtitle feature switch**, named Yun · 字幕, plus one explicit combined audio/text-processing consent checkbox. When enabled, the app prefers native Chinese captions, translates available foreign text into Simplified Chinese, and uses consented audio recognition/translation when usable native cues are absent. There is no separate native-text translation switch. Foreign originals are hidden during text translation; bitmap or burned-in subtitles cannot be replaced by this text-only pipeline.

Existing fully enabled and consented workflows are retained. Earlier partial settings are not silently expanded into additional uploads: open Yun settings, enable the single switch and save. New installations remain off by default. Existing approved installations do not need reapproval. Provider/model/target remain operator-controlled; no API key is included in the APK.

The visible experimental label and version suffix have been removed. Device authorization, request signing, usage limits, consent validation and privacy controls remain in place.

## Playback and source maintenance

The app retains application-managed source discovery/health checks, masked numeric source identifiers, bounded playback-aware background work, source recovery, favorites, channel catalogs, program guides, audio-only listening, and the existing startup animation. A successful probe is not proof of sustained playback quality. Shared upstream/network conditions and content-provider availability still affect reliability.

## Caption service and limits

The existing deployed 0.8.28 translation endpoint is compatible; this Android-only update requires no new server deployment. The optional [0.8.28.1 quota patch](docs/CAPTION_QUOTA_UPDATE-0.8.28.1.md) changes server budget accounting separately. Installing an APK does not change/reset quotas or increase Groq capacity. Per-device allowance remains subject to global daily/minute caps, concurrency and provider limits. Caption accuracy and latency are not guaranteed.

## Installation and signing

Minimum Android version: **Android 7.0 / API 24**. Compile SDK and target SDK: **36**. Landscape, touchscreen and Leanback hardware features are explicitly optional.

The current application ID is **com.yuntai.android.apps.livetv**. The APK and AAB are signed with the retained private upload certificate used for the recent Play bundles. The key is not distributed in this repository.

Earlier review APKs used **org.example.iptv** and a different certificate. They are separate applications; settings, favorites and caption-device approval do not automatically migrate to the new application ID. A Google Play-installed build may use Google's separate app signing certificate and should be updated through Play when a sideload certificate does not match. Do not uninstall solely to force an update without considering local data.

The APK is for direct sideload testing. The AAB is for Play Console upload and cannot be installed directly. Verify the SHA-256 checksum before use.

## Build validation and known limits

119 Android JVM tests passed. Release APK/AAB builds completed; lint reported 0 errors and 121 warnings. Signatures, retained upload certificate, ZIP integrity, SDK/package values and 16 KiB APK ZIP alignment were checked. Production channel/source/guide/logo/startup assets match 0.8.28; generated baseline profiles change with code.

Python tests were not rerun for this Android-only change. Physical-device settings/focus, actual subtitle routing, model quality/latency, long-session playback and Play Console processing remain unverified. No Play review submission was made by this workflow. Removing a label is not a claim of production certification.

Content providers control availability and territorial/distribution rights. Installing this app does not grant a content subscription or rebroadcasting rights.

Privacy contact and deletion requests: **yuntaiapp@gmail.com**. Do not post API keys, full playback URLs, audio or subtitle text in public issues.
