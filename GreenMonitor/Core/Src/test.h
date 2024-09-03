/*
 * sensor_test.h
 *
 *  Created on: Aug 20, 2024
 *      Author: esthe
 */

#ifndef SRC_TEST_H_
#define SRC_TEST_H_

#include "stm32f4xx_hal.h"
#include <stdio.h>
#define BAUD_RATE 115200

HAL_StatusTypeDef test_sensor(UART_HandleTypeDef * huart, float * temperature_humidity_buffer);

#endif /* SRC_TEST_H_ */
