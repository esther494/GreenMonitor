/*
 * sensor_test.c
 *
 *  Created on: Aug 20, 2024
 *      Author: esthe
 */

#include "test.h"

HAL_StatusTypeDef send_test_data_temperature (UART_HandleTypeDef * huart, float * temperature_humidity_buffer) {
	char data_buffer[50];
	int length = snprintf(data_buffer, sizeof(data_buffer), "%.2f test", temperature_humidity_buffer[0]);

	// Transmit the formatted string using DMA
	return HAL_UART_Transmit_DMA(huart, (uint8_t*)data_buffer, length);
}

HAL_StatusTypeDef send_test_data_humidity (UART_HandleTypeDef * huart, float * temperature_humidity_buffer) {
	char data_buffer[50];
	int length = snprintf(data_buffer, sizeof(data_buffer), "%.2f test", temperature_humidity_buffer[1]);

	// Transmit the formatted string using DMA
	return HAL_UART_Transmit_DMA(huart, (uint8_t*)data_buffer, length);
}

HAL_StatusTypeDef send_test_data_light (UART_HandleTypeDef * huart, float * light_moisture_buffer) {
	char data_buffer[50];
	int length = snprintf(data_buffer, sizeof(data_buffer), "%.2f test", light_moisture_buffer[0]);

	// Transmit the formatted string using DMA
	return HAL_UART_Transmit_DMA(huart, (uint8_t*)data_buffer, length);
}

HAL_StatusTypeDef send_test_data_moisture (UART_HandleTypeDef * huart, float * light_moisture_buffer) {
	char data_buffer[50];
	int length = snprintf(data_buffer, sizeof(data_buffer), "%.2f test", light_moisture_buffer[1]);

	// Transmit the formatted string using DMA
	return HAL_UART_Transmit_DMA(huart, (uint8_t*)data_buffer, length);
}
