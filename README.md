# Yuntai TV

A minimal live TV app for Android TV, Google TV, and Android tablets. This repository distributes beta APKs, release notes, and the public privacy policy.

- [Privacy Policy](PRIVACY_POLICY.md)
- [Download the 0.8.22-beta APK](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.22-beta-review.apk)
- [Download beta releases](https://github.com/weiranm007/Yuntai-TV/releases)
- [Version 0.8.22-beta release notes](releases/v0.8.22-beta.md)

## Version 0.8.22-beta

Audio-only listening mode is available from a blue slide switch in the playback toolbar and from the remote-control main menu. It retains channel audio, displays the current logo and name, and now shows a narrower live frequency spectrum computed from current decoded PCM. A persistent button or the Back key restores video after closing any open overlays.

An independent recovery banner explains sustained buffering, active recovery, retry countdowns, network disconnection, and successful restoration. It does not depend on the auto-hiding status bar.

Spectrum processing is local and does not use the microphone, record audio, or automatically upload it. Optional AI captions require separate device approval and explicit audio-processing consent. Listening mode does not guarantee background or screen-off playback; existing Android lifecycle and picture-in-picture restrictions apply. Bandwidth savings depend on the source's audio rendition.

Automatic screenshot/OCR channel-identity detection is not enabled. A commercial or missing logo is not treated as proof of a mismatched channel.

## Installation

Download the APK from [Releases](https://github.com/weiranm007/Yuntai-TV/releases), verify its SHA-256 checksum, and allow installation when prompted by Android. Version 0.8.22-beta retains the existing beta review certificate and can update an older beta signed with that certificate. Existing caption approval and configuration are preserved; no backend redeployment is needed for this version. Builds with another signing certificate may not update in place.

Minimum Android version: Android 5.0 / API 21. Cloud authorization and captions require Android 6.0 / API 23 or later and the configured authorization workflow.

## Beta status

This is a review-signed beta, not a Google Play production release. Automated checks do not establish real-device playback quality. See the release notes and validation manifest for completed checks and outstanding device tests.

Broadcasters and content providers control their content, availability, territory restrictions, and distribution rights. Installing this app does not grant a content subscription or rebroadcasting rights.

Privacy contact and data-deletion requests: **yuntaiapp@gmail.com**. Never submit API keys, full stream URLs, raw reports, audio, or subtitle text in public issues.
