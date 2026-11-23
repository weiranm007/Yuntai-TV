# Yuntai TV

A minimal live TV app for Android TV, Google TV, Android phones and tablets. This repository distributes beta builds, release notes, validation manifests and the public privacy policy.

- [Privacy Policy](PRIVACY_POLICY.md)
- [Download the 0.8.28-beta APK](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.28-beta.apk)
- [Google Play upload AAB](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.28-beta-play.aab)
- [Caption and pairing service update ZIP](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-caption-service-0.8.28-update.zip)
- [Version 0.8.28-beta release notes](releases/v0.8.28-beta.md)
- [Checksums](downloads/SHA256SUMS-0.8.28-beta.txt)
- [Validation manifest](downloads/VALIDATION-0.8.28-beta.json)
- [Beta releases](https://github.com/weiranm007/Yuntai-TV/releases)

## Version 0.8.28-beta

Native foreign-text translation can show Chinese without first flashing the original text. Rolling cues are deduplicated and merged into bounded batches, with limited preceding dialogue used only for semantic context. Stale results are discarded and channel changes invalidate old work. Native Chinese is preferred; original foreign captions are shown when translation is off. Bitmap/burned-in captions cannot be replaced by this text pipeline.

Cloud audio/text processing now has one explicit combined consent, which existing users must reconfirm. Global caption and native foreign-text translation switches remain independent. No Groq API key is embedded in the APK.

Private-beta pairing uses a five-minute, four-digit code with transactional collision protection and owner-only Cloud Shell confirmation. No fingerprint needs to be typed. Existing approvals persist. This does not enable anonymous self-authorization.

Settings use clearer heading/item/choice hierarchy while retaining the existing dark theme. The top menu background extends to the screen edges and no longer reserves a hidden status-bar gap; interactive controls still avoid visible system bars and display cutouts. Existing source maintenance, masked line identifiers, catalogs and startup animation are retained.

**Deploy the companion server update for contextual translation and new short codes.** It preserves the existing authorization mode, secrets and quotas. See the [operator update guide](docs/NATIVE_SUBTITLE_UPDATE-0.8.28.md). The assistant packaged the update but did not deploy it.

Rate limits are retained. Operator quota, provider throttling and concurrent-task feedback use distinct fixed error categories. The operator-versus-Groq cause of a reported intermittent HTTP 429 remains unverified pending safe failed-request logs. This release does not promise to resolve provider capacity or guarantee instantaneous subtitles.

## Installation and signing

Minimum Android version: **Android 7.0 / API 24**. Compile SDK and target SDK: **36**. Landscape, touchscreen and Leanback hardware features are explicitly optional.

The current application ID is **com.yuntai.android.apps.livetv**. The APK and AAB are signed with the retained private upload certificate used for the recent Play bundles. The key is not distributed in this repository.

Earlier review APKs used **org.example.iptv** and a different certificate. They are separate applications; settings, favorites and caption-device approval do not automatically migrate to the new application ID. A Google Play-installed build may use Google's separate app signing certificate and should be updated through Play when a sideload certificate does not match. Do not uninstall solely to force an update without considering local data.

The APK is for direct sideload testing. The AAB is for Play Console upload and cannot be installed directly. Verify the SHA-256 checksum before use.

## Validation and beta status

118 Android JVM tests and 128 Python tests passed. The final Python run included a local Firestore emulator with no skipped tests, covering REST approval, short-code collisions, parallel requests, cancellation and authorization lifecycle. Lint reported 0 errors and 121 warnings. APK/AAB signatures, retained upload certificate, ZIP integrity, SDK values and 16 KiB APK ZIP alignment were checked. Production content assets were compared with 0.8.27 and preserved; generated baseline profiles changed.

Six Android media-test cases were compiled but not executed on a device. Physical-device focus, scrolling, menu placement, subtitle latency/semantic quality, provider capacity, long-session playback and Play Console processing remain unverified. Automated checks do not establish production reliability or approval. No update was submitted for Play review by this workflow.

Broadcasters and content providers control availability, territorial restrictions and distribution rights. Installing the app does not grant a content subscription or rebroadcasting rights.

Privacy contact and data-deletion requests: **yuntaiapp@gmail.com**. Never submit API keys, full stream URLs, audio or subtitle text in public issues.
