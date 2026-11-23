# Yuntai TV

A minimal live TV app for Android TV, Google TV, Android phones and tablets. This repository distributes beta builds, release notes, validation manifests and the public privacy policy.

- [Privacy Policy](PRIVACY_POLICY.md)
- [Download the 0.8.27-beta APK](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.27-beta.apk)
- [Google Play upload AAB](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.27-beta-play.aab)
- [Version 0.8.27-beta release notes](releases/v0.8.27-beta.md)
- [Checksums](downloads/SHA256SUMS-0.8.27-beta.txt)
- [Validation manifest](downloads/VALIDATION-0.8.27-beta.json)
- [Beta releases](https://github.com/weiranm007/Yuntai-TV/releases)

## Version 0.8.27-beta

Source addresses are hidden in source controls; users see stable source numbers, watching scores and safe media-check status. Automatic maintenance prioritizes the current channel's backups and actual-category neighbors, yields to low playback buffer, and uses bounded time, request and byte budgets. Failed current channels can request targeted discovery. Hourly directory attempts and approximately 30-minute unavailable-source checks are subject to Android scheduling and playback headroom.

The media checker validates consecutive complete segments, video tracks, sample timestamps, decoder availability, playlist advancement and download headroom. It does not run a second player or guarantee long-session stability. Two completed all-source failure rounds with recent network evidence can temporarily hide a non-current channel; positive evidence restores it while retaining favorites and IDs. Open channel drawers defer membership/order changes.

Chinese native captions are preferred. Native foreign text translation is off by default and requires a global translation choice and separate text-processing consent. Native cues suppress duplicate ASR, and the existing consented audio fallback can resume when usable native cues are absent. Bitmap subtitles are displayed but are not OCR-translated.

**Native text translation requires the companion server update.** The currently checked service responded to /v1/health but returned 404 for /v1/translate; it was not redeployed from this environment. Original subtitles remain available when translation is unavailable. See the [operator update guide](docs/NATIVE_SUBTITLE_UPDATE-0.8.27.md). No API keys or private signing keys are distributed here.

Channel-switch previews are about 10% larger. Recovery and switching notices share a centered upper-screen safe-area anchor and avoid overlap.

## Installation and signing

Minimum Android version: **Android 7.0 / API 24**. Compile SDK and target SDK: **36**. Landscape, touchscreen and Leanback hardware features are explicitly optional.

The current application ID is **com.yuntai.android.apps.livetv**. The APK and AAB are signed with the retained private upload certificate used for the recent Play bundles. The key is not distributed in this repository.

Earlier review APKs used **org.example.iptv** and a different certificate. They are separate applications; settings, favorites and caption-device approval do not automatically migrate to the new application ID. A Google Play-installed build may use Google's separate app signing certificate and should be updated through Play when a sideload certificate does not match. Do not uninstall solely to force an update without considering local data.

The APK is for direct sideload testing. The AAB is for Play Console upload and cannot be installed directly. Verify the SHA-256 checksum before use.

## Validation and beta status

Release APK and AAB builds completed; 111 JVM tests passed. 109 Python tests passed and 13 infrastructure-dependent tests were skipped. Lint reported 0 errors and 122 warnings. Signatures, ZIP integrity, package/SDK values and 16 KiB APK ZIP alignment were checked. Catalog/source/guide/logo assets and startup-video content were compared with 0.8.26 and preserved.

Six Android media-test cases were compiled but not run because ADB initialization is blocked by a read-only Android home. Physical-device focus, scrolling, Android 16 behavior, real-network channel availability, long-session playback, end-to-end deployed native translation and Play Console processing remain unverified. Automated checks do not establish production reliability or approval.

Broadcasters and content providers control content availability, territory restrictions and distribution rights. Installing this app does not grant a content subscription or rebroadcasting rights.

Privacy contact and data-deletion requests: **yuntaiapp@gmail.com**. Never submit API keys, full stream URLs, raw reports, audio or subtitle text in public issues.
