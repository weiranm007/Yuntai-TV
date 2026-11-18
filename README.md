# Yuntai TV

A minimal live TV app for Android TV, Google TV, and Android tablets. This repository distributes beta APKs, release notes, and the public privacy policy.

- [Privacy Policy](PRIVACY_POLICY.md)
- [Download the 0.8.21-beta APK](https://raw.githubusercontent.com/weiranm007/Yuntai-TV/main/downloads/yuntai-tv-0.8.21-beta-review.apk)
- [Download beta releases](https://github.com/weiranm007/Yuntai-TV/releases)
- [Version 0.8.21-beta release notes](RELEASE_NOTES.md)

## Version 0.8.21-beta

Audio-only listening mode is available from the playback toolbar and remote-control main menu. It disables the video track, retains channel audio, and displays the current channel logo, name, and an amplitude waveform computed from decoded audio. Turn it off to restore video. Channel navigation, the program guide, optional AI captions, and playback recovery remain available.

The waveform does not use the microphone, record audio, or automatically upload it. AI captions are a separate optional cloud feature requiring device approval and explicit audio-processing consent. Listening mode does not guarantee background or screen-off playback; existing Android lifecycle and picture-in-picture restrictions still apply. Bandwidth savings depend on the source's audio rendition.

## Installation

Download the APK from [Releases](https://github.com/weiranm007/Yuntai-TV/releases), verify its SHA-256 checksum, and allow installation when prompted by Android. Version 0.8.21-beta retains the existing beta review certificate and can update an older beta signed with that certificate. Existing caption approval and configuration are preserved; no backend redeployment is needed for this version. Builds with another signing certificate may not update in place.

Minimum Android version: Android 5.0 / API 21. Cloud authorization and captions require Android 6.0 / API 23 or later and the configured authorization workflow.

## Beta status

This is a review-signed beta, not a Google Play production release. Automated checks do not establish real-device playback quality. See the release notes and validation manifest for completed checks and outstanding device tests.

Broadcasters and content providers control their content, availability, territory restrictions, and distribution rights. Installing this app does not grant a content subscription or rebroadcasting rights.

Privacy contact and data-deletion requests: **yuntaiapp@gmail.com**. Never submit API keys, full stream URLs, raw reports, audio, or subtitle text in public issues.
