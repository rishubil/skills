---
title: Toybox.Ant
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html
---

## Module: Toybox.Ant

## Overview

## See Also:

- [Core Topics - ANT and ANT Plus](https://developer.garmin.com/connect-iq/core-topics/ant-and-ant-plus/)
- [ANT Basics](https://www.thisisant.com/developer/ant/ant-basics/#104_tab)
- [ANT Downloads & Resources](https://www.thisisant.com/developer/resources/downloads/)

## Classes Under Namespace

**Classes:** [BurstListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstListener.html), [BurstPayload](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayload.html), [BurstPayloadIterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayloadIterator.html), [ChannelAssignment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/ChannelAssignment.html), [CryptoConfig](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/CryptoConfig.html), [DeviceConfig](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/DeviceConfig.html), [EncryptionInvalidSettingsException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/EncryptionInvalidSettingsException.html), [GenericChannel](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/GenericChannel.html), [Message](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/Message.html), [UnableToAcquireChannelException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/UnableToAcquireChannelException.html), [UnableToAcquireEncryptedChannelException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/UnableToAcquireEncryptedChannelException.html)

## Constant Summary

### MessageId

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MSG\_ID\_RF\_EVENT | 0x01 | API Level 1.0.0 |  |
| MSG\_ID\_UNASSIGN\_CHANNEL | 0x41 | API Level 1.0.0 |  |
| MSG\_ID\_ASSIGN\_CHANNEL | 0x42 | API Level 1.0.0 |  |
| MSG\_ID\_CHANNEL\_ID | 0x51 | API Level 1.0.0 |  |
| MSG\_ID\_CHANNEL\_PERIOD | 0x43 | API Level 1.0.0 |  |
| MSG\_ID\_CHANNEL\_RF\_FREQUENCY | 0x45 | API Level 1.0.0 |  |
| MSG\_ID\_NETWORK\_KEY | 0x46 | API Level 1.0.0 |  |
| MSG\_ID\_TRANSMIT\_POWER | 0x47 | API Level 1.0.0 |  |
| MSG\_ID\_CHANNEL\_TRANSMIT\_POWER | 0x60 | API Level 1.0.0 |  |
| MSG\_ID\_LIB\_CONFIG | 0x6E | API Level 1.0.0 |  |
| MSG\_ID\_RESET\_SYSTEM | 0x4A | API Level 1.0.0 |  |
| MSG\_ID\_OPEN\_CHANNEL | 0x4B | API Level 1.0.0 |  |
| MSG\_ID\_CLOSE\_CHANNEL | 0x4C | API Level 1.0.0 |  |
| MSG\_ID\_BROADCAST\_DATA | 0x4E | API Level 1.0.0 |  |
| MSG\_ID\_ACKNOWLEDGED\_DATA | 0x4F | API Level 1.0.0 |  |
| MSG\_ID\_CHANNEL\_RESPONSE\_EVENT | 0x40 | API Level 1.0.0 |  |

### MessageCode

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MSG\_CODE\_EVENT\_RX\_FAIL | 0x02 | API Level 1.0.0 |  |
| MSG\_CODE\_EVENT\_TX | 0x03 | API Level 1.0.0 |  |
| MSG\_CODE\_EVENT\_TRANSFER\_RX\_FAILED | 0x04 | API Level 1.0.0 |  |
| MSG\_CODE\_EVENT\_TRANSFER\_TX\_COMPLETED | 0x05 | API Level 1.0.0 |  |
| MSG\_CODE\_EVENT\_TRANSFER\_TX\_FAILED | 0x06 | API Level 1.0.0 |  |
| MSG\_CODE\_EVENT\_CHANNEL\_CLOSED | 0x07 | API Level 1.0.0 |  |
| MSG\_CODE\_CHANNEL\_IN\_WRONG\_STATE | 0x15 | API Level 1.0.0 |  |
| MSG\_CODE\_CHANNEL\_ID\_NOT\_SET | 0x18 | API Level 1.0.0 |  |
| MSG\_CODE\_TRANSFER\_IN\_PROGRESS | 0x1F | API Level 1.0.0 |  |
| MSG\_CODE\_INVALID\_MESSAGE | 0x28 | API Level 1.0.0 |  |
| MSG\_CODE\_EVENT\_QUE\_OVERFLOW | 0x35 | API Level 1.0.0 |  |
| MSG\_CODE\_EVENT\_CRYPTO\_NEGOTIATION\_SUCCESS | 0x38 | API Level 2.3.0 |  |
| MSG\_CODE\_EVENT\_CRYPTO\_NEGOTIATION\_FAIL | 0x39 | API Level 2.3.0 |  |
| MSG\_CODE\_EVENT\_CONNECTION\_REJECTED | 0xFF | API Level 5.1.0 | Ant connection is rejected by the user. |

### NetworkType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| NETWORK\_PUBLIC | 0 | API Level 1.0.0 |  |
| NETWORK\_PLUS | 1 | API Level 1.0.0 |  |
| NETWORK\_PRIVATE | 2 | API Level 1.2.0 |  |

### ChannelType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CHANNEL\_TYPE\_TX\_NOT\_RX | 0x10 | API Level 1.0.0 | Bidirectional Transmit (Master) |
| CHANNEL\_TYPE\_RX\_NOT\_TX | 0x00 | API Level 1.0.0 | Bidirectional Receive (Slave) |
| CHANNEL\_TYPE\_RX\_ONLY | 0x40 | API Level 1.2.0 | Receive Only (Slave) |
| CHANNEL\_TYPE\_SHARED\_BIDIRECTIONAL\_RECEIVE | 0x20 | API Level 3.1.0 | Shared Bidirectional Receive (Slave) |
| CHANNEL\_TYPE\_SHARED\_BIDIRECTIONAL\_TRANSMIT | 0x30 | API Level 3.1.0 | Shared Bidirectional Transmit (Master) |

Error codes passed to the failure functions in the BurstListener

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| BURST\_ERROR\_OUT\_OF\_MEMORY | 0 | API Level 2.2.0 | There was not enough memory available to send/receive a burst message |
| BURST\_ERROR\_SEQUENCE\_NUMBER\_FAIL | 1 | API Level 2.2.0 | A burst packet was received out of order and the entire message was dropped |
| BURST\_ERROR\_RF\_FAIL | 2 | API Level 2.2.0 | A burst failed over the air |
| BURST\_ERROR\_TRANSFER\_IN\_PROGRESS | 3 | API Level 2.2.0 | Burst was blocked by another burst from the native system code |
