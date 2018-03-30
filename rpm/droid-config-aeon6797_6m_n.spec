# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device aeon6797_6m_n
%define vendor planet

%define vendor_pretty Planet
%define device_pretty Gemini PDA

# Community HW adaptations need this
%define community_adaptation 1

# Adjust this for your device
%define pixel_ratio 2.0

Provides: ofono-configs

%include droid-configs-device/droid-configs.inc
