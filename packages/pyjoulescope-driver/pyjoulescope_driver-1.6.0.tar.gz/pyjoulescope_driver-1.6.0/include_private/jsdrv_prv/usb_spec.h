/*
 * Copyright 2014-2022 Jetperch LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef JSDRV_USB_SPEC_H__
#define JSDRV_USB_SPEC_H__

#include "jsdrv/cmacro_inc.h"
#include <stdint.h>

JSDRV_CPP_GUARD_START

#define USB_EP_DIR_OUT (0x00U)
#define USB_EP_DIR_IN (0x80U)
#define USB_EP_DIR_MASK (0x80U)

/* USB standard descriptor endpoint type */
#define USB_EP_CONTROL (0x00U)
#define USB_EP_ISOCHRONOUS (0x01U)
#define USB_EP_BULK (0x02U)
#define USB_EP_INTERRUPT (0x03U)
#define USB_EP_NUMBER_MASK (0x0FU)

/* Control endpoint */
#define USB_EP_STANDARD_CONTROL_ID (0)
#define USB_EP_CONTROL_OUT (USB_EP_STANDARD_CONTROL_ID | USB_ENDPOINT_OUT)
#define USB_EP_CONTROL_IN  (USB_EP_STANDARD_CONTROL_ID | USB_ENDPOINT_IN)
#define USB_EP_CONTROL_PACKET_SIZE_MAX (64U)

/* USB standard descriptor length */
#define USB_DESCRIPTOR_LENGTH_DEVICE (0x12U)
#define USB_DESCRIPTOR_LENGTH_CONFIGURE (0x09U)
#define USB_DESCRIPTOR_LENGTH_INTERFACE (0x09U)
#define USB_DESCRIPTOR_LENGTH_ENDPOINT (0x07U)
#define USB_DESCRIPTOR_LENGTH_DEVICE_QUALITIER (0x0AU)
#define USB_DESCRIPTOR_LENGTH_OTG_DESCRIPTOR (5U)
#define USB_DESCRIPTOR_LENGTH_BOS_DESCRIPTOR (5U)

/* USB Device Capability Type Codes */
#define USB_DESCRIPTOR_TYPE_DEVICE_CAPABILITY_WIRELESS (0x01U)
#define USB_DESCRIPTOR_TYPE_DEVICE_CAPABILITY_USB20_EXTENSION (0x02U)
#define USB_DESCRIPTOR_TYPE_DEVICE_CAPABILITY_SUPERSPEED (0x03U)

/* USB standard descriptor type */
#define USB_DESCRIPTOR_TYPE_DEVICE (0x01U)
#define USB_DESCRIPTOR_TYPE_CONFIGURE (0x02U)
#define USB_DESCRIPTOR_TYPE_STRING (0x03U)
#define USB_DESCRIPTOR_TYPE_INTERFACE (0x04U)
#define USB_DESCRIPTOR_TYPE_ENDPOINT (0x05U)
#define USB_DESCRIPTOR_TYPE_DEVICE_QUALITIER (0x06U)
#define USB_DESCRIPTOR_TYPE_OTHER_SPEED_CONFIGURATION (0x07U)
#define USB_DESCRIPTOR_TYPE_INTERFACE_POWER (0x08U)
#define USB_DESCRIPTOR_TYPE_OTG (0x09U)
#define USB_DESCRIPTOR_TYPE_DEBUG (0x0AU)
#define USB_DESCRIPTOR_TYPE_INTERFACE_ASSOCIATION (0x0BU)
#define USB_DESCRIPTOR_TYPE_BOS (0x0FU)
#define USB_DESCRIPTOR_TYPE_DEVICE_CAPABILITY (0x10U)

#define USB_REQUEST_TYPE_DIR_OUT (0x00)
#define USB_REQUEST_TYPE_DIR_IN (0x80U)
#define USB_REQUEST_TYPE_DIR_MASK (0x80U)

#define USB_REQUEST_TYPE_TYPE_MASK (0x60U)
#define USB_REQUEST_TYPE_TYPE_SHIFT (5U)
#define USB_REQUEST_TYPE_TYPE_STANDARD (0U)
#define USB_REQUEST_TYPE_TYPE_CLASS (0x20U)
#define USB_REQUEST_TYPE_TYPE_VENDOR (0x40U)

#define USB_REQUEST_TYPE_RECIPIENT_MASK (0x1FU)
#define USB_REQUEST_TYPE_RECIPIENT_SHIFT (0U)
#define USB_REQUEST_TYPE_RECIPIENT_DEVICE (0x00U)
#define USB_REQUEST_TYPE_RECIPIENT_INTERFACE (0x01U)
#define USB_REQUEST_TYPE_RECIPIENT_ENDPOINT (0x02U)
#define USB_REQUEST_TYPE_RECIPIENT_OTHER (0x03U)

#define USB_REQUEST_TYPE(dir_, type_, recipient_) \
        (USB_REQUEST_TYPE_DIR_##dir_ | USB_REQUEST_TYPE_TYPE_##type_ | USB_REQUEST_TYPE_RECIPIENT_##recipient_)

#define USB_REQUEST_TYPE_IS_IN(setup_u_) \
        (USB_REQUEST_TYPE_DIR_IN == ((setup_u_).s.bmRequestType & USB_REQUEST_TYPE_DIR_MASK))

#define USB_REQUEST_TYPE_IS_OUT(setup_u_) \
        (USB_REQUEST_TYPE_DIR_OUT == ((setup_u_).s.bmRequestType & USB_REQUEST_TYPE_DIR_MASK))

#define USB_CTRL_SIZE_FULL (64U)
#define USB_CTRL_SIZE_HIGH (512U)
#define USB_CTRL_TRANSFER_SIZE_MAX  (4096U)         // WinUsb_ControlTransfer limit

/* USB standard request */
#define USB_REQUEST_STANDARD_GET_STATUS (0x00U)
#define USB_REQUEST_STANDARD_CLEAR_FEATURE (0x01U)
#define USB_REQUEST_STANDARD_RESERVED_2 (0x02U)
#define USB_REQUEST_STANDARD_SET_FEATURE (0x03U)
#define USB_REQUEST_STANDARD_RESERVED_4 (0x04U)
#define USB_REQUEST_STANDARD_SET_ADDRESS (0x05U)
#define USB_REQUEST_STANDARD_GET_DESCRIPTOR (0x06U)
#define USB_REQUEST_STANDARD_SET_DESCRIPTOR (0x07U)
#define USB_REQUEST_STANDARD_GET_CONFIGURATION (0x08U)
#define USB_REQUEST_STANDARD_SET_CONFIGURATION (0x09U)
#define USB_REQUEST_STANDARD_GET_INTERFACE (0x0AU)
#define USB_REQUEST_STANDARD_SET_INTERFACE (0x0BU)
#define USB_REQUEST_STANDARD_SYNCH_FRAME (0x0CU)

/* USB standard request GET Status */
#define USB_REQUEST_STANDARD_GET_STATUS_DEVICE_SELF_POWERED_SHIFT (0U)
#define USB_REQUEST_STANDARD_GET_STATUS_DEVICE_REMOTE_WARKUP_SHIFT (1U)

#define USB_REQUEST_STANDARD_GET_STATUS_ENDPOINT_HALT_MASK (0x01U)
#define USB_REQUEST_STANDARD_GET_STATUS_ENDPOINT_HALT_SHIFT (0U)

#define USB_REQUEST_STANDARD_GET_STATUS_OTG_STATUS_SELECTOR (0xF000U)

/* USB standard request CLEAR/SET feature */
#define USB_REQUEST_STANDARD_FEATURE_SELECTOR_ENDPOINT_HALT (0U)
#define USB_REQUEST_STANDARD_FEATURE_SELECTOR_DEVICE_REMOTE_WAKEUP (1U)
#define USB_REQUEST_STANDARD_FEATURE_SELECTOR_DEVICE_TEST_MODE (2U)
#define USB_REQUEST_STANDARD_FEATURE_SELECTOR_B_HNP_ENABLE (3U)
#define USB_REQUEST_STANDARD_FEATURE_SELECTOR_A_HNP_SUPPORT (4U)
#define USB_REQUEST_STANDARD_FEATURE_SELECTOR_A_ALT_HNP_SUPPORT (5U)

/* USB standard descriptor configure bmAttributes */
#define USB_DESCRIPTOR_CONFIGURE_ATTRIBUTE_D7_MASK (0x80U)
#define USB_DESCRIPTOR_CONFIGURE_ATTRIBUTE_D7_SHIFT (7U)

#define USB_DESCRIPTOR_CONFIGURE_ATTRIBUTE_SELF_POWERED_MASK (0x40U)
#define USB_DESCRIPTOR_CONFIGURE_ATTRIBUTE_SELF_POWERED_SHIFT (6U)

#define USB_DESCRIPTOR_CONFIGURE_ATTRIBUTE_REMOTE_WAKEUP_MASK (0x20U)
#define USB_DESCRIPTOR_CONFIGURE_ATTRIBUTE_REMOTE_WAKEUP_SHIFT (5U)

/* USB standard descriptor endpoint bmAttributes */
#define USB_DESCRIPTOR_ENDPOINT_ADDRESS_DIRECTION_MASK (0x80U)
#define USB_DESCRIPTOR_ENDPOINT_ADDRESS_DIRECTION_SHIFT (7U)
#define USB_DESCRIPTOR_ENDPOINT_ADDRESS_DIRECTION_OUT (0U)
#define USB_DESCRIPTOR_ENDPOINT_ADDRESS_DIRECTION_IN (0x80U)

#define USB_DESCRIPTOR_ENDPOINT_ADDRESS_NUMBER_MASK (0x0FU)
#define USB_DESCRIPTOR_ENDPOINT_ADDRESS_NUMBER_SHFIT (0U)

#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_TYPE_MASK (0x03U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_NUMBER_SHFIT (0U)

#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_SYNC_TYPE_MASK (0x0CU)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_SYNC_TYPE_SHFIT (2U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_SYNC_TYPE_NO_SYNC (0x00U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_SYNC_TYPE_ASYNC (0x04U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_SYNC_TYPE_ADAPTIVE (0x08U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_SYNC_TYPE_SYNC (0x0CU)

#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_USAGE_TYPE_MASK (0x30U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_USAGE_TYPE_SHFIT (4U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_USAGE_TYPE_DATA_ENDPOINT (0x00U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_USAGE_TYPE_FEEDBACK_ENDPOINT (0x10U)
#define USB_DESCRIPTOR_ENDPOINT_ATTRIBUTE_USAGE_TYPE_IMPLICIT_FEEDBACK_DATA_ENDPOINT (0x20U)

#define USB_DESCRIPTOR_ENDPOINT_MAXPACKETSIZE_SIZE_MASK (0x07FFu)
#define USB_DESCRIPTOR_ENDPOINT_MAXPACKETSIZE_MULT_TRANSACTIONS_MASK (0x1800u)
#define USB_DESCRIPTOR_ENDPOINT_MAXPACKETSIZE_MULT_TRANSACTIONS_SHFIT (11U)

#define USB_STRING_LANG_ENGLISH (0x0409)

enum usb_speed_e {
    USB_SPEED_FULL = 0x00U,
    USB_SPEED_LOW = 0x01U,
    USB_SPEED_HIGH = 0x02U,
    USB_SPEED_SUPERSPEED_GEN1 = 0x03U,
    USB_SPEED_UNKNOWN = 0xFFU,
};

enum usb_transfer_type_e {
    USB_TRANSFER_TYPE_CONTROL = 0,
    USB_TRANSFER_TYPE_ISOCHRONOUS = 1,
    USB_TRANSFER_TYPE_BULK = 2,
    USB_TRANSFER_TYPE_INTERRUPT = 3,
};

/* Set up packet structure */
struct usb_setup_s {
    uint8_t bmRequestType;
    uint8_t bRequest;
    uint16_t wValue;
    uint16_t wIndex;
    uint16_t wLength;
};

typedef union usb_setup_u {
    uint64_t u64;
    struct usb_setup_s s;
} usb_setup_t;

JSDRV_CPP_GUARD_END

#endif /* JSDRV_USB_SPEC_H__ */
