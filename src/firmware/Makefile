PROJECT_NAME = $(shell basename "$(realpath ./)")

APPLICATION_SRCS = $(notdir $(wildcard ./*.c))
APPLICATION_SRCS += softdevice_handler.c
APPLICATION_SRCS += ble_advdata.c
APPLICATION_SRCS += ble_conn_params.c
APPLICATION_SRCS += app_timer.c
APPLICATION_SRCS += app_button.c
APPLICATION_SRCS += ble_nus.c
APPLICATION_SRCS += nrf_assert.c
APPLICATION_SRCS += nrf_drv_common.c
APPLICATION_SRCS += nrf_drv_gpiote.c
APPLICATION_SRCS += nrf_drv_uart.c
APPLICATION_SRCS += nrf_drv_clock.c
APPLICATION_SRCS += retarget.c
APPLICATION_SRCS += ble_srv_common.c
APPLICATION_SRCS += ble_advertising.c
APPLICATION_SRCS += app_uart.c
APPLICATION_SRCS += fstorage.c
APPLICATION_SRCS += app_util_platform.c
APPLICATION_SRCS += app_error_weak.c

# MPU6050
APPLICATION_SRCS += nrf_drv_twi.c
APPLICATION_SRCS += mpu6050.c

LIBRARY_PATHS += ../../include
LIBRARY_PATHS += ./config
SOURCE_PATHS  += ../../src

# BSP
LIBRARY_PATHS += ../../lib/bsp
LIBRARY_PATHS += ../../lib/mpu6050
SOURCE_PATHS  += ../../lib/mpu6050

BOARD = BOARD_SENSOR_TAG
NRF_MODEL = nrf51
SDK_VERSION = 12
SOFTDEVICE_MODEL = s130

CFLAGS+=-g -DDEBUG
NRF_BASE_PATH ?= ../../nrf5x-base
include $(NRF_BASE_PATH)/make/Makefile
