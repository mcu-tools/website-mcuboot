---
layout: flow
title: Documentation
permalink: /documentation/
jumbotron:
  title: Documentation
  inner_class: text-white
  description: ""
  image: /assets/images/content/MCUboot_banner.jpg
flow:
  - row: main_content_row
---
### Table of contents

#### General
- [Release notes](/documentation/release-notes/)
- [Release process](/documentation/release-process/)
- [Bootloader design](/documentation/design/)
- [Encrypted image](/documentation/encrypted-images/)
- [imgtool](/documentation/imgtool/)
- [ecdsa](/documentation/ecdsa/)
- [Signed Images](/documentation/signed-images/)


#### Usage instructions
- [Zephyr](/documentation/readme-zephyr/)
- [Mynewt](/documentation/readme-mynewt/)
- [RIOT](/documentation/readme-riot/)
- [Mbed-OS](/documentation/readme-mbed/)

#### Testing
- [**Zephyr** test plan](/documentation/testplan-zephyr/)
- [**Mynewt** test plan](/documentation/testplan-mynewt/)


### Browsing
Information and documentation on the bootloader is stored within the source. For more information 
in the source, here are some pointers:

boot/bootutil: The core of the bootloader itself.
boot/boot_serial: Support for serial upgrade within the bootloader itself.
boot/zephyr: Port of the bootloader to Zephyr
boot/mynewt: Mynewt bootloader app
boot/mbed: Port of the bootloader to Mbed-OS
imgtool: A tool to securely sign firmware images for booting by MCUboot.
sim: A bootloader simulator for testing and regression