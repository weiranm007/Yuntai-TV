# Yuntai TV

A minimal live TV app for Android TV, Google TV, Android phones and tablets. This repository distributes beta builds, release notes, validation manifests and the public privacy policy.

- [Privacy Policy](PRIVACY_POLICY.md)
- [Download the 0.8.26-beta APK](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.26-beta.apk)
- [Google Play upload AAB](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.26-beta-play.aab)
- [Version 0.8.26-beta release notes](releases/v0.8.26-beta.md)
- [Checksums](downloads/SHA256SUMS-0.8.26-beta.txt)
- [Validation manifest](downloads/VALIDATION-0.8.26-beta.json)
- [Beta releases](https://github.com/weiranm007/Yuntai-TV/releases)

## Version 0.8.26-beta

The main menu now contains Settings, Current channel management, Audio-only listening, Help & feedback, and Exit. Playlist import, Automatic sources, duplicate captions and duplicate programme-guide entries were removed from this menu. Existing automatic refresh behavior is retained.

Settings are grouped under Picture & playback, Captions & translation, Interface & display, and Help & about. Current channel management retains favorites, source selection/enable/disable, and playback; it no longer presents add-source, official-watch-link, or diagnostics actions. An empty source list no longer opens an add-source form.

Audio-only listening retains the live channel audio, with a compact spectrum computed locally from decoded PCM and a persistent return-to-video action. Optional cloud AI captions remain a separate consent-based beta feature. Recovery notices remain available during buffering and recovery.

## Installation and signing

Minimum Android version: **Android 7.0 / API 24**. Compile SDK and target SDK: **36**. Landscape, touchscreen and Leanback hardware features are explicitly optional.

The current application ID is **com.yuntai.android.apps.livetv**. The APK and AAB are signed with the retained private upload certificate used for the recent Play bundles. The key is not distributed in this repository.

Earlier review APKs used **org.example.iptv** and a different certificate. They are separate applications; settings, favorites and caption-device approval do not automatically migrate to the new application ID. A Google Play-installed build may use Google's separate app signing certificate and should be updated through Play when a sideload certificate does not match. Do not uninstall solely to force an update without considering local data.

The APK is for direct sideload testing. The AAB is for Play Console upload and cannot be installed directly. Verify the SHA-256 checksum before use.

## Validation and beta status

Release APK and AAB builds completed; 102 JVM tests passed. Lint reported 0 errors and 114 warnings. Signatures, ZIP integrity, package/SDK values and 16 KiB APK ZIP alignment were checked. Catalog/source/guide/logo assets and startup-video content were compared with 0.8.25 and preserved.

Physical-device focus, scrolling, settings dialogs, Android 16 behavior, long-session playback and Play Console processing remain unverified. Automated checks do not establish production reliability or approval.

Broadcasters and content providers control content availability, territory restrictions and distribution rights. Installing this app does not grant a content subscription or rebroadcasting rights.

Privacy contact and data-deletion requests: **yuntaiapp@gmail.com**. Never submit API keys, full stream URLs, raw reports, audio or subtitle text in public issues.
